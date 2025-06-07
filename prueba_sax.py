# FECHA: 2025/05/01 12:32:29 p.m. GMT-05:00  | url_base: | st_prefix_base: st |

# Codigo Streamlit para generación de fomularios
#
import pretty_errors
import os
import urllib.request
from urllib.parse import urlparse
import json
#from datetime import date, datetime, time
import datetime
import time as tiempo
from xml.dom import minidom
from distutils import errors
from distutils.log import error
from multiprocessing.sharedctypes import Value
from itertools import cycle
import pandas as pd
import numpy as np
import pytz
import altair as alt
import streamlit as st
import streamlit.components.v1 as components
from bs4 import BeautifulSoup
# Para AgGrid >>>>>>>>>>
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import pysaxon11.pysaxon11 as pysx

from py_nx_obs.oa_search import oa_search_fn
from py_nx_obs.sem_schol_api import sem_schol_search_fn
from py_nx_obs.aggrid_controls import aggrid_controls

from py_nx_obs.nx_search_general_params import EXPLANATION

#from lxml import etree
#from pysaxon11 import transform, file_path
#from st_aggrid.grid_options_builder import GridOptionsBuilder
#from st_aggrid.shared import JsCode

#*********************************************************************************************
#from functionforDownloadButtons import download_button

from example_app_csv_wrangler.functionforDownloadButtons import download_button # local on MVP

#[st.exception](https://docs.streamlit.io/library/api-reference/status/st.exception)
#e = RuntimeError('This is an exception of type RuntimeError')
#st.exception(e)

#[st.error](https://docs.streamlit.io/library/api-reference/status/st.error)
#EMOJI = U+23F0
#st.error('This is an error', icon = EMOJI)

ROOT = os.path.join(os.path.dirname(__file__))

np.random.seed(42)

st.markdown("## SISTEMA DE VIGILANCIA E INTELIGENCIA (MVP)")
st.markdown("###### FREEMIND TO STREAMLIT v0.0")
st.markdown("###### 2025/05/01 12:32:29 p.m. GMT-05:00 ")

with st.expander("AVANCE"):
    st.markdown(EXPLANATION)
MD_LEVEL_PY = "".join(0*"#")
st.markdown(MD_LEVEL_PY + " ---")
TAB1, TAB2 = st.tabs(["SISTEM PROMPTS", "AVANZADA"])
with TAB1:
    MD_LEVEL_PY = "".join(4*"#")
    st.markdown(MD_LEVEL_PY + " GENERADOR DE PROMPT V0.0.4")
    with st.form(key="ID_827275177", clear_on_submit=False):
        COLLECT_ANSWER = []
        ID_827275177_FORM_RESULT = {
            "form_key": "ID_827275177",
            "md_markdown": [],
            "columns": [],
            "selectbox": [],
            "text_input": [],
            "submit": []}
        MD_LEVEL_PY = "".join(3*"#")
        st.markdown(MD_LEVEL_PY + " PROMPT GENERATOR")
        COL1, COL2 = st.columns([5, 5])
        with COL1:
            MD_LEVEL_PY = "".join(5*"#")
            st.markdown(MD_LEVEL_PY + " DATOS DOC")
            ID_827275177_1_SELECTBOX = st.selectbox(
                "IDIOMA",
                ["SPANISH", "ENGLISH"],
                key="ID_1999857775")
            ID_827275177_FORM_RESULT.update({"ID_827275177_1_SELECTBOX": [
                "",
                "",
                str(ID_827275177_1_SELECTBOX)]})
            ID_827275177_2_SELECTBOX = st.selectbox(
                "ACTION",
                ["WRITE", "ANALYZE", "BRAINSTORM", "CRAFT", "CREATE", "EXPLAIN", "EXPLORE", "FIND", "GENERATE", "GIVE", "HELP", "INCREASE", "JUSTIFY", "OPTIMIZE", "OUTLINE", "RESEARCH", "SUGGEST", "SUMMARIZE", "TRANSLATE", "UNDERSTAND"],
                key="ID_243614855")
            ID_827275177_FORM_RESULT.update({"ID_827275177_2_SELECTBOX": [
                "",
                "",
                str(ID_827275177_2_SELECTBOX)]})
            ID_827275177_3_SELECTBOX = st.selectbox(
                "TEXTUAL STRUCTURE",
                ["A LINKEDIN ARTICLE", "A BLOG POST", "A BRIEF", "A CARTOON DESCRIPTION", "A CASE STUDY", "A CONTENT MARKETING STRATEGY", "A JOKE", "A LINKEDIN POST", "A PAPER", "A PERSONALITY-DRIVEN, WEEKLY NEWSLETTER", "A PRESS RELEASE", "A PROCEDURE MANUAL", "A STEP BY STEP PROCEDURE", "A TECHNICAL REPORT", "A TWEET", "A VIDEO SCRIPT", "A YOUTUBE VIDEO SCRIPT", "AD COPY", "AN ARTICLE", "AN ELEVATOR PITCH", "AN EXTENSIVE PIECE", "AN INFOGRAPHY CONTENT", "AN INSTAGRAM POST", "AN SOP", "ANALYSIS", "ARTICLE", "BLOG POST", "BOOK OUTLINE", "CUSTOMER RETENTION", "DATA FOR REPORTING & CLIENT CALLS", "EMAIL SEQUENCE", "ESSAY", "FINANCIAL STATEMENTS", "GAPS IN THE TECH STACK", "HEADLINE", "HIGH-CONVERTING SALES SCRIPTS", "HIGH-GROWTH MARKETS AND AUDIENCES TO TARGET", "HUMAN-SOUNDING REVIEWS", "IDEAS FOR PRODUCTS", "IDEAS TO REFRESH CREATIVES", "NDAS", "NEW EFFECTIVE IDEAS FOR LEAD GENERATION", "PRODUCT DESCRIPTION", "QUESTIONS FOR PODCAST INTERVIEWS", "RECIPE", "SALES COPY", "SEO KEYWORDS", "SOCIAL MEDIA BIOS & POSTS FOR INCREASED ENGAGEMENT", "SOCIAL MEDIA POST", "STEP BY STEP PROCEDURE", "SUMMARY", "UPSELL PAGES", "VIDEO SCRIPT", "WEBSITE COPY FOR A GLOBAL AUDIENCE", "WITH FEEDBACK TO TEAM MEMBERS", "WORD-BY-WORD SCRIPTS FOR YOUTUBE AND REELS"],
                key="ID_1530700427")
            ID_827275177_FORM_RESULT.update({"ID_827275177_3_SELECTBOX": [
                "",
                "",
                str(ID_827275177_3_SELECTBOX)]})
            ID_827275177_4_SELECTBOX = st.selectbox(
                "TONO",
                ["ASSERTIVE", "ACADEMIC", "ANALYTICAL", "CASUAL", "CONFIDENT", "CONFRONTATIONAL", "DESCRIPTIVE", "DIRECT", "ENGAGING", "EXPLANATION", "FICTIONAL", "FORMAL", "INFORMAL", "FRIENDLY", "HUMOROUS", "INFORMAL", "INFORMATIVE", "INSPIRATIONAL", "NARRATIVE", "OBJECTIVE", "OPINION", "PERSUASIVE", "TECHNICAL", "WITTY"],
                key="ID_980953339")
            ID_827275177_FORM_RESULT.update({"ID_827275177_4_SELECTBOX": [
                "",
                "",
                str(ID_827275177_4_SELECTBOX)]})
            ID_827275177_5_SELECTBOX = st.selectbox(
                "ESTILO",
                ["WRITING", "POETIC", "JOKE", "FICTIONAL"],
                key="ID_1072878670")
            ID_827275177_FORM_RESULT.update({"ID_827275177_5_SELECTBOX": [
                "",
                "",
                str(ID_827275177_5_SELECTBOX)]})
            ID_827275177_6_SLIDER = st.slider(label="N PALABRAS", min_value=250, max_value=2000, value=800, step=50, key="ID_479160003 ")
            ID_827275177_FORM_RESULT.update({"ID_827275177_6_SLIDER": [
                "slider",
                "N PALABRAS",
                str(ID_827275177_6_SLIDER)]})
            ID_827275177_7_SELECTBOX = st.selectbox(
                "FORMATO SALIDA",
                ["MARKDOWN", "A TABLE", "BULLET POINTS", "CODE", "EISENHOWER MATRIX", "ESSAYS", "GANTT CHART", "GRAPHS", "HTML", "JSON", "LIST", "OUTLINED RTF", "PARAGRAPHS", "PDF", "PLAIN TEXT", "PLAIN TEXT FILE", "PRESENTATION SLIDES", "REPORTS", "RICH TEXT", "ROOT CAUSE ANALYSIS", "SPREADSHEET", "STANDARD", "STEP-BY-STEP INSTRUCTIONS", "SUMMARISE", "SUMMARY", "TABLE", "TIMELINES/SCHEDULES", "WORD CLOUD", "XML", "XML MIND MAP"],
                key="ID_1942886858")
            ID_827275177_FORM_RESULT.update({"ID_827275177_7_SELECTBOX": [
                "",
                "",
                str(ID_827275177_7_SELECTBOX)]})
            ID_827275177_8_SELECTBOX = st.selectbox(
                "FORMA PERSONA",
                ["WE FORM", "I FORM", "SHE / HE FORM", "THEY FORM"],
                key="ID_946760784")
            ID_827275177_FORM_RESULT.update({"ID_827275177_8_SELECTBOX": [
                "",
                "",
                str(ID_827275177_8_SELECTBOX)]})
            ID_827275177_9_SELECTBOX = st.selectbox(
                "MEJORAMIENTO",
                ["SUMMARIZE", "ADAPT", "AMPLIFY", "CLARIFY", "CONDENSE", "DIVERSIFY", "DOWNPLAY", "ELABORATE", "ELEVATE", "EMPHASIZE / REITERATE", "ENLIVEN / ENERGIZE", "ENRICH / EMBELLISH", "EXAGGERATE", "EXPAND", "EXPLAIN", "FORMALIZE", "GLAMORIZE", "HUMANIZE", "ILLUMINATE", "ILLUSTRATE", "INFORMALIZE", "MODERNIZE", "NEUTRALIZE", "PARAPHRASE", "REFRAME", "REINTERPRET", "SENSATIONALIZE", "SIMPLIFY", "SOFT-PEDAL", "STREAMLINE", "SYNTHESIZE"],
                key="ID_760094202")
            ID_827275177_FORM_RESULT.update({"ID_827275177_9_SELECTBOX": [
                "",
                "",
                str(ID_827275177_9_SELECTBOX)]})
        with COL2:
            MD_LEVEL_PY = "".join(5*"#")
            st.markdown(MD_LEVEL_PY + "  ACTUAR COMO:")
            ID_827275177_2_SELECTBOX = st.selectbox(
                "ADJETIVO 2",
                ["TOP TIER", "APPRENTICE", "CORPORATE", "GURU", "HIGHLY SKILLED", "INSTRUCTOR", "JUNIOR", "NOVICE", "PROFESSOR", "SENIOR", "SKI", "SKILLED", "STUDENT", "TOP LEAD", "TYPICAL"],
                key="ID_793401905")
            ID_827275177_FORM_RESULT.update({"ID_827275177_2_SELECTBOX": [
                "",
                "",
                str(ID_827275177_2_SELECTBOX)]})
            ID_827275177_3_SELECTBOX = st.selectbox(
                "AREA2",
                ["OKR", "ACADEMIC", "AI", "AI AND CHINA", "AI IN UX", "AIR FORCE", "ARMY", "ART", "BOARD", "BUSINESS", "C-LEVEL", "CHATGPT", "CLAUDE", "CLOUD COMPUTING", "CODE AND GENERATIVE AI", "COMPUTER VISION", "CORPORATE", "CUSTOMER SUCCESS", "DATA ENGINEERING", "DATA SCIENCE AT THE INTERSECTION OF MACHINE LEARNING", "DESIGN", "DESIGN AND PRODUCT", "DEVOPS", "DYSTOPIA AND EXPONENTIAL TECHNOLOGY", "EDUCATION", "EMERGING TECH", "ENGINEERING", "EXPONENTIAL TECHNOLOGY", "FINANCIAL", "FUTURE", "GENERAL", "GENERATIVA AI", "GENERATIVE AI", "GENERATIVE AI PROSPECTS", "GOOGLE BARD", "HARDWARE", "HEALTH", "HHRR", "INDUSTRIAL", "INNOVATION", "INSTAGRAM", "INVESTING", "LEGAL", "LIFE SCIENCES", "LINKEDIN", "LLM", "LOGISTICS", "MACHINE LEARNING", "MARKETING", "MEDICINE", "MILITAR", "ML", "MLOPS", "NATIONAL DEFENSE", "NAVY", "OPERATIONS", "POLICE", "PRODUCT", "PRODUCTIVITY", "PROMPT ENGINEERING", "PSYCHOLOGY", "R & D", "RETAIL", "SALES", "SEO", "SERVICES", "SINGULARITY", "SINGULARITY AND TRANSHUMANISM", "SOCIAL NETWORKS", "SOFTWARE", "SOFTWARE DEVELOPMENT", "SPECIAL FORCES", "TALENT", "TECH VALUATIONS", "TECHNOLOGY", "TUTORIAL", "TWITTER / X", "VENTURE CAPITAL", "VIDEO", "YOUTUBE"],
                key="ID_1875864804")
            ID_827275177_FORM_RESULT.update({"ID_827275177_3_SELECTBOX": [
                "",
                "",
                str(ID_827275177_3_SELECTBOX)]})
            ID_827275177_4_SELECTBOX = st.selectbox(
                "ROL2",
                ["EXPERT & STRATEGIST", "ACCOUNTANT", "ADMIRAL", "ADVERTISER", "AMBANI", "ARTIST", "ARTIST", "ASSISTANT", "BACKEND DESIGNER", "BEST SELLING AUTHOR", "BUSINESS COACH", "BUYER PERSONA", "CAPE", "CAPTAIN", "CEO", "CODER", "COMMUNICATOR", "CONSULTANT", "CONTENT CREATOR", "COPYWRITER", "CORONEL", "CORPORAL", "DATA SCIENTIST", "DEAN", "DECISION MAKER", "DEVELOPER", "DEVOPS ENGINEER", "DIGITAL CONTENT CREATOR", "DIRECTORS", "DOCTOR", "ELON MUSK", "ENGINEER", "ENTREPRENEUR", "EXECUTIVES", "FINANCIAL CONSULTANT", "FRONTEND DESIGNER", "GARYVEE", "GENERAL", "GENERAL PUBLIC", "GHOSTWRITER", "GRAPHICS DESIGNER", "HISTORIAN", "HUMAN", "INFANT", "INFLUENCER", "INTERVIEWER", "INVENTOR", "JOURNALIST", "LAWYER", "LEAD", "LIFE COACH", "LIUTENANT", "MACHINE LEARNING ENGINEER", "MARINE", "MARKETER", "MARKETING CONSULTANT", "MASTERS", "MEMBER", "MINDSET COACH", "NUTRITIONIST", "OFFICERS", "PHD", "PILOT", "POLITICIAN", "PRO MARKETER", "PROFESSOR", "PROJECT MANAGER", "PROMPT ENGINEER", "RESEARCHER", "SALES PERSON", "SALESPERSON", "SARGEANT", "SENIOR TECHNICAL WRITER", "SEO SPECIALIST", "SOCIAL MEDIA SPECIALIST", "SOFTWARE ARCHITECT", "SOFTWARE ENGINEER", "SOLDIER", "SOLOPRENEUR", "SPECIALIST", "STEVE JOBS", "STOCK BROKER", "STOCKBROKER", "STRATEGIST", "STUDENT", "TEAM", "TEAM MEMBER", "TECHNICAL WRITER", "TECHNICIAN", "THERAPIST", "TOP EXECUTIVES", "TUTOR", "VP", "WEBSITE DESIGNER", "WRITER"],
                key="ID_1809820365")
            ID_827275177_FORM_RESULT.update({"ID_827275177_4_SELECTBOX": [
                "",
                "",
                str(ID_827275177_4_SELECTBOX)]})
            MD_LEVEL_PY = "".join(5*"#")
            st.markdown(MD_LEVEL_PY + " DIRIGIDO A")
            ID_827275177_7_SELECTBOX = st.selectbox(
                "ADJETIVO 3",
                ["CORPORATE", "APPRENTICE", "GURU", "HIGHLY SKILLED", "INSTRUCTOR", "JUNIOR", "NOVICE", "PROFESSOR", "SENIOR", "SKI", "SKILLED", "STUDENT", "TOP LEAD", "TOP TIER", "TYPICAL"],
                key="ID_1164157265")
            ID_827275177_FORM_RESULT.update({"ID_827275177_7_SELECTBOX": [
                "",
                "",
                str(ID_827275177_7_SELECTBOX)]})
            ID_827275177_8_SELECTBOX = st.selectbox(
                "AREA 3",
                ["GENERAL", "ACADEMIC", "AI", "AI AND CHINA", "AI IN UX", "AIR FORCE", "ARMY", "ART", "BOARD", "BUSINESS", "C-LEVEL", "CLOUD COMPUTING", "CODE AND GENERATIVE AI", "COMPUTER VISION", "CORPORATE", "CUSTOMER SUCCESS", "DATA ENGINEERING", "DATA SCIENCE AT THE INTERSECTION OF MACHINE LEARNING", "DESIGN", "DESIGN AND PRODUCT", "DEVOPS", "DYSTOPIA AND EXPONENTIAL TECHNOLOGY", "EDUCATION", "EMERGING TECH", "ENGINEERING", "EXPONENTIAL TECHNOLOGY", "FINANCIAL", "FUTURE", "GENERATIVA AI", "GENERATIVE AI", "GENERATIVE AI PROSPECTS", "HARDWARE", "HEALTH", "HHRR", "INDUSTRIAL", "INNOVATION", "INSTAGRAM", "INVESTING", "LEGAL", "LIFE SCIENCES", "LINKEDIN", "LLM", "LOGISTICS", "MACHINE LEARNING", "MARKETING", "MEDICINE", "MILITAR", "ML", "MLOPS", "NATIONAL DEFENSE", "NAVY", "OKR", "OPERATIONS", "POLICE", "PRODUCT", "PRODUCTIVITY", "PROMPT ENGINEERING", "PSYCHOLOGY", "R & D", "RETAIL", "SALES", "SEO", "SERVICES", "SINGULARITY", "SINGULARITY AND TRANSHUMANISM", "SOCIAL NETWORKS", "SOFTWARE", "SOFTWARE DEVELOPMENT", "SPECIAL FORCES", "TALENT", "TECH VALUATIONS", "TECHNOLOGY", "TUTORIAL", "TWITTER / X", "VENTURE CAPITAL", "VIDEO", "YOUTUBE"],
                key="ID_1615155112")
            ID_827275177_FORM_RESULT.update({"ID_827275177_8_SELECTBOX": [
                "",
                "",
                str(ID_827275177_8_SELECTBOX)]})
            ID_827275177_9_SELECTBOX = st.selectbox(
                "ROL 3",
                ["DECISION MAKER", "ACCOUNTANT", "ADMIRAL", "ADVERTISER", "AMBANI", "ARTIST", "ARTIST", "ASSISTANT", "BACKEND DESIGNER", "BEST SELLING AUTHOR", "BUSINESS COACH", "BUYER PERSONA", "CAPE", "CAPTAIN", "CEO", "CODER", "COMMUNICATOR", "CONSULTANT", "CONTENT CREATOR", "COPYWRITER", "CORONEL", "CORPORAL", "DATA SCIENTIST", "DEAN", "DECISION MAKER", "DEVELOPER", "DEVOPS ENGINEER", "DIGITAL CONTENT CREATOR", "DIRECTORS", "DOCTOR", "ELON MUSK", "ENGINEER", "ENTREPRENEUR", "EXECUTIVES", "EXPERT & STRATEGIST", "FINANCIAL CONSULTANT", "FRONTEND DESIGNER", "GARYVEE", "GENERAL", "GENERAL PUBLIC", "GHOSTWRITER", "GRAPHICS DESIGNER", "HISTORIAN", "HUMAN", "INFANT", "INFLUENCER", "INTERVIEWER", "INVENTOR", "JOURNALIST", "LAWYER", "LEAD", "LIFE COACH", "LIUTENANT", "MACHINE LEARNING ENGINEER", "MARINE", "MARKETER", "MARKETING CONSULTANT", "MASTERS", "MEMBER", "MINDSET COACH", "NUTRITIONIST", "OFFICERS", "PHD", "PILOT", "POLITICIAN", "PRO MARKETER", "PROFESSOR", "PROJECT MANAGER", "PROMPT ENGINEER", "RESEARCHER", "SALES PERSON", "SALESPERSON", "SARGEANT", "SENIOR TECHNICAL WRITER", "SEO SPECIALIST", "SOCIAL MEDIA SPECIALIST", "SOFTWARE ARCHITECT", "SOFTWARE ENGINEER", "SOLDIER", "SOLOPRENEUR", "SPECIALIST", "STEVE JOBS", "STOCK BROKER", "STOCKBROKER", "STRATEGIST", "STUDENT", "TEAM", "TEAM MEMBER", "TECHNICAL WRITER", "TECHNICIAN", "THERAPIST", "TOP EXECUTIVES", "TUTOR", "VP", "WEBSITE DESIGNER", "WRITER"],
                key="ID_1291017469")
            ID_827275177_FORM_RESULT.update({"ID_827275177_9_SELECTBOX": [
                "",
                "",
                str(ID_827275177_9_SELECTBOX)]})
        ID_827275177_3_SELECTBOX = st.selectbox(
            "TÍTULO",
            ["2 PREGUNTAS CLAVE AL HABILITAR PROCESOS DE CAMBIO EN TU EMPRESA", "5 APLICACIONES PARA LA EFECTIVIDAD ORGANIZACIONAL", "5 CLAVES PARA DEJAR DE SER SÓLO UN JEFE Y CONVERTIRTE EN UN BUEN LÍDER", "5 CLAVES PARA NO SER UN JEFE Y CONVERTIRTE EN UN BUEN LÍDER", "5 DIFERENCIAS ENTRE TELETRABAJO Y DIGITAL WORKPLACE", "5 PASOS PARA EVITAR REUNIONES IMPRODUCTIVAS Y LA JUNTITIS", "7 RAZONES POR LAS QUE FRACASA LA PLANIFICACIÓN ESTRATÉGICA", "8 TIPS PARA DEFINIR OKRS PARA EL PRÓXIMO PERÍODO", "ADIOS A LAS EVALUACIONE ANUALES: PORQUÉ LAS EMPRESAS LIDERES ELIGEN \"AGILIZAR EL DESEMPEÑO\"", "BALANCED SCORECARD U OKR, CUÁL MODELO ELEGIR", "BASES PARA ENTENDER LOS OKRS OBJETIVOS Y RESULTADOS CLAVE", "BENEFICIOS DE LOS OKRS PARA TU ORGANIZACIÓN", "BONO DE U2 UTILIZA OKR", "CFR, EL SECRETO PARA UNA GESTIÓN CONTINUADA DEL RENDIMIENTO EXITOSA", "CICLOS DE OKRS", "CLAVES PARA ENTENDER CÓMO FUNCIONA LA \"GESTIÓN CONTINUA DEL DESEMPEÑO\"", "COMPARACIÓN ENTRE OKR'S Y HOSHIN KANRI", "CONSIDERACIONES AL ADOPTAR OKRS", "CREACIÓN DE OBJETIVOS PERSONALES A TRAVES DE LOS OKRS", "CREATIVIDAD EN LA AUSENCIA DE RECURSOS CRÍTICOS", "CREATIVIDAD, EL HÁBITO INDISPENSABLE PARA EL ÉXITO EMPRESARIAL", "CUANDO JOHN DOERR REGALO LOS OKR A GOOGLE", "CÓMO CREAR OKRS COMPLETOS PARA IMPULSAR EL CRECIMIENTO", "CÓMO CREAR OKRS COMPLETOS: UNA GUÍA INTEGRAL", "CÓMO ESTABLECER OKR CLAROS Y PROCESABLES", "CÓMO IMPLEMENTAR OKRS CON UNA METODOLOGIA ÁGIL", "CÓMO NIVELAR LA CANCHA Y SALIR ADELANTE EN TIEMPOS DE CRISIS", "CÓMO USAR OKRS JUNTO CON KPIS (KEY PERFORMANCE INDICATORS)", "DECISIONES TARDÍAS TAL VEZ DEBE BAJAR EL CENTRO DE GRAVEDAD EN SU ORGANIZACIÓN", "EL BIENESTAR DE TU EQUIPO", "EL GRAN VALOR DE UN PROPÓSITO", "EL MIEDO AL CAMBIO EN LAS PERSONAS COMO EN LAS EMPRESAS", "EL ORIGEN DE LOS OKRS", "EMPRESAS QUE USAN OKR", "EN ESTRATEGIA, EL TIEMPO ES LO PRIMERO", "ERRORES COMUNES DE OKRS", "ES EL ENFOQUE DE DISEÑO (DESIGN THINKINGREALMENTE UN ENFOQUE INTEGRAL?", "ES UNA BUENA PRÁCTICA BAJAR TUS OKR EN CASCADA", "ESTRATEGIAS PARA ALINEAR LOS OKR CON LA ESTRATEGIA Y LAS PRIORIDADES DE LA ORGANIZACIÓN", "GANA UN EQUIPO MAS PRODUCTIVO AL FOMENTAR SUS PASATIEMPOS", "GESTIÓN DEL CAMBIO, QUÉ MODELO SEGUIR", "IMPACTO DE OKRS EN LA PRODUCTIVIDAD", "INNOVACIÓN PARA LA MOTIVACIÓN DE LOS EMPLEADOS ¿CÓMO?", "KPIS Y OKRS, CÓMO SE COMPLEMENTAN", "LA FÓRMULA OKR CFR PARA GESTIONAR EL DESEMPEÑO Y FIJAR COMPENSACIONES", "LA IMPORTANCIA DE LAS ACCIONES EN EL MARCO DE LOS OKR", "LA ORGANIZACIÓN MÁS GIL CORRE CON VENTAJA", "LAS ACCIONES CORRESPONDIENTES A LOS OKR SON ESENCIALES EN SU ÉXITO", "LOS OKRS EN LAS STARTUPS", "LOS OKRS LLEGARON PARA QUEDARSE", "MANTENER UN EQUIPO MOTIVADO CON RETOS Y OKRS", "MISIÓN, VISIÓN Y VALORES", "MÉTODOS DE SEGUIMIENTO Y NOTIFICACIÓN DE LOS PROGRESOS REALIZADOS EN LA CONSECUCIÓN DE LOS OKR.", "NO ESTAMOS NI EN TECNOLOGÍA NI SOFTWARE, ¿QUÉ ME PUEDEN APORTAR LOS OKR?", "OBJETIVOS Y RESULTADOS CLAVE EN TIEMPOS DE ADAPTACIÓN", "OFERTAS INNOVADORAS SERVICIOS LOGÍSTICOS TODO UN RETO", "OKR ACTIONS: THE FUEL FOR SUCCESS", "OKR USA LA FÓRMULA  DE GOOGLE A TU FAVOR", "OKRS AHORA MÁS QUE NUNCA: AGILIDAD EN LA DEFINICION DE OBJETIVOS", "OKRS PARA EL DÍA A DÍA", "OKRS POR DENTRO: SECRETOS DE EMPRESAS QUE SE ANIMARON A CAMBIAR", "PASO A PASO: SESIÓN DE DEFINICIÓN DE TUS OKR + DESIGN THINKING", "PASO A PASO: SESIÓN PARA DEFINICIÓN DE TUS OKR USANDO DESIGN THINKING", "PASOS PARA IMPLANTACIÓN DE UN PLAN PILOTO DE OKR EN UNA PYME", "PRIMEROS PASOS EN EL ESTABLECIMIENTO DE OBJETIVOS OKRS", "PROYECTOS EN CRISIS: PORQUÉ  SENTIRSE UN NÁUFRAGO ES EL PRIMER PASO PARA SALIR DEL ATOLLADERO", "RESOLVER RETOS INTERNAMENTE O CONTRATAR ESPECIALISTAS", "REUNIONES PRODUCTIVAS", "SUPERPODERES DE LOS OKRS", "TE ESTÁS VOLVIENDO LOCO ENTRE EL HOME OFFICE Y HOME SCHOOLING", "TELETRABAJO MÁS PRODUCTIVO CON OKR", "TIPOS DE OKRS", "TODO LO QUE NECESITAS SABER PARA ESTABLECER OKRS EN TU ORGANIZACIÓN", "TÉCNICAS PARA FOMENTAR LA RESPONSABILIDAD Y LA MEJORA CONTINUA CON OKRS", "USAR UN ENFOQUE DE DESIGN THINKING PARA DEFINIR TUS OKRS", "¡OH NO! OKR,  ¿SON OTRO ACRÓNIMO DE 3 LETRAS INÚTIL?", "¿PORQUÉ ES IMPORTANTE LA INNOVACIÓN CONSTANTE EN TU EMPRESA?", "¿QUÉ SON LOS OKR Y POR QUÉ SON IMPORTANTES?", "¿QUÉ SUCEDIÓ EN MI EMPRESA DESPUÉS DE CONOCER E IMPLEMENTAR LOS OKRS?"],
            key="ID_1194427067")
        ID_827275177_FORM_RESULT.update({"ID_827275177_3_SELECTBOX": [
            "",
            "",
            str(ID_827275177_3_SELECTBOX)]})
        ID_827275177_4_TEXT_INPUT = st.text_input("ALTERNATIVA DE PROPUESTA DE TÍTULO CON FRASE PODEROSA", key="ID_424884899")
        ID_827275177_FORM_RESULT.update({"ID_827275177_4_TEXT_INPUT": [
            "text_input",
            "",
            str(ID_827275177_4_TEXT_INPUT)]})
        # Every form must have a submit button.
        ID_827275177_SUBMITTED = st.form_submit_button(
            "PROMPT",
            help="Submit_ID_827275177")
        if ID_827275177_SUBMITTED:
            # print()
            COLLECT_ANSWER = ",".join(COLLECT_ANSWER)
            FORM_RESULT = ID_827275177_FORM_RESULT
            SEARCH_TERMS_KEY = FORM_RESULT["form_key"]
            print(json.dumps(FORM_RESULT))
            SEARCH_TERMS = str(FORM_RESULT["ID_1373687557_3_TEXT_INPUT"][2])
            SEARCH_ENGINE = str(FORM_RESULT["ID_1373687557_4_RADIO"][2])
            print(SEARCH_TERMS)
            DEBUG_FLAG = ID_1373687557_5_CHECKBOX
            if SEARCH_ENGINE == "OPENAIRE":
                PD_DF = oa_search_fn(SEARCH_TERMS, DEBUG_FLAG)
                aggrid_controls(PD_DF) # LLAMADO AGGRID FIJO
            elif SEARCH_ENGINE == "SEMANTIC SCHOLAR":
                SEM_SCHOL_LIMIT = "20"
                PD_DF = sem_schol_search_fn(SEARCH_TERMS, DEBUG_FLAG, SEM_SCHOL_LIMIT)
                st.success("Implementación en desarrollo y prueba")
            elif SEARCH_ENGINE == "CONSENSUS":
                st.warning("Explorar inmediatamente esta opción")
            else:
                st.warning("ID_827275177: Implementación pendiente para este buscador")
with TAB2:
    with st.form(key="ID_578618110", clear_on_submit=False):
        COLLECT_ANSWER = []
        ID_578618110_FORM_RESULT = {
            "form_key": "ID_578618110",
            "md_markdown": [],
            "selectbox": [],
            "selectbox": [],
            "selectbox": [],
            "text_input": [],
            "action": [],
            "submit": []}
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " BÚSQUEDA AVANZADA")
        ID_578618110_2_SELECTBOX = st.selectbox(
            "CONTENT SOURCES",
            ["ALL CONTENT", "RESEARCH  PRODUCTS", "PROJECTS", "ORGANIZATIONS", "DATA SOURCES"],
            key="ID_1663024493")
        ID_578618110_FORM_RESULT.update({"ID_578618110_2_SELECTBOX": [
            "",
            "",
            str(ID_578618110_2_SELECTBOX)]})
        ID_578618110_3_SELECTBOX = st.selectbox(
            "SEARCH FIELD",
            ["ANY FIELD", "ACRONYM", "TITLE", "KEYWORD", "FUNDER", "FUNDING STREAM"],
            key="ID_1608630295")
        ID_578618110_FORM_RESULT.update({"ID_578618110_3_SELECTBOX": [
            "",
            "",
            str(ID_578618110_3_SELECTBOX)]})
        ID_578618110_4_SELECTBOX = st.selectbox(
            "LOGICAL CONECTOR",
            ["IS", "IS NOT"],
            key="ID_1621409680")
        ID_578618110_FORM_RESULT.update({"ID_578618110_4_SELECTBOX": [
            "",
            "",
            str(ID_578618110_4_SELECTBOX)]})
        ID_578618110_5_TEXT_INPUT = st.text_input("TÉRMINOS DE BÚSQUEDA", key="ID_1215491467")
        ID_578618110_FORM_RESULT.update({"ID_578618110_5_TEXT_INPUT": [
            "text_input",
            "INPUT TERMS",
            str(ID_578618110_5_TEXT_INPUT)]})
        # Every form must have a submit button.
        ID_578618110_SUBMITTED = st.form_submit_button(
            "BUSCAR",
            help="Submit_ID_578618110")
        if ID_578618110_SUBMITTED:
            # print()
            COLLECT_ANSWER = ",".join(COLLECT_ANSWER)
            FORM_RESULT = ID_578618110_FORM_RESULT
            SEARCH_TERMS_KEY = FORM_RESULT["form_key"]
            print(json.dumps(FORM_RESULT))
            SEARCH_TERMS = str(FORM_RESULT["ID_1373687557_3_TEXT_INPUT"][2])
            SEARCH_ENGINE = str(FORM_RESULT["ID_1373687557_4_RADIO"][2])
            print(SEARCH_TERMS)
            DEBUG_FLAG = ID_1373687557_5_CHECKBOX
            if SEARCH_ENGINE == "OPENAIRE":
                PD_DF = oa_search_fn(SEARCH_TERMS, DEBUG_FLAG)
                aggrid_controls(PD_DF) # LLAMADO AGGRID FIJO
            elif SEARCH_ENGINE == "SEMANTIC SCHOLAR":
                SEM_SCHOL_LIMIT = "20"
                PD_DF = sem_schol_search_fn(SEARCH_TERMS, DEBUG_FLAG, SEM_SCHOL_LIMIT)
                st.success("Implementación en desarrollo y prueba")
            elif SEARCH_ENGINE == "CONSENSUS":
                st.warning("Explorar inmediatamente esta opción")
            else:
                st.warning("ID_578618110: Implementación pendiente para este buscador")
MD_LEVEL_PY = "".join(0*"#")
st.markdown(MD_LEVEL_PY + " ---")
MD_LEVEL_PY = "".join(0*"#")
st.markdown(MD_LEVEL_PY + " ---")
with st.sidebar:
    MD_LEVEL_PY = "".join(3*"#")
    st.markdown(MD_LEVEL_PY + " FILTRO DE RESULTADOS")
    with st.form(key="ID_392813717", clear_on_submit=False):
        COLLECT_ANSWER = []
        ID_392813717_FORM_RESULT = {
            "form_key": "ID_392813717",
            "selectbox": [],
            "selectbox": [],
            "checkgroup": [],
            "submit": []}
        ID_392813717_1_SELECTBOX = st.selectbox(
            "RESULTS PER PAGE",
            ["10", "20", "50", "100"],
            key="ID_937675360")
        ID_392813717_FORM_RESULT.update({"ID_392813717_1_SELECTBOX": [
            "",
            "",
            str(ID_392813717_1_SELECTBOX)]})
        ID_392813717_2_SELECTBOX = st.selectbox(
            "SORT BY",
            ["RELEVANCE", "DATE (MOST RECENT)", "DATE (LEAST RECENT)"],
            key="ID_56969866")
        ID_392813717_FORM_RESULT.update({"ID_392813717_2_SELECTBOX": [
            "",
            "",
            str(ID_392813717_2_SELECTBOX)]})
        ID_392813717_1_CHECKBOX = st.checkbox("BACK [<]", key="ID_1401272221")
        #"ID_392813717_1_CHECKBOX_BACK [<]" :ID_392813717_1_CHECKBOX
        ID_392813717_FORM_RESULT.update({"ID_392813717_1_CHECKBOX": [
            "checkbox",
            "BACK [<]",
            str(ID_392813717_1_CHECKBOX)]})
        ID_392813717_2_CHECKBOX = st.checkbox("1", key="ID_1012597754")
        #"ID_392813717_2_CHECKBOX_1" :ID_392813717_2_CHECKBOX
        ID_392813717_FORM_RESULT.update({"ID_392813717_2_CHECKBOX": [
            "checkbox",
            "1",
            str(ID_392813717_2_CHECKBOX)]})
        ID_392813717_3_CHECKBOX = st.checkbox("2", key="ID_1084757217")
        #"ID_392813717_3_CHECKBOX_2" :ID_392813717_3_CHECKBOX
        ID_392813717_FORM_RESULT.update({"ID_392813717_3_CHECKBOX": [
            "checkbox",
            "2",
            str(ID_392813717_3_CHECKBOX)]})
        ID_392813717_4_CHECKBOX = st.checkbox("3", key="ID_110522183")
        #"ID_392813717_4_CHECKBOX_3" :ID_392813717_4_CHECKBOX
        ID_392813717_FORM_RESULT.update({"ID_392813717_4_CHECKBOX": [
            "checkbox",
            "3",
            str(ID_392813717_4_CHECKBOX)]})
        ID_392813717_5_CHECKBOX = st.checkbox("4", key="ID_542246257")
        #"ID_392813717_5_CHECKBOX_4" :ID_392813717_5_CHECKBOX
        ID_392813717_FORM_RESULT.update({"ID_392813717_5_CHECKBOX": [
            "checkbox",
            "4",
            str(ID_392813717_5_CHECKBOX)]})
        ID_392813717_6_CHECKBOX = st.checkbox("5", key="ID_789110284")
        #"ID_392813717_6_CHECKBOX_5" :ID_392813717_6_CHECKBOX
        ID_392813717_FORM_RESULT.update({"ID_392813717_6_CHECKBOX": [
            "checkbox",
            "5",
            str(ID_392813717_6_CHECKBOX)]})
        ID_392813717_7_CHECKBOX = st.checkbox("NEXT [>]", key="ID_1201023962")
        #"ID_392813717_7_CHECKBOX_NEXT [>]" :ID_392813717_7_CHECKBOX
        ID_392813717_FORM_RESULT.update({"ID_392813717_7_CHECKBOX": [
            "checkbox",
            "NEXT [>]",
            str(ID_392813717_7_CHECKBOX)]})
        # Every form must have a submit button.
        ID_392813717_SUBMITTED = st.form_submit_button(
            "Configurar Resultado",
            help="Submit_ID_392813717")
        if ID_392813717_SUBMITTED:
            # print()
            COLLECT_ANSWER = ",".join(COLLECT_ANSWER)
            FORM_RESULT = ID_392813717_FORM_RESULT
            SEARCH_TERMS_KEY = FORM_RESULT["form_key"]
            print(json.dumps(FORM_RESULT))
            SEARCH_TERMS = str(FORM_RESULT["ID_1373687557_3_TEXT_INPUT"][2])
            SEARCH_ENGINE = str(FORM_RESULT["ID_1373687557_4_RADIO"][2])
            print(SEARCH_TERMS)
            DEBUG_FLAG = ID_1373687557_5_CHECKBOX
            if SEARCH_ENGINE == "OPENAIRE":
                PD_DF = oa_search_fn(SEARCH_TERMS, DEBUG_FLAG)
                aggrid_controls(PD_DF) # LLAMADO AGGRID FIJO
            elif SEARCH_ENGINE == "SEMANTIC SCHOLAR":
                SEM_SCHOL_LIMIT = "20"
                PD_DF = sem_schol_search_fn(SEARCH_TERMS, DEBUG_FLAG, SEM_SCHOL_LIMIT)
                st.success("Implementación en desarrollo y prueba")
            elif SEARCH_ENGINE == "CONSENSUS":
                st.warning("Explorar inmediatamente esta opción")
            else:
                st.warning("ID_392813717: Implementación pendiente para este buscador")
    st.button("DESCARGAR RESULTADOS", key="ID_432621706")
    MD_LEVEL_PY = "".join(2*"#")
    st.markdown(MD_LEVEL_PY + " PRUEBA DE FILTROS")
    with st.form(key="ID_1790660493", clear_on_submit=False):
        COLLECT_ANSWER = []
        ID_1790660493_FORM_RESULT = {
            "form_key": "ID_1790660493",
            "md_markdown": [],
            "md_markdown": [],
            "md_markdown": [],
            "md_markdown": [],
            "md_markdown": [],
            "md_markdown": [],
            "md_markdown": [],
            "md_markdown": [],
            "md_markdown": [],
            "md_markdown": [],
            "date_input": [],
            "date_input": [],
            "checkgroup": [],
            "submit": []}
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " ACCESS")
        ID_1790660493_1_RADIO = st.radio("ACCESS CANTIDAD:", [
            "OPTION",
            "OPTION",
            "OPTION",
            "OPTION",
            "OPTION"], key="ID_1659208099")
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_1_RADIO": [
            "radio",
            "ACCESS CANTIDAD:",
            str(ID_1790660493_1_RADIO)]})
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " EXPAND: VIEW ALL>")
        st.markdown("---")
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " DOCUMENT TYPE")
        ID_1790660493_1_CHECKBOX = st.checkbox("OPTION", key="ID_867425173")
        #"ID_1790660493_1_CHECKBOX_OPTION" :ID_1790660493_1_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_1_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_1_CHECKBOX)]})
        ID_1790660493_2_CHECKBOX = st.checkbox("OPTION", key="ID_1047357274")
        #"ID_1790660493_2_CHECKBOX_OPTION" :ID_1790660493_2_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_2_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_2_CHECKBOX)]})
        ID_1790660493_3_CHECKBOX = st.checkbox("OPTION", key="ID_1730770885")
        #"ID_1790660493_3_CHECKBOX_OPTION" :ID_1790660493_3_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_3_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_3_CHECKBOX)]})
        ID_1790660493_4_CHECKBOX = st.checkbox("OPTION", key="ID_1016645675")
        #"ID_1790660493_4_CHECKBOX_OPTION" :ID_1790660493_4_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_4_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_4_CHECKBOX)]})
        ID_1790660493_5_CHECKBOX = st.checkbox("OPTION", key="ID_962593433")
        #"ID_1790660493_5_CHECKBOX_OPTION" :ID_1790660493_5_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_5_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_5_CHECKBOX)]})
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " EXPAND: VIEW ALL>")
        st.markdown("---")
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " FIELD OF SCIENCE (FOS)")
        ID_1790660493_1_CHECKBOX = st.checkbox("OPTION", key="ID_1300456493")
        #"ID_1790660493_1_CHECKBOX_OPTION" :ID_1790660493_1_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_1_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_1_CHECKBOX)]})
        ID_1790660493_2_CHECKBOX = st.checkbox("OPTION", key="ID_186859501")
        #"ID_1790660493_2_CHECKBOX_OPTION" :ID_1790660493_2_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_2_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_2_CHECKBOX)]})
        ID_1790660493_3_CHECKBOX = st.checkbox("OPTION", key="ID_1862601516")
        #"ID_1790660493_3_CHECKBOX_OPTION" :ID_1790660493_3_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_3_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_3_CHECKBOX)]})
        ID_1790660493_4_CHECKBOX = st.checkbox("OPTION", key="ID_293376226")
        #"ID_1790660493_4_CHECKBOX_OPTION" :ID_1790660493_4_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_4_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_4_CHECKBOX)]})
        ID_1790660493_5_CHECKBOX = st.checkbox("OPTION", key="ID_41773725")
        #"ID_1790660493_5_CHECKBOX_OPTION" :ID_1790660493_5_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_5_CHECKBOX": [
            "checkbox",
            "OPTION",
            str(ID_1790660493_5_CHECKBOX)]})
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " EXPAND: VIEW ALL>")
        st.markdown("---")
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " FUNDER (FUND)")
        ID_1790660493_1_MULTISELECT = st.multiselect("CANT: FUNDER",[
            "OPTION", "OPTION", "OPTION", "OPTION", "OPTION"],
            [],
            key="ID_1166407207")
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_1_MULTISELECT": [
            "multiselect",
            "CANT: FUNDER",
            str(ID_1790660493_1_MULTISELECT)]})
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " EXPAND: VIEW ALL>")
        st.markdown("---")
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " SDG (BETA)")
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " EXPAND: VIEW ALL>")
        st.markdown("---")
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " COUNTRY")
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " EXPAND: VIEW ALL>")
        st.markdown("---")
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " LANGUAGE")
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " EXPAND: VIEW ALL>")
        st.markdown("---")
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " SOURCE")
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " EXPAND: VIEW ALL>")
        st.markdown("---")
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " RESEARCH COMMUNITY")
        MD_LEVEL_PY = "".join(5*"#")
        st.markdown(MD_LEVEL_PY + " EXPAND: VIEW ALL>")
        st.markdown("---")
        MD_LEVEL_PY = "".join(4*"#")
        st.markdown(MD_LEVEL_PY + " YEAR RANGE")
        ID_1790660493_11_DATE_INPUT = st.date_input("FROM", datetime.date(2018, 1, 1), key="ID_751857579")
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_11_DATE_INPUT": [
            "date_input",
            "FROM",
            str(ID_1790660493_11_DATE_INPUT)]})
        ID_1790660493_12_DATE_INPUT = st.date_input("TO", datetime.date(2018, 12, 1), key="ID_1421253580")
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_12_DATE_INPUT": [
            "date_input",
            "TO",
            str(ID_1790660493_12_DATE_INPUT)]})
        ID_1790660493_1_CHECKBOX = st.checkbox("THIS YEAR", key="ID_1864569817")
        #"ID_1790660493_1_CHECKBOX_THIS YEAR" :ID_1790660493_1_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_1_CHECKBOX": [
            "checkbox",
            "THIS YEAR",
            str(ID_1790660493_1_CHECKBOX)]})
        ID_1790660493_2_CHECKBOX = st.checkbox("LAS 5 YEARS", key="ID_16448974")
        #"ID_1790660493_2_CHECKBOX_LAS 5 YEARS" :ID_1790660493_2_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_2_CHECKBOX": [
            "checkbox",
            "LAS 5 YEARS",
            str(ID_1790660493_2_CHECKBOX)]})
        ID_1790660493_3_CHECKBOX = st.checkbox("LAST 10 YEARS", key="ID_1797391363")
        #"ID_1790660493_3_CHECKBOX_LAST 10 YEARS" :ID_1790660493_3_CHECKBOX
        ID_1790660493_FORM_RESULT.update({"ID_1790660493_3_CHECKBOX": [
            "checkbox",
            "LAST 10 YEARS",
            str(ID_1790660493_3_CHECKBOX)]})
        # Every form must have a submit button.
        ID_1790660493_SUBMITTED = st.form_submit_button(
            "FILTRAR",
            help="Submit_ID_1790660493")
        if ID_1790660493_SUBMITTED:
            # print()
            COLLECT_ANSWER = ",".join(COLLECT_ANSWER)
            FORM_RESULT = ID_1790660493_FORM_RESULT
            SEARCH_TERMS_KEY = FORM_RESULT["form_key"]
            print(json.dumps(FORM_RESULT))
            SEARCH_TERMS = str(FORM_RESULT["ID_1373687557_3_TEXT_INPUT"][2])
            SEARCH_ENGINE = str(FORM_RESULT["ID_1373687557_4_RADIO"][2])
            print(SEARCH_TERMS)
            DEBUG_FLAG = ID_1373687557_5_CHECKBOX
            if SEARCH_ENGINE == "OPENAIRE":
                PD_DF = oa_search_fn(SEARCH_TERMS, DEBUG_FLAG)
                aggrid_controls(PD_DF) # LLAMADO AGGRID FIJO
            elif SEARCH_ENGINE == "SEMANTIC SCHOLAR":
                SEM_SCHOL_LIMIT = "20"
                PD_DF = sem_schol_search_fn(SEARCH_TERMS, DEBUG_FLAG, SEM_SCHOL_LIMIT)
                st.success("Implementación en desarrollo y prueba")
            elif SEARCH_ENGINE == "CONSENSUS":
                st.warning("Explorar inmediatamente esta opción")
            else:
                st.warning("ID_1790660493: Implementación pendiente para este buscador")
with st.form(key="ID_1789643611", clear_on_submit=False):
    COLLECT_ANSWER = []
    ID_1789643611_FORM_RESULT = {
        "form_key": "ID_1789643611",
        "file_uploader": []}
    ID_1789643611_1_FILE_UPLOADER = st.file_uploader("Upload a CSV", key="ID_1089680246")
    ID_1789643611_FORM_RESULT.update({"ID_1789643611_1_FILE_UPLOADER": [
        "file_uploader",
        "CARGUE RESULTADO",
        str(ID_1789643611_1_FILE_UPLOADER)]})
    # Every form must have a submit button.
    ID_1789643611_SUBMITTED = st.form_submit_button(
        "",
        help="Submit_ID_1789643611")
    if ID_1789643611_SUBMITTED:
        # print()
        COLLECT_ANSWER = ",".join(COLLECT_ANSWER)
        FORM_RESULT = ID_1789643611_FORM_RESULT
        SEARCH_TERMS_KEY = FORM_RESULT["form_key"]
        print(json.dumps(FORM_RESULT))
        SEARCH_TERMS = str(FORM_RESULT["ID_1373687557_3_TEXT_INPUT"][2])
        SEARCH_ENGINE = str(FORM_RESULT["ID_1373687557_4_RADIO"][2])
        print(SEARCH_TERMS)
        DEBUG_FLAG = ID_1373687557_5_CHECKBOX
        if SEARCH_ENGINE == "OPENAIRE":
            PD_DF = oa_search_fn(SEARCH_TERMS, DEBUG_FLAG)
            aggrid_controls(PD_DF) # LLAMADO AGGRID FIJO
        elif SEARCH_ENGINE == "SEMANTIC SCHOLAR":
            SEM_SCHOL_LIMIT = "20"
            PD_DF = sem_schol_search_fn(SEARCH_TERMS, DEBUG_FLAG, SEM_SCHOL_LIMIT)
            st.success("Implementación en desarrollo y prueba")
        elif SEARCH_ENGINE == "CONSENSUS":
            st.warning("Explorar inmediatamente esta opción")
        else:
            st.warning("ID_1789643611: Implementación pendiente para este buscador")
import components_example_html as cxh
# bootstrap 4 collapse example
# data for example
with st.sidebar:
    components.html(cxh.component_example_body, height=520, )
