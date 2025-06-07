import streamlit as st
import os
import json
import pandas as pd
from collections import Counter
from typing import Optional, List, Dict, Any

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
    node_counter = 0
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
            node_counter += 1
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
            summary["TOTAL LINKS"] +=1

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

    # Column visibility
    show_n = st.sidebar.checkbox("Show N", value=True)
    show_type = st.sidebar.checkbox("Show Type", value=True)
    show_parent = st.sidebar.checkbox("Show Parent", value=True)
    show_hid = st.sidebar.checkbox("Show Hidden", value=True)
    show_name = st.sidebar.checkbox("Show Name", value=True)
    show_filetype = st.sidebar.checkbox("Show Filetype", value=True)
    show_path = st.sidebar.checkbox("Show Path", value=True)
    show_size = st.sidebar.checkbox("Show Size", value=True)

    # Filters
    type_filter = st.sidebar.selectbox("Filter by Type", ["Any", "File", "Dir", "Link"])
    filetype_filter = st.sidebar.multiselect("Filter by Filetype", file_types)

    # Apply filters
    filtered_df = df.copy()  # Start with a copy to avoid modifying the original
    if type_filter != "Any":
        filtered_df = filtered_df[filtered_df["TYPE"] == type_filter]
    if filetype_filter:
        filtered_df = filtered_df[filtered_df["FILETYPE"].isin(filetype_filter)]

    # Display the table
    displayed_columns = []
    if show_n:
        displayed_columns.append("ID")
    if show_type:
        displayed_columns.append("TYPE")
    if show_parent:
        displayed_columns.append("PARENT_NAME")  # Use the helper column
    if show_hid:
        displayed_columns.append("HID")
    if show_name:
        displayed_columns.append("NAME")
    if show_filetype:
        displayed_columns.append("FILETYPE")
    if show_path:
        displayed_columns.append("PATH")
    if show_size:
        displayed_columns.append("SIZE")
    if displayed_columns: #check if any column is selected
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
    st.title("File System Scanner")
    start_dir = st.text_input("Enter the starting directory to scan:", ".") # "." is current dir
    if st.button("Scan"):
        if start_dir:
          if os.path.exists(start_dir):
            results = scan_directory(start_dir)
            display_results(results)
          else:
            st.error(f"Error: The directory '{start_dir}' does not exist.")
        else:
            st.error("Please enter a starting directory.")

if __name__ == "__main__":
    main()

