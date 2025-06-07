"""
Streamlit Mermaid Diagram Viewer App - Refactored Version
This app displays Mermaid diagrams from various sources using a modular approach.
"""

import streamlit as st
from mermaid_utils import mermaid_viewer
from mermaid_examples import (
    MVP_ARCHITECTURE_GEMINI, 
    MERMAID_CODE_BASE, 
    CRUD_NICE_EXAMPLE, 
    ER_EXAMPLE, 
    CRUD_DEEPSEEK_MERMAID, 
    COBOLagencyASPER_Process
)

# App title
st.title("COBOL Code Flowchart")

# Debug option
DEBUG = st.toggle(f"**DEBUG**", value=False)

# Information about Mermaid (commented out for reference)
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

# Create dictionary of predefined diagrams
predefined_diagrams = {
    "MVP_ARCHITECTURE_GEMINI": MVP_ARCHITECTURE_GEMINI,
    "MERMAID_CODE_BASE": MERMAID_CODE_BASE,
    "CRUD_NICE_EXAMPLE": CRUD_NICE_EXAMPLE,
    "ER_EXAMPLE": ER_EXAMPLE,
    "CRUD_DEEPSEEK_MERMAID": CRUD_DEEPSEEK_MERMAID,
    "COBOLagencyASPER_Process": COBOLagencyASPER_Process
}

# Use the mermaid_viewer from our utils module
current_mermaid_code = mermaid_viewer(
    predefined_diagrams=predefined_diagrams,
    default_diagram_name="MERMAID_CODE_BASE",
    allow_file_upload=True,
    allow_editing=True,
    debug_mode=DEBUG,
    height="1200px"
)

# You can use the returned mermaid code for further processing if needed
if DEBUG:
    st.write("Current diagram code length:", len(current_mermaid_code))
