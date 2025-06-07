import streamlit as st
import os
import json
from collections import defaultdict
import polars as pl
import datetime
import time

def initialize_session_state():
    """
    Initializes the session state with default values.
    """
    #default_scan_dir = "/home1/hugo/PycharmProjects/okrocket/cobol/code/aws-mainframe-modernization-carddemo"
    default_scan_dir = "./"
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
        "DISPLAY_PAGE_SIZE": 10, # Default page size.  Added default value here.
        "current_page": 1, # Add this line
        "show_table_submitted": False, # Add this line
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

def display_table_filter_form(n):

    st.markdown("##### SET FORM FILTERS")
    with st.expander("(click to expand / collapse)"):
        """
        Displays the form for filtering the table.
        """
        # Use columns to display checkboxes horizontally
        col1, col2, col3, col4 = st.columns(4)

        st.session_state["STAT_HIDE_N"] = col1.checkbox("HIDE_N", key=f"ck_box_{n}_00", value=st.session_state["STAT_HIDE_N"])
        st.session_state["STAT_HIDE_TYPE"] = col2.checkbox("HIDE_TYPE", key=f"ck_box_{n}_01", value=st.session_state["STAT_HIDE_TYPE"])
        st.session_state["STAT_HIDE_PARENT"] = col3.checkbox("HIDE_PARENT", key=f"ck_box_{n}_02", value=st.session_state["STAT_HIDE_PARENT"])
        st.session_state["STAT_HIDE_HIDDEN"] = col4.checkbox("HIDE_HIDDEN", key=f"ck_box_{n}_03", value=st.session_state["STAT_HIDE_HIDDEN"])

        col5, col6, col7, col8 = st.columns(4)
        st.session_state["STAT_HIDE_NAME"] = col5.checkbox("HIDE_NAME", key=f"ck_box_{n}_04", value=st.session_state["STAT_HIDE_NAME"])
        st.session_state["STAT_HIDE_EXTENSION"] = col6.checkbox("HIDE_EXTENSION", key=f"ck_box_{n}_05", value=st.session_state["STAT_HIDE_EXTENSION"])
        st.session_state["STAT_HIDE_PATH"] = col7.checkbox("HIDE_PATH", key=f"ck_box_{n}_06", value=st.session_state["STAT_HIDE_PATH"])
        st.session_state["STAT_HIDE_SIZE"] = col8.checkbox("HIDE_SIZE", key=f"ck_box_{n}_07", value=st.session_state["STAT_HIDE_SIZE"])
        st.session_state["STAT_MULT_SELECT_TYPE"] = st.multiselect("MULT_SELECT_TYPE",["Any", "File", "Dir", "Link"], key=f"MS_TYPE_{n}", default=st.session_state["STAT_MULT_SELECT_TYPE"])
        st.session_state["STAT_MULT_EXTENSION"] = st.multiselect("MULT_EXTENSION", st.session_state["unique_extensions"], key=f"MS_EXTENSION_{n}", default=st.session_state["STAT_MULT_EXTENSION"])
        st.session_state["DISPLAY_PAGE_SIZE"] = st.number_input("Display Page Size", key=f"NUMBER_INPUT_{n}", min_value=1, value=st.session_state["DISPLAY_PAGE_SIZE"])

    show_table_submitted = st.button("SHOW TABLE", key=f"SHOW_TABLE_{n}" ) # change form_submit_button to button

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

        st.subheader(f"File System Scan Results for directory \"{st.session_state['STAT_SCAN_DIR']}\"")
        st.markdown(f"##### File System Scan Results")
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

        # Create a Polars DataFrame for display
        df = pl.DataFrame(display_data)
        st.session_state["export_df"] = df.to_pandas()  # Store the dataframe to export as Pandas DataFrame

        # Display the dataframe with column auto-sizing
        st.dataframe(df, use_container_width=True)


    elif st.session_state["show_table_submitted"]: # add this condition
        st.info("Please SCAN the directory first.")

def display_scan_resultsi_paginated():
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

        st.subheader(f"File System Scan Results for directory \"{st.session_state['STAT_SCAN_DIR']}\"")
        st.markdown(f"##### File System Scan Results")
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

        # Create a Polars DataFrame for display
        df = pl.DataFrame(display_data)
        st.session_state["export_df"] = df.to_pandas()  # Store the dataframe to export as Pandas DataFrame

        # Display the dataframe with column auto-sizing
        st.dataframe(df, use_container_width=True)


    elif st.session_state["show_table_submitted"]: # add this condition
        st.info("Please SCAN the directory first.")

def handle_save_table():
    """
    Handles the SAVE TABLE button click event.
    """
    if st.session_state["export_df"] is not None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        export_format = st.session_state["export_format"]
        filename = f"fs_scan_{timestamp}.{export_format.lower()}"
        save_path = os.path.join("csv", filename)

        # Ensure the 'csv' directory exists
        if not os.path.exists("csv"):
            try:
                os.makedirs("csv")
                st.success("Created directory 'csv' to save the file.")
            except OSError as e:
                st.error(f"Error creating directory 'csv': {e}")
                return

        try:
            if export_format == "CSV":
                st.session_state["export_df"].to_csv(save_path, index=False)
                st.success(f"Table saved to {save_path}")
            elif export_format == "XML":
                # Create the root element
                root = ET.Element("root")
                # Iterate through the rows of the dataframe
                for _, row in st.session_state["export_df"].iterrows():
                    # Create a new element for each row
                    element = ET.SubElement(root, "row")
                    # Add the columns and values as sub-elements
                    for col, val in row.items():
                        child = ET.SubElement(element, col)
                        child.text = str(val)  # Convert value to string
                # Create an XML string from the root element
                xml_string = ET.tostring(root, encoding="utf-8")
                # Use minidom to pretty print the XML
                parsed_xml = minidom.parseString(xml_string)
                pretty_xml_string = parsed_xml.toprettyxml(indent="  ")
                # Write the XML string to a file
                with open(save_path, "w") as f:
                    f.write(pretty_xml_string)
                st.success(f"Table saved to {save_path}")
            elif export_format == "EXCEL":
                st.session_state["export_df"].to_excel(save_path, index=False)
                st.success(f"Table saved to {save_path}")
        except Exception as e:
            st.error(f"Error saving table to {save_path}: {e}")

    else:
        st.warning("No table data to save. Please scan the directory and display the table first.")


def handle_save_table_old():
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
    Displays the summary of the scan results using Polars.
    """
    if st.session_state["scan_results"]:
        st.markdown("##### SUMMARY")
        # Create a Polars DataFrame
        df = pl.DataFrame(st.session_state["scan_results"])

        # Calculate summary statistics using Polars
        total_nodes = df.height
        total_dirs = df.filter(pl.col("TYPE") == "Dir").height
        total_hidden_dirs = df.filter((pl.col("TYPE") == "Dir") & (pl.col("HID") == True)).height
        total_linked_dirs = df.filter((pl.col("TYPE") == "Link") ).height # Removed the  (pl.col("PATH").is_dir())
        total_files = df.filter(pl.col("TYPE") == "File").height
        total_hidden_files = df.filter((pl.col("TYPE") == "File") & (pl.col("HID") == True)).height
        total_linked_files = df.filter((pl.col("TYPE") == "Link")  ).height # Removed the  (pl.col("PATH").is_file())).height
        total_links = df.filter(pl.col("TYPE") == "Link").height

        # Create a summary DataFrame
        summary_df = pl.DataFrame({
            "Metric": [
                "Total Nodes", "Total Dirs", "Total Hidden Dirs", "Total Linked Dirs",
                "Total Files", "Total Hidden Files", "Total Linked Files", "Total Links"
            ],
            "Value": [
                total_nodes, total_dirs, total_hidden_dirs, total_linked_dirs,
                total_files, total_hidden_files, total_linked_files, total_links
            ]
        })

        # Display the summary DataFrame with column auto-sizing
        st.dataframe(summary_df, use_container_width=True)

def main():
    NO_MAIN = '''
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

    st.session_state["STAT_SCAN_DIR"] = st.text_input("**SCAN_DIR**", value=st.session_state["STAT_SCAN_DIR"])
    st.button("SCAN", on_click=handle_scan_button) # added back
    #display_session_state()

    st.session_state["show_table_submitted"] = display_table_filter_form(0) # call to display form
    display_scan_results()

    if st.button("SAVE TABLE"):
        handle_save_table()
    display_summary()

#if __name__ == "__main__":
#    main()
    '''
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
    st.session_state["show_table_submitted"] = display_table_filter_form(1) # call to display form
    #display_session_state()

    st.session_state["STAT_SCAN_DIR"] = st.text_input("**SCAN_DIR**", value=st.session_state["STAT_SCAN_DIR"])
    st.button("SCAN", on_click=handle_scan_button) # added back

   # st.sidebar.button("SCAN", key="SCAN_BUTTON", on_click=handle_scan_button) # added back
    display_scan_results()
    display_summary()

    st.session_state["export_format"] = st.radio(
        "Export Format",
        ["CSV", "XML", "EXCEL"],  # Options for the radio buttons
        index=0,  # Default to CSV
    )
    if st.button("SAVE TABLE", key="SAVE TABLE"):
        handle_save_table()

if __name__ == "__main__":
    main()

