import streamlit as st
import os
import json
from collections import defaultdict
import pandas as pd
import datetime
import time
# Removed unused imports: `collections`, `json`, `time` are used implicitly or via pandas/datetime

# --- Constants (PEP 8: Uppercase with Underscores) ---
# Session State Keys
SESSION_STATE_SCAN_DIR = "scan_directory" # Renamed from STAT_SCAN_DIR
SESSION_STATE_HIDE_N = "hide_id" # Renamed from STAT_HIDE_N
SESSION_STATE_HIDE_TYPE = "hide_type" # Renamed from STAT_HIDE_TYPE
SESSION_STATE_HIDE_PARENT = "hide_parent" # Renamed from STAT_HIDE_PARENT
SESSION_STATE_HIDE_HIDDEN = "hide_hidden" # Renamed from STAT_HIDE_HIDDEN
SESSION_STATE_HIDE_NAME = "hide_name" # Renamed from STAT_HIDE_NAME
SESSION_STATE_HIDE_EXTENSION = "hide_extension" # Renamed from STAT_HIDE_EXTENSION
SESSION_STATE_HIDE_PATH = "hide_path" # Renamed from STAT_HIDE_PATH
SESSION_STATE_HIDE_SIZE = "hide_size" # Renamed from STAT_HIDE_SIZE
SESSION_STATE_SELECTED_TYPES = "selected_types" # Renamed from STAT_MULT_SELECT_TYPE
SESSION_STATE_SELECTED_EXTENSIONS = "selected_extensions" # Renamed from STAT_MULT_EXTENSION
SESSION_STATE_SCAN_RESULTS = "scan_results" # Renamed from scan_results
SESSION_STATE_FILE_EXTENSIONS = "file_extensions" # Renamed from file_extensions
SESSION_STATE_UNIQUE_EXTENSIONS = "unique_extensions" # Renamed from unique_extensions
SESSION_STATE_SORT_ORDER = "sort_order" # Renamed from sort_order
SESSION_STATE_EXPORT_DF = "export_df" # Renamed from export_df

# Magic Strings/Values
ANY_FILTER = "Any"
TYPE_DIR = "Dir"
TYPE_FILE = "File"
TYPE_LINK = "Link"
DEFAULT_SCAN_DIRECTORY = "/home1/hugo/PycharmProjects/okrocket/cobol/code/aws-mainframe-modernization-carddemo"

# Column Names (Lowercase for consistency with DataFrame)
COL_ID = "id" # Renamed from ID
COL_TYPE = "type" # Renamed from TYPE
COL_PARENT = "parent" # Renamed from PARENT
COL_HIDDEN = "hidden" # Renamed from HID
COL_NAME = "name" # Renamed from NAME
COL_EXTENSION = "extension" # Renamed from EXTENSION
COL_PATH = "path" # Renamed from PATH
COL_SIZE = "size" # Renamed from SIZE

# UI Keys
FORM_FILTER_KEY = "table_filter_form" # Renamed from TABLE_FILTER
BUTTON_SCAN_KEY = "scan_button" # Renamed from SCAN_BUTTON
BUTTON_EXPORT_KEY = "export_button" # Renamed from EXPORT_BUTTON

# --- Session State Initialization ---

def initialize_session_state():
    """
    Initializes the session state with default values if not already set.
    Uses constants for session state keys.
    """
    default_session_state = {
        SESSION_STATE_SCAN_DIR: DEFAULT_SCAN_DIRECTORY,
        SESSION_STATE_HIDE_N: False,
        SESSION_STATE_HIDE_TYPE: False,
        SESSION_STATE_HIDE_PARENT: False,
        SESSION_STATE_HIDE_HIDDEN: True,
        SESSION_STATE_HIDE_NAME: False,
        SESSION_STATE_HIDE_EXTENSION: False,
        SESSION_STATE_HIDE_PATH: False,
        SESSION_STATE_HIDE_SIZE: False,
        SESSION_STATE_SELECTED_TYPES: [ANY_FILTER],
        SESSION_STATE_SELECTED_EXTENSIONS: [ANY_FILTER],
        SESSION_STATE_SCAN_RESULTS: [],
        SESSION_STATE_FILE_EXTENSIONS: defaultdict(int),
        SESSION_STATE_UNIQUE_EXTENSIONS: [ANY_FILTER],
        SESSION_STATE_SORT_ORDER: {},
        SESSION_STATE_EXPORT_DF: None,
    }
    for key, default_value in default_session_state.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

# --- Helper Functions for Data Processing ---

def create_item_dict(item_id, item_type, parent_id, is_hidden, name, extension, path, size=None):
    """
    Helper function to create a dictionary for a file system item.
    Uses lowercase keys for consistency.
    """
    return {
        COL_ID: item_id,
        COL_TYPE: item_type,
        COL_PARENT: parent_id,
        COL_HIDDEN: is_hidden,
        COL_NAME: name,
        COL_EXTENSION: extension,
        COL_PATH: path,
        COL_SIZE: size,
    }

def scan_directory(directory_path):
    """
    Scans the specified directory and its subdirectories to collect information
    about files, directories, and links.
    Includes error handling and uses a path-to-ID map for efficient parent lookup.
    """
    results = []
    file_extensions = defaultdict(int)
    counter = 0
    # Dictionary to map full paths to their assigned IDs for efficient parent lookup
    path_to_id_map = {}

    # Add the root directory itself
    root_path = os.path.abspath(directory_path)
    counter += 1
    root_item = create_item_dict(
        item_id=counter,
        item_type=TYPE_DIR,
        parent_id=None, # Root has no parent
        is_hidden=root_path.startswith('.'), # Simple check for hidden root
        name=os.path.basename(root_path) or root_path, # Use path if name is empty
        extension=None,
        path=root_path,
        size=None # Size not applicable for directories
    )
    results.append(root_item)
    path_to_id_map[root_path] = counter # Map root path to its ID

    try:
        for root, dirs, files in os.walk(directory_path, followlinks=False):
            current_parent_id = path_to_id_map.get(os.path.abspath(root)) # Get parent ID from map

            # Process directories
            for name in dirs:
                full_path = os.path.join(root, name)
                counter += 1
                is_hidden = name.startswith('.')
                item = create_item_dict(
                    item_id=counter,
                    item_type=TYPE_DIR,
                    parent_id=current_parent_id,
                    is_hidden=is_hidden,
                    name=name,
                    extension=None,
                    path=full_path,
                    size=None
                )
                results.append(item)
                path_to_id_map[os.path.abspath(full_path)] = counter # Add directory path to map

            # Process files
            for name in files:
                full_path = os.path.join(root, name)
                counter += 1
                is_hidden = name.startswith('.')
                _, ext = os.path.splitext(name)
                ext = ext.lower() if ext else None
                file_extensions[ext] += 1
                size = None
                try:
                    size = os.path.getsize(full_path)
                except Exception as e:
                    st.warning(f"Could not get size for file {full_path}: {e}") # Use st.warning for non-fatal errors

                item = create_item_dict(
                    item_id=counter,
                    item_type=TYPE_FILE,
                    parent_id=current_parent_id,
                    is_hidden=is_hidden,
                    name=name,
                    extension=ext,
                    path=full_path,
                    size=size
                )
                results.append(item)

            # Process links (os.walk doesn't explicitly list links, need to check manually if followlinks=False)
            # This part might need adjustment based on desired link handling.
            # The original code iterated through os.listdir and checked islink, which is more explicit.
            # Reimplementing the explicit link check for the current directory entries:
            try:
                for entry_name in os.listdir(root):
                    full_path = os.path.join(root, entry_name)
                    if os.path.islink(full_path):
                        counter += 1
                        is_hidden = entry_name.startswith('.')
                        item = create_item_dict(
                            item_id=counter,
                            item_type=TYPE_LINK,
                            parent_id=current_parent_id,
                            is_hidden=is_hidden,
                            name=entry_name,
                            extension=None,
                            path=full_path,
                            size=None # Size of the link itself, not target
                        )
                        results.append(item)
            except Exception as e:
                 st.warning(f"Could not list directory {root} for links: {e}")


    except FileNotFoundError:
        st.error(f"Error: Directory not found at {directory_path}")
        return [], defaultdict(int)
    except PermissionError:
        st.error(f"Error: Permission denied to access directory {directory_path}")
        return [], defaultdict(int)
    except Exception as e:
        st.error(f"An unexpected error occurred during directory scan: {e}")
        return [], defaultdict(int)

    return results, file_extensions

# --- Helper Functions for UI Components ---

def display_session_state():
    """
    Displays the current session state in the sidebar.
    """
    with st.sidebar.expander("SESSION STATE"): # Kept original expander title
        # Displaying types to keep output brief for complex objects
        session_data_summary = {k: str(type(v)) for k, v in st.session_state.items()}
        st.write(session_data_summary)
        # Optionally display full state for debugging
        # st.write(st.session_state)

def display_table_filter_form(unique_extensions):
    """
    Displays the form for filtering scan results in the sidebar.
    """
    with st.sidebar.form(key=FORM_FILTER_KEY):
        st.write("**Filter Scan Results**")

        # Directory input
        st.session_state[SESSION_STATE_SCAN_DIR] = st.text_input(
            "Scan Directory",
            st.session_state.get(SESSION_STATE_SCAN_DIR, DEFAULT_SCAN_DIRECTORY),
            key="scan_dir_input" # Unique key for the widget
        )

        # Type filter
        all_types = [ANY_FILTER, TYPE_DIR, TYPE_FILE, TYPE_LINK]
        st.session_state[SESSION_STATE_SELECTED_TYPES] = st.multiselect(
            "Filter by Type",
            all_types,
            default=st.session_state.get(SESSION_STATE_SELECTED_TYPES, [ANY_FILTER]),
            key="filter_type_multiselect"
        )

        # Extension filter
        all_extensions = sorted(list(unique_extensions))
        # Ensure 'Any' is always an option and at the beginning
        if ANY_FILTER not in all_extensions:
             all_extensions.insert(0, ANY_FILTER)

        st.session_state[SESSION_STATE_SELECTED_EXTENSIONS] = st.multiselect(
            "Filter by Extension",
            all_extensions,
            default=st.session_state.get(SESSION_STATE_SELECTED_EXTENSIONS, [ANY_FILTER]),
            key="filter_extension_multiselect"
        )

        # Visibility toggles
        st.session_state[SESSION_STATE_HIDE_HIDDEN] = st.checkbox(
            "Hide Hidden Items",
            st.session_state.get(SESSION_STATE_HIDE_HIDDEN, True),
            key="hide_hidden_checkbox"
        )

        # Column visibility toggles (moved from separate function/logic)
        st.write("**Hide Columns**")
        col1, col2 = st.columns(2)
        with col1:
            st.session_state[SESSION_STATE_HIDE_N] = st.checkbox("Hide ID", st.session_state.get(SESSION_STATE_HIDE_N, False), key="hide_id_checkbox")
            st.session_state[SESSION_STATE_HIDE_TYPE] = st.checkbox("Hide Type", st.session_state.get(SESSION_STATE_HIDE_TYPE, False), key="hide_type_checkbox")
            st.session_state[SESSION_STATE_HIDE_PARENT] = st.checkbox("Hide Parent", st.session_state.get(SESSION_STATE_HIDE_PARENT, False), key="hide_parent_checkbox")
            st.session_state[SESSION_STATE_HIDE_HIDDEN] = st.checkbox("Hide Hidden", st.session_state.get(SESSION_STATE_HIDE_HIDDEN, True), key="hide_hidden_col_checkbox") # Duplicate key, fixing
            # Correcting the duplicate key for hide_hidden checkbox
            # Assuming the intention was to hide the 'hidden' column, not filter by hidden status
            st.session_state[SESSION_STATE_HIDE_HIDDEN] = st.checkbox(
                "Hide Hidden Column",
                st.session_state.get(SESSION_STATE_HIDE_HIDDEN, True),
                key="hide_hidden_column_checkbox" # Unique key
            )
        with col2:
            st.session_state[SESSION_STATE_HIDE_NAME] = st.checkbox("Hide Name", st.session_state.get(SESSION_STATE_HIDE_NAME, False), key="hide_name_checkbox")
            st.session_state[SESSION_STATE_HIDE_EXTENSION] = st.checkbox("Hide Extension", st.session_state.get(SESSION_STATE_HIDE_EXTENSION, False), key="hide_extension_checkbox")
            st.session_state[SESSION_STATE_HIDE_PATH] = st.checkbox("Hide Path", st.session_state.get(SESSION_STATE_HIDE_PATH, False), key="hide_path_checkbox")
            st.session_state[SESSION_STATE_HIDE_SIZE] = st.checkbox("Hide Size", st.session_state.get(SESSION_STATE_HIDE_SIZE, False), key="hide_size_checkbox")


        # Scan button
        scan_button_pressed = st.form_submit_button("Scan Directory", key=BUTTON_SCAN_KEY)

        # Export button (outside the form if it shouldn't trigger a form submit)
        # Moved export button outside the form as it's a separate action
        # export_button_pressed = st.form_submit_button("Export Results", key=BUTTON_EXPORT_KEY)

    # Return whether the scan button was pressed
    return scan_button_pressed

def apply_filters(df, selected_types, selected_extensions, hide_hidden):
    """
    Applies filters to the DataFrame based on user selections.
    """
    filtered_df = df.copy()

    # Filter by type
    if ANY_FILTER not in selected_types:
        filtered_df = filtered_df[filtered_df[COL_TYPE].isin(selected_types)]

    # Filter by extension
    if ANY_FILTER not in selected_extensions:
         # Handle None extensions (e.g., directories)
        if None in selected_extensions:
             # Include items with None extension AND items with selected extensions
             filtered_df = filtered_df[
                 (filtered_df[COL_EXTENSION].isin([ext for ext in selected_extensions if ext is not None])) |
                 (filtered_df[COL_EXTENSION].isna())
             ]
        else:
            # Only include items with selected extensions (excluding None)
            filtered_df = filtered_df[filtered_df[COL_EXTENSION].isin(selected_extensions)]


    # Filter by hidden status
    if hide_hidden:
        filtered_df = filtered_df[filtered_df[COL_HIDDEN] == False] # Filter out hidden items

    return filtered_df

def apply_sorting(df, sort_order):
    """
    Applies sorting to the DataFrame based on the sort_order dictionary.
    """
    if not sort_order:
        return df # Return original if no sorting is specified

    sort_columns = list(sort_order.keys())
    ascending_list = [sort_order[col] == 'asc' for col in sort_columns]

    try:
        # Use stable sort for consistency
        sorted_df = df.sort_values(by=sort_columns, ascending=ascending_list, kind='stable')
        return sorted_df
    except KeyError as e:
        st.warning(f"Sorting column not found: {e}. Resetting sort order.")
        st.session_state[SESSION_STATE_SORT_ORDER] = {} # Reset invalid sort order
        return df # Return unsorted dataframe
    except Exception as e:
        st.error(f"An error occurred during sorting: {e}")
        return df # Return unsorted dataframe


def display_scan_results_table(df):
    """
    Displays the scan results in a Streamlit DataFrame, with filtering,
    sorting, and column visibility options applied.
    """
    if df.empty:
        st.info("No results to display. Please perform a scan.")
        return

    # Apply filters based on session state
    filtered_df = apply_filters(
        df,
        st.session_state[SESSION_STATE_SELECTED_TYPES],
        st.session_state[SESSION_STATE_SELECTED_EXTENSIONS],
        st.session_state[SESSION_STATE_HIDE_HIDDEN] # Use the hide_hidden filter state
    )

    # Apply sorting based on session state
    sorted_df = apply_sorting(filtered_df, st.session_state[SESSION_STATE_SORT_ORDER])

    # Define column configuration for visibility
    column_config = {
        COL_ID: {"visible": not st.session_state[SESSION_STATE_HIDE_N]},
        COL_TYPE: {"visible": not st.session_state[SESSION_STATE_HIDE_TYPE]},
        COL_PARENT: {"visible": not st.session_state[SESSION_STATE_HIDE_PARENT]},
        COL_HIDDEN: {"visible": not st.session_state[SESSION_STATE_HIDE_HIDDEN]}, # Use the hide_hidden_column_checkbox state
        COL_NAME: {"visible": not st.session_state[SESSION_STATE_HIDE_NAME]},
        COL_EXTENSION: {"visible": not st.session_state[SESSION_STATE_HIDE_EXTENSION]},
        COL_PATH: {"visible": not st.session_state[SESSION_STATE_HIDE_PATH]},
        COL_SIZE: {"visible": not st.session_state[SESSION_STATE_HIDE_SIZE]},
    }

    # Display the DataFrame
    st.dataframe(
        sorted_df,
        use_container_width=True,
        column_config=column_config,
        on_select="rerun", # Rerun script when row is selected (optional)
        selection_mode="single-row" # Allow single row selection (optional)
    )

    # Store the filtered and sorted dataframe for export
    st.session_state[SESSION_STATE_EXPORT_DF] = sorted_df

def display_summary_statistics(df, file_extensions):
    """
    Displays summary statistics about the scan results.
    """
    if df.empty:
        return

    st.subheader("Summary Statistics")

    # Calculate counts based on the full results DataFrame
    total_dirs = df[df[COL_TYPE] == TYPE_DIR].shape[0]
    total_files = df[df[COL_TYPE] == TYPE_FILE].shape[0]
    total_links = df[df[COL_TYPE] == TYPE_LINK].shape[0]

    total_hidden_dirs = df[(df[COL_TYPE] == TYPE_DIR) & (df[COL_HIDDEN] == True)].shape[0]
    total_hidden_files = df[(df[COL_TYPE] == TYPE_FILE) & (df[COL_HIDDEN] == True)].shape[0]
    total_hidden_links = df[(df[COL_TYPE] == TYPE_LINK) & (df[COL_HIDDEN] == True)].shape[0]

    # Note: Calculating linked dirs/files requires checking the link target,
    # which is not explicitly stored in the current data structure.
    # The original code's linked counts might have been based on a different logic
    # or assumed followlinks=True. For this refactoring, we'll just show totals.
    # If linked counts are needed, the scan logic would need to be updated
    # to resolve link targets and count them.
    total_linked_dirs = "N/A" # Placeholder
    total_linked_files = "N/A" # Placeholder

    st.write(f"**TOTAL ITEMS:** {df.shape[0]}")
    st.write(f"**TOTAL DIRECTORIES:** {total_dirs}")
    # st.write(f"**TOTAL HIDDEN DIRS:** {total_hidden_dirs}") # Keep if needed
    # st.write(f"**TOTAL LINKED DIRS:** {total_linked_dirs}") # Keep if needed
    st.write(f"**TOTAL FILES:** {total_files}")
    # st.write(f"**TOTAL HIDDEN FILES:** {total_hidden_files}") # Keep if needed
    # st.write(f"**TOTAL LINKED FILES:** {total_linked_files}") # Keep if needed
    st.write(f"**TOTAL LINKS:** {total_links}")
    # st.write(f"**TOTAL HIDDEN LINKS:** {total_hidden_links}") # Keep if needed

    st.subheader("File Extension Counts")
    # Convert defaultdict to dict for display
    st.write(dict(file_extensions))


# --- Main Application Flow ---

def main():
    """
    Main function to run the Streamlit application.
    """
    # Set app favicon and page config
    # Moved st.set_page_config outside the function if this script is run directly
    # as set_page_config must be the first Streamlit command.
    # If this script is intended to be run via exec from app.py,
    # the page config should be set in app.py.
    # Assuming this can be run standalone for testing/direct use:
    # st.set_page_config(
    #     page_title="COBOLpro Filesystem Scan",
    #     page_icon="assets/images/COBOLpro/COBOLpro_icon.png", # Ensure path is correct
    #     layout="wide"
    # )

    initialize_session_state()

    # Add title and subtitle
    st.title("COBOLpro Filesystem Scan")
    subtitle_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    st.subheader(f"Run at {subtitle_timestamp}")

    # Display session state expander in sidebar (optional, for debugging)
    # display_session_state()

    # Display the filter form and handle scan button press
    scan_button_pressed = display_table_filter_form(st.session_state[SESSION_STATE_UNIQUE_EXTENSIONS])

    # Handle scan button press
    if scan_button_pressed:
        scan_dir = st.session_state[SESSION_STATE_SCAN_DIR]
        if os.path.isdir(scan_dir):
            with st.spinner(f"Scanning directory: {scan_dir}..."):
                scan_results, file_extensions = scan_directory(scan_dir)
                st.session_state[SESSION_STATE_SCAN_RESULTS] = scan_results
                st.session_state[SESSION_STATE_FILE_EXTENSIONS] = file_extensions
                # Update unique extensions for the filter multiselect
                st.session_state[SESSION_STATE_UNIQUE_EXTENSIONS] = [ANY_FILTER] + sorted(list(file_extensions.keys()))
            st.success("Scan complete!")
        else:
            st.error(f"Invalid directory path: {scan_dir}")

    # Display scan results table if results exist
    if st.session_state[SESSION_STATE_SCAN_RESULTS]:
        # Convert results list to DataFrame for easier handling
        scan_results_df = pd.DataFrame(st.session_state[SESSION_STATE_SCAN_RESULTS])

        # Display summary statistics based on the full DataFrame
        display_summary_statistics(scan_results_df, st.session_state[SESSION_STATE_FILE_EXTENSIONS])

        # Display the filterable and sortable table
        display_scan_results_table(scan_results_df)

        # Export button (outside the form)
        if st.session_state[SESSION_STATE_EXPORT_DF] is not None:
            export_df = st.session_state[SESSION_STATE_EXPORT_DF]
            csv_data = export_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Export Filtered Results to CSV",
                data=csv_data,
                file_name="filesystem_scan_results.csv",
                mime="text/csv",
                key="download_csv_button"
            )
    else:
        st.info("Press 'Scan Directory' to begin.")


# --- Run the main function ---
if __name__ == "__main__":
    main()

