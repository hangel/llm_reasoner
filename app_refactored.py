# https://github.com/PablocFonseca/streamlit-aggrid
import streamlit as st
import pandas as pd # Imported but not used in the provided snippet
import os
import sys
import socket
from PIL import Image # Imported but not used in the provided snippet
from datetime import datetime
from pathlib import Path

# --- Configuration ---
MVP_VERSION = "0.0.0.12"
# PG_CONFIG is defined but empty and not used.
PG_CONFIG = """
"""

# File paths for assets
ASSETS_DIR = "assets/images"
COBOLAGENCY_VERTICAL_LOGO = os.path.join(ASSETS_DIR, "COBOLagency/COBOL_FullLockup-White_VERTICAL.png")
COBOLPRO_VERTICAL_LOGO = os.path.join(ASSETS_DIR, "COBOLpro/COBOLpro_Vertical_FullLockup.png")
COBOLAGENCY_QR = os.path.join(ASSETS_DIR, "COBOLagency/COBOLagency_QR.png")
COBOLPRO_QR = os.path.join(ASSETS_DIR, "COBOLpro/COBOLpro_QR.png")
OLLAMA_LOGO = os.path.join(ASSETS_DIR, "OllamaLogo_S.png") # Imported but not used in the provided snippet
OKROCKET_LOGO = os.path.join(ASSETS_DIR, "OKRocket_Rocket_Logo.png") # Imported but not used in the provided snippet
OKR_LOGO_3x3 = os.path.join(ASSETS_DIR, "OKR_VerdeMosaico_3x3.png") # Imported but not used in the provided snippet

# Default QR code to display
DEFAULT_QR_CODE = COBOLPRO_QR

# Define the root directory of the application
APP_ROOT = os.path.join(os.path.dirname(__file__))

# Dictionary mapping module names to their file paths
MODULE_DASHBOARDS = {
    "**ST_GROQ_DOCUMENTER**": os.path.join(APP_ROOT, "st_groq_documenter_refactored.py"),
    "**SCAN FILESYSTEM**": os.path.join(APP_ROOT, "st_scan_fs_Gemini25Flash_000_refactored.py"),
    "**CLIP_MVP**": os.path.join(APP_ROOT, "st_CLIP_MVP_Flash25_000_refactored.py"),
}

# System Tables information (centralized constant)
SYSTEM_TABLES_INFO = [
    {'table': 'sqlite_master', 'description': 'Master listing of all database objects in the database and the SQL used to create each object.'},
    {'table': 'sqlite_sequence', 'description': 'Lists the last sequence number used for the AUTOINCREMENT column in a table. The sqlite_sequence table will only be created once an AUTOINCREMENT column has been defined in the database and at least one sequence number value has been generated and used in the database.'},
    {'table': 'sqlite_stat1', 'description': 'This table is created by the ANALYZE command to store statistical information about the tables and indexes analyzed. This information will be later used by the query optimizer.'}
]

# --- Page Configuration ---
st.set_page_config(
    page_title=f"COBOLpro Preview by OKRocket® Platform v{MVP_VERSION}",
    page_icon=os.path.join(ASSETS_DIR, "COBOLpro/COBOLpro_icon.png"),
    layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': f"[**COBOL**__pro__](https://www.cobolpro.com) SERVICES MVP v{MVP_VERSION} Preview!"
    }
)

# --- Helper Functions ---

def get_local_ip_and_port():
    """
    Attempts to get the local network IP address and a socket port
    by connecting to an external address.
    Returns a tuple (ip_address, port) or (None, None) if an error occurs.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        socket_port = s.getsockname()[1]
        s.close()
        return ip_address, socket_port
    except Exception as e:
        st.error(f"Could not determine local IP and port: {e}")
        return None, None

def generate_execution_data_markdown(hostname, ip_address, socket_port, streamlit_version, python_version_info, python_path, python_abspath, script_name, headers):
    """
    Generates a markdown table string with execution data.
    """
    current_datetime_formatted = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return f"""
|    PARAM   |     VALUE    |
|------------|--------------|
| **DATE:** | _{current_datetime_formatted}_ |
| **HOST:** | _{hostname}_ |
| **IP:** | _{ip_address}_ |
| **SOCKET:**| _{socket_port}_ |
| **ST_VER** | {streamlit_version} |
| **PY_VER** | {python_version_info.major}.{python_version_info.minor}.{python_version_info.micro} |
| **PY_PATH** | {python_path} |
| **PY_ABSPATH** | {python_abspath} |
| **PY_SCR** | {script_name} |
| **USER-AGENT** | {headers.get("User-Agent", "N/A")} |
| **HEADERS** | {headers} |
"""

def render_sidebar(logo_path, caption, module_options, initial_module_key):
    """
    Renders the sidebar content including logo, execution data,
    session state, and module selector.
    """
    # Get execution details
    hostname = socket.gethostname()
    ip_address, socket_port = get_local_ip_and_port()
    streamlit_version = st.__version__
    python_version_info = sys.version_info
    python_path = Path.cwd()
    python_abspath = os.path.abspath(__file__)
    script_name = os.path.basename(__file__)
    headers = st.context.headers

    # Store python path in session state
    st.session_state['python_path'] = str(python_path)

    # Generate execution data markdown
    execution_data_markdown = generate_execution_data_markdown(
        hostname, ip_address, socket_port, streamlit_version,
        python_version_info, python_path, python_abspath, script_name, headers
    )

    with st.sidebar:
        # Display logo and caption
        st.image(logo_path, caption=caption, width=250)

        # Display execution data
        with st.expander("**FULL HEADERS**"):
            st.markdown(execution_data_markdown)

        # Display session state
        with st.expander("**SESSION STATE**"):
            st.write(st.session_state)

        st.sidebar.markdown("---")

        # Module Selector Radio Button
        # Determine initial index based on query parameters or default
        query_params = st.query_params.get("example", [initial_module_key])[0]
        try:
            initial_index = list(module_options.keys()).index(query_params)
        except ValueError:
            initial_index = 0 # Default to the first module if query param is invalid

        choice = st.radio(
            "**MODULE SELECTOR**",
            list(module_options.keys()),
            index=initial_index,
            help="Select module to be executed",
            label_visibility="visible",
            key="RADIO MENU"
        )
        return choice

def execute_module(module_path):
    """
    Reads and executes the Python script at the given module_path.
    Displays the source code in an expander after execution.
    Uses exec(), which should be used with caution.
    """
    try:
        with open(module_path, encoding="utf-8") as code_file:
            module_code = code_file.read()
            # Using exec() to run the module code. Be cautious with untrusted sources.
            exec(module_code, globals())

        # Display the source code
        with st.expander('Script Source Code v0:'):
            st.markdown(f"""``` python
{module_code}
```""")
    except FileNotFoundError:
        st.error(f"Error: Module file not found at {module_path}")
    except Exception as e:
        st.error(f"Error executing module {module_path}: {e}")


# --- Main Application Flow ---

# Note: Inline HTML/CSS. Consider externalizing for larger styles.
inline_style = """
<style>
    p {
        color: #1c1614;
        backgroud-color: #f7f4f2; /* Note: backgroud-color is a typo, should be background-color */
        font-family: 'sans serif';
        font-size: 12px;
        /* textColor is not a valid CSS property, likely intended to be color */
        /* textColor: #1c1614; */
    }
</style>
"""
# st.html(inline_style) # This line is commented out in the original code

# Render the sidebar and get the selected module choice
selected_module_key = render_sidebar(
    logo_path=DEFAULT_QR_CODE,
    caption=f"OKRocket® Platform v 0.1 {datetime.now().strftime('%Y/%m/%d')}",
    module_options=MODULE_DASHBOARDS,
    initial_module_key=list(MODULE_DASHBOARDS.keys())[0] # Use the first module as default
)

# Get the path for the selected module
selected_module_path = MODULE_DASHBOARDS.get(selected_module_key)

# Execute the selected module
if selected_module_path:
    execute_module(selected_module_path)
else:
    st.error(f"Could not find path for selected module: {selected_module_key}")

# --- Display System Tables Info (Example of using the constant) ---
# This part was in the original code but not actively displayed.
# Adding a section to show how the constant could be used.
# sys_tables_markdown = "|table|description|\n"
# sys_tables_markdown += "|---|---|\n"
# for table_info in SYSTEM_TABLES_INFO:
#     sys_tables_markdown += f"|**{table_info['table']}**|_{table_info['description']}_|\n"
# st.markdown(sys_tables_markdown) # Uncomment to display this section

