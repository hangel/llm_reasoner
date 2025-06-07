import streamlit as st
import os
import pandas as pd
from pathlib import Path
import json

# Set page to wide layout
st.set_page_config(layout="wide")

# Initialize session state variables if not present
if "STAT_SCAN_DIR" not in st.session_state:
    st.session_state.STAT_SCAN_DIR = "/home1/hugo/PycharmProjects/okrocket/cobol/code/aws-mainframe-modernization-carddemo"
if "STAT_HIDE_N" not in st.session_state:
    st.session_state.STAT_HIDE_N = False
if "STAT_HIDE_TYPE" not in st.session_state:
    st.session_state.STAT_HIDE_TYPE = False
if "STAT_HIDE_PARENT" not in st.session_state:
    st.session_state.STAT_HIDE_PARENT = False
if "STAT_HIDE_HIDDEN" not in st.session_state:
    st.session_state.STAT_HIDE_HIDDEN = True
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
if "scan_results" not in st.session_state:
    st.session_state.scan_results = None
if "extension_counts" not in st.session_state:
    st.session_state.extension_counts = {}

# Function to check if a file/directory is hidden
def is_hidden(path):
    name = os.path.basename(path)
    return name.startswith('.') or (os.name == 'nt' and os.stat(path).st_file_attributes & 2)

# Function to scan directory recursively
def scan_directory(start_dir):
    results = []
    node_id = 0
    extensions = set()
    
    summary = {
        "TOTAL_NODES": 0,
        "TOTAL_DIRS": 0,
        "TOTAL_HIDDEN_DIRS": 0,
        "TOTAL_LINKED_DIRS": 0,
        "TOTAL_FILES": 0,
        "TOTAL_HIDDEN_FILES": 0,
        "TOTAL_LINKED_FILES": 0,
        "TOTAL_LINKS": 0
    }
    
    extension_counts = {}
    
    def scan_node(path, parent_id):
        nonlocal node_id, extensions
        
        try:
            current_id = node_id
            node_id += 1
            
            summary["TOTAL_NODES"] += 1
            
            path_obj = Path(path)
            is_symlink = path_obj.is_symlink()
            
            if is_symlink:
                summary["TOTAL_LINKS"] += 1
            
            if path_obj.is_dir():
                node_type = "Dir"
                size = 0
                extension = ""
                
                summary["TOTAL_DIRS"] += 1
                
                if is_hidden(path):
                    summary["TOTAL_HIDDEN_DIRS"] += 1
                
                if is_symlink:
                    summary["TOTAL_LINKED_DIRS"] += 1
                
                results.append({
                    "ID": current_id,
                    "TYPE": node_type,
                    "PARENT": parent_id,
                    "HID": is_hidden(path),
                    "NAME": os.path.basename(path),
                    "EXTENSION": extension,
                    "PATH": path,
                    "SIZE": size
                })
                
                try:
                    for child in os.listdir(path):
                        scan_node(os.path.join(path, child), current_id)
                except (PermissionError, FileNotFoundError):
                    pass
                    
            else:  # File
                node_type = "File"
                try:
                    size = os.path.getsize(path)
                except (FileNotFoundError, PermissionError):
                    size = 0
                
                name = os.path.basename(path)
                extension = os.path.splitext(name)[1].lower()[1:] if '.' in name else ""
                
                if extension:
                    extensions.add(extension)
                    extension_counts[extension] = extension_counts.get(extension, 0) + 1
                
                summary["TOTAL_FILES"] += 1
                
                if is_hidden(path):
                    summary["TOTAL_HIDDEN_FILES"] += 1
                
                if is_symlink:
                    summary["TOTAL_LINKED_FILES"] += 1
                
                results.append({
                    "ID": current_id,
                    "TYPE": node_type,
                    "PARENT": parent_id,
                    "HID": is_hidden(path),
                    "NAME": name,
                    "EXTENSION": extension,
                    "PATH": path,
                    "SIZE": size
                })
                
        except Exception as e:
            st.error(f"Error scanning {path}: {str(e)}")
    
    try:
        start_dir = os.path.abspath(start_dir)
        scan_node(start_dir, -1)
    except Exception as e:
        st.error(f"Error starting scan: {str(e)}")
    
    return results, list(extensions), extension_counts, summary

# Function to filter the scan results
def filter_results(results, type_filter, extension_filter):
    filtered = results.copy()
    
    if "Any" not in type_filter:
        filtered = [item for item in filtered if item["TYPE"] in type_filter]
    
    if "Any" not in extension_filter:
        filtered = [item for item in filtered if item["EXTENSION"] in extension_filter]
    
    return filtered

# Display session state in sidebar expander
with st.sidebar.expander("SESSION_STATE"):
    session_data = {key: value for key, value in st.session_state.items()}
    session_df = pd.DataFrame(list(session_data.items()), columns=["Name", "Value"])
    st.dataframe(session_df)

# Sidebar form for table filters
with st.sidebar.form(key="TABLE_FILTER"):
    st.header("Table Filter Settings")
    
    # Checkbox widgets for hiding columns
    col1, col2 = st.columns(2)
    
    with col1:
        hide_n = st.checkbox("Hide N", value=st.session_state.STAT_HIDE_N)
        hide_type = st.checkbox("Hide Type", value=st.session_state.STAT_HIDE_TYPE)
        hide_parent = st.checkbox("Hide Parent", value=st.session_state.STAT_HIDE_PARENT)
        hide_hidden = st.checkbox("Hide Hidden", value=st.session_state.STAT_HIDE_HIDDEN)
    
    with col2:
        hide_name = st.checkbox("Hide Name", value=st.session_state.STAT_HIDE_NAME)
        hide_extension = st.checkbox("Hide Extension", value=st.session_state.STAT_HIDE_EXTENSION)
        hide_path = st.checkbox("Hide Path", value=st.session_state.STAT_HIDE_PATH)
        hide_size = st.checkbox("Hide Size", value=st.session_state.STAT_HIDE_SIZE)
    
    # Directory path input
    scan_dir = st.text_input("Directory to Scan", value=st.session_state.STAT_SCAN_DIR)
    
    # Type and Extension multiselect
    available_types = ["Any", "File", "Dir"]
    mult_select_type = st.multiselect(
        "Select Types", 
        options=available_types,
        default=st.session_state.STAT_MULT_SELECT_TYPE
    )
    
    # Dynamic options for extensions based on scan results
    extension_options = ["Any"]
    if "extension_list" in st.session_state:
        extension_options.extend(st.session_state.extension_list)
    
    mult_extension = st.multiselect(
        "Select Extensions",
        options=extension_options,
        default=st.session_state.STAT_MULT_EXTENSION
    )
    
    # Submit button
    show_table_button = st.form_submit_button("SHOW TABLE")
    
    # Update session state when form is submitted
    if show_table_button:
        st.session_state.STAT_HIDE_N = hide_n
        st.session_state.STAT_HIDE_TYPE = hide_type
        st.session_state.STAT_HIDE_PARENT = hide_parent
        st.session_state.STAT_HIDE_HIDDEN = hide_hidden
        st.session_state.STAT_HIDE_NAME = hide_name
        st.session_state.STAT_HIDE_EXTENSION = hide_extension
        st.session_state.STAT_HIDE_PATH = hide_path
        st.session_state.STAT_HIDE_SIZE = hide_size
        st.session_state.STAT_SCAN_DIR = scan_dir
        st.session_state.STAT_MULT_SELECT_TYPE = mult_select_type
        st.session_state.STAT_MULT_EXTENSION = mult_extension

# Scan button outside the form
if st.sidebar.button("SCAN"):
    with st.spinner("Scanning directory..."):
        try:
            results, extension_list, extension_counts, summary = scan_directory(st.session_state.STAT_SCAN_DIR)
            
            st.session_state.scan_results = results
            st.session_state.extension_list = extension_list
            st.session_state.extension_counts = extension_counts
            st.session_state.summary = summary
            
            # Update extension options
            st.session_state.STAT_MULT_EXTENSION = ["Any"] + extension_list
            
            st.success(f"Scan complete! Found {len(results)} items.")
        except Exception as e:
            st.error(f"Error during scan: {str(e)}")

# Main content area
st.title("File System Explorer")

# Display extension summary if available
if "extension_counts" in st.session_state and st.session_state.extension_counts:
    with st.expander("Extension Summary"):
        ext_data = [(ext, count) for ext, count in st.session_state.extension_counts.items()]
        ext_df = pd.DataFrame(ext_data, columns=["Extension", "Count"])
        ext_df = ext_df.sort_values(by="Count", ascending=False)
        st.dataframe(ext_df)

# Display scan results if available
if "scan_results" in st.session_state and st.session_state.scan_results:
    # Filter results based on selection
    filtered_results = filter_results(
        st.session_state.scan_results,
        st.session_state.STAT_MULT_SELECT_TYPE,
        st.session_state.STAT_MULT_EXTENSION
    )
    
    # Create a DataFrame from the filtered results
    df = pd.DataFrame(filtered_results)
    
    # Rename columns for display
    df_display = df.rename(columns={
        "ID": "N",
        "TYPE": "TYPE",
        "PARENT": "PARENT",
        "HID": "HID",
        "NAME": "NAME",
        "EXTENSION": "FILETYPE",
        "PATH": "PATH",
        "SIZE": "SIZE"
    })
    
    # Remove columns based on hide settings
    columns_to_display = []
    
    if not st.session_state.STAT_HIDE_N:
        columns_to_display.append("N")
    if not st.session_state.STAT_HIDE_TYPE:
        columns_to_display.append("TYPE")
    if not st.session_state.STAT_HIDE_PARENT:
        columns_to_display.append("PARENT")
    if not st.session_state.STAT_HIDE_HIDDEN:
        columns_to_display.append("HID")
    if not st.session_state.STAT_HIDE_NAME:
        columns_to_display.append("NAME")
    if not st.session_state.STAT_HIDE_EXTENSION:
        columns_to_display.append("FILETYPE")
    if not st.session_state.STAT_HIDE_PATH:
        columns_to_display.append("PATH")
    if not st.session_state.STAT_HIDE_SIZE:
        columns_to_display.append("SIZE")
    
    # Show the filtered dataframe
    st.dataframe(df_display[columns_to_display], use_container_width=True)
    
    # Display summary
    if "summary" in st.session_state:
        with st.expander("Summary Statistics"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Nodes", st.session_state.summary["TOTAL_NODES"])
                st.metric("Total Dirs", st.session_state.summary["TOTAL_DIRS"])
                st.metric("Total Hidden Dirs", st.session_state.summary["TOTAL_HIDDEN_DIRS"])
            
            with col2:
                st.metric("Total Files", st.session_state.summary["TOTAL_FILES"])
                st.metric("Total Hidden Files", st.session_state.summary["TOTAL_HIDDEN_FILES"])
                st.metric("Total Links", st.session_state.summary["TOTAL_LINKS"])
            
            with col3:
                st.metric("Total Linked Dirs", st.session_state.summary["TOTAL_LINKED_DIRS"])
                st.metric("Total Linked Files", st.session_state.summary["TOTAL_LINKED_FILES"])
else:
    st.info("Click the SCAN button to scan the specified directory.")
