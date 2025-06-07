<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xmlns:a="http://namespace.openaire.eu/sygma" xmlns="http://namespace.openaire.eu/sygma" exclude-result-prefixes="#default" xpath-default-namespace="http://namespace.openaire.eu/sygma">
	<!--
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xmlns:nxobs="http://namespace.netux.com/nxobs">
========
20220721
++++++++
Agregar atributos: total, pag y size
========
20220526
++++++++
PENDIENTES:
* Manejo de "HTML escaped" para normalizar su despliegue y procesamiento.
	+ Deseable "desescapar" los contenidos para procesarlos dentro del árbol de contenido recibido
	+ Usar la versión NxOBS page ampliadqa para detallar el despliegue de salida
* Ampliar los parámetros para incluír TODO lo descriptivo de las consultas a OpenAIRE
========
20220525
++++++++
Revisar parámetros en <doc></doc>
========
20220524
++++++++
* Generación de HTML básico a partir de formato de salida estándar NxOBS
* Inicio de prueba de paso de parámetros a la XSLT
	- se agrega var1 [pasó OK]
* Agregar conjunto de parámetros básicos, generados desde hoja de cálculo
	1- Creación de elementos Python: asignados dinámicamente al valor de ejecución
	2- Creación de elementos XSLT en dos sitios: [Funcional
		 pero requiere ajustar el listado del generador de parámetros 
			a los valores necesarios. 
		Se usará la documentación completa de OpenAIRE API que ya está en 
		https://docs.google.com/spreadsheets/d/1-bIyVpiDKw7vnrDkcKvXeOcVkRMzNrEJVJq1c5UwzeU/edit#gid=1293117939 ]
		2.1- Asignación de <xsl:param name... al archivo xsl
		2.2- Asignación de los valores obtenidoas como atributos al elemnto <doc> 
========
20220524
++++++++
Inicio de prueba de paso de parámetros a la XSLT
========
20220523
++++++++

========
20220523
++++++++
Completar el formato XML que resulta de la consulta
incluyendo mediante elk paso de parámetros la siguiente información
    query
    timestamp
    parámetros
    fuente
    tipo de dato
para

    Iterar en la respuesta
    Tener una visión ampliada
    Actuar con el resultado
    Generar productos NxOBS




========
20220519
++++++++
* Explorar conflictos con namespaces que impiden navegar a XPATH: [OK] MUY IMPORTANTE LA DECLARACIÓN DE XSL:STYLESHEET COMO QUEDÓ
#####################################################
# https://stackoverflow.com/questions/10981312/xml-element-has-namespace-my-xpath-does-not-work
XPath interprets an unprefixed element name as belonging to "no namespace" and this is the reason elements with unprefixed names belonging to a default (nonempty) namespace aren't selected when only their unprefixed name is specified as a node-test in an XPath expression.

The solution is either:

    1. Create a namespace binding where a prefix (say "x") is associated with the default namespace, then specify x:elementName instead of elementName.
    2. Use long, ugly and unreliable expressions like: *[name() = 'elementName']
#####################################################
========
20220516
++++++++
1 Explorar la conversión de formato sygma
* XSL está OK en Spy [OK]
* Investigar XSL en Python []
2 Definir formato unificado []
* * Tipo (Openaire | Sygma)
* * Query Completo (String con escapes para evitar &amp;)(modificar XML Obtenido y agregar atributos query, fecha, tipo,)
* * Params
* * * # page              = 1# integer
* * * # size              = 100# integer
* * * # format            = # json | xml | csv | tsv
* * * # model             = # openaire | sygma
* * * # sortBy            = # sortBy =field,[ascending|descending]. 
							# 'field' is one of: dateofcollection, resultstoragedate, resultstoragedate, resultembargoenddate, resultembargoendyear, resultdateofacceptance, resultacceptanceyear
* * * # hasECFunding      = # true | false
* * * # hasWTFunding      = # true | false
* * * # funder            = # WT | EC | ARC | ANDS | NSF | FCT | NHMRC
* * * # fundingStream     = # ...
* * * # FP7scientificArea = # ...
* * * # keywords          = # White-space separated list of keywords.
* * Fecha de Query
* * Enlace OpenAire
* * DOI
* * Tipo resultado del Documento refeenciado (PDF | HTML | XML | LaTeX | Text | Otros)
* * Título (String)
* * Palabras Clave (Del Documento)
* * Abstract
* * Vínculos a Imágenes
* * Vínculos a Tablas
* * Conclusiones
* * Vínculo a Documento Completo
========
20220427
++++++++
* Se aplaza desarrollo de modelo "openaire" para acelerar desarrollo
* Ajuste de lectura de Autores del modelo "sygma".
* Completar el modelo nxobs
* XSL para convertir de modelo nxobs a mm

PENDIENTES:
++++++++++
* sygma2doc
* openaire2doc (Aplazado)
* doc_oa2nxobs (Aplazado)
* doc_sy2nxobs: Visión unificada de los resultados
* nxobs2mm: Para visualizar, evaluar, generar documentación -doc, html-) 

DOCUMENTACIÓN ENTREGABLE MAYO 1
+++++++++++++++++++++++++++++++
* Completar documento de especificaciones de NxOBS http://localhost/netux/0000%20VTIC/NxOBS_Implementacion.mm
* Prototipo Integración de Recursos de Búsqueda como parte del proceso de desarrollo de los productos solicitados
	* Vigilancia
	* Inteligencia
	* Referenciaciones

========
20220426
++++++++
OpenAIRE to NxOBS
'''''''''''''''''
Normalizador de datos entre los resultados de la API de OpenAIRE para Publicaciones. 
Obtener un formato común para documentos de NxOBS. 
- Paso intermedio llevar a formato doc/nopdes/node 
- Conversión a formato FreeMind
	<xsl:output encoding="utf-8" method="xml" indent="yes" standalone="yes" exclude-result-prefixes="#default" omit-xml-declaration="yes" xpath-default-namespace="#default"/>
-->
	<xsl:output encoding="utf-8" method="xml" indent="yes"/>
	<xsl:strip-space elements="*"/>
	<xsl:param name='project'>NxOBS</xsl:param>
	<xsl:param name='size'>0</xsl:param>
	<xsl:param name='page'>0</xsl:param>
	<xsl:param name='total'/>
	<xsl:param name='product'>i</xsl:param>
	<xsl:param name='privacy'>p</xsl:param>
	<xsl:param name='date'/>
	<xsl:param name='query'/>
	<xsl:param name='keywords'/>
	<xsl:param name='model'>sygma</xsl:param>
	<xsl:param name="api_endpoint">publications</xsl:param>
	<xsl:param name="result-ns">
		<xsl:choose>
			<xsl:when test="//namespace::*[.='http://namespace.openaire.eu/sygma']">http://namespace.openaire.eu/sygma</xsl:when>
		</xsl:choose>
		<xsl:choose>
			<xsl:when test="//namespace::*[.='http://www.driver-repository.eu/namespace/dri']">http://www.driver-repository.eu/namespace/dri</xsl:when>
		</xsl:choose>
	</xsl:param>
	<xsl:param name="return">
		<xsl:text>&#xa;</xsl:text>
	</xsl:param>
	<!-- -->
	<!-- TEMPLATE  MAIN -->
	<xsl:template match="/">
		<xsl:choose>
			<xsl:when test="$model='sygma'">
				<xsl:element name="doc" xpath-default-namespace="http://namespace.openaire.eu/sygma">
					<xsl:attribute name='project'><xsl:value-of select='$project'/></xsl:attribute>
					<xsl:attribute name='size'><xsl:value-of select='normalize-space(/response/header/size)'/></xsl:attribute>
					<xsl:attribute name='page'><xsl:value-of select='normalize-space(/response/header/page)'/></xsl:attribute>
					<xsl:attribute name='total'><xsl:value-of select='normalize-space(/response/header/total)'/></xsl:attribute>
					<xsl:attribute name='product'><xsl:value-of select='$product'/></xsl:attribute>
					<xsl:attribute name='privacy'><xsl:value-of select='$privacy'/></xsl:attribute>
					<xsl:attribute name='date'><xsl:value-of select='$date'/></xsl:attribute>
					<xsl:attribute name='query'><xsl:value-of select='$query'/></xsl:attribute>
					<xsl:attribute name='keywords'><xsl:value-of select='$keywords'/></xsl:attribute>
					<xsl:attribute name="model"><xsl:value-of select="$model"/></xsl:attribute>
					<xsl:attribute name="model-ns"><xsl:value-of select="$result-ns"/></xsl:attribute>
					<xsl:attribute name="api_endpoint"><xsl:value-of select="$api_endpoint"/></xsl:attribute>
					<xsl:call-template name="tp_sygma"/>
				</xsl:element>
			</xsl:when>
			<xsl:when test="$model='openaire'">
				<xsl:element name="doc">
					<xsl:attribute name="timestamp"><xsl:value-of select="$timestamp"/></xsl:attribute>
					<xsl:attribute name="model"><xsl:value-of select="$model"/></xsl:attribute>
					<xsl:attribute name="model-ns"><xsl:value-of select="$result-ns"/></xsl:attribute>
					<xsl:attribute name="oa_endpoint"><xsl:value-of select="$oa_endpoint"/></xsl:attribute>
					<xsl:attribute name="oa_queryterms"><xsl:value-of select="$oa_queryterms"/></xsl:attribute>
					<xsl:call-template name="tp_openaire"/>
				</xsl:element>
			</xsl:when>
		</xsl:choose>
		<!--		<xsl:for-each select="*"/> -->
	</xsl:template>
	<!-- TEMPLATE SYGMA -->
	<xsl:template name="tp_sygma">
		<xsl:element name="nodes">
			<xsl:attribute name="count"><xsl:value-of select="count(/a:response/a:publications/a:publication)"/></xsl:attribute>
			<xsl:attribute name="count_child"><xsl:value-of select="count(*)"/></xsl:attribute>
			<xsl:attribute name="root_ns"><xsl:value-of select="namespace-uri()"/></xsl:attribute>
			<xsl:for-each select="/a:response/a.header/*">
				<xsl:attribute name="{local-name()}"><xsl:value-of select="normalize-space(.)"/></xsl:attribute>
			</xsl:for-each>
			<xsl:for-each select="/a:response/a:publications/a:publication">
				<xsl:call-template name="mk_sygma_publication_node"/>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>
	<!-- TEMPLATE SYGMA PUBLICATION NODE -->
	<xsl:template name="mk_sygma_publication_node">
		<xsl:element name="node">
			<xsl:attribute name="n"><xsl:value-of select="position()"/></xsl:attribute>
			<xsl:for-each select="*[not(name()='authors')]">
			<xsl:sort select="name()"/>
				<xsl:attribute name="{local-name()}"><xsl:value-of select="normalize-space(.)"/></xsl:attribute>
			</xsl:for-each>
			<xsl:for-each select="authors">
				<xsl:attribute name="{local-name()}"><xsl:value-of select="normalize-space(.)"/></xsl:attribute>
			</xsl:for-each>
			<xsl:variable name="authors_list">
				<xsl:for-each select="a:authors/a:author">
					<xsl:value-of select="normalize-space(text())"/>
					<xsl:if test="position()!=last()">
						<xsl:value-of select="'; '"/>
					</xsl:if>
				</xsl:for-each>
			</xsl:variable>
			<xsl:attribute name="authors"><xsl:value-of select="$authors_list"/></xsl:attribute>
		</xsl:element>
	</xsl:template>
	<!-- TEMPLATE SYGMA_RESULT_NODE -->
	<!--
	<xsl:template name="mk_sygma_result_node">
		<xsl:element name="node">
			<xsl:attribute name="n"><xsl:value-of select="position()"/></xsl:attribute>
			<xsl:for-each select="*[not(name()='authors')]">
				<xsl:choose>
					<xsl:when test="*[not(name()='authors')]">
					</xsl:when>
					<xsl:otherwise/>
				</xsl:choose>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>
	-->
	<!-- TEMPLATE OPENAIRE -->
	<xsl:template name="tp_openaire">
		<xsl:element name="nodes">
			<xsl:attribute name="count"><xsl:value-of select="count(/response)"/></xsl:attribute>
			<xsl:for-each select="/response/header/*" xmlns:dri="http://www.driver-repository.eu/namespace/dri">
				<xsl:attribute name="{local-name()}"><xsl:value-of select="normalize-space(.)"/></xsl:attribute>
			</xsl:for-each>
			<xsl:for-each select="/response/results/result" xmlns:dri="http://www.driver-repository.eu/namespace/dri" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:oaf="http://namespace.openaire.eu/oaf">
				<xsl:call-template name="mk_openaire_result_node"/>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>
	<!-- TEMPLATE OPENAIRE_RESULT_NODE -->
	<xsl:template name="mk_openaire_result_node">
		<xsl:element name="node">
			<xsl:attribute name="n"><xsl:value-of select="position()"/></xsl:attribute>
			<xsl:for-each select="*[not(name()='authors')]">
				<xsl:choose>
					<xsl:when test="*[not(name()='authors')]">
						<xsl:attribute name="{name()}"><xsl:value-of select="normalize-space(.)"/></xsl:attribute>
					</xsl:when>
					<xsl:otherwise/>
				</xsl:choose>
			</xsl:for-each>
			<!--
			<xsl:if test="count(*[not(name()='authors')])>0">
				<xsl:for-each select="*[not(name()='authors')]">
					<xsl:call-template name="mk_openaire_result_node"/>
				</xsl:for-each>
			</xsl:if>
-->
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
