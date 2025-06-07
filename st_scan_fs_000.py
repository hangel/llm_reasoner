import streamlit as st
import os
import json
import pandas as pd
from collections import Counter
from typing import Optional, List, Dict, Any

# --- Session State Initialization ---
def init_session_state():
    """
    Initializes session state variables if they are not already present.
    """
    if "STAT_SCAN_DIR" not in st.session_state:
        st.session_state.STAT_SCAN_DIR = "./"
    if "STAT_HIDE_N" not in st.session_state:
        st.session_state.STAT_HIDE_N = False
    if "STAT_HIDE_TYPE" not in st.session_state:
        st.session_state.STAT_HIDE_TYPE = False
    if "STAT_HIDE_PARENT" not in st.session_state:
        st.session_state.STAT_HIDE_PARENT = False
    if "STAT_HIDE_HIDDEN" not in st.session_state:
        st.session_state.STAT_HIDE_HIDDEN = False
    if "STAT_HIDE_NAME" not in st.session_state:
        st.session_state.STAT_HIDE_NAME = False
    if "STAT_HIDE_EXTENSION" not in st.session_state:
        st.session_state.STAT_HIDE_EXTENSION = False
    if "STAT_HIDE_PATH" not in st.session_state:
        st.session_state.STAT_HIDE_PATH = False
    if "STAT_HIDE_SIZE" not in st.session_state:
        st.session_state.STAT_HIDE_SIZE = False
    if "STAT_MULT_SELECT_TYPE" not in st.session_state:
        st.session_state.STAT_MULT_SELECT_TYPE = ["Any"]
    if "STAT_MULT_EXTENSION" not in st.session_state:
        st.session_state.STAT_MULT_EXTENSION = ["Any"]
    if "scan_results" not in st.session_state:  # To store scan results
        st.session_state.scan_results = None

# --- Helper Functions ---
def scan_directory(start_dir: str) -> Dict[str, Any]:
    """
    Recursively scans the directory tree starting from start_dir and returns a dictionary
    containing information about each file and directory.

    Args:
        start_dir (str): The path to the directory to start the scan from.

    Returns:
        Dict[str, Any]: A dictionary representing the file system structure.
    """
    node_list = []
    file_types = []
    node_counter = 0
    stack = [(start_dir, None)]

    while stack:
        current_path, parent_id = stack.pop()
        try:
            for item in os.listdir(current_path):
                full_path = os.path.join(current_path, item)
                node_counter += 1
                is_hidden = item.startswith(".")
                file_extension = ""
                size = None

                if os.path.isdir(full_path):
                    node_type = "Dir"
                    stack.append((full_path, node_counter))
                elif os.path.isfile(full_path):
                    node_type = "File"
                    size = os.path.getsize(full_path)
                    file_extension = os.path.splitext(item)[1][1:]
                    if file_extension and file_extension not in file_types:
                        file_types.append(file_extension)
                elif os.path.islink(full_path):
                    node_type = "Link"
                    file_extension = "ln"
                    size = 0
                else:
                    node_type = "Other"
                    size = 0
                    file_extension = "NA"

                node_list.append({
                    "ID": node_counter,
                    "TYPE": node_type,
                    "PARENT": parent_id,
                    "HID": is_hidden,
                    "NAME": item,
                    "EXTENSION": file_extension,
                    "PATH": full_path,
                    "SIZE": size
                })
        except PermissionError:
            st.warning(f"Permission denied for: {current_path}. Skipping.")
            node_counter += 1
            node_list.append({
                "ID": node_counter,
                "TYPE": "Dir",
                "PARENT": parent_id,
                "HID": False,
                "NAME": os.path.basename(current_path),
                "EXTENSION": "NA",
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

def display_results():
    """
    Displays the scanned data in a table with filtering and column visibility options,
    and shows a summary of the scan.
    """
    if st.session_state.scan_results is None:
        st.write("Please perform a scan first.")
        return

    nodes = st.session_state.scan_results["nodes"]
    file_types = st.session_state.scan_results["file_types"]
    summary = create_summary(st.session_state.scan_results)

    # Create a DataFrame
    df = pd.DataFrame(nodes)
    df['PARENT_NAME'] = df['PARENT'].apply(lambda x: next((n['NAME'] for n in nodes if n['ID'] == x), None))

     # Apply filters from session state
    filtered_df = df.copy()
    if st.session_state.STAT_MULT_SELECT_TYPE and "Any" not in st.session_state.STAT_MULT_SELECT_TYPE:
        filtered_df = filtered_df[filtered_df["TYPE"].isin(st.session_state.STAT_MULT_SELECT_TYPE)]

    if st.session_state.STAT_MULT_EXTENSION and "Any" not in st.session_state.STAT_MULT_EXTENSION:
        filtered_df = filtered_df[filtered_df["EXTENSION"].isin(st.session_state.STAT_MULT_EXTENSION)]

    # Column visibility
    displayed_columns = []
    if not st.session_state.STAT_HIDE_N:
        displayed_columns.append("ID")
    if not st.session_state.STAT_HIDE_TYPE:
        displayed_columns.append("TYPE")
    if not st.session_state.STAT_HIDE_PARENT:
        displayed_columns.append("PARENT_NAME")
    if not st.session_state.STAT_HIDE_HIDDEN:
        displayed_columns.append("HID")
    if not st.session_state.STAT_HIDE_NAME:
        displayed_columns.append("NAME")
    if not st.session_state.STAT_HIDE_EXTENSION:
        displayed_columns.append("EXTENSION")
    if not st.session_state.STAT_HIDE_PATH:
        displayed_columns.append("PATH")
    if not st.session_state.STAT_HIDE_SIZE:
        displayed_columns.append("SIZE")

    if displayed_columns:
        st.dataframe(filtered_df[displayed_columns], hide_index=True)
    else:
        st.write("No columns selected to display.")

    # Display the summary
    st.subheader("Summary")
    st.write(json.dumps(summary, indent=4))



def main():
    """
    Main function to run the Streamlit application.
    """
    st.set_page_config(layout="wide")
    st.title("File System Scanner")
    init_session_state()

    # --- Sidebar Form ---
    with st.sidebar.form(key="TABLE_FILTER"):
        st.subheader("Table Filter")
        st.session_state.STAT_HIDE_N = st.checkbox("Hide N", value=st.session_state.STAT_HIDE_N)
        st.session_state.STAT_HIDE_TYPE = st.checkbox("Hide Type", value=st.session_state.STAT_HIDE_TYPE)
        st.session_state.STAT_HIDE_PARENT = st.checkbox("Hide Parent", value=st.session_state.STAT_HIDE_PARENT)
        st.session_state.STAT_HIDE_HIDDEN = st.checkbox("Hide Hidden", value=st.session_state.STAT_HIDE_HIDDEN)
        st.session_state.STAT_HIDE_NAME = st.checkbox("Hide Name", value=st.session_state.STAT_HIDE_NAME)
        st.session_state.STAT_HIDE_EXTENSION = st.checkbox("Hide Extension", value=st.session_state.STAT_HIDE_EXTENSION)
        st.session_state.STAT_HIDE_PATH = st.checkbox("Hide Path", value=st.session_state.STAT_HIDE_PATH)
        st.session_state.STAT_HIDE_SIZE = st.checkbox("Hide Size", value=st.session_state.STAT_HIDE_SIZE)
        st.session_state.STAT_SCAN_DIR = st.text_input("Scan Directory", value=st.session_state.STAT_SCAN_DIR)
        st.session_state.STAT_MULT_SELECT_TYPE = st.multiselect(
            "Filter by Type", ["Any", "File", "Dir", "Link"], default=st.session_state.STAT_MULT_SELECT_TYPE
        )
        st.session_state.STAT_MULT_EXTENSION = st.multiselect(
            "Filter by Extension",  st.session_state.STAT_MULT_EXTENSION, default=st.session_state.STAT_MULT_EXTENSION
        )
        show_table_button = st.form_submit_button("Show Table")

    # --- SCAN Button ---
    if st.sidebar.button("Scan"):
        if os.path.exists(st.session_state.STAT_SCAN_DIR):
            st.session_state.scan_results = scan_directory(st.session_state.STAT_SCAN_DIR)
            unique_extensions = ["Any"] + list(set(node["EXTENSION"] for node in st.session_state.scan_results["nodes"] if node["EXTENSION"] != "NA"))
            st.session_state.STAT_MULT_EXTENSION = unique_extensions
            st.session_state.STAT_MULT_SELECT_TYPE = ["Any", "File", "Dir", "Link"]  # Reset type filter
            st.write("Scan Complete.  Click Show Table to View Results")
        else:
            st.error(f"Error: The directory '{st.session_state.STAT_SCAN_DIR}' does not exist.")
            st.session_state.scan_results = None #clear results
    # --- Display Session State ---
    with st.sidebar.expander("Session State"):
        session_state_data = {k: str(v) for k, v in st.session_state.items()}  # Convert values to strings
        st.dataframe(pd.DataFrame(list(session_state_data.items()), columns=['Key', 'Value']))

    if show_table_button:
        display_results()

if __name__ == "__main__":
    main()

