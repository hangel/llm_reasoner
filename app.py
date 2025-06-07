# https://github.com/PablocFonseca/streamlit-aggrid
from multiprocessing.sharedctypes import Value
import sqlite3
import streamlit as st
import pandas as pd
import json
import os
import sys
import platform
import socket
from PIL import Image
from datetime import date, datetime, time
from streamlit.web.server.websocket_headers import _get_websocket_headers
import streamlit as st
import streamlit_modal as modal
import streamlit.components.v1 as components
#import components_example_html as cxh
import utils as utl
from PIL import Image
from datetime import date, datetime, time
from pathlib import Path
from dashboards import DASHBOARDS as dashboards

MVP_VERSION = "0.0.0.12"
PG_CONFIG = """
"""
st.set_page_config(
        page_title=f"COBOLpro Preview by OKRocket® Platform v{MVP_VERSION}",
        page_icon="assets/images/COBOLpro/COBOLpro_icon.png",
        layout="wide",
        menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': f"[**COBOL**__pro__](https://www.cobolpro.com) SERVICES MVP v{MVP_VERSION} Preview!"
    }
)



code = """
<style>
    p {
        color: #1c1614;
        backgroud-color: #f7f4f2;
        font-family: 'sans serif';
        font-size: 12px;
        textColor: #1c1614;
    }
</style>
"""

def LOCAL_IP() :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    #st.write(f"{s.getsockname()}")
    LOCAL_IP_ADDRESS = s.getsockname()[0]
    SOCKET_PORT = s.getsockname()[1]
    s.close()
    return(LOCAL_IP_ADDRESS, SOCKET_PORT)
    
#st.html(code)

root = os.path.join(os.path.dirname(__file__))

#headers = _get_websocket_headers()
headers = st.context.headers

COBOLagency_vertical_logo = "assets/images/COBOLagency/COBOL_FullLockup-White_VERTICAL.png"
COBOLpro_vertical_logo = "assets/images/COBOLagency/COBOLpro_Vertical_FullLockup.png"
COBOLAGENCY_QR = "assets/images/COBOLagency/COBOLagency_QR.png"
COBOLpro_QR = "assets/images/COBOLpro/COBOLpro_QR.png"
QR_CODE = COBOLpro_QR
OLLAMA_LOGO = "assets/images/OllamaLogo_S.png"
OKROCKET_LOGO = "assets/images/OKRocket_Rocket_Logo.png"
OKR_LOGO_3x3 = "assets/images/OKR_VerdeMosaico_3x3.png"

#LOGO = Image.open('F1ML_logo_sq.png')
LOGO = OKR_LOGO_3x3
#LOGO = COBOLAGENCY_QR
LOGO = QR_CODE
HOSTNAME = socket.gethostname()
#IP_ADDRS = socket.gethostbyname(socket.gethostname())
IP_ADDRS,SOCKET_PORT = LOCAL_IP()
F_NOW = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
F_NOW_S = datetime.now().strftime("%Y/%m/%d")
PY_VER = sys.version_info

PY_PATH    = Path.cwd()
PY_ABSPATH = os.path.abspath(__file__)

st.session_state['PY_PATH'] = f"{PY_PATH}"

EXEC_DATA = f"""
|    PARAM   |     VALUE    |
|------------|--------------| 
| **DATE:**  | _{F_NOW}_ | 
| **HOST:**  | _{HOSTNAME}_ | 
| **IP:**    | _{IP_ADDRS}_ |
| **SOCKET:**| _{SOCKET_PORT}_ |
| **ST_VER** | {st.__version__} |
| **PY_VER** | {PY_VER.major}.{PY_VER.minor}.{PY_VER.micro} |
| **PY_PATH** | {PY_PATH} |
| **PY_ABSPATH** | {PY_ABSPATH} |
| **PY_SCR** | {os.path.basename(__file__)} |
| **USER-AGENT** | {headers["User-Agent"]} |
| **HEADERS** | {headers} |
"""
with st.sidebar.expander("**FULL HEADERS**"):
    st.markdown(EXEC_DATA)

with st.sidebar.expander("**SESSION STATE**"):
    st.write(st.session_state)

HOSTNAME  = socket.gethostname()
IP_ADDRS  = socket.gethostbyname(socket.gethostname())
IP_SOCKET = socket.gethostbyname(socket.gethostname())
F_NOW = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
F_NOW_S = datetime.now().strftime("%Y/%m/%d")
#st.sidebar.image(NETUX_SALUD_LOGO, caption=f'SISTEMA GENERAL DE REPORTES {F_NOW_S}')

#st.sidebar.image(COBOLpro_vertical_logo, caption=f"OKRocket® Platform v 0.1 {F_NOW_S}", width=175)
st.sidebar.image(LOGO, caption=f"OKRocket® Platform v 0.1 {F_NOW_S}", width=250)
#st.sidebar.title(f"{F_NOW}")

EXEC_DATA = f"""
|    PARAM   |     VALUE    |
|------------|--------------| 
| **DATE:** | _{F_NOW}_ | 
| **HOST:**  | _{HOSTNAME}_ | 
| **IP:**    | _{IP_ADDRS}_ |
| **ST_VER** | {st.__version__} |
| **PY_VER** | {PY_VER.major}.{PY_VER.minor}.{PY_VER.micro} |
| **PY_PATH** | {__file__} |
| **PY_SCR** | {os.path.basename(__file__)} |
| **USER-AGENT** | {headers["User-Agent"]} |
| **HEADERS** | {headers} |

"""
#

#Sys Tables
#https://www.techonthenet.com/sqlite/sys_tables/index.php
SysTables = [{'table': 'sqlite_master', 'description': 'Master listing of all database objects in the database and the SQL used to create each object.'},
	{'table': 'sqlite_sequence', 'description': 'Lists the last sequence number used for the AUTOINCREMENT column in a table. The sqlite_sequence table will only be created once an AUTOINCREMENT column has been defined in the database and at least one sequence number value has been generated and used in the database.'},
	{'table': 'sqlite_stat1', 'description': 'This table is created by the ANALYZE command to store statistical information about the tables and indexes analyzed. This information will be later used by the query optimizer.'}]

MD =      "|table|description|\n"
MD = MD + "|---|---|\n"
for SYS_TABLE in SysTables:
    MD = MD + f"|**{SYS_TABLE['table']}**|_{SYS_TABLE['description']}_|\n"



#st.set_page_config(layout="wide")
root = os.path.join(os.path.dirname(__file__))
st.sidebar.write("ROOT: {root}")
# st.sidebar.markdown("![Netux logo](http://localhost/netux/Netux_favicon_256.png)")
#st.sidebar.markdown("![Netux logo](https://uploads-ssl.webflow.com/5d66946a1b07767aacb25958/5d66a65a071de8b2d1f132e0_Logo%20v5%20t-n.png)")
#st.sidebar.title(f"AI TESTS")
#st.sidebar.subheader("(O/S LLM\'s & API\'s)")
st.sidebar.subheader(f"{F_NOW}")
#st.sidebar.title("CONSENSUS (SEMANTIC SCHOLAR) & RESOOMER & SIGUEN!")
#logo_netux = "<img src='https://uploads-ssl.webflow.com/5d66946a1b07767aacb25958/5d66a65a071de8b2d1f132e0_Logo%20v5%20t-n.png' width='100%' alt='Netux logo'/>"
#logo_netux = "<img src='http://localhost/netux/icon_256_rev.png' width='100%' alt='Netux logo'/>"

NO_DASHBOARDS = """
dashboards = {
    "**ST_GROQ_DOCUMENTER**":     os.path.join(root, "st_groq_documenter.py"),
    "**SCAN FILESYSTEM**"   :     os.path.join(root, "st_scan_fs_Gemini25Flash_000.py"),
    "**CLIP_MVP**"          :     os.path.join(root, "st_CLIP_MVP_Flash25_000.py"),
}
"""

ELEMENTS_MATERIAL_UI = '''
    "Ele 2.1 Create an element with a child": os.path.join(root, "elements_2_1.py"),
    "Ele 2.2 Create an element with multiple children": os.path.join(root, "elements_2_2.py"),
    "Ele 2.3 Create an element with nested children": os.path.join(root, "elements_2_3.py"),
    "Ele 2.4 Add properties to an element": os.path.join(root, "elements_2_4.py"),
    "Ele 2.5.1 Material UI elements ": os.path.join(root, "elements_2_5_1.py"),
    "Ele 2.5.2 Other elements": os.path.join(root, "elements_2_5_2.py"),
    "Ele 3.1 Retrieve an element's data": os.path.join(root, "elements_3_1.py"),
    "Ele 3.2 Synchronize a session state": os.path.join(root, "elements_3_2.py"),
    "Ele 3.3 Avoid many reloads with lazy()": os.path.join(root, "elements_3_3.py"),
    "Ele 3.4 Invoke a callback hot-key": os.path.join(root, "elements_3_4.py"),
    "Ele 3.5 Invoke a callback periodically": os.path.join(root, "elements_3_5.py"),
    "Ele 4 Draggable and resizable dashboard": os.path.join(root, "elements_4.py"),
    "Ele 5.1 Monaco code and diff editor": os.path.join(root, "elements_5_1.py"),
    "Ele 5.2 Nivo charts": os.path.join(root, "elements_5_2.py"),
    "Ele 5.3 Media player": os.path.join(root, "elements_5_3.py"),
    "**** CODE ****": os.path.join(root, "update_mm.py"),
    "date_parm": os.path.join(root, "date_param.py"),
    "format_func": os.path.join(root, "format_func.py"),
    "JSPlumb Test": os.path.join(root, "jsplumb/jsplumb_test.py"),
'''

init_module = list(dashboards.keys())[0]
#with st.sidebar:
#    components.html(logo_netux,)
#choice_from_url = query_params = st.experimental_get_query_params().get("example", ["OBSERVATORIO via FreeMind"])[0]
query_params = st.query_params.get("example",  [init_module])[0]

choice_from_url = query_params
index = list(dashboards.keys()).index(choice_from_url)

st.sidebar.markdown("---")
# st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, captions=None, label_visibility="visible")
choice = st.sidebar.radio("**MODULE SELECTOR**", list(dashboards.keys()), index=index, help="Select module to be executed", label_visibility="visible", key="RADIO MENU")
path = dashboards[choice]

with open(path, encoding="utf-8") as code:
    c = code.read()
    exec(c, globals())

    with st.expander('Script Source Code v0:'):
        st.markdown(f"""``` python
{c}```""")


