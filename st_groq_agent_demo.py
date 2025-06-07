#import time
import os
import sys
import platform
#import socket_get_websocket_headers
import streamlit as st
#import time
from datetime import date, datetime, time
from groq import Groq
from py_analysis import MD_APP, MD_SEARCH, MD_AGENT, MD_GROQ_AGENT_DEMO
#from streamlit.web.server.websocket_headers import _get_websocket_headers
#from streamlit.web.server.websocket_headers import st.context.headers
from self_discover import REASONING_MODULES
import pytz
import pysaxon11.pysaxon11 as pysx
from xml.dom import minidom
from lxml import etree
from datetime import date, datetime, time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
from groq_models import GROQ_MODELS
from self_discover import (
    REASONING_MODULES,
    select_reasoning_modules,
    adapt_reasoning_modules,
    implement_reasoning_structure,
    execute_reasoning_structure
    )

api_key = os.environ.get("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/models"
LST_MODELS= GROQ_MODELS["models"]

DATA_MODEL_PROMPT = """
The goal is to upropose the data model necessary for an app to implement a "Legacy Code Documentation System" (LCDS) used by large corporations whose core and applications run mostly dependent of legacy code.  LCDS should be able to produce:
1. A complete metadata about the supplied code that describe as much factor related to it: 
  * Creator Organization
  * Application where the code is part of
  * Coding Language
  * Language version
  * Author
  * Revisio
  * Creation Date
  * OS / Software platform where it runs on
  * Use cases
  * Use frequency
  * Corporate experts on the subject
  Suggest as much additional metadata as required
2. A complete verbal code description
3. Requirements / Dependencies (For example: 
  * Libraries
  * Copy Books
  * Data sources
  * Environment variables
  * Deployment infrastructure, etcetera)
4. A table for each line of the source code with at least this data: "Line Number", "Indent level", "Line code", "code type")
5. A table describing the foloowing elements of code:
  * Divisions
  * Required libraries
  * Required external resources
  * Variables
  * Procedures
  present each element in a row with at least these columns: "Element Type", "Line Numbers List" (where is defined, altered, referenced or called), "Parent line" (lower indent level). Add any additional fields required.
6. A User Manual
7. A visual flowchart of the code expressed in Mermaind syntax
"""

def GET_MODELS():
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    MODELS= GROQ_MODELS
    response = requests.get(url, headers=headers)
    
    MODELS_JSON = response.json()["data"]
    N_MODELS= len(MODELS_JSON)
    
    MODELS_LIST = []
    for i in range(N_MODELS) :
    #   MODELS_LIST.append(MODELS_JSON["data"][i]["id"])
       MODELS_LIST.append(MODELS_JSON[i]["id"])
    #st.write(str(MODELS_LIST)) 
    if DEBUG:
        st.write(f"N UPDATED MODELS: {N_MODELS}\n{MODELS_LIST}")
        #print(MODELS_JSON)
    return(MODELS_LIST)


def LST_STATIC_MODELS(LST_MODELS):
    N_MODELS= len(LST_MODELS)
    MODELS_LIST = []
    for i in range(N_MODELS) :
    #   MODELS_LIST.append(MODELS_JSON["data"][i]["id"])
       MODELS_LIST.append(LST_MODELS[i]["id"])
    return(MODELS_LIST)


CLAUDE_PROMPT = """
Follow this instruction:
1. Act as a COBOL guru. Taking a sequence of steps such as:
  1.1. Plan an outline.
  1.2. Decide what, if any, web searches are needed to gather more information making it a list
  1,3, Write a first draft.
  1.4. Read over the first draft to spot unjustified arguments or extraneous information.
  1.5. Revise the draft taking into account any weaknesses spotted.

A 'COBOL code' will be supplied as an annexed file.

YOUR TASKS ARE:
1, GENERATE A TABLE WITH CODE COMPONENTS
Use this headers for the table:
  * Line Number: Number, where the element described, appears
  * Element Type ( Variable | Procedure | Other): the type of elementt described
  * Name: Element Name
  * Description: Element description accoring is purpose in the code
2. DESCRIPTION, the purpose of the 'COBOL code' given, complete lists for:
   * Variables
   * Procedures
3. WORKFLOW: Give a workflow diagram representing the 'COBOL code' in JSON notation
# COBOL code:
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CRUD-INDEXED-FILE.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT EMPLOYEE-FILE
               ASSIGN TO "EMPLOYEE.DAT"
               ORGANIZATION IS INDEXED
               ACCESS MODE IS DYNAMIC
               RECORD KEY IS EMP-ID
               FILE STATUS IS FILE-STATUS.
       
       DATA DIVISION.
       FILE SECTION.
       FD EMPLOYEE-FILE.
       01 EMPLOYEE-RECORD.
           05 EMP-ID         PIC 9(5).
           05 EMP-NAME       PIC X(20).
           05 EMP-DEPARTMENT PIC X(10).
           05 EMP-SALARY     PIC 9(6)V99.
       WORKING-STORAGE SECTION.
       01 FILE-STATUS        PIC X(2).
           88 FILE-OK        VALUE "00".
           88 END-OF-FILE VALUE "10".
           88 DUPLICATE-RECORD VALUE "22".
           88 RECORD-NOT-FOUND VALUE "23".
           88 FILE-NOT-FOUND VALUE "35".
       01 WS-WORK-RECORD.
           05 WORK-EMP-ID         PIC 9(5).
           05 WORK-EMP-NAME       PIC X(20).
           05 WORK-EMP-DEPARTMENT PIC X(10).
           05 WORK-EMP-SALARY     PIC 9(6)V99.
       01 WS-OPTION PIC 9.
       01 WS-EOFThe goal is to upropose the data model necessary for an app to implement a "Legacy Code Documentation System" (LCDS) used by large corporations whose core and applications run mostly dependent of legacy code.  LCDS should be able to produce:
1. A complete metadata about the supplied code that describe as much factor related to it: 
  * Creator Organization
  * Application where the code is part of
  * Coding Language
  * Language version
  * Author
  * Revisio
  * Creation Date
  * OS / Software platform where it runs on
  * Use cases
  * Use frequency
  * Corporate experts on the subject
  Suggest as much additional metadata as required
2. A complete verbal code description
3. Requirements / Dependencies (For example: 
  * Libraries
  * Copy Books
  * Data sources
  * Environment variables
  * Deployment infrastructure, etcetera)
4. A table for each line of the source code with at least this data: "Line Number", "Indent level", "Line code", "code type")
5. A table describing the foloowing elements of code:
  * Divisions
  * Required libraries
  * Required external resources
  * Variables
  * Procedures
  present each element in a row with at least these columns: "Element Type", "Line Numbers List" (where is defined, altered, referenced or called), "Parent line" (lower indent level). Add any additional fields required.
6. A User Manual
7. A visual flowchart of the code expressed in Mermaind syntax PIC X VALUE "N".
       
.
       01 USER-CHOICE        PIC X.
       01 FILE-CREATED PIC X VALUE 'N'.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM INITIALIZE-FILE
           PERFORM MAIN-LOOP UNTIL USER-CHOICE = "Q".
           PERFORM SAFE-CLOSE
           STOP RUN.
                  
       MAIN-LOOP.
           DISPLAY 
      -  "Enter (C)reate, (R)ead, (U)pdate, (D)elete, "
      -  "(S)ave or (Q)uit: " 
      -  WITH NO ADVANCING.
           ACCEPT USER-CHOICE.
           EVALUATE USER-CHOICE
               WHEN "C"
                   PERFORM CREATE-RECORD
               WHEN "R"
                   PERFORM READ-RECORD
               WHEN "U"
                   PERFORM UPDATE-RECORD
               WHEN "D"
                   PERFORM DELETE-RECORD
               WHEN "S"
                   PERFORM SAVE-FILE
                   CONTINUE
               WHEN "Q"
                   PERFORM QUIT-ROUTINE
               WHEN OTHER
                   DISPLAY "Invalid choice."
           END-EVALUATE.
            
       OLD-CREATE-RECORD.
           IF FILE-CREATED = 'N'
              OPEN OUTPUT EMPLOYEE-FILE
              CLOSE EMPLOYEE-FILE
              MOVE 'Y' TO FILE-CREATED
           END-IF.
           OPEN I-O EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           DISPLAY "Enter employee name: " WITH NO ADVANCING.
           ACCEPT EMP-NAME.
           DISPLAY "Enter employee department: " WITH NO ADVANCING.
           ACCEPT EMP-DEPARTMENT.
           DISPLAY "Enter employee salary: " WITH NO ADVANCING.
           ACCEPT EMP-SALARY.
           WRITE EMPLOYEE-RECORD
               INVALID KEY DISPLAY "Employee ID already exists."
           END-WRITE.
           CLOSE EMPLOYEE-FILE.

        CREATE-RECORD.
           MOVE SPACES TO WS-WORK-RECORD
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-ID.
           DISPLAY "Enter employee name: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-NAME.
           DISPLAY "Enter employee department: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-DEPARTMENT.
           DISPLAY "Enter employee salary: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-SALARY.
           MOVE WS-WORK-RECORD TO EMPLOYEE-RECORD
           WRITE EMPLOYEE-RECORD
           INVALID KEY
               DISPLAY "Record already exists."
           END-WRITE.
       
      
       READ-RECORD.
           OPEN INPUT EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           READ EMPLOYEE-FILE
               KEY IS EMP-ID
               INVALID KEY DISPLAY "Employee not found."
           END-READ.
           IF FILE-OK
               DISPLAY EMPLOYEE-RECORD
           END-IF.
       
       UPDATE-RECORD.
           OPEN I-O EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           READ EMPLOYEE-FILE
               KEY IS EMP-ID
               INVALID KEY DISPLAY "Employee not found."
           END-READ.

               DISPLAY "Enter new employee name: " WITH NO ADVANCING.
               ACCEPT EMP-NAME.
               DISPLAY "Enter new employee dept: " WITH NO ADVANCING.
               ACCEPT EMP-DEPARTMENT.
               DISPLAY "Enter new employee salary: " WITH NO ADVANCING.
               ACCEPT EMP-SALARY.
               REWRITE EMPLOYEE-RECORD
                   INVALID KEY DISPLAY "Error updating record."
               END-REWRITE.
               CLOSE EMPLOYEE-FILE.
       
       DELETE-RECORD.
           OPEN I-O EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           READ EMPLOYEE-FILE
               KEY IS EMP-ID
               INVALID KEY DISPLAY "Employee not found."
           END-READ.
           IF FILE-OK
               DELETE EMPLOYEE-FILE RECORD
                   INVALID KEY DISPLAY "Error deleting record."
               END-DELETE
           END-IF.
           CLOSE EMPLOYEE-FILE.

       SAVE-FILE.
           DISPLAY "Closing file and exiting...".
           CLOSE EMPLOYEE-FILE.
           STOP RUN.
       
       QUIT-ROUTINE.
           DISPLAY "Closing file and exiting...".
           CLOSE EMPLOYEE-FILE.
           STOP RUN.

       SAFE-CLOSE.
           CLOSE EMPLOYEE-FILE
           IF FILE-OK
               DISPLAY "File closed successfully."
           ELSE
               DISPLAY "Error closing file: " FILE-STATUS
           END-IF.       

       CREATE-FILE.
           OPEN OUTPUT EMPLOYEE-FILE
           IF FILE-OK
               DISPLAY "File created successfully."
               CLOSE EMPLOYEE-FILE
               OPEN I-O EMPLOYEE-FILEYou are an AI assistant designed to provide detailed, step-by-step responses. Your outputs should follow this structure:

1. Begin with a <thinking> section.
2. Inside the thinking section:
   a. Briefly analyze the question and outline your approach.
   b. Present a clear plan of steps to solve the problem.
   c. Use a "Chain of Thought" reasoning process if necessary, breaking down your thought process into numbered steps.
3. Include a <reflection> section for each idea where you:
   a. Review your reasoning.
   b. Check for potential errors or oversights.
   c. Confirm or adjust your conclusion if necessary.
4. Be sure to close all reflection sections.
5. Close the thinking section with </thinking>.
6. Provide your final answer in an <output> section.

Always use these tags in your responses. Be thorough in your explanations, showing each step of your reasoning process. Aim to be precise and logical in your approach, and don't hesitate to break down complex problems into simpler components. Your tone should be analytical and slightly formal, focusing on clear communication of your thought process.

Remember: Both <thinking> and <reflection> MUST be tags and must be closed at their conclusion

Make sure all <tags> are on separate lines with no other text. Do not include other text on a line containing a tag.
           ELSE
               DISPLAY "Error creating file: " FILE-STATUS
               STOP RUN
           END-IF.
       
       INITIALIZE-FILE.
           OPEN I-O EMPLOYEE-FILE
           IF FILE-OK
               DISPLAY "File opened successfully."
           ELSE
               IF FILE-NOT-FOUND
                   PERFORM CREATE-FILE
               ELSE
                   DISPLAY "Error opening file: " FILE-STATUS
                   STOP RUN
               END-IF
           END-IF.
       
"""

REFLECTION_PROMPT = '''
You are an AI assistant designed to provide detailed, step-by-step responses. Your outputs should follow this structure:

1. Begin with a <thinking> section.
2. Inside the thinking section:
   a. Briefly analyze the question and outline your approach.
   b. Present a clear plan of steps to solve the problem.
   c. Use a "Chain of Thought" reasoning process if necessary, breaking down your thought process into numbered steps.
3. Include a <reflection> section for each idea where you:
   a. Review your reasoning.
   b. Check for potential errors or oversights.
   c. Confirm or adjust your conclusion if necessary.
4. Be sure to close all reflection sections.
5. Close the thinking section with </thinking>.
6. Provide your final answer in an <output> section.

Always use these tags in your responses. Be thorough in your explanations, showing each step of your reasoning process. Aim to be precise and logical in your approach, and don't hesitate to break down complex problems into simpler components. Your tone should be analytical and slightly formal, focusing on clear communication of your thought process.

Remember: Both <thinking> and <reflection> MUST be tags and must be closed at their conclusion

Make sure all <tags> are on separate lines with no other text. Do not include other text on a line containing a tag.
'''

def MK_SIDEBAR_INFO():
    root = os.path.join(os.path.dirname(__file__))
#    headers = _get_websocket_headers()
    headers = st.context.headers
    
    HOSTNAME = socket.gethostname()
    IP_ADDRS = socket.gethostbyname(socket.gethostname())
    F_NOW = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    F_NOW_S = datetime.now().strftime("%Y/%m/%d")
    PY_VER = sys.version_info
    
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
    | **AGENT** | {headers["User-Agent"]} |
    | **AGENT** | {headers} |
    
    """
    with st.sidebar.expander("**FULL HEADERS**"):
        st.markdown(EXEC_DATA)

    with st.sidebar.expander("**SESSION STATE**"):
        st.write(st.session_state)
    return(F_NOW_S)

def show_code(i):
    PATH = TAB_LIST[i][1]
    with open(PATH, encoding="utf-8") as code:
        c = code.read()
        #exec(c, globals())

        with st.expander(f'**Script Source Code v{i}-`{PATH}`:**'):
            st.markdown(f"""``` python
{c}```""")

GROQ_LOGO_LIGHT = "../okrocket/assets/images/groqcloudlight.png"
OKROCKET_LOGO   = "../okrocket/assets/images/OKRocket_Rocket_Logo.png"
F_NOW_S1 = datetime.now().strftime("%Y/%m/%d")
st.image(GROQ_LOGO_LIGHT, caption=f"**Groq Agent & Chat Bot Demos** v 0.1 {F_NOW_S1}", width=250)
DEBUG = st.toggle(f"**`DEBUG`**", value=False)
            #st.write('CODE HERE')
st.title("Groq Agent & Chat Bot Demos")

TAB_LIST = [
["AGENT","st_groq_agent_demo.py"],
["APP_PY","app.py"],
["SELF_DICOVER","self_discover.py"],
["APP_AGENT","app_agent.py"],
["REASONING_MODULES","reasoning_modules.py"],
["ST_GROQ_AGENT_DEMO","st_groq_agent_demo.py"],
]


MODELS= GROQ_MODELS


def MK_GROK_CLIENT():
    API_KEY = os.environ.get("GROQ_API_KEY")
    if API_KEY is None:
        try:
            API_KEY = st.secrets["GROQ_API_KEY"]
        except KeyError:
            # Handle the case where GROQ_API_KEY is neither in the environment variables nor in Streamlit secrets
            st.error("API key not found.")
            st.stop()
    client = Groq(api_key=API_KEY)
    return(client)

def MK_FORM(client, LST_MODELS):
    #MODELS_LIST = MODELS
    model_list = LST_STATIC_MODELS(LST_MODELS)
    if DEBUG:
        st.write(f"STATICMODELS: {model_list}")
    model = st.radio(f"**Select your GROQ Cloud LLM for this reasoning task**", model_list, index = 3, key="radio_tab2", horizontal=True, help="llama3-70b-8192/mixtral are recommended for better performance, - mixtral appears to be slower")
    #st.stop()
    tab00, tab01, tab02, tab03, tab04, tab05, tab06 = st.tabs(["**AGENT**", "**`APP.PY`**", "**`SELF_DISCOVER`**", "**`APP_AGENT`**", "**`REASONING MODULES`**", "**`ST_GROQ_AGENT_DEMO`**", "**`ABOUT`**"])
    with tab00:
        tab1, tab2 = st.tabs(["**Self-Discover**", "**Text Generation**"])


    with tab01:
        col21, col22 = st.columns(2)
    
        with col21: 
            with st.expander("**`app.py` analysis**", expanded=True):
                st.markdown(MD_APP)
        with col22:
            show_code(1)
    
    with tab02:
        col31, col32 = st.columns(2)
    
        with col31:
            with st.expander("**`self_discover.py` analysis**", expanded=True):
                st.markdown(MD_SEARCH) 
        with col32:
            show_code(2)
    
    with tab03:
        col41, col42 = st.columns(2)
    
        with col41:
            with st.expander("**`app_agent.py` analysis**", expanded=True):
                st.markdown(MD_AGENT) 
        with col42:
            show_code(3)
    with tab04:
        col51, col52 = st.columns(2)
    
        with col51:
            with st.expander("**`REASONING MODULES`**", expanded=True):
    #            MD = "|MODULE|\n|-----|"
                MD = "" + "\n"
                for i, MODULE in enumerate(REASONING_MODULES):
    #                MD = MD + "\n|" + MODULE + "|"
                    MD = MD + MODULE + "\n"
            st.markdown(MD) 
        with col52:
            show_code(4)
    
    with tab05:
        col61, col62 = st.columns(2)
    
        with col61:
            with st.expander("**`st_groq_agent_demo.py` analysis**", expanded=True):
                st.markdown(MD_GROQ_AGENT_DEMO) 
        with col62:
            show_code(5)
    
    with tab06:
                st.info("""['Self-Discover: Large Language Models Self-Compose Reasoning Structures'](https://arxiv.org/abs/2402.03620) - Zhou et al (2024)
        
    This is based on MrCatID's [implementation](https://github.com/catid/self-discover/blob/main/self_discover.py). 
    Credits to [Martin A](https://twitter.com/mdda123) for sharing this at [ML Singapore](https://www.meetup.com/machine-learning-singapore/)
        """)
    with tab2:
        system_prompt = st.text_input("System Prompt", "You are a friendly chatbot.", key="tab1")
        user_prompt = st.text_input("User Prompt", "Tell me a joke like Groucho.")
    
        button = st.empty()
        time_taken = st.empty()
        response = st.empty()
        
        BTN_TEXT_GENERATE = button.button("Generate")
    
        if BTN_TEXT_GENERATE:
            stream = client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}],
                stream=True
                )
    
            #start_time = time.time()
            #datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            start_time = datetime.now()
    
            streamed_text = ""
    
            for chunk in stream:
                chunk_content = chunk.choices[0].delta.content
                if chunk_content is not None:
                    streamed_text = streamed_text + chunk_content
                    response.info(streamed_text)
    
            #time_taken.success(f"Time taken: {round(time.time() - start_time,4)} seconds")
            end_time = datetime.now()
            time_taken.success(f"Time taken: {end_time - start_time} seconds")
    
    with tab1:
        task = st.text_area("What is your task?", key="tab2", value="Your mission, should you choose to accept it, is to uncover critical insights from global events that allow for early intervention and strategic planning, ultimately helping businesses and organizations navigate complex and volatile environments. You will dive deep into the vast and dynamic dataset provided by the Global Database of Events, Language, and Tone GDELT . This year, we're presenting two challenges, designed to test your data skills and creativity.")
        #reasoning_model = st.radio("Select your LLM for this reasoning task", model_list, index = 3, key="rd_tab1", horizontal=True, help="llama3-70b-8192/mixtral1 are recommended for better performance, - mixtral appears to be slower")
    
        button = st.empty()

        BTN_RUN_TAB1 = button.button("Run")    
    
    return(BTN_RUN_TAB1, BTN_TEXT_GENERATE, task, model)

def TAB1_EXEC_FORM(client, task, model):
    step4  = st.empty()
    step3  = st.empty() 
    step2  = st.empty()
    step1  = st.empty()

    from self_discover import (
        REASONING_MODULES,
        select_reasoning_modules,
        adapt_reasoning_modules,
        implement_reasoning_structure,
        execute_reasoning_structure
        )

    #select_reasoning_modules = ""
    prompt = select_reasoning_modules(REASONING_MODULES, task)
    stream_1 = client.chat.completions.create(
        model = model,
        messages=[{"role": "system", "content": "You are a world class expert in reasoning."},
                {"role": "user", "content": prompt}],
        stream=True
    )
    
    select_reasoning_modules = ""
    for chunk in stream_1:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content is not None:
            select_reasoning_modules = select_reasoning_modules + chunk_content
            step1.info("## Step 1: SELECT relevant reasoning modules for the task \n \n"+select_reasoning_modules)
    

    prompt = adapt_reasoning_modules(select_reasoning_modules, task)
    stream_2 = client.chat.completions.create(
        model = model,
        messages=[{"role": "system", "content": "You are a world class expert in reasoning."},
                {"role": "user", "content": prompt}],
        stream=True
    )

    adapted_modules = ""
    for chunk in stream_2:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content is not None:
            adapted_modules = adapted_modules + chunk_content
            step2.info("## Step 2: ADAPT the selected reasoning modules to be more specific to the task. \n \n " + adapted_modules)

    prompt = implement_reasoning_structure(adapted_modules, task)
    stream_3 = client.chat.completions.create(
        model = model,
        messages=[{"role": "system", "content": "You are a world class expert in reasoning."},
                {"role": "user", "content": prompt}],
        stream=True
    )

    reasoning_structure = ""
    for chunk in stream_3:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content is not None:
            reasoning_structure = reasoning_structure + chunk_content
            step3.info("## Step 3: IMPLEMENT the adapted reasoning modules into an actionable reasoning structure. \n \n " + reasoning_structure)

    prompt = execute_reasoning_structure(reasoning_structure, task)
    stream_4 = client.chat.completions.create(
        model = model,
        messages=[{"role": "system", "content": "You are a world class expert in reasoning."},
                {"role": "user", "content": prompt}],
        stream=True
    )

    result = ""
    for chunk in stream_4:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content is not None:
            result = result + chunk_content
            step4.info("## Step 4: Execute the reasoning structure to solve a specific task instance. \n \n " + result)
    
if __name__ == "__main__":
    MODELS_LIST = GET_MODELS()
    LST_STATIC_MODELS(LST_MODELS)
    MK_SIDEBAR_INFO()
    client = MK_GROK_CLIENT()
    BTN_RUN_TAB1, BTN_TEXT_GENERATE, task, model = MK_FORM(client, LST_MODELS)
    if DEBUG:
        fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        st.success("MK_FORM(client) " + fnow)

    if BTN_RUN_TAB1:
        if DEBUG:
            st.write(f"BTN_RUN_TAB1; {BTN_RUN_TAB1}, BTN_TEXT_GENERATE: {BTN_TEXT_GENERATE}, task: {task}, model: {model}")
        
        fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        with st.spinner(text=f"In Process + {fnow}"):
            if DEBUG:
                st.success("START: " + fnow)
                fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                st.success("MK_SIDEBAR_INFO() " + fnow)
            client = MK_GROK_CLIENT()
            if DEBUG:
                fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                st.success("MK_GROK_CLIENT() " + fnow)
            if BTN_RUN_TAB1:
                #st.write("RUN PRESSED")
                TAB1_EXEC_FORM(client, task, model)




