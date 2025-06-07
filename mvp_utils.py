# mvp_utils.py
import streamlit as st
import socket
import sys
import os
from datetime import datetime
from pathlib import Path

def get_local_ip():
    """Gets the local IP address and an available socket port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        ip_address = s.getsockname()[0]
        port = s.getsockname()[1] # Note: This port is ephemeral
    except Exception:
        ip_address = '127.0.0.1'
        port = 'N/A'
    finally:
        s.close()
    return ip_address, port

def get_current_timestamp(format="%Y/%m/%d %H:%M:%S"):
    """Returns the current timestamp formatted as a string."""
    return datetime.now().strftime(format)

def get_system_info_markdown():
    """Gathers system and execution info and returns it as a Markdown string."""
    hostname = socket.gethostname()
    ip_addr, socket_port = get_local_ip()
    f_now = get_current_timestamp()
    py_ver = sys.version_info
    py_path = Path.cwd()
    # Use sys.argv[0] for the running script path for better reliability
    try:
        script_path = Path(sys.argv[0]).resolve()
        script_name = script_path.name
        script_abs_path = str(script_path)
    except Exception:
        script_path = Path(__file__).resolve() # Fallback
        script_name = script_path.name
        script_abs_path = str(script_path)


    headers = {}
    try:
        # Use st.context is preferred over internal _get_websocket_headers
        # Check if running in streamlit context before accessing headers
        if hasattr(st, 'context') and st.context.headers:
             headers = st.context.headers
             user_agent = headers.get("User-Agent", "N/A")
        else:
             user_agent = "N/A (Not in Streamlit context or headers unavailable)"
    except Exception:
        user_agent = "N/A (Error fetching headers)"


    # Using f-string for multi-line definition for readability
    exec_data = f"""
|    PARAM       |     VALUE                                         |
|----------------|---------------------------------------------------|
| **DATE:** | _{f_now}_                                         |
| **HOST:** | _{hostname}_                                      |
| **IP:** | _{ip_addr}_                                       |
| **SOCKET:** | _{socket_port}_ (Ephemeral)                       |
| **ST_VER** | {st.__version__}                                  |
| **PY_VER** | {py_ver.major}.{py_ver.minor}.{py_ver.micro}      |
| **PY_CWD** | `{py_path}`                                       |
| **PY_SCR_PATH**| `{script_abs_path}`                               |
| **PY_SCR_NAME**| `{script_name}`                                   |
| **USER-AGENT** | _{user_agent}_                                    |

<details>
<summary>Full Headers (Click to expand)</summary>
<pre><code>{headers}</code></pre>
</details>
"""
    st.session_state['PY_PATH'] = f"{py_path}"
    return exec_data

def load_css(css_file_path):
    """Loads CSS from a file and applies it using st.markdown."""
    try:
        with open(css_file_path) as f:
            css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file not found at: {css_file_path}")
    except Exception as e:
        st.error(f"Error loading CSS file {css_file_path}: {e}")
    return(css)

