import streamlit as st
import os
from streamlit_mermaid import st_mermaid
from mermaid_examples import MVP_ARCHITECTURE_GEMINI, MERMAID_CODE_BASE, CRUD_NICE_EXAMPLE, ER_EXAMPLE, CRUD_DEEPSEEK_MERMAID, COBOLagencyASPER_Process

st.title("COBOL Code Flowchart")

DEBUG = st.toggle(f"**DEBUG**", value=False)

REFERENCE = '''
st.markdown(
    """
    ## Mermaid
    [Mermaid](https://mermaid-js.github.io/mermaid/#/) is a diagramming and charting tool that uses text-based descriptions to render diagrams.
    """
)
'''
st.markdown(
    """
    ### Mermaid Flowchart Visualization
    """
)

def READ_FILE(FILE_PATH):
    # Read the COBOL code from the file
    with open(FILE_PATH, 'r') as FILE_CONTENT:
        CODE_FROM_FILE = FILE_CONTENT.read()
#    st.write(CODE_FROM_FILE)

    # Divide the COBOL code into its component CODE_LINES
    #CODE_LINES = CODE_FROM_FILE.split('\n')
    return(CODE_FROM_FILE)
    
MMD_LIST = [
"MVP_ARCHITECTURE_GEMINI", "MERMAID_CODE_BASE", "CRUD_NICE_EXAMPLE", "ER_EXAMPLE", "CRUD_DEEPSEEK_MERMAID", "COBOLagencyASPER_Process"
]
FILE_TYPE_LIST = ["mmd"]
MMD_CODE_NAME = st.radio(f"**SELECT A DIAGRAM TO DISPLAY**", MMD_LIST)
UPLOADED_FILE = st.file_uploader(f"**CHOOSE A LOCAL MMD FILE TO BE DISPLAYED**", type=FILE_TYPE_LIST, accept_multiple_files=False)

if UPLOADED_FILE:
#    MMD_CODE_NAME = MMD_CODE
#    MMD_CODE = globals()[MMD_CODE_NAME]
    FILE_NAME = UPLOADED_FILE.name
    FILE_PATH = os.path.abspath(f"mermaid/{FILE_NAME}")
    
    st.write(f"({FILE_NAME=}")
    st.write(f"({FILE_PATH=}")
    MMD_CODE = READ_FILE(FILE_PATH)
    MMD_CODE_NAME = FILE_NAME
else:
    if MMD_CODE_NAME:
        MMD_CODE = globals()[MMD_CODE_NAME]
    else:
        MMD_CODE_NAME = "MERMAID_CODE_BASE"
        MMD_CODE = globals()["MERMAID_CODE_BASE"]


if DEBUG:
    st.write(f"{type(MMD_CODE_NAME)} : {dir(MMD_CODE_NAME)}")
    st.write(MMD_CODE_NAME)

MMD_CODE = st.text_area(f"\"{MMD_CODE_NAME}\" Mermaid Code Input", height=300, value=MMD_CODE)

#MERMAID_CODE = st.text_area("Mermaid Code Input", height=300, value=MMD_CODE)
MERMAID_CODE = MMD_CODE

st_mermaid(MERMAID_CODE, height="1200px")
