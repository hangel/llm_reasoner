import streamlit as st
import os
import json
import pandas as pd
from collections import Counter
from typing import Optional, List, Dict, Any
import mvp_config as config # Renamed import for clarity
import mvp_utils as utils   # Renamed import for clarity


def setup_sidebar(modules):
    """Configures and displays the Streamlit sidebar elements."""
    st.sidebar.image(
        str(config.LOGOS[config.SIDEBAR_LOGO_KEY]), # Ensure path is string
        caption=f"OKRocket® Platform\nCOBOLpro MVP Preview v{config.MVP_VERSION} [{utils.get_current_timestamp('%Y/%m/%d')}]",
        width=250
    )

    with st.sidebar.expander("**Execution Info**", expanded=False):
        exec_data = utils.get_system_info_markdown()
        st.markdown(exec_data, unsafe_allow_html=True) # Allow HTML for details tag

    with st.sidebar.expander("**Session State**", expanded=False):
        st.write(st.session_state)

    st.sidebar.markdown("---")

    # --- Module Selection ---
    module_names = list(modules.keys())
    default_module = module_names[0] # Default to the first module

    # Try to get selection from URL query parameters
    query_params = st.query_params.get("module", [default_module])
    # Ensure query_param value is a valid key before finding index
    selected_module_name = query_params[0] if query_params[0] in module_names else default_module

    try:
        # Get index based on potentially updated selected_module_name
        index = module_names.index(selected_module_name)
    except ValueError:
        index = 0 # Fallback if name somehow still invalid

    choice = st.sidebar.radio(
        "**MODULE SELECTOR**",
        module_names,
        index=index,
        help="Select the module to execute",
        label_visibility="visible"
    )

    # Update query params when selection changes for bookmarking/sharing
    if selected_module_name != choice:
        st.query_params["module"] = choice

    return modules[choice] # Return the Path object for the selected module

def scan_directory(start_dir: str) -> Dict[str, Any]:
    """
    Recursively scans the directory tree starting from start_dir and returns a dictionary
    containing information about each file and directory.

    Args:
        start_dir (str): The path to the directory to start the scan from.

    Returns:
        Dict[str, Any]: A dictionary representing the file system structure.
        The dictionary has the following structure:
        {
            "nodes": [
                {
                    "ID": int,
                    "TYPE": str,  # "File" or "Dir"
                    "PARENT": Optional[int],
                    "HID": bool,
                    "NAME": str,
                    "FILETYPE": str,
                    "PATH": str,
                    "SIZE": Optional[int]
                },
                ...
            ],
            "file_types": List[str]
        }
    """
    node_list = []
    file_types = []
    node_counter = 0;
    # Use a stack to avoid recursion depth issues
    stack = [(start_dir, None)]  # (path, parent_id)

    while stack:
        current_path, parent_id = stack.pop()
        try:  # Handle potential permission errors
            for item in os.listdir(current_path):
                full_path = os.path.join(current_path, item)
                node_counter += 1
                is_hidden = item.startswith(".")
                file_type = ""
                size = None

                if os.path.isdir(full_path):
                    node_type = "Dir"
                    stack.append((full_path, node_counter))  # Add to stack for later processing
                elif os.path.isfile(full_path):
                    node_type = "File"
                    size = os.path.getsize(full_path)
                    file_type = os.path.splitext(item)[1][1:]  # Extract file extension, remove the leading dot
                    if file_type not in file_types:
                        file_types.append(file_type)
                elif os.path.islink(full_path):
                    node_type = "Link"
                    file_type = "ln"
                    size = 0
                else:
                    node_type = "Other" #handle other file types
                    size = 0
                    file_type = "NA"

                node_list.append({
                    "ID": node_counter,
                    "TYPE": node_type,
                    "PARENT": parent_id,
                    "HID": is_hidden,
                    "NAME": item,
                    "FILETYPE": file_type,
                    "PATH": full_path,
                    "SIZE": size
                })
        except PermissionError:
            st.warning(f"Permission denied for: {current_path}. Skipping.")
            # Create a dummy node to represent the inaccessible directory
            node_counter += 1;
            node_list.append({
                    "ID": node_counter,
                    "TYPE": "Dir",
                    "PARENT": parent_id,
                    "HID": False,
                    "NAME": os.path.basename(current_path),
                    "FILETYPE": "NA",
                    "PATH": current_path,
                    "SIZE": 0
                })
    return {"nodes": node_list, "file_types": file_types}


def create_summary(data: Dict[str, Any]) -> Dict[str, int]:
    """
    Calculates summary statistics from the scanned data.

    Args:
        data (Dict[str, Any]): The dictionary returned by the scan_directory function.

    Returns:
        Dict[str, int]: A dictionary containing the summary statistics.
    """
    nodes = data["nodes"]
    summary = {
        "TOTAL NODES": len(nodes),
        "TOTAL DIRS": 0,
        "TOTAL HIDDEN DIRS": 0,
        "TOTAL LINKED DIRS": 0,
        "TOTAL FILES": 0,
        "TOTAL HIDDEN FILES": 0,
        "TOTAL LINKED FILES": 0,
        "TOTAL LINKS": 0,
    }

    for node in nodes:
        if node["TYPE"] == "Dir":
            summary["TOTAL DIRS"] += 1
            if node["HID"]:
                summary["TOTAL HIDDEN DIRS"] += 1
        elif node["TYPE"] == "File":
            summary["TOTAL FILES"] += 1
            if node["HID"]:
                summary["TOTAL HIDDEN FILES"] += 1
        elif node["TYPE"] == "Link":
            summary["TOTAL LINKS"] += 1

    return summary

def display_results(data: Dict[str, Any]):
    """
    Displays the scanned data in a table with filtering and column visibility options,
    and shows a summary of the scan.

    Args:
        data (Dict[str, Any]): The dictionary returned by the scan_directory function.
    """
    nodes = data["nodes"]
    file_types = data["file_types"]
    summary = create_summary(data)

    # Create a DataFrame for easier manipulation
    df = pd.DataFrame(nodes)
    df['PARENT_NAME'] = df['PARENT'].apply(lambda x: next((n['NAME'] for n in nodes if n['ID'] == x), None))

    # --- Filters ---
    st.sidebar.subheader("Filters")
    # Use session state to persist filter values
    if "type_filter" not in st.session_state:
        st.session_state.type_filter = "Any"
    if "filetype_filter" not in st.session_state:
        st.session_state.filetype_filter = []

    # Create filters, using stored session state values as defaults
    st.session_state.type_filter = st.sidebar.selectbox(
        "Filter by Type", ["Any", "File", "Dir", "Link"],
        index=["Any", "File", "Dir", "Link"].index(st.session_state.type_filter), key="type_filter_selectbox" #Added key
    )
    st.session_state.filetype_filter = st.sidebar.multiselect(
        "Filter by Filetype", file_types, default=st.session_state.filetype_filter, key="filetype_filter_multiselect" #Added key
    )

    # Apply filters
    filtered_df = df.copy()
    if st.session_state.type_filter != "Any":
        filtered_df = filtered_df[filtered_df["TYPE"] == st.session_state.type_filter]
    if st.session_state.filetype_filter:
        filtered_df = filtered_df[filtered_df["FILETYPE"].isin(st.session_state.filetype_filter)]

    # --- Column Visibility ---
    st.sidebar.subheader("Column Visibility")
    # Use session state to persist column visibility
    if "show_n" not in st.session_state:
        st.session_state.show_n = True
    if "show_type" not in st.session_state:
        st.session_state.show_type = True
    if "show_parent" not in st.session_state:
        st.session_state.show_parent = True
    if "show_hid" not in st.session_state:
        st.session_state.show_hid = True
    if "show_name" not in st.session_state:
        st.session_state.show_name = True
    if "show_filetype" not in st.session_state:
        st.session_state.show_filetype = True
    if "show_path" not in st.session_state:
        st.session_state.show_path = True
    if "show_size" not in st.session_state:
        st.session_state.show_size = True

    # Create checkboxes for column visibility, using stored session state
    st.session_state.show_n = st.sidebar.checkbox("Show N", value=st.session_state.show_n, key="show_n_checkbox") #Added key
    st.session_state.show_type = st.sidebar.checkbox("Show Type", value=st.session_state.show_type, key="show_type_checkbox") #Added key
    st.session_state.show_parent = st.sidebar.checkbox("Show Parent", value=st.session_state.show_parent, key="show_parent_checkbox") #Added key
    st.session_state.show_hid = st.sidebar.checkbox("Show Hidden", value=st.session_state.show_hid, key="show_hid_checkbox") #Added key
    st.session_state.show_name = st.sidebar.checkbox("Show Name", value=st.session_state.show_name, key="show_name_checkbox") #Added key
    st.session_state.show_filetype = st.sidebar.checkbox("Show Filetype", value=st.session_state.show_filetype, key="show_filetype_checkbox") #Added key
    st.session_state.show_path = st.sidebar.checkbox("Show Path", value=st.session_state.show_path, key="show_path_checkbox") #Added key
    st.session_state.show_size = st.sidebar.checkbox("Show Size", value=st.session_state.show_size, key="show_size_checkbox") #Added key

    # Display the table
    if st.button("Display Table"): # Button to control table display
        displayed_columns = []
        if st.session_state.show_n:
            displayed_columns.append("ID")
        if st.session_state.show_type:
            displayed_columns.append("TYPE")
        if st.session_state.show_parent:
            displayed_columns.append("PARENT_NAME")
        if st.session_state.show_hid:
            displayed_columns.append("HID")
        if st.session_state.show_name:
            displayed_columns.append("NAME")
        if st.session_state.show_filetype:
            displayed_columns.append("FILETYPE")
        if st.session_state.show_path:
            displayed_columns.append("PATH")
        if st.session_state.show_size:
            displayed_columns.append("SIZE")
        if displayed_columns:
            st.dataframe(filtered_df[displayed_columns], hide_index=True)
        else:
            st.write("No columns selected to display.")

    # Display the summary
    st.subheader("Summary")
    st.write(json.dumps(summary, indent=4))



def main():
    available_modules = config.DASHBOARDS

    if not available_modules:
        st.error("Configuration Error: No modules found in 'mvp_config.py'.")
        return # Stop execution if no modules are defined

    # Setup sidebar and get the selected module's path
    selected_module_path = setup_sidebar(available_modules)

    # Execute the selected module
    run_selected_module(selected_module_path)


    """
    Main function to run the Streamlit application.
    """
    st.set_page_config(layout="wide")  # Make Streamlit use the full width of the page
    st.title("File System Scanner")

    # Initialize session state for filters before the scan
    if "type_filter" not in st.session_state:
        st.session_state.type_filter = "Any"
    if "filetype_filter" not in st.session_state:
        st.session_state.filetype_filter = []
    if "file_types" not in st.session_state:
        st.session_state.file_types = []

    # Sidebar for filters (always visible)
    st.sidebar.subheader("Filters")
     # Create filters, using stored session state values as defaults
    st.session_state.type_filter = st.sidebar.selectbox(
        "Filter by Type", ["Any", "File", "Dir", "Link"],
        index=["Any", "File", "Dir", "Link"].index(st.session_state.type_filter), key="type_filter_selectbox" #Added key
    )
    st.session_state.filetype_filter = st.sidebar.multiselect(
        "Filter by Filetype", st.session_state.file_types, default=st.session_state.filetype_filter, key="filetype_filter_multiselect" #Added key
    )
   
    start_dir = st.text_input("Enter the starting directory to scan:", ".")
    if st.button("Scan"):
        if start_dir:
            if os.path.exists(start_dir):
                results = scan_directory(start_dir)
                # Update session state with new file types, preserving existing filter values if possible
                previous_filetype_filter = st.session_state.filetype_filter
                st.session_state.file_types = results["file_types"]
                # Rebuild filetype filter
                st.sidebar.subheader("Filters")
                st.session_state.type_filter = st.sidebar.selectbox(
                    "Filter by Type", ["Any", "File", "Dir", "Link"],
                    index=["Any", "File", "Dir", "Link"].index(st.session_state.type_filter), key="type_filter_selectbox" #Added key
                )
                st.session_state.filetype_filter = st.sidebar.multiselect(
                    "Filter by Filetype", results["file_types"],
                    default=[ft for ft in previous_filetype_filter if ft in results["file_types"]], key="filetype_filter_multiselect" #Added key
                )
                display_results(results)
            else:
                st.error(f"Error: The directory '{start_dir}' does not exist.")
        else:
            st.error("Please enter a starting directory.")



if __name__ == "__main__":
    main()

