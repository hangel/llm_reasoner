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
from reasoner_prompt import REASONER_PROMPT_BASE
#from streamlit.web.server.websocket_headers import _get_websocket_headers
#from streamlit.web.server.websocket_headers import st.context.headers
from self_discover import REASONING_MODULES
import pytz
#import pysaxon11.pysaxon11 as pysx
from xml.dom import minidom
from lxml import etree
from datetime import date, datetime, time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
#from groq_models import GROQ_MODELS
from self_discover import (
    REASONING_MODULES,
    select_reasoning_modules,
    adapt_reasoning_modules,
    implement_reasoning_structure,
    execute_reasoning_structure
    )

MVP_VERSION = "0.0.0.12"
PG_CONFIG = """
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
"""


DEBUG = st.toggle(f"**`DEBUG`**", value=False)
api_key = os.environ.get("GROQ_API_KEY")
DEFAULT_MODEL_INDEX = 7


true = True
null = None

HEADERS = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
VERSION = "0.1"

#GROQ_MODELS = requests.get(MODELS_URL, headers=HEADERS)

#url = "https://api.groq.com/openai/v1/models"
#LST_MODELS= GROQ_MODELS["models"]
#LST_MODELS= GROQ_MODELS.json()["data"]
def GET_MODELS():
    true = True
    null = None
    MODELS_URL = "https://api.groq.com/openai/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
#    MODELS= GROQ_MODELS
    step0  = st.empty()
    try:
        response = requests.get(MODELS_URL, headers=headers)
    except:
        step0.error(f"#### Groq Model Network Error. Verify Connection")
    
    MODELS_JSON = response.json()["data"]
    N_MODELS= len(MODELS_JSON)
    
    MODELS_LIST = []
    for i in range(N_MODELS) :
       MODELS_LIST.append(MODELS_JSON[i]["id"])
    return(MODELS_LIST)

def CREATE_TASK(UPLOADED_FILE):
    #st.write(UPLOADED_FILE)
    TASK_CODE = ""
    for LINE in UPLOADED_FILE:
        TASK_CODE = TASK_CODE + str(LINE, encoding='utf-8', errors='replace')
    return(TASK_CODE)


def LST_STATIC_MODELS(LST_MODELS):
    LST_MODELS = []
    N_MODELS= len(LST_MODELS)
    if DEBUG:
        st.write(N_MODELS)

    for i in range(N_MODELS) :
       if DEBUG:
           st.write(f"i= {i}")
           st.write(f"LST_MODELS[i]= {LST_MODELS[i]}")
       MODELS_LIST.append(LST_MODELS[i])
    return(MODELS_LIST)

def show_code(i):
    PATH = TAB_LIST[i][1]
    with open(PATH, encoding="utf-8") as code:
        c = code.read()
        #exec(c, globals())

        with st.expander(f'**Script Source Code v{i}-`{PATH}`:**'):
            st.markdown(f"""``` python
{c}```""")

def MK_GROQ_CLIENT():
    API_KEY = os.environ.get("GROQ_API_KEY")
    if API_KEY is None:
        try:
            API_KEY = st.secrets["GROQ_API_KEY"]
        except KeyError:
            # Handle the case where GROQ_API_KEY is neither in the environment variables nor in Streamlit secrets
            st.error("API key not found.")
            st.stop()
    CLIENT = Groq(api_key=API_KEY)
    return(CLIENT)

def MK_FORM(CLIENT, LST_MODELS):
    #MODELS_LIST = MODELS
    MODEL_LIST = LST_STATIC_MODELS(LST_MODELS)
    if DEBUG:
        st.write(f"STATICMODELS: {MODEL_LIST}")
    model = st.radio(f"**Select your GROQ Cloud LLM for this reasoning task**", sorted(MODEL_LIST), index = DEFAULT_MODEL_INDEX, key="radio_TAB_CODE_GEN", horizontal=True, help="llama3.2 model series are recommended for better performance, - mixtral appears to be slower")
    #st.stop()
    tab00, tab01, tab02, tab03, tab04, tab05, tab06 = st.tabs(["**PREVIEW**", "**`APP.PY`**", "**`SELF_DISCOVER`**", "**`APP_AGENT`**", "**`REASONING MODULES`**", "**`ST_GROQ_AGENT_DEMO`**", "**`ABOUT`**"])
    with tab00:
        TAB_CODE_ANALYZER, TAB_CODE_GEN, TAB_REASONER = st.tabs(["**CODE ANALYZER**", "**COBOL CODE GENERATION**", "**REASONER**"])


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

    with TAB_CODE_GEN:
        CODE_GEN_PROMPT = "Create COBOL code for implementing CRUD and listing on an indexed file over an indexed file with an English menu."
    
        system_prompt = st.text_input("System Prompt", "I'll help you in your coding tasks.", key="TAB_CODE_ANALYZER")
        user_prompt = st.text_input("User Prompt", CODE_GEN_PROMPT)
    
        button = st.empty()
        time_taken = st.empty()
        response = st.empty()
        
        BTN_TEXT_GENERATE = button.button("Generate")
    
        if BTN_TEXT_GENERATE:
            stream = CLIENT.chat.completions.create(
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
    
    with TAB_CODE_ANALYZER:
        CODE_ANALIZER_PROMPT = """Keep this consideration before proceeding  with INSTRUCTIONS:
Going forward, avoid simply agreeing with my points or taking my conclusions at face value.
I want real intellectual challenge, not just affirmation. Whenever I propose an idea, do this:

* Question my assumptions. What am I treating as true that might be questionable? 
* Offer a skeptic's viewpoint. What objections would a critical, well-informed voice raise? 
* Check my reasoning. Are there flaws or leaps in logic I've overlooked? 
* Suggest alternative angles. How else might the idea be viewed, interpreted or challenged? 
* Focus on accuracy over agreement. 
* If my argument is weak or wrong, correct me plainly and show me how. 
* Stay constructive but rigorous. 
* You are not here to argue for argument's sake, but to sharpen my thinking and keep me honest. 
* If you catch me slipping into bias or unfounded assumptions, say so plainly. 
* Let's refine both our conclusions and the way we reach them.
And now...
**FOLLOW THESE INSTRUCTIONS**:
0. Ask for as many directions needed to perform completely the task
1. Act as a COBOL guru. Taking a sequence of steps such as:
  1.1. Plan an outline.
  1.2. Decide what, if any, web searches are needed to gather more information making it a list
  1.3. Write a first draft.
  1.4. Read over the first draft to spot unjustified arguments or extraneous information.
  1.5. Revise the draft taking into account any weaknesses spotted.
A 'COBOL code' will be supplied as an annexed file.

YOUR TASKS ARE:
0. **Verify COBOL code Syntax**
1. **GENERATE A TABLE WITH CODE COMPONENTS**
Use headers like this for the table:
  * Line Number: Number, where the element described, appears
  * Element Type ( Variable | Procedure | Other): the type of element described
  * Name: Element Name
  * Description: Element description according is purpose in the code
2. **DESCRIPTION, the purpose of the 'COBOL code' given**, complete lists for:
   * Variables
   * Procedures
3. **WORKFLOW**: Give a workflow diagram including all "DATA DIVISION" and "PROCEDURE DIVISION" from the 'COBOL code' in Mermaid notation

For the Mermaid code syntax check this reference example:
```mermaid
graph LR;
    A((START));
    B[Open File];
    C[Main Loop];
    D{Main Menu};
    E[Create Record];
    F[Read Record];
    G[Update Record];
    H[Delete Record];
    I[Save File];
    J[Quit Program];
    K[Safe Close];
    L[Create File];
    L1((File Status));
    Z((STOP))
    A ==> B;
    L1 ==o|Normal Start| C;
    C --> D;
    D --> E;
    D --> F;
    D --> G;
    D --> H;
    E --> C;
    F --> C;
    G --> C;
    H --> C;
    I --> K;
    D --> J;
    J -->|Safe Exit| I;
    L1 --> |File Not Found| L;
    L --> B;
   B ==o L1;
   K ==> Z;

    subgraph SAFE START
       B; L1; L;
    end

    subgraph SAFE CLOSE
        I; K;
    end
    
    subgraph MAIN MENU
     C; D; E; F; G; H; J;
    end
```
COBOL CODE:
    """
        UPLOADED_FILE = st.file_uploader(f"**CHOOSE A LOCAL FILE TO ANALIZE**", key="Uploader1", accept_multiple_files=False)
        if UPLOADED_FILE:
            LOADED_CODE = CREATE_TASK(UPLOADED_FILE)
            TASK = f"{REASONER_PROMPT_BASE}\n{LOADED_CODE}"
        else :
            TASK = CODE_ANALIZER_PROMPT
        task = st.text_area("**__What is your task?__**", key="TAB_CODE_GEN", height=400, value=TASK)
        button = st.empty()

        BTN_RUN_TAB_ANALYZER = button.button("Run", key="Run1")    
        if BTN_RUN_TAB_ANALYZER:
            if DEBUG:
                st.success("START: " + fnow)
                st.success("MK_SIDEBAR_INFO() " + fnow)

            fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            with st.spinner(text=f"In Process + {fnow}"):
                CLIENT = MK_GROQ_CLIENT()
                st.success("MK_GROQ_CLIENT() " + fnow)
                REASONER_EXEC_FORM(CLIENT, task, model)

    
    with TAB_REASONER:
        TASK = f"{REASONER_PROMPT_BASE}"
        task = st.text_area("**__What is your task?__**", key="TAB_REASONER", height=400, value=TASK)
        button = st.empty()

        BTN_RUN_TAB_REASONER = button.button("Run", key="Run3")    
        if BTN_RUN_TAB_REASONER:
            if DEBUG:
                st.success("START: " + fnow)
                st.success("MK_SIDEBAR_INFO() " + fnow)

            fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            with st.spinner(text=f"In Process + {fnow}"):
                CLIENT = MK_GROQ_CLIENT()
                st.success("MK_GROQ_CLIENT() " + fnow)
                REASONER_EXEC_FORM(CLIENT, task, model)

    
    
    return(BTN_RUN_TAB_ANALYZER, BTN_TEXT_GENERATE, BTN_RUN_TAB_REASONER, task, model)

def REASONER_EXEC_FORM(CLIENT, task, model):
    step4  = st.empty()
    step3  = st.empty() 
    step2  = st.empty()
    step1  = st.empty()
    step0  = st.empty()

    from self_discover import (
        REASONING_MODULES,
        select_reasoning_modules,
        adapt_reasoning_modules,
        implement_reasoning_structure,
        execute_reasoning_structure
        )

    #select_reasoning_modules = ""
    prompt = select_reasoning_modules(REASONING_MODULES, task)
    stream_1 = CLIENT.chat.completions.create(
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
    stream_2 = CLIENT.chat.completions.create(
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
    stream_3 = CLIENT.chat.completions.create(
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
    stream_4 = CLIENT.chat.completions.create(
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

COBOLagency_vertical_logo = "assets/images/COBOLagency/COBOL_FullLockup-White_VERTICAL.png"
COBOLpro_vertical_logo = "assets/images/COBOLpro/COBOLpro_Vertical_FullLockup.png"
GROQ_LOGO_LIGHT = "../okrocket/assets/images/groqcloudlight.png"
OKROCKET_LOGO   = "../okrocket/assets/images/OKRocket_Rocket_Logo.png"
TOP_IMAGE = COBOLpro_vertical_logo
F_NOW_S1 = datetime.now().strftime("%Y/%m/%d")
st.image(TOP_IMAGE, caption=f"Groq Based **COBOL**__pro®__ MVP Preview** v {VERSION} {F_NOW_S1}", width=200)

            #st.write('CODE HERE')
st.html(f"<h1><b>Groq Based</b> COBOL<i>pro</i> <b>MVP Preview v{VERSION} {F_NOW_S1}</b></h1>")

TAB_LIST = [
["AGENT","st_groq_agent_demo.py"],
["APP_PY","app.py"],
["SELF_DICOVER","self_discover.py"],
["APP_AGENT","app_agent.py"],
["REASONING_MODULES","reasoning_modules.py"],
["ST_GROQ_AGENT_DEMO","st_groq_agent_demo.py"],
]

#MODELS= GROQ_MODELS

    
if __name__ == "__main__":
    UPLOADED_FILE = ''
    MODELS_LIST       = GET_MODELS()
    CLIENT = MK_GROQ_CLIENT()
    BTN_RUN_TAB_ANALYZER, BTN_TEXT_GENERATE, BTN_RUN_TAB_ANALYZER, task, model = MK_FORM(CLIENT, MODELS_LIST)
    fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if DEBUG:
            st.write(f"BTN_RUN_TAB_ANALYZER; {BTN_RUN_TAB_ANALYZER}, BTN_TEXT_GENERATE: {BTN_TEXT_GENERATE}, task: {task}, model: {model}")
WAIT = """
    if BTN_RUN_TAB_ANALYZER:
        if DEBUG:
            st.success("START: " + fnow)
            st.success("MK_SIDEBAR_INFO() " + fnow)

        fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        with st.spinner(text=f"In Process + {fnow}"):
            CLIENT = MK_GROQ_CLIENT()
            st.success("MK_GROQ_CLIENT() " + fnow)
            REASONER_EXEC_FORM(CLIENT, task, model)
"""
