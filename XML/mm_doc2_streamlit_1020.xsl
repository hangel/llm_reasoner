<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2009 (http://www.altova.com) by bv (bv) -->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<!--
PROCESA XML: 'OpenAIRE_ExplorePageDoc.xml' con XSL: 'mm_doc2oa_streamlit.xsl'
GENERA PYTHON: 000_pd_oa_nxobs.py
-->
	<!--
********
20240226
********
Revisión de Problema con Tabs

-->
	<!--
********
20221026
********
Se agrega SEM_SCHOL_LIMIT a sem_schol_search_fn()
TAREAS:
1. En oa_search_fn:
    Cambiara despliegue SuperModal por un despliegue nativo ST
    usando st.expander
2. Convertir 
* Ajustes para mejorar despliegue estable usando layout ipo "expander"
-->
	<!--
********
20221024
********
* Ajustes para mejorar despliegue estable usando layout ipo "expander"
-->
	<!--
********
20221018
********
* Alinear iframe de tabla responsive con submit de search
-->
	<!--
********
20221017
********
* agregar selector para `iframe`[OK]
-->
	<!--
********
20220926
********
- Ajustrar la estructura de FORM_RESULT así:
  $form_key_FORM_RESULT = {"form_key": $form_key}
  por cada elemento de form que se valla procesando, actualizar el diccionario FORM_RESULT
  si no existe 'key()' para @type
	crear una entrada en el diccionario para @type asi:
		FORM_RESULT.update({"input_text": [[str(1), "@TEXT", "VALORES ENTRADOS", str(1000)]]})
  si ya existe 'key()':
	append a la lista ya existente, con una lista para el nuevo input
        FORM_RESULT["input_text"].append([str(2), "@TEXT 2", "VALORES ENTRADOS 2", str(2000)])
- Incluir manejo de opciones para radio, checkbox, multiselect y semejantes usando
  diccionario/lista(?) que describa las opciones de opciones. Copiar de 
- Depurar despliegue de resultados de búsqueda 
- Se aplaza refactorizar mmdoc2oa_streamlit y librerías para oa_search, saxon, html
- PENDIENTES: 
  * Expolorar components
  * Verificar implmentación de faltantes del API
  * Versión horizontal usando columnas para opciones de radio y checkbox
  * Integración de Semantic Scholar
  * Integración de OKMaps
-->
	<!--
********
20220918
********
- Se agrega parámetro oa_search para controlar la ejecución de búsqueda real mientra se depura FORM_RESULT 
- Ajustrar la estructura de FORM_RESULT así:
  $form_key_FORM_RESULT = {"form_key": $form_key}
  por cada elemento de form que se valla procesando, actualizar el diccionario FORM_RESULT
  si no existe 'key()' para @type
	crear una entrada en el diccionario para @type asi:
		FORM_RESULT.update({"input_text": [[str(1), "@TEXT", "VALORES ENTRADOS", str(1000)]]})
  si ya existe 'key()':
	append a la lista ya existente, con una lista para el nuevo input
        FORM_RESULT["input_text"].append([str(2), "@TEXT 2", "VALORES ENTRADOS 2", str(2000)])
- Integrar oa_fix_read.py [OK]
- Leer Resultados del diccionario de la forma para obtener 'SEARCH_TERMS' usando:
  init_module = list(dashboards.keys())[0]
- Ampliar el concepto de submit usando  'SECCIÓN DE CONEXIÓN CON OA_SEARCH'
        if ID_1373687557_SUBMITTED:
            COLLECT_ANSWER=",".join(collect_answer)
            st.write(COLLECT_ANSWER)
            print(json.dumps(ID_1373687557_FORM_RESULT))
            # SECCIÓN DE CONEXIÓN CON OA_SEARCH
            #
            SEARCH_TERMS = ID_1373687557_3_TEXT_INPUT
            DEBUG_FLAG = False
            PD_DF = oa_search_fn(SEARCH_TERMS, DEBUG_FLAG)
            aggrid_controls(PD_DF) # LLAMADO AGGRID FIJO


  - Refactorizar XSL
  1- Crear un diccionario de parámetros de nodos del doc expresado a partir del MindMap
  2- Simplificar y unificar los siguientes componentes de la XSL: [PEND]
  * EN TEMPLATE: Un solo listado general de parámetros
  * EN LLAMADO A TEMPLATE: Garantizr la integridad del paso de parámetros
  * EN PROCESOS DE RECURSIÓN: Garantizar la integridad del flujo de parámetros
  * MINIMIZAR EL NÜMERO DE TEMPLATES (IDEAL Sólo UNO) dentro de él manejar los conceptos de:
    * Layout
    * Componente de Layout
    * Form
    * Form_part
    * Elemento lineal

- Generación de  captura de forma para cada input construyendo progresivamente el string del diccionario que será usado con exec()...
  con $form_result que será construido.progresivamente co los elementos de  las 'form' al ejecutar
  el submit correspondiente.
  ETAPAS Y ANTECEDENTES:
 ====================== 
  * el diccionario tenrá un identificador por cada tipo de form_input (ahí es donde se van a construir) con una estructura así:
    "type_ID": "objeto capturado"
  * Cada elemento de tipo 'input' en una 'form' generea una entrada específica en un string en forma de dictionary que será usado para update
    myDict.update({'five':'Olive', 'six':'Nivo', 'seven':'Xavier'});
- Generalización de tratamiento de layouts usando modeo de 'sidebar'
- Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping)
- [Include Session State API Callbacks] (https://docs.streamlit.io/library/advanced-features/session-state) para swer usado en:
  - Paginación
  - Personalización por sesión de usuario

- Configura el python de salida usando Tabs y formas anidadas en cada tab.
   - Enfocar todas las recursiones en "mk_node" 
     - Simplificar conservando TODOS los params
     - Depurar
	 - Discriminar el tipo de recursión para los objetos tipo "layout" incluyendo un parámetro extra para agregar "$pad" a todos los nodos hijos
-->
	<!--
********
20220916
********
- URGENTE: Integrar oa_fix_read.py
  - Refactorizar XSL
  1- Crear un diccionario de parámetros de nodos del doc expresado a partir del MindMap
  2- Simplificar y unificar los siguientes componentes de la XSL: [PEND]
  * EN TEMPLATE: Un solo listado general de parámetros
  * EN LLAMADO A TEMPLATE: Garantizr la integridad del paso de parámetros
  * EN PROCESOS DE RECURSIÓN: Garantizar la integridad del flujo de parámetros
  * MINIMIZAR EL NÜMERO DE TEMPLATES (IDEAL Sólo UNO) dentro de él manejar los conceptos de:
    * Layout
    * Componente de Layout
    * Form
    * Form_part
    * Elemento lineal

- Generación de  captura de forma para cada input construyendo progresivamente el string del diccionario que será usado con exec()...
  con $form_result que será construido.progresivamente co los elementos de  las 'form' al ejecutar
  el submit correspondiente.
  ETAPAS Y ANTECEDENTES:
 ====================== 
  * el diccionario tenrá un identificador por cada tipo de form_input (ahí es donde se van a construir) con una estructura así:
    "type_ID": "objeto capturado"
  * Cada elemento de tipo 'input' en una 'form' generea una entrada específica en un string en forma de dictionary que será usado para update
    myDict.update({'five':'Olive', 'six':'Nivo', 'seven':'Xavier'});
- Generalización de tratamiento de layouts usando modeo de 'sidebar'
- Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping)
- [Include Session State API Callbacks] (https://docs.streamlit.io/library/advanced-features/session-state) para swer usado en:
  - Paginación
  - Personalización por sesión de usuario

- Configura el python de salida usando Tabs y formas anidadas en cada tab.
   - Enfocar todas las recursiones en "mk_node" 
     - Simplificar conservando TODOS los params
     - Depurar
	 - Discriminar el tipo de recursión para los objetos tipo "layout" incluyendo un parámetro extra para agregar "$pad" a todos los nodos hijos
-->
	<!--
********
20220915
********
- URGENTE: Refactorizar XSL
  1- Crear un diccionario de parámetros de nodos del doc expresado a partir del MindMap
  2- Simplificar y unificar los siguientes componentes de la XSL: [PEND]
  * EN TEMPLATE: Un solo listado general de parámetros
  * EN LLAMADO A TEMPLATE: Garantizr la integridad del paso de parámetros
  * EN PROCESOS DE RECURSIÓN: Garantizar la integridad del flujo de parámetros
  * MINIMIZAR EL NÜMERO DE TEMPLATES (IDEAL Sólo UNO) dentro de él manejar los conceptos de:
    * Layout
    * Componente de Layout
    * Form
    * Form_part
    * Elemento lineal

- Generación de  captura de forma para cada input construyendo progresivamente el string del diccionario que será usado con exec()...
  con $form_result que será construido.progresivamente co los elementos de  las 'form' al ejecutar
  el submit correspondiente.
  ETAPAS Y ANTECEDENTES:
 ====================== 
  * el diccionario tenrá un identificador por cada tipo de form_input (ahí es donde se van a construir) con una estructura así:
    "type_ID": "objeto capturado"
  * Cada elemento de tipo 'input' en una 'form' generea una entrada específica en un string en forma de dictionary que será usado para update
    myDict.update({'five':'Olive', 'six':'Nivo', 'seven':'Xavier'});
- Generalización de tratamiento de layouts usando modeo de 'sidebar'
- Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping)
- [Include Session State API Callbacks] (https://docs.streamlit.io/library/advanced-features/session-state) para swer usado en:
  - Paginación
  - Personalización por sesión de usuario
  -

- Configura el python de salida usando Tabs y formas anidadas en cada tab.
   - Enfocar todas las recursiones en "mk_node" 
     - Simplificar conservando TODOS los params
     - Depurar
	 - Discriminar el tipo de recursión para los objetos tipo "layout" incluyendo un parámetro extra para agregar "$pad" a todos los nodos hijos
-->
	<!--
********
20220913
********
- Generación de  captura de forma para cada input construyendo progresivamente el string del diccionario que será usado con exec()...
  con $form_result que será construido.progresivamente co los elementos de  las 'form' al ejecutar
  el submit correspondiente.
  ETAPAS Y ANTECEDENTES:
 ====================== 
  * el diccionario tenrá un identificador por cada tipo de form_input (ahí es donde se van a construir) con una estructura así:
    "type_ID": "objeto capturado"
  * Cada elemento de tipo 'input' en una 'form' generea una entrada específica en un string en forma de dictionary que será usado para update
    myDict.update({'five':'Olive', 'six':'Nivo', 'seven':'Xavier'});
- Generalización de tratamiento de layouts usando modeo de 'sidebar'
- Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping)
- [Include Session State API Callbacks] (https://docs.streamlit.io/library/advanced-features/session-state) para swer usado en:
  - Paginación
  - Personalización por sesión de usuario
  -

- Configura el python de salida usando Tabs y formas anidadas en cada tab.
   - Enfocar todas las recursiones en "mk_node" 
     - Simplificar conservando TODOS los params
     - Depurar
	 - Discriminar el tipo de recursión para los objetos tipo "layout" incluyendo un parámetro extra para agregar "$pad" a todos los nodos hijos
-->
	<!--
********
20220912
********
- Generación de  captura de forma para cada input construyendo progresivamente el string del diccionario que será usado con exec().
  el diccionario tenrá un identificador por cada tipo de form_input (ahí es donde se van a construir) con una estructura así:
  type_ID: objeto capturado
- Generalización de tratamiento de layouts usando modeo de 'sidebar'
- Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping)
- [Include Session State API Callbacks] (https://docs.streamlit.io/library/advanced-features/session-state) para swer usado en:
  - Paginación
  - Personalización por sesión de usuario
  -

- Configura el python de salida usando Tabs y formas anidadas en cada tab.[OK]
   - Enfocar todas las recursiones en "mk_node" 
     - Simplificar conservando TODOS los params
     - Depurar
	 - Discriminar el tipo de recursión para los objetos tipo "layout" incluyendo un parámetro extra para agregar "$pad" a todos los nodos hijos
-->
	<!--
********
20220909
********
- Generación de  captura de form para cada input construyendo progresivamente el string del diccionario que será usado con exec().
  el diccionario tenrá un identificador por cada tipo de form_input (ahí es donde se van a construir) con una estructura así:
  type_ID: objeto capturado
- Generalización de tratamiento de layouts usando modeo de 'sidebar'
- Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping)
- [Include Session State API Callbacks] (https://docs.streamlit.io/library/advanced-features/session-state) para swer usado en:
  - Paginación
  - Personalización por sesión de usuario
  -

- Configura el python de salida usando Tabs y formas anidadas en cada tab.
   - Enfocar todas las recursiones en "mk_node" 
     - Simplificar conservando TODOS los params
     - Depurar
	 - Discriminar el tipo de recursión para los objetos tipo "layout" incluyendo un parámetro extra para agregar "$pad" a todos los nodos hijos
-->
	<!--
********
20220907
********
- Generación de  captura de form para cada input construyendo progresivamente el string del diccionario que será usado con exec()
- Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping)
- [Include Session State API Callbacks] (https://docs.streamlit.io/library/advanced-features/session-state)
- Procesamiento de st.sidebar [OK]

- Configura el python de salida usando Tabs y formas anidadas en cada tab.
   - Enfocar todas las recursiones en "mk_node"
     - Simplificar conservando TODOS los params
     - Depurar
	 - Discriminar el tipo de recursión para los objetos tipo "layout" incluyendo un parámetro extra para agregar "$pad" a todos los nodos hijos
-->
	<!--
********
20220908
********
 - flexibilización de md_markdown
-->
	<!--
********
20220906
********
- Generación de  captura de form para cada input construyendo progresivamente el string del diccionario que será usado con exec()
- Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping)
- [Include Session State API Callbacks] (https://docs.streamlit.io/library/advanced-features/session-state)
- 

- Configura el python de salida usando Tabs y formas anidadas en cada tab.
   - Enfocar todas las recursiones en "mk_node"
     - Simplificar conservando TODOS los params
     - Depurar
	 - Discriminar el tipo de recursión para los objetos tipo "layout" incluyendo un parámetro extra para agregar "$pad" a todos los nodos hijos
   - Generación de columns con contenido anidado [OK]
   - Prueba de layouts anidados entre columnss / tabs usando cuidadosamente with col_nn/tab_nn :... [OK]
   - Add tooltip a submit para ver el nombre de la forma (¿y del botón?) [OK]
   - Generación de índice posicional de nodo según jerarquía estructural [OK]
-->
	<!--
********
20220829
********
- Configura el python de salida usando Tabs y formas anidadas en cada tab. [OK]
   - Enfocar todas las recursiones en "mk_node"
     - Simplificar conservando TODOS los params
     - Depurar
	 - Discriminar el tipo de recursión para los objetos tipo "layout" incluyendo un parámetro extra para agregar "$pad" a todos los nodos hijos [OK]
   - Generación de columns con contenido anidado [OK]
   - Prueba de layouts anidados entre columnss / tabs usando cuidadosamente with col_nn/tab_nn :... [OK]
   - Add tooltip a submit para ver el nombre de la forma (¿y del botón?) [OK]
   - Generación de  captura de form para cada input construyendo progresivamente el strin del diccionario que será usado con exec()
   - Geración de índice posicional de nodo según jerarquía estructural
   - Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping)
   - [Include Session State API Callbacks] (https://docs.streamlit.io/library/advanced-features/session-state)
-->
	<!--
********
20220824
********
- Configura el python de salida usando Tabs y formas anidadas en cada tab
   1 - Para el procesamiento de tabs usar el control de layout con " with tabn:" y aumentando $indent con $pad para los nodos contenidos
 - Crear la orientación horizontal para checkboxes (se incluirá lógica de wraping) [OK]
-->
	<!--
********
20220809
********
- Desligar el contenido de los tabs de los tabs. En el estado actual no se permite anidamiento de Columnas bajo tabs.
	 Probablemente cada tab deberá ser procesado como una página independiente[OK]
-->
	<!--
********
20220731
********
- Implemementar 'columns' y 'col' con un patrón semejante a 'tabs' y 'tab' [OK]
-->
	<!--
********
20220727
********
******************************************************************************
*        PROPÓSITO:                                                          *  
*        FORMULARIO Y RESULTADOS: COMPLETO, Y PÚBLICADO EN WEB PARA NETUX    *
******************************************************************************
=========== 
¿QuÉ SIGUE?
=========== 
- Integrar conversión de Datos recibidos a función que implementa API
- Convertir código probado en Jupyter-lab a módulo python Streamlit para uso genérico
- Generar arreglo de returno de valores de submit
- Mejorar procesamiento de nodos de tipo 'md_head', para ser flexibles según valor de @default (n'#')	

================ 
METAS INMEDIATAS
================ 
1- Formulario Emulado Completo desplegado en columna lateral izquierda
2- Convertir la búsqueda Python (Textual) en función/librería Streamlit
3- Buscar en OpenAIRE desde formulario con Libreria OpenAIRE (2)

==================== 
DETALLES PENDIENTES:
==================== 
- Integrar conversión de Datos recibidos a función que implementa API
- Convertir código probado en Jupyter-lab a módulo Streamlit para uso genérico
- Generar arreglo de returno de valores de submit
- Mejorar procesamiento de nodos de tipo 'md_head', para ser flexibles según valor de @default (n'#')	
-->
	<!--
********
20220725
********
PEND:
- Integrar conversión de Datos recibidos a función que implementa API
- Convertir código probado en Jupyter-lab a módulo Streamlit para uso genérico
- Generar arreglo de returno de valores de submit
- Mejorar procesamiento de nodos de tipo 'md_head', para ser flexibles según valor de @default (n'#')	
-->
	<!--
********
20220724
********
PEND:
- Generar arreglo de returno de valores de submit
- Hacer md_head flexible con @default x '#'
LISTO:
- Carga externa de datos [OK]
- Descarga de Tabla resultado [OK]
- Prueba integración de components HTML [OK]
- Conversión de datos recibidos de OpenAIRE a formato para importar a Pandas [OK]
- Problema en generación de contenido de tabs con "groupbox" [OK] -resuelto en la generación de cada 'tab'[OK]
	El indice posicional de "tab" debe fluir inmutablemente por cada nodo contenido en él para garantizar el despliegue agrupado. [OK]
    Debe dejarse esta tarea a la recursividad, garantizando que en 'nodo' y cada uno de sus @types se preserve al llamar las templates específicas  [OK]
- Se cambió el pipeline de desarrollo así: [OK]
	- transformar "mm" file en "OpenAIRE_ExplorePageDoc.xml" versión compacta [OK]
    - migración a nuevo XSL 'mmdoc2oa_streamlit' para la generación de  streamlit python [OK] (Proceso continuo)
********
CHECKBOX? [OK]
********
- Implementación de soporte a st.html [OK]
- Generación global de streamlit considerando  [OK]
	- forms (recursive through form_parts)
    - generic
		- layout
		- objects (text, button)
-->
	<!--
********
20220723
********
- Implementación de soporte a st.html
- Generación global de streamlit considerando
	- forms (recursive through form_parts)
    - generic
		- layout
		- objects (text, button)
- Generar arreglo de returno de valores de submit
- Hacer md_head flexible con @default
-->
	<!--
********
20220721
********
* Generar código Python Streamlit para NxOBS a partir de mm descriptor de proyecto [OK] (Proceso continuo)
- Agregar Hora según : https://www.oreilly.com/library/view/xslt-2nd-edition/9780596527211/ch04s05.html [OK]
- Generar arreglo de valores para options [OK]
.............................................................................................................
-->
	<xsl:output method="text" encoding="utf-8" omit-xml-declaration="yes" indent="yes"/>
	<xsl:param name="url_base">
		<xsl:value-of select="/map/@href"/>
	</xsl:param>
	<xsl:param name="creation_date">
		<xsl:value-of select="format-dateTime(current-dateTime(), 
                          '[Y0001]/[M01]/[D01] [h01]:[m01]:[s01] [P] [z] ')"/>
	</xsl:param>
	<xsl:param name="pad">
		<xsl:text>    </xsl:text>
	</xsl:param>
	<xsl:param name="ret">
		<xsl:text>&#010;</xsl:text>
	</xsl:param>
	<xsl:param name="code_tracker">0</xsl:param>
	<xsl:param name="st_layout"/>
	<xsl:param name="indent"/>
	<xsl:param name="st_prefix_base">st</xsl:param>
	<xsl:param name="type"/>
	<xsl:param name="pos"/>
	<xsl:param name="group_pos"/>
	<xsl:param name="name"/>
	<xsl:param name="variable_name"/>
	<xsl:param name="st_prefix"/>
	<xsl:param name="n_tabs"/>
	<xsl:param name="n_cols"/>
	<xsl:param name="form_key">
		<xsl:value-of select="/doc/@ID"/>
	</xsl:param>
	<xsl:param name="node_key"/>
	<xsl:param name="oa_search"/>
	<xsl:param name="submit_return">
		<xsl:text/>
	</xsl:param>
	<xsl:param name="collect_answer">
		<xsl:text/>
	</xsl:param>
	<xsl:param name="form_return"/>
	<!-- STREAMLIT CODE -->
	<!--
===================================================== 
           TEMPLATES ESPECÍFICOS SIMPLES 
===================================================== 
-->
	<xsl:template match="/">
		<xsl:value-of select="concat('# ', 'FECHA: ', $creation_date, ' | url_base:', $url_base, ' | st_prefix_base: ', $st_prefix_base,' |')"/><![CDATA[
# Codigo Streamlit para busqueda y despliegue de resultados en OpenAIRE para NxOBS. Usa Pandas
#
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


ROOT = os.path.join(os.path.dirname(__file__))

np.random.seed(42)
]]>
st.markdown("## <xsl:value-of select="/doc/@name"/>")
st.markdown("###### FREEMIND TO STREAMLIT v0.0")
st.markdown("###### <xsl:value-of select="$creation_date"/>")
<xsl:for-each select="doc/node[@type != 'no']">
			<xsl:call-template name="mk_node_tree">
				<xsl:with-param name="pos">
					<xsl:value-of select="position()"/>
				</xsl:with-param>
				<xsl:with-param name="indent">
					<xsl:value-of select="$indent"/>
				</xsl:with-param>
				<xsl:with-param name="node_level">
					<xsl:value-of select="number(0)"/>
				</xsl:with-param>
				<xsl:with-param name="name">
					<xsl:value-of select="upper-case(@TEXT)"/>
				</xsl:with-param>
				<xsl:with-param name="type">
					<xsl:value-of select="@type"/>
				</xsl:with-param>
				<xsl:with-param name="st_prefix">
					<xsl:value-of select="$st_prefix_base"/>
				</xsl:with-param>
				<xsl:with-param name="node_key">
					<xsl:value-of select="concat(generate-id(), '_', @ID)"/>
				</xsl:with-param>
				<xsl:with-param name="form_key">
					<xsl:choose>
						<xsl:when test="@type= 'form'">@ID</xsl:when>
						<xsl:otherwise/>
					</xsl:choose>
				</xsl:with-param>
				<xsl:with-param name="collect_answer">
					<xsl:value-of select="$collect_answer"/>
				</xsl:with-param>
			</xsl:call-template>
		</xsl:for-each>
		<xsl:value-of select="$ret"/>
	</xsl:template>
	<!-- MK_NODE_TREE -->
	<xsl:template name="mk_node_tree">
		<xsl:param name="type"/>
		<xsl:param name="node_level"/>
		<xsl:param name="pos"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="st_prefix"/>
		<xsl:param name="n_tabs"/>
		<xsl:param name="n_cols"/>
		<xsl:param name="node_key"/>
		<xsl:param name="st_layout"/>
		<xsl:param name="submit_return"/>
		<xsl:param name="form_return"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:variable name="node_level-iter">
			<xsl:value-of select="$node_level"/>
		</xsl:variable>
		<xsl:if test="$code_tracker= 1">
			<xsl:value-of select="concat('&#010;', $indent, '# form_key: ', $form_key, ' | node_level: ', $node_level, ' | pos: ', $pos, ' | - ', @type, ': ', upper-case(@TEXT))"/>
		</xsl:if>
		<xsl:choose>
			<xsl:when test="$type= 'form'">
				<xsl:call-template name="mk_st_form">
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="form_return">
						<xsl:text>"{}"</xsl:text>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="concat($pos, '.', position())"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="$node_level"/>
					</xsl:with-param>
					<xsl:with-param name="node_key">
						<xsl:value-of select="concat(generate-id(), '_', @ID)"/>
					</xsl:with-param>
					<xsl:with-param name="st_layout">
						<xsl:value-of select="$st_layout"/>
					</xsl:with-param>
					<xsl:with-param name="submit_return">
						<xsl:value-of select="$submit_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="@ID"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
				<xsl:call-template name="mk_st_submit">
					<xsl:with-param name="submit_text">Submit_<xsl:value-of select="@ID"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="concat($indent, $pad)"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="@ID"/>
					</xsl:with-param>
					<xsl:with-param name="form_return">
						<xsl:text>"{}"</xsl:text>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="node[@type='submit']/@TEXT"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'iframe'">
				<xsl:call-template name="mk_st_iframe">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'checkgroup'">
				<xsl:if test="count(node[@type= 'checkbox']) > 0">
					<xsl:for-each select="node">
						<xsl:call-template name="mk_node_tree">
							<xsl:with-param name="name">
								<xsl:value-of select="upper-case(@TEXT)"/>
							</xsl:with-param>
							<xsl:with-param name="pos">
								<xsl:value-of select="$pos"/>
							</xsl:with-param>
							<xsl:with-param name="indent">
								<xsl:value-of select="$indent"/>
							</xsl:with-param>
							<xsl:with-param name="group_pos">
								<xsl:value-of select="$pos"/>
							</xsl:with-param>
							<xsl:with-param name="type">
								<xsl:value-of select="@type"/>
							</xsl:with-param>
							<xsl:with-param name="node_level">
								<xsl:value-of select="number($node_level) + 1"/>
							</xsl:with-param>
							<xsl:with-param name="form_key">
								<xsl:value-of select="$form_key"/>
							</xsl:with-param>
							<xsl:with-param name="collect_answer">
								<xsl:value-of select="$collect_answer"/>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:for-each>
				</xsl:if>
			</xsl:when>
			<xsl:when test="$type= 'checkbox'">
				<xsl:call-template name="mk_checkbox">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'selectbox'">
				<xsl:call-template name="mk_selectbox">
					<xsl:with-param name="pos">
						<xsl:value-of select="concat($pos, '.', position())"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="node_key">
						<xsl:value-of select="@ID"/>
					</xsl:with-param>
					<xsl:with-param name="submit_return">
						<xsl:value-of select="$submit_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_return">
						<xsl:value-of select="$form_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'submit'"/>
			<xsl:when test="$type= 'html'">
				<xsl:call-template name="mk_html">
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'button'">
				<xsl:value-of select="concat('&#010;', $indent, 'st.button(&quot;', normalize-space(@TEXT), '&quot;, key=&quot;', @ID, '&quot;)')"/>
			</xsl:when>
			<xsl:when test="$type= 'md_markdown'">
				<xsl:variable name="md_level">
					<xsl:value-of select="concat('MD_LEVEL_PY = &quot;&quot;.join(', @params, '*&quot;#&quot;)')"/>
				</xsl:variable>
				<xsl:value-of select="concat('&#010;', $indent, $md_level)"/>
				<xsl:value-of select="concat('&#010;', $indent, 'st.markdown(MD_LEVEL_PY + &quot; ', upper-case(@TEXT), '&quot;)')"/>
				<xsl:if test="@TEXT= 'expand: View all&gt;'">
					<xsl:value-of select="concat('&#010;', $indent, 'st.markdown(&quot;---&quot;)')"/>
				</xsl:if>
				<xsl:if test="count(node[@type != 'no']) > 0">
					<xsl:for-each select="node[@type != 'no']">
						<xsl:call-template name="mk_node_tree">
							<xsl:with-param name="pos">
								<xsl:value-of select="concat($pos, '.', position())"/>
							</xsl:with-param>
							<xsl:with-param name="indent">
								<xsl:value-of select="$indent"/>
							</xsl:with-param>
							<xsl:with-param name="node_level">
								<xsl:value-of select="$node_level"/>
							</xsl:with-param>
							<xsl:with-param name="group_pos">
								<xsl:value-of select="position()"/>
							</xsl:with-param>
							<xsl:with-param name="name">
								<xsl:value-of select="upper-case(@TEXT)"/>
							</xsl:with-param>
							<xsl:with-param name="type">
								<xsl:value-of select="@type"/>
							</xsl:with-param>
							<xsl:with-param name="st_prefix">
								<xsl:value-of select="$st_prefix"/>
							</xsl:with-param>
							<xsl:with-param name="n_tabs">
								<xsl:value-of select="$n_tabs"/>
							</xsl:with-param>
							<xsl:with-param name="n_cols">
								<xsl:value-of select="$n_cols"/>
							</xsl:with-param>
							<xsl:with-param name="node_key">
								<xsl:value-of select="concat(generate-id(), '_', @ID)"/>
							</xsl:with-param>
							<xsl:with-param name="st_layout">
								<xsl:value-of select="$st_layout"/>
							</xsl:with-param>
							<xsl:with-param name="submit_return"/>
							<xsl:with-param name="form_return"/>
							<xsl:with-param name="form_key">
								<xsl:value-of select="$form_key"/>
							</xsl:with-param>
							<xsl:with-param name="collect_answer">
								<xsl:value-of select="$collect_answer"/>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:for-each>
				</xsl:if>
			</xsl:when>
			<xsl:when test="$type= 'md_head'">
				<xsl:value-of select="concat('&#010;', $indent, 'st.markdown(&quot;## ', upper-case(@TEXT), '&quot;')"/>
			</xsl:when>
			<xsl:when test="$type= 'text'">
				<xsl:value-of select="concat('&#010;', $indent, 'st.write(&quot;', upper-case(@TEXT), '&quot;)')"/>
			</xsl:when>
			<xsl:when test="$type= 'expander'">
				<xsl:call-template name="mk_expander">
					<xsl:with-param name="n_tabs">
						<xsl:value-of select="$n_tabs"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="position()"/>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<!--
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< LAYOUTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-->
			<xsl:when test="@type= 'tabs'">
				<xsl:variable name="n_tabs">
					<xsl:value-of select="count(node[@type= 'tab'])"/>
				</xsl:variable>
				<xsl:if test="$n_tabs > 0">
					<xsl:call-template name="mk_tabs">
						<xsl:with-param name="n_tabs">
							<xsl:value-of select="$n_tabs"/>
						</xsl:with-param>
						<xsl:with-param name="group_pos">
							<xsl:value-of select="position()"/>
						</xsl:with-param>
						<xsl:with-param name="name">
							<xsl:value-of select="upper-case(@TEXT)"/>
						</xsl:with-param>
						<xsl:with-param name="indent">
							<xsl:value-of select="$indent"/>
						</xsl:with-param>
						<xsl:with-param name="node_level">
							<xsl:value-of select="number($node_level) + 1"/>
						</xsl:with-param>
						<xsl:with-param name="form_key">
							<xsl:value-of select="$form_key"/>
						</xsl:with-param>
						<xsl:with-param name="collect_answer">
							<xsl:value-of select="$collect_answer"/>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:if>
			</xsl:when>
			<xsl:when test="$type= 'columns'">
				<xsl:variable name="n_cols">
					<xsl:value-of select="count(node[@type= 'col'])"/>
				</xsl:variable>
				<xsl:if test="$n_cols > 0">
					<xsl:call-template name="mk_cols">
						<xsl:with-param name="n_cols">
							<xsl:value-of select="$n_cols"/>
						</xsl:with-param>
						<xsl:with-param name="group_pos">
							<xsl:value-of select="position()"/>
						</xsl:with-param>
						<xsl:with-param name="name">
							<xsl:value-of select="upper-case(@TEXT)"/>
						</xsl:with-param>
						<xsl:with-param name="indent">
							<xsl:value-of select="$indent"/>
						</xsl:with-param>
						<xsl:with-param name="node_level">
							<xsl:value-of select="number($node_level) + 1"/>
						</xsl:with-param>
						<xsl:with-param name="form_key">
							<xsl:value-of select="$form_key"/>
						</xsl:with-param>
						<xsl:with-param name="collect_answer">
							<xsl:value-of select="$collect_answer"/>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:if>
			</xsl:when>
			<xsl:when test="$type= 'sidebar'">
				<xsl:variable name="n_cols">
					<xsl:value-of select="count(node[@type= 'col'])"/>
				</xsl:variable>
				<xsl:call-template name="mk_sidebar">
					<xsl:with-param name="n_cols">
						<xsl:value-of select="$n_cols"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="position()"/>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'download_button'">
				<xsl:value-of select="concat('&#010;', $indent, 'st.download_button(&quot;Download file&quot;, file', '&quot;, key=&quot;', @ID, '&quot;)')"/>
			</xsl:when>
			<!--
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FORM COMPONENTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-->
			<xsl:when test="$type= 'text_input'">
				<xsl:call-template name="mk_text_input">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'radio'">
				<xsl:call-template name="mk_radio">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'multiselect'">
				<xsl:call-template name="mk_multiselect">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'slider'">
				<xsl:call-template name="mk_slider">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'select_slider'">
				<xsl:call-template name="mk_selectslider">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'number_input'">
				<xsl:value-of select="concat('&#010;', $indent, 'choice = ', 'st.number_input(&quot;Pick a number&quot;, 0, 10', ', key=&quot;', @ID, '&quot;)', ', key=&quot;', @ID, '&quot;)')"/>
			</xsl:when>
			<xsl:when test="$type= 'text_area'">
				<xsl:call-template name="mk_text_area">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'time_input'">
				<xsl:call-template name="mk_time_input">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'date_input'">
				<xsl:call-template name="mk_date_input">
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'file_uploader'">
				<xsl:call-template name="mk_file_uploader">
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="$name"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="$type"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$group_pos"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="$node_level"/>
					</xsl:with-param>
					<xsl:with-param name="submit_return">
						<xsl:value-of select="$submit_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_return">
						<xsl:value-of select="$form_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'camera_input'">
				<xsl:call-template name="mk_camera_input">
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="$name"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="$type"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$group_pos"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="$node_level"/>
					</xsl:with-param>
					<xsl:with-param name="submit_return">
						<xsl:value-of select="$submit_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_return">
						<xsl:value-of select="$form_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$type= 'color_picker'">
				<xsl:call-template name="mk_color_picker">
					<xsl:with-param name="pos">
						<xsl:value-of select="$pos"/>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="$name"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="$indent"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="$type"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$group_pos"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="$node_level"/>
					</xsl:with-param>
					<xsl:with-param name="submit_return">
						<xsl:value-of select="$submit_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_return">
						<xsl:value-of select="$form_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise/>
		</xsl:choose>
		<!--
<<<<<<<<< RECURSIÓN GENERAL >>>>>>>>>
-->
		<xsl:if test="count(node[@type != 'no']) > 0">
			<xsl:for-each select="node">
				<xsl:call-template name="mk_node_tree">
					<xsl:with-param name="pos">
						<xsl:value-of select="concat($pos, '.', position())"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="concat($indent, $pad)"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="node_key">
						<xsl:value-of select="@ID"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="submit_return">
						<xsl:value-of select="$submit_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_return">
						<xsl:value-of select="$form_return"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>
	<!--
===================================================== 
           TEMPLATES ESPECÍFICOS SIMPLES 
===================================================== 
-->
	<!-- MK_TABS -->
	<xsl:template name="mk_tabs">
		<xsl:param name="indent"/>
		<xsl:param name="n_tabs"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<!-- PREÁMBULO -->
		<xsl:variable name="tabs_creator">
			<xsl:for-each select="node[@type= 'tab']">TAB<xsl:value-of select="position()"/>
				<xsl:if test="position() != last()">, </xsl:if>
			</xsl:for-each>
		</xsl:variable>
		<xsl:variable name="tabs_definition">
			<xsl:for-each select="node[@type= 'tab']">"<xsl:value-of select="upper-case(@TEXT)"/>"<xsl:if test="position() != last()">, </xsl:if>
			</xsl:for-each>
		</xsl:variable>
		<xsl:value-of select="concat('&#010;', $indent, $tabs_creator, ' = st.tabs([', $tabs_definition, '])')"/>
		<xsl:for-each select="node[@type= 'tab']">
			<xsl:call-template name="mk_tab">
				<xsl:with-param name="pos">
					<xsl:value-of select="concat($pos, '.', position())"/>
				</xsl:with-param>
				<xsl:with-param name="indent">
					<xsl:value-of select="$indent"/>
				</xsl:with-param>
				<xsl:with-param name="name">
					<xsl:value-of select="upper-case(@TEXT)"/>
				</xsl:with-param>
				<xsl:with-param name="type">
					<xsl:value-of select="@type"/>
				</xsl:with-param>
				<xsl:with-param name="group_pos">
					<xsl:value-of select="position()"/>
				</xsl:with-param>
				<xsl:with-param name="node_level">
					<xsl:value-of select="number($node_level) + 1"/>
				</xsl:with-param>
				<xsl:with-param name="form_key">
					<xsl:value-of select="$form_key"/>
				</xsl:with-param>
				<xsl:with-param name="collect_answer">
					<xsl:value-of select="$collect_answer"/>
				</xsl:with-param>
			</xsl:call-template>
		</xsl:for-each>
	</xsl:template>
	<!-- MK_TAB -->
	<xsl:template name="mk_tab">
		<xsl:param name="n_tabs"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="n_cols"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:if test="count(node) > 0">
			<xsl:value-of select="concat('&#010;', $indent, 'with TAB', $group_pos, ':')"/>
			<xsl:for-each select="node">
				<xsl:call-template name="mk_node_tree">
					<xsl:with-param name="pos">
						<xsl:value-of select="concat($pos, '.', position())"/>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="concat($indent, $pad)"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$group_pos"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>
	<!-- MK_COLS -->
	<xsl:template name="mk_cols">
		<xsl:param name="indent"/>
		<xsl:param name="n_cols"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<!-- PREÁMBULO -->
		<!--		<xsl:value-of select= "concat('&#010;st.subheader(&quot;COLUMNAS&quot;)', ' # ENTRADA')"/> -->
		<xsl:variable name="cols_creator">
			<xsl:for-each select="node[@type= 'col']">COL<xsl:value-of select="position()"/>
				<xsl:if test="position() != last()">, </xsl:if>
			</xsl:for-each>
		</xsl:variable>
		<xsl:variable name="cols_definition">
			<xsl:for-each select="node[@type= 'col']">
				<xsl:value-of select="@params"/>
				<xsl:if test="position() != last()">, </xsl:if>
			</xsl:for-each>
		</xsl:variable>
		<xsl:value-of select="concat('&#010;', $indent, $cols_creator, ' = st.columns([', $cols_definition, '])')"/>
		<!-- ENCABEZADO DE CADA COL -->
		<xsl:for-each select="node[@type= 'col']">
			<xsl:call-template name="mk_col">
				<xsl:with-param name="pos">
					<xsl:value-of select="concat($pos, '.', position())"/>
				</xsl:with-param>
				<xsl:with-param name="name">
					<xsl:value-of select="upper-case(@TEXT)"/>
				</xsl:with-param>
				<xsl:with-param name="indent">
					<xsl:value-of select="$indent"/>
				</xsl:with-param>
				<xsl:with-param name="type">
					<xsl:value-of select="@type"/>
				</xsl:with-param>
				<xsl:with-param name="group_pos">
					<xsl:value-of select="position()"/>
				</xsl:with-param>
				<xsl:with-param name="node_level">
					<xsl:value-of select="number($node_level) + 1"/>
				</xsl:with-param>
				<xsl:with-param name="form_key">
					<xsl:value-of select="$form_key"/>
				</xsl:with-param>
				<xsl:with-param name="collect_answer">
					<xsl:value-of select="$collect_answer"/>
				</xsl:with-param>
			</xsl:call-template>
		</xsl:for-each>
	</xsl:template>
	<!-- MK_COL -->
	<xsl:template name="mk_col">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:if test="count(node) > 0">
			<xsl:value-of select="concat('&#010;', $indent, 'with COL', $group_pos, ':')"/>
			<xsl:for-each select="node">
				<xsl:call-template name="mk_node_tree">
					<xsl:with-param name="pos">
						<xsl:value-of select="concat($pos, '.', position())"/>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="concat($indent, $pad)"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$group_pos"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>
	<!-- MK_SIDEBAR -->
	<xsl:template name="mk_sidebar">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:if test="count(node) > 0">
			<xsl:value-of select="concat('&#010;', $indent, 'with st.sidebar', ':')"/>
			<xsl:for-each select="node">
				<xsl:call-template name="mk_node_tree">
					<xsl:with-param name="pos">
						<xsl:value-of select="concat($pos, '.', position())"/>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="concat($indent, $pad)"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="$group_pos"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>
	<!--
===================================================== 
           TEMPLATES FORMS / INPUT WIDGETS 
===================================================== 
-->
	<!-- MK_ST_FORM -->
	<xsl:template name="mk_st_form">
		<xsl:param name="indent"/>
		<xsl:param name="node_key"/>
		<xsl:param name="submit_return"/>
		<xsl:param name="form_return"/>
		<xsl:param name="node_level"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="st_layout"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, 'with st.form(key=&quot;', @ID, '&quot;, clear_on_submit=False):')"/>
		<xsl:value-of select="concat('&#010;', $indent,$pad,'COLLECT_ANSWER = []')"/>
		<xsl:variable name="FORM_WIDGETS_SEED">
			<xsl:for-each select="node">
				<xsl:value-of select="concat(',&#010;',$indent,$pad,$pad,'&quot;',@type,'&quot;: []')"/>
			</xsl:for-each>
		</xsl:variable>
		<xsl:value-of select="concat('&#010;', $indent, $pad, @ID, '_FORM_RESULT', ' = {&#010;',$indent,$pad,$pad,'&quot;form_key&quot;: ','&quot;', @ID, '&quot;',$FORM_WIDGETS_SEED,'}')"/>
		<xsl:if test="count(node[@type != 'no']) > 0">
			<xsl:for-each select="node">
				<xsl:call-template name="mk_node_tree">
					<xsl:with-param name="pos">
						<xsl:value-of select="concat($pos, '.', position())"/>
					</xsl:with-param>
					<xsl:with-param name="indent">
						<xsl:value-of select="concat($indent, $pad)"/>
					</xsl:with-param>
					<xsl:with-param name="type">
						<xsl:value-of select="@type"/>
					</xsl:with-param>
					<xsl:with-param name="node_level">
						<xsl:value-of select="number($node_level) + 1"/>
					</xsl:with-param>
					<xsl:with-param name="group_pos">
						<xsl:value-of select="position()"/>
					</xsl:with-param>
					<xsl:with-param name="name">
						<xsl:value-of select="upper-case(@TEXT)"/>
					</xsl:with-param>
					<xsl:with-param name="st_prefix">
						<xsl:value-of select="$st_prefix"/>
					</xsl:with-param>
					<xsl:with-param name="n_tabs">
						<xsl:value-of select="$n_tabs"/>
					</xsl:with-param>
					<xsl:with-param name="n_cols">
						<xsl:value-of select="$n_cols"/>
					</xsl:with-param>
					<xsl:with-param name="node_key">
						<xsl:value-of select="concat(generate-id(), '_', @ID)"/>
					</xsl:with-param>
					<xsl:with-param name="st_layout">
						<xsl:value-of select="$st_layout"/>
					</xsl:with-param>
					<xsl:with-param name="form_return">
						<xsl:value-of select="$form_return"/>
					</xsl:with-param>
					<xsl:with-param name="submit_return">
						<xsl:value-of select="$submit_return"/>
					</xsl:with-param>
					<xsl:with-param name="form_key">
						<xsl:value-of select="$form_key"/>
					</xsl:with-param>
					<xsl:with-param name="collect_answer">
						<xsl:value-of select="$collect_answer"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>
	<!-- MK_ST_SUBMIT -->
	<xsl:template name="mk_st_submit">
		<xsl:param name="indent"/>
		<xsl:param name="submit_return"/>
		<xsl:param name="name"/>
		<xsl:param name="form_return"/>
		<xsl:param name="submit_text"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, '# Every form must have a submit button.')"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_SUBMITTED = st.form_submit_button(&#010;',$indent,$pad,'&quot;', normalize-space($name), '&quot;,&#010;',$indent,$pad,'help=&quot;', normalize-space($submit_text), '&quot;)')"/>
		<xsl:value-of select="concat('&#010;', $indent, 'if ', $form_key, '_SUBMITTED', ':')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, '# print(', $collect_answer,')')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'COLLECT_ANSWER = &quot;,&quot;.join(COLLECT_ANSWER)')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'FORM_RESULT = ',$form_key,'_FORM_RESULT')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'SEARCH_TERMS_KEY = FORM_RESULT[&quot;form_key&quot;]')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'print(json.dumps(', 'FORM_RESULT))')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'SEARCH_TERMS = str(FORM_RESULT[&quot;ID_1373687557_3_TEXT_INPUT&quot;][2])')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'SEARCH_ENGINE = str(FORM_RESULT[&quot;ID_1373687557_4_RADIO&quot;][2])')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'print(SEARCH_TERMS)')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'DEBUG_FLAG = ID_1373687557_5_CHECKBOX')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'if SEARCH_ENGINE == &quot;OPENAIRE&quot;:')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, $pad, 'PD_DF = oa_search_fn(SEARCH_TERMS, DEBUG_FLAG)')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, $pad, 'aggrid_controls(PD_DF) # LLAMADO AGGRID FIJO')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'elif SEARCH_ENGINE == &quot;SEMANTIC SCHOLAR&quot;:')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, $pad, 'SEM_SCHOL_LIMIT = &quot;20&quot;')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, $pad, 'PD_DF = sem_schol_search_fn(SEARCH_TERMS, DEBUG_FLAG, SEM_SCHOL_LIMIT)')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, $pad, 'st.success(&quot;Implementación en desarrollo y prueba&quot;)')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'elif SEARCH_ENGINE == &quot;CONSENSUS&quot;:')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, $pad, 'st.warning(&quot;Explorar inmediatamente esta opción&quot;)')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'else:')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, $pad, 'st.warning(&quot;',$form_key,': Implementación pendiente para este buscador&quot;)')"/>
		<xsl:if test="$oa_search = '1'">
			<xsl:value-of select="concat('&#010;', $indent, $pad, 'PD_DF = oa_search_fn(SEARCH_TERMS, DEBUG_FLAG)')"/>
			<xsl:value-of select="concat('&#010;', $indent, $pad, 'aggrid_controls(PD_DF) # LLAMADO AGGRID FIJO')"/>
		</xsl:if>
		<!--
        if ID_1373687557_SUBMITTED:
            # print()
            COLLECT_ANSWER = ",".join(COLLECT_ANSWER)
            FORM_RESULT = ID_1373687557_FORM_RESULT
            SEARCH_TERMS_KEY = FORM_RESULT["form_key"]
            print(json.dumps(FORM_RESULT))
            #SEARCH_TERMS = FORM_RESULT.get(SEARCH_TERMS_KEY)[2]
            SEARCH_TERMS = str(FORM_RESULT["ID_1373687557_3_TEXT_INPUT"][2])
            print(SEARCH_TERMS)
            DEBUG_FLAG = False
-->
		<!--
Aqui se debe usar "exec()" como se explica en [Python's exec(): Execute Dynamically Generated Code](https://realpython.com/python-exec/)
exec("result= sum(number**2 for number in numbers if number % 2== 0)")
 -->
	</xsl:template>
	<!-- MK_RADIO -->
	<xsl:template name="mk_radio">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:variable name="radio_definition">
			<xsl:for-each select="node[@type= 'radio_option']">
				<xsl:value-of select="concat('&#010;',$indent,$pad,'&quot;',upper-case(@TEXT),'&quot;')"/>
				<xsl:if test="position() != last()">,</xsl:if>
			</xsl:for-each>
		</xsl:variable>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = st.radio(&quot;', upper-case(@TEXT), '&quot;, [', $radio_definition, ']', ', key=&quot;', @ID, '&quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="variable_name">
				<xsl:value-of select="$variable_name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_TEXT_INPUT -->
	<xsl:template name="mk_text_input">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case($type), ' = ', 'st.text_input(&quot;', upper-case(@default), '&quot;', ', key=&quot;', @ID, '&quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="variable_name">
				<xsl:value-of select="$variable_name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_MULTISELECT -->
	<xsl:template name="mk_multiselect">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:variable name="multiselect_definition">
			<xsl:for-each select="node[@type= 'multi_option']">
				<xsl:value-of select="concat($indent,$pad,' &quot;',upper-case(normalize-space(@TEXT)),'&quot;')"/>
				<xsl:if test="position() != last()">
					<xsl:value-of select="concat(',','&#010;')"/>
				</xsl:if>
			</xsl:for-each>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="count(node[@default= 'True'] > 0)">
				<xsl:variable name="multiselect_default">
					<xsl:for-each select="node[@default= 'True']">
						<xsl:value-of select="concat('&quot;',upper-case(normalize-space(@TEXT)),'&quot;')"/>
						<xsl:if test="position() != last()">,</xsl:if>
					</xsl:for-each>
				</xsl:variable>
				<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case($type), ' = ', 'st.multiselect(&quot;', upper-case(normalize-space(@TEXT)), '&quot;,[&#10;',$indent,$pad,normalize-space($multiselect_definition),'],&#10;',$indent,$pad,'[',$multiselect_default,'],&#010;',$indent,$pad,'key=&quot;', @ID, '&quot;)')"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case($type), ' = ', 'st.multiselect(&quot;', upper-case(normalize-space(@TEXT)), '&quot;,[&#10;',$indent,$pad,normalize-space($multiselect_definition),'],&#010;',$indent,$pad,'key=&quot;', @ID, '&quot;)')"/>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="variable_name">
				<xsl:value-of select="$variable_name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_SLIDER -->
	<xsl:template name="mk_slider">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.slider(label=&quot;', upper-case(@TEXT), '&quot;, min_value=', @min, ', max_value=', @max, ', value=', @value, ', step=',  @step, ', key=&quot;', @ID, ' &quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="variable_name">
				<xsl:value-of select="$variable_name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_SELECTSLIDER -->
	<xsl:template name="mk_selectslider">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:variable name="selectslider_definition">[<xsl:for-each select="node[@type= 'slider_option']">"<xsl:value-of select="upper-case(@TEXT)"/>"<xsl:if test="position() != last()">, </xsl:if>
			</xsl:for-each>]
		</xsl:variable>
		<xsl:variable name="selectslider_default">
			<xsl:choose>
				<xsl:when test="count(node[@default != ''] > 0)">
					<xsl:for-each select="node[@default != '']">
						<xsl:if test="position()= 1">, (</xsl:if>"<xsl:value-of select="upper-case(@TEXT)"/>"<xsl:if test="position() != last()">, </xsl:if>
						<xsl:if test="position()= last()">)</xsl:if>
					</xsl:for-each>
				</xsl:when>
				<xsl:otherwise>
					<xsl:text/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>
		<xsl:variable name="selectslider_definition_all" select="concat(normalize-space($selectslider_definition), normalize-space($selectslider_default))"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.select_slider(&quot;', upper-case(@TEXT), '&quot;, ', $selectslider_definition_all, ', key=&quot;', @ID, '&quot;)')"/>
		<!-- <xsl:value-of select= "concat('&#010;', $indent, 'choice= ', 'st.multiselect(&quot;', upper-case(@TEXT), '&quot;, ', normalize-space($multiselect_definition), ', key=&quot;', @ID, '&quot;)')"/> -->
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="variable_name">
				<xsl:value-of select="$variable_name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_CHECKBOX -->
	<xsl:template name="mk_checkbox">
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="n_checkboxs"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<!--
		<xsl:variable name="checkbox_name">
			<xsl:value-of select="upper-case(translate($name,' []&lt;&gt;','_'))"/>
		</xsl:variable>
-->
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.checkbox(&quot;', $name, '&quot;, key=&quot;', @ID, '&quot;)')"/>
		<xsl:variable name="collect_answer">
			<xsl:value-of select="concat($collect_answer, '&quot;', $form_key, '_', position(), '_', upper-case(@type), '_', $name, '&quot; :', $form_key, '_', position(), '_', upper-case(@type))"/>
		</xsl:variable>
		<xsl:value-of select="concat('&#010;', $indent, '#', $collect_answer)"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_SELECTBOX -->
	<xsl:template name="mk_selectbox">
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="node_key"/>
		<xsl:param name="n_checkboxs"/>
		<xsl:param name="submit_return"/>
		<xsl:param name="form_return"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:variable name="select_options">
			<xsl:value-of select="concat('&quot;', upper-case(@TEXT), '&quot;,&#10;',$indent,$pad, '[')"/>
			<xsl:for-each select="node">"<xsl:value-of select="upper-case(@TEXT)"/>"<xsl:if test="position() != last()">, </xsl:if>
			</xsl:for-each>]</xsl:variable>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.',@type,'(&#010;',$indent,$pad, $select_options,',&#010;',$indent,$pad, 'key=&quot;', @ID, '&quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="variable_name">
				<xsl:value-of select="$variable_name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_TEXTAREA -->
	<xsl:template name="mk_text_area">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.text_area(&quot;', upper-case(@TEXT), '&quot;, key=&quot;', @ID, '&quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="variable_name">
				<xsl:value-of select="$variable_name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_TIME_INPUT -->
	<xsl:template name="mk_time_input">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.time_input(&quot;', upper-case(@TEXT), '&quot;, datetime.time(', @hh, ', ', @mm, '), key=&quot;', @ID, '&quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="variable_name">
				<xsl:value-of select="$variable_name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_DATE_INPUT -->
	<xsl:template name="mk_date_input">
		<xsl:param name="n_cols"/>
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.date_input(&quot;', upper-case(@TEXT), '&quot;, datetime.date(', @yy, ', ', @mm, ', ', @dd, '), key=&quot;', @ID, '&quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="variable_name">
				<xsl:value-of select="$variable_name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_COLOR_PICKER -->
	<xsl:template name="mk_color_picker">
		<xsl:param name="type"/>
		<xsl:param name="node_level"/>
		<xsl:param name="pos"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="st_prefix"/>
		<xsl:param name="n_tabs"/>
		<xsl:param name="n_cols"/>
		<xsl:param name="node_key"/>
		<xsl:param name="st_layout"/>
		<xsl:param name="submit_return"/>
		<xsl:param name="form_return"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.color_picker(&quot;Pick a color&quot;', ', key=&quot;', @ID, '&quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_CAMERA_INPUT -->
	<xsl:template name="mk_camera_input">
		<xsl:param name="type"/>
		<xsl:param name="node_level"/>
		<xsl:param name="pos"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="st_prefix"/>
		<xsl:param name="n_tabs"/>
		<xsl:param name="n_cols"/>
		<xsl:param name="node_key"/>
		<xsl:param name="st_layout"/>
		<xsl:param name="submit_return"/>
		<xsl:param name="form_return"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.camera_input(&quot;Take a picture&quot;', ', key=&quot;', @ID, '&quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_FILE_UPLOADER -->
	<xsl:template name="mk_file_uploader">
		<xsl:param name="type"/>
		<xsl:param name="node_level"/>
		<xsl:param name="pos"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="st_prefix"/>
		<xsl:param name="n_tabs"/>
		<xsl:param name="n_cols"/>
		<xsl:param name="node_key"/>
		<xsl:param name="st_layout"/>
		<xsl:param name="submit_return"/>
		<xsl:param name="form_return"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_', position(), '_', upper-case(@type), ' = ', 'st.file_uploader(&quot;Upload a CSV&quot;', ', key=&quot;', @ID, '&quot;)')"/>
		<xsl:call-template name="mk_collect_answer">
			<xsl:with-param name="pos">
				<xsl:value-of select="$pos"/>
			</xsl:with-param>
			<xsl:with-param name="name">
				<xsl:value-of select="$name"/>
			</xsl:with-param>
			<xsl:with-param name="indent">
				<xsl:value-of select="$indent"/>
			</xsl:with-param>
			<xsl:with-param name="type">
				<xsl:value-of select="$type"/>
			</xsl:with-param>
			<xsl:with-param name="group_pos">
				<xsl:value-of select="$group_pos"/>
			</xsl:with-param>
			<xsl:with-param name="node_level">
				<xsl:value-of select="$node_level"/>
			</xsl:with-param>
			<xsl:with-param name="submit_return">
				<xsl:value-of select="$submit_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_return">
				<xsl:value-of select="$form_return"/>
			</xsl:with-param>
			<xsl:with-param name="form_key">
				<xsl:value-of select="$form_key"/>
			</xsl:with-param>
			<xsl:with-param name="collect_answer">
				<xsl:value-of select="$collect_answer"/>
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<!-- MK_HTML -->
	<xsl:template name="mk_html">
		<xsl:param name="indent"/>
		<xsl:param name="n_tabs"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:text>&#010;import components_example_html as cxh</xsl:text>
		<xsl:text>&#010;# bootstrap 4 collapse example</xsl:text>
		<xsl:text>&#010;# data for example</xsl:text>
		<xsl:value-of select="concat('&#010;', $indent, 'with st.sidebar:')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'components.html(', 'cxh.component_example_body, height=520, )')"/>
	</xsl:template>
	<!-- MK_ST_IFRAME -->
	<xsl:template name="mk_st_iframe">
		<xsl:param name="type"/>
		<xsl:param name="node_level"/>
		<xsl:param name="pos"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="st_prefix"/>
		<xsl:param name="n_tabs"/>
		<xsl:param name="n_cols"/>
		<xsl:param name="node_key"/>
		<xsl:param name="st_layout"/>
		<xsl:param name="submit_return"/>
		<xsl:param name="form_return"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, @text)"/>
		<xsl:value-of select="concat('&#010;', $indent, 'components.iframe(&quot;',@url , '&quot;, height=1100, scrolling=True)')"/>
		<!--
		<xsl:value-of select="concat('&#010;', $indent, 'components.iframe(&quot;',@url , '&quot;, height=600, scrolling=True)')"/>
		    <script>
    // Selecting the iframe element
    var iframe = document.getElementById("myIframe");
    
    // Adjusting the iframe height onload event
    iframe.onload = function(){
        iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
    }
    </script>
-->
	</xsl:template>
	<!-- MK_EXPANDER -->
	<xsl:template name="mk_expander">
		<xsl:param name="indent"/>
		<xsl:param name="n_tabs"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:if test="node[@type='explanation']/@text !=''">
			<xsl:value-of select="concat('&#010;', $indent, 'EXPLANATION = &quot;&quot;&quot;&#010;',node[@type='explanation']/@text,'&#010;&quot;&quot;&quot;')"/>
		</xsl:if>
		<xsl:value-of select="concat('&#010;', $indent, 'with st.',@type,'(&quot;',$name,'&quot;):')"/>
		<xsl:value-of select="concat('&#010;', $indent, $pad, 'st.markdown(EXPLANATION)')"/>
	</xsl:template>
	<!-- MK_COLLECT_ANSWER -->
	<xsl:template name="mk_collect_answer">
		<xsl:param name="pos"/>
		<xsl:param name="name"/>
		<xsl:param name="variable_name"/>
		<xsl:param name="indent"/>
		<xsl:param name="type"/>
		<xsl:param name="group_pos"/>
		<xsl:param name="node_level"/>
		<xsl:param name="node_key"/>
		<xsl:param name="n_checkboxs"/>
		<xsl:param name="submit_return"/>
		<xsl:param name="form_return"/>
		<xsl:param name="form_key"/>
		<xsl:param name="collect_answer"/>
		<xsl:value-of select="concat('&#010;', $indent, $form_key, '_FORM_RESULT.update({&quot;', $form_key, '_', position(), '_', upper-case(@type),'&quot;: [&#010;')"/>
		<xsl:value-of select="concat($indent,$pad,'&quot;',$type,'&quot;,&#010;',$indent,$pad,'&quot;',$name,'&quot;,&#010;',$indent,$pad,'str(',$form_key, '_', position(), '_', upper-case(@type),')]})')"/>
		<xsl:if test="$code_tracker = '1'">
			<xsl:value-of select="concat('&#010;', $indent, '#', $collect_answer)"/>
		</xsl:if>
	</xsl:template>
</xsl:stylesheet>
