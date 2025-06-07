import streamlit as st
import urllib.request
import os
import pytz
import pandas as pd
import pysaxon11.pysaxon11 as pysx
#from icecream import ic 
#from pysaxon11 import transform, file_path

from xml.dom import minidom
from lxml import etree
from datetime import date, datetime, time
from urllib.parse import urlparse
from pathlib import Path


# Procesar .mm hasta .py
# 20220809
#
DEBUG = st.toggle("**DEBUG**", value=False)
PY_PATH_IN = str(st.session_state['PY_PATH']) + '/'
#PY_PATH_IN = "../"
if DEBUG:
   st.write(PY_PATH_IN)

outdir     = "output/"  # INPUT
mm_in      = "OpenAIRE_ExplorePage.mm"
xsl_mm2doc = "XML/mm2doc.xsl"
out_doc    = "prueba_sax.xml"
#xsl_doc2py = "XML/mm_doc2oa_streamlit.xsl"
xsl_doc2py = "XML/mm_doc2_streamlit.xsl"
out_py     = "prueba_sax.py"


st.header("Genera Streamlit-Python desde MindMap")
DICT_MM_IN = {
            "COBOLpro® Concept": "mm/COBOLproConcept.mm",
            "COBOLpro® Base": "mm/COBOLpro_MVP.mm",
            "COBOLagency® Base": "mm/COBOLagencyConcept.mm",
            "COBOLagency® MVP": "mm/COBOLagency_MVP.mm",
            "OKRocket® Base": "mm/OKRocketConcept.mm",
            "REPOSITORIOS DE INVESTIGACIÓN": "mm/Base_Page.mm",
            "PRUEBA FORMULARIO COMPLEJO": "mm/OpenAIRE_ExplorePage.mm",
            "GOOGLE GEMINI PROJECT": "mm/GoogleGemini_Prompt.mm",
            "SISTEMA DE VIGILANCIA E INTELIGENCIA (MVP)": "mm/Vigilancia_Page.mm",
            "OPCIÓN SEMANTIC SCHOLAR": "mm/Base_Page.mm",
            "OPCIÓN CONSENSUS": "mm/Base_Page.mm",
            "OPEN KMAPS": "mm/Base_Page.mm",
            "OPCIÓN TIM": "mm/Base_Page.mm",
            "OPCIÓN GOOGLE": "mm/Base_Page.mm",
            "OPCIÓN WIKIPEDIA": "mm/Base_Page.mm",
}

ID_MAP = st.radio("", [
            "COBOLpro® Concept",
            "COBOLagency® MVP",
            "COBOLagency® Base",
            "OKRocket® Base",
            "REPOSITORIOS DE INVESTIGACIÓN",
            "PRUEBA FORMULARIO COMPLEJO",
            "GOOGLE GEMINI PROJECT",
            "SISTEMA DE VIGILANCIA E INTELIGENCIA (MVP)",
            #"OPCIÓN SEMANTIC SCHOLAR",
            #"OPCIÓN CONSENSUS",
            #"OPEN KMAPS",
            #"OPCIÓN TIM",
            #"OPCIÓN GOOGLE",
            #"OPCIÓN WIKIPEDIA", 
            ], key="ID_MAP")

new_mm = st.button("Generar Código")

mm_in = DICT_MM_IN[ID_MAP]

if DEBUG:
   st.write(DICT_MM_IN)
   st.write(ID_MAP + ": '" + mm_in + "'" + "' Selected")

if DEBUG:
   st.write(f"{os.getcwd()=}")
#st.stop()

if new_mm:
    with st.spinner(text="en proceso"):
        fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        if DEBUG:
            st.write(f"{mm_in=} {xsl_mm2doc=} {outdir=} {out_doc=}" )
        st.success("Start UPDATE: " + fnow)
#        exec("ic('Start UPTDATE: ' + fnow)")
        pysx.transform(mm_in, xsl_mm2doc, outdir + out_doc, str(PY_PATH_IN))
        fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        st.success("MM to DOC OK : " + fnow)
        if DEBUG:
            st.write(f"{outdir=} {out_doc=} {xsl_doc2py=} {out_py=} {out_doc=}" )
        pysx.transform(outdir + out_doc, xsl_doc2py, out_py, str(PY_PATH_IN))     
        fnow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        st.success("DOC to PY OK : " + fnow)
