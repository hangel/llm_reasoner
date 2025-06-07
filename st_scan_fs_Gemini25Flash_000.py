import streamlit as st
import os
import json
from collections import defaultdict
import pandas as pd
import datetime
import time

def initialize_session_state():
    """
    Initializes the session state with default values.
    """
    default_scan_dir = "/home1/hugo/PycharmProjects/okrocket/cobol/code/aws-mainframe-modernization-carddemo"
    default_session_state = {
        "STAT_SCAN_DIR": default_scan_dir,
        "STAT_HIDE_N": False,
        "STAT_HIDE_TYPE": False,
        "STAT_HIDE_PARENT": False,
        "STAT_HIDE_HIDDEN": True,
        "STAT_HIDE_NAME": False,
        "STAT_HIDE_EXTENSION": False,
        "STAT_HIDE_PATH": False,
        "STAT_HIDE_SIZE": False,
        "STAT_MULT_SELECT_TYPE": ["Any"],
        "STAT_MULT_EXTENSION": ["Any"],
        "scan_results": [],
        "file_extensions": defaultdict(int),
        "unique_extensions": ["Any"],
        "sort_order": {},  # Store sort order
        "export_df": None,  # Store the dataframe to export
    }
    for key, default_value in default_session_state.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

def display_session_state():
    """
    Displays the current session state in the sidebar.
    """
    with st.sidebar.expander("SESSION_STATE"):
        session_data = {k: str(v) for k, v in st.session_state.items()}
        st.table(session_data)

def scan_directory(directory):
    """
    Recursively scans the directory and returns the file information.

    Args:
        directory (str): The directory to scan.

    Returns:
        tuple: (list of file information dictionaries, dictionary of file extensions)
    """
    results = []
    counter = 0
    extensions = defaultdict(int)
    try:
        for root, dirs, files in os.walk(directory):
            for name in dirs:
                counter += 1
                full_path = os.path.join(root, name)
                parent_path = os.path.dirname(full_path)
                parent_id = next((item["ID"] for item in results if item["PATH"] == parent_path), None)
                is_hidden = name.startswith('.')
                try:
                    results.append({
                        "ID": counter,
                        "TYPE": "Dir",
                        "PARENT": parent_id,
                        "HID": is_hidden,
                        "NAME": name,
                        "EXTENSION": "",
                        "PATH": full_path,
                        "SIZE": 0  # Size is 0 for directories
                    })
                except Exception as e:
                    st.error(f"Error processing directory {full_path}: {e}")

            for name in files:
                counter += 1
                full_path = os.path.join(root, name)
                parent_path = os.path.dirname(full_path)
                parent_id = next((item["ID"] for item in results if item["PATH"] == parent_path), None)
                is_hidden = name.startswith('.')
                _, ext = os.path.splitext(name)
                extensions[ext.lower()] += 1
                try:
                    size = os.path.getsize(full_path)
                except OSError:
                    size = 0
                try:
                    results.append({
                        "ID": counter,
                        "TYPE": "File",
                        "PARENT": parent_id,
                        "HID": is_hidden,
                        "NAME": name,
                        "EXTENSION": ext.lower()[1:] if ext else "",
                        "PATH": full_path,
                        "SIZE": size
                    })
                except Exception as e:
                    st.error(f"Error processing file {full_path}: {e}")
            for name in [os.path.join(root, x) for x in os.listdir(root) if os.path.islink(os.path.join(root, x))]:
                counter += 1
                parent_path = os.path.dirname(name)
                parent_id = next((item["ID"] for item in results if item["PATH"] == parent_path), None)
                is_hidden = os.path.basename(name).startswith('.')
                try:
                    results.append({
                        "ID": counter,
                        "TYPE": "Link",
                        "PARENT": parent_id,
                        "HID": is_hidden,
                        "NAME": os.path.basename(name),
                        "EXTENSION": "",
                        "PATH": name,
                        "SIZE": 0  # Size is 0 for links
                    })
                except Exception as e:
                    st.error(f"Error processing link {name}: {e}")
        return results, extensions
    except Exception as e:
        st.error(f"Error scanning directory {directory}: {e}")
        return [], {}

def handle_scan_button():
    """
    Handles the SCAN button click event.
    """
    with st.spinner("Scanning directory..."):
        st.session_state["scan_results"], st.session_state["file_extensions"] = scan_directory(st.session_state["STAT_SCAN_DIR"])
        st.session_state["unique_extensions"] = ["Any"] + sorted(st.session_state["file_extensions"].keys())
        st.session_state["STAT_MULT_EXTENSION"] = st.session_state["unique_extensions"]

def display_table_filter_form():
    """
    Displays the form for filtering the table.
    """
    with st.sidebar.form(key="TABLE_FILTER"):
        st.session_state["STAT_HIDE_N"] = st.checkbox("HIDE_N", value=st.session_state["STAT_HIDE_N"])
        st.session_state["STAT_HIDE_TYPE"] = st.checkbox("HIDE_TYPE", value=st.session_state["STAT_HIDE_TYPE"])
        st.session_state["STAT_HIDE_PARENT"] = st.checkbox("HIDE_PARENT", value=st.session_state["STAT_HIDE_PARENT"])
        st.session_state["STAT_HIDE_HIDDEN"] = st.checkbox("HIDE_HIDDEN", value=st.session_state["STAT_HIDE_HIDDEN"])
        st.session_state["STAT_HIDE_NAME"] = st.checkbox("HIDE_NAME", value=st.session_state["STAT_HIDE_NAME"])
        st.session_state["STAT_HIDE_EXTENSION"] = st.checkbox("HIDE_EXTENSION", value=st.session_state["STAT_HIDE_EXTENSION"])
        st.session_state["STAT_HIDE_PATH"] = st.checkbox("HIDE_PATH", value=st.session_state["STAT_HIDE_PATH"])
        st.session_state["STAT_HIDE_SIZE"] = st.checkbox("HIDE_SIZE", value=st.session_state["STAT_HIDE_SIZE"])
        st.session_state["STAT_SCAN_DIR"] = st.text_input("SCAN_DIR", value=st.session_state["STAT_SCAN_DIR"])
        st.session_state["STAT_MULT_SELECT_TYPE"] = st.multiselect("MULT_SELECT_TYPE", ["Any", "File", "Dir", "Link"], default=st.session_state["STAT_MULT_SELECT_TYPE"])
        st.session_state["STAT_MULT_EXTENSION"] = st.multiselect("MULT_EXTENSION", st.session_state["unique_extensions"], default=st.session_state["STAT_MULT_EXTENSION"])
        show_table_submitted = st.form_submit_button("SHOW TABLE")
    st.sidebar.write("Updated MULT_EXTENSION:")
    st.sidebar.write(st.session_state["STAT_MULT_EXTENSION"])
    return show_table_submitted

def display_scan_results():
    """
    Displays the filtered scan results in a table.
    """
    if st.session_state["scan_results"]:
        filtered_results = st.session_state["scan_results"]

        # Apply Type filter
        if "Any" not in st.session_state["STAT_MULT_SELECT_TYPE"]:
            filtered_results = [item for item in filtered_results if item["TYPE"] in st.session_state["STAT_MULT_SELECT_TYPE"]]

        # Apply Extension filter
        if "Any" not in st.session_state["STAT_MULT_EXTENSION"]:
            filtered_results = [item for item in filtered_results if item["EXTENSION"] in [ext.lower() for ext in st.session_state["STAT_MULT_EXTENSION"] if ext != "Any"]]

        st.subheader("File System Scan Results")
        display_data = []
        for i, item in enumerate(filtered_results):
            display_item = {}
            if not st.session_state["STAT_HIDE_N"]:
                display_item["N"] = i + 1
            if not st.session_state["STAT_HIDE_TYPE"]:
                display_item["TYPE"] = item["TYPE"]
            if not st.session_state["STAT_HIDE_PARENT"]:
                parent_name = next((r["NAME"] for r in st.session_state["scan_results"] if r["ID"] == item["PARENT"]), None)
                display_item["PARENT"] = parent_name
            if not st.session_state["STAT_HIDE_HIDDEN"]:
                display_item["HID"] = item["HID"]
            if not st.session_state["STAT_HIDE_NAME"]:
                display_item["NAME"] = item["NAME"]
            if not st.session_state["STAT_HIDE_EXTENSION"]:
                display_item["FILETYPE"] = item["EXTENSION"]
            if not st.session_state["STAT_HIDE_PATH"]:
                display_item["PATH"] = item["PATH"]
            if not st.session_state["STAT_HIDE_SIZE"]:
                display_item["SIZE"] = item["SIZE"] if item["TYPE"] == "File" else 0  # Ensure size is always an int
            display_data.append(display_item)

        # Create a Pandas DataFrame for sorting and exporting
        df = pd.DataFrame(display_data)
        st.session_state["export_df"] = df  # store the df

        # Add sorting functionality
        columns = df.columns
        NO_SORT = '''
        selected_column = st.selectbox("Select a column to sort:", columns)
        if selected_column:
            if selected_column in st.session_state["sort_order"]:
                if st.session_state["sort_order"][selected_column] == "asc":
                    sort_direction = "desc"
                else:
                    sort_direction = "asc"
            else:
                sort_direction = "asc"
            st.session_state["sort_order"][selected_column] = sort_direction

            if sort_direction == "asc":
                df = df.sort_values(by=selected_column, ascending=True)
            else:
                df = df.sort_values(by=selected_column, ascending=False)
        '''
        # Display the table
        st.dataframe(df)
    elif st.session_state["show_table_submitted"]: # add this condition
        st.info("Please SCAN the directory first.")

def handle_save_table():
    """
    Handles the SAVE TABLE button click event.
    """
    if st.session_state["export_df"] is not None: # check if there is data to save
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"fs_scan_{timestamp}.csv"
        save_path = os.path.join("csv", filename)  # Saves to a 'csv' subdirectory

        # Ensure the 'csv' directory exists
        if not os.path.exists("csv"):
            try:
                os.makedirs("csv")
                st.success("Created directory 'csv' to save the file.")
            except OSError as e:
                st.error(f"Error creating directory 'csv': {e}")
                return  # Stop if directory creation fails

        try:
            st.session_state["export_df"].to_csv(save_path, index=False)
            st.success(f"Table saved to {save_path}")
        except Exception as e:
            st.error(f"Error saving table to {save_path}: {e}")
    else:
        st.warning("No table data to save. Please scan the directory and display the table first.")

def display_summary():
    """
    Displays the summary of the scan results.
    """
    if st.session_state["scan_results"]:
        st.subheader("SUMMARY")
        total_nodes = len(st.session_state["scan_results"])
        total_dirs = sum(1 for item in st.session_state["scan_results"] if item["TYPE"] == "Dir")
        total_hidden_dirs = sum(1 for item in st.session_state["scan_results"] if item["TYPE"] == "Dir" and item["HID"])
        total_linked_dirs = sum(1 for item in st.session_state["scan_results"] if item["TYPE"] == "Link" and os.path.isdir(item["PATH"]))
        total_files = sum(1 for item in st.session_state["scan_results"] if item["TYPE"] == "File")
        total_hidden_files = sum(1 for item in st.session_state["scan_results"] if item["TYPE"] == "File" and item["HID"])
        total_linked_files = sum(1 for item in st.session_state["scan_results"] if item["TYPE"] == "Link" and os.path.isfile(item["PATH"]))
        total_links = sum(1 for item in st.session_state["scan_results"] if item["TYPE"] == "Link")

        st.write(f"**TOTAL NODES:** {total_nodes}")
        st.write(f"**TOTAL DIRS:** {total_dirs}")
        st.write(f"**TOTAL HIDDEN DIRS:** {total_hidden_dirs}")
        st.write(f"**TOTAL LINKED DIRS:** {total_linked_dirs}")
        st.write(f"**TOTAL FILES:** {total_files}")
        st.write(f"**TOTAL HIDDEN FILES:** {total_hidden_files}")
        st.write(f"**TOTAL LINKED FILES:** {total_linked_files}")
        st.write(f"**TOTAL LINKS:** {total_links}")

def main():
    """
    Main function to run the Streamlit application.
    """
    # Set app favicon
    PAGE__CONFIG_NO = """
    st.set_page_config(page_title="COBOLpro Filesystem Scan", page_icon="assets/images/COBOLpro/COBOLpro_icon.png", layout="wide")
    """

    initialize_session_state()
    # Add title and subtitle
    st.title("COBOLpro Filesystem Scan")
    subtitle_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    st.subheader(f"Run at {subtitle_timestamp}")
    #display_session_state()

    NO_SIDEBAR = """
    # Add image and caption to the sidebar
    st.sidebar.image("assets/images/COBOLpro/COBOLpro_QR.png", width=250)
    st.sidebar.caption(
        '''
        OKRocket® Platform COBOLpro \n
        MVP Preview v0.0.0.1 [2025/04/29]
        '''
        help="For demonstration purposes only",
    )
    """


    st.sidebar.button("SCAN", on_click=handle_scan_button)
    st.session_state["show_table_submitted"] = display_table_filter_form() # capture the return value
    display_scan_results()
    if st.button("SAVE TABLE"):
        handle_save_table()
    display_summary()

if __name__ == "__main__":
    main()

