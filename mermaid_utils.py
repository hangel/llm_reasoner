# [Mermaid Utils](https://claude.ai/chat/853f8857-b6a9-4536-be73-8f5f2927fc9a)
"""
Mermaid Utility Module for Streamlit Applications
Contains functions to handle Mermaid diagram display, loading, and processing.
"""

import os
import streamlit as st
from streamlit_mermaid import st_mermaid


def read_mermaid_file(file_path):
    """
    Read Mermaid code from a file.
    
    Args:
        file_path (str): Path to the Mermaid file
        
    Returns:
        str: Content of the Mermaid file
    """
    try:
        with open(file_path, 'r') as file_content:
            return file_content.read()
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return ""


def mermaid_viewer(
        predefined_diagrams=None,
        default_diagram_name=None,
        allow_file_upload=True,
        allow_editing=True,
        debug_mode=False,
        height="1200px"
    ):
    """
    Display a Mermaid diagram viewer with options for selection,
    file upload, and direct editing.
    
    Args:
        predefined_diagrams (dict): Dictionary of diagram name -> mermaid code
        default_diagram_name (str): Name of default diagram to show
        allow_file_upload (bool): Whether to allow file uploads
        allow_editing (bool): Whether to allow editing the diagram code
        debug_mode (bool): Whether to show debug information
        height (str): Height of the mermaid diagram
        
    Returns:
        str: The currently displayed Mermaid code
    """
    # Initialize variables
    mermaid_code = ""
    diagram_name = default_diagram_name or "Default Diagram"
    
    # Handle predefined diagrams
    if predefined_diagrams:
        diagram_names = list(predefined_diagrams.keys())
        selected_diagram = st.radio(f"**SELECT A DIAGRAM TO DISPLAY**", diagram_names)
        diagram_name = selected_diagram
        mermaid_code = predefined_diagrams[selected_diagram]
    
    # Handle file upload
    if allow_file_upload:
        uploaded_file = st.file_uploader(
            f"**CHOOSE A LOCAL MMD FILE TO BE DISPLAYED**", 
            type=["mmd"], 
            accept_multiple_files=False
        )
        
        if uploaded_file:
            file_name = uploaded_file.name
            file_path = os.path.abspath(f"mermaid/{file_name}")
            
            if debug_mode:
                st.write(f"(file_name={file_name})")
                st.write(f"(file_path={file_path})")
                
            mermaid_code = read_mermaid_file(file_path)
            diagram_name = file_name
    
    # Debug information
    if debug_mode and diagram_name:
        st.write(f"{type(diagram_name)} : {dir(diagram_name)}")
        st.write(diagram_name)
    
    # Allow editing of mermaid code
    if allow_editing:
        mermaid_code = st.text_area(
            f"\"{diagram_name}\" Mermaid Code Input", 
            height=300, 
            value=mermaid_code
        )
    
    # Display the mermaid diagram
    st_mermaid(mermaid_code, height=height)
    
    return mermaid_code
