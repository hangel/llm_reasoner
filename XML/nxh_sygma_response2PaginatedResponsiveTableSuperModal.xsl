<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2009 (http://www.altova.com) by s0315 (s0315) -->
<!-- 

## nxh_sygma_response2PaginatedResponsiveTableSuprModal.xsl -->
<!-- 

#### 20221020

-->
<!-- 

#### 20221017

* Agregar botón Supermodal como en : http://localhost/nxobs/NxOBS/MVP/WebDevTrick_supermodal.html

  para crear una ficha para cada node de respuesta de OA Search

  para aquellos campos que tengan display: none;

-->
<!-- 

#### 20221016



* Convert OpenAIRE Search Result converts nxh_sygma_publications_yyymmdd_hhmmss.xml

  into nxh_sygma_publications_yyymmdd_hhmmss.html

  HTML basic for Spy local test

  SOURCE: [sachinrana95/responsive_table.md](https://gist.github.com/sachinrana95/c0c54722b95f98bba0db47441a4601dd)

* Build `oa_result_fields.xml` with every possible field in oa-response. (Consider build it dinamically from every search result) 

-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" exclude-result-prefixes="fo" xmlns="">
	<xsl:output method="html" encoding="utf-8" omit-xml-declaration="yes" indent="yes" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xpath-default-namespace="http://namespace.openaire.eu/sygma"/>
	<xsl:param name="creation_date">
		<xsl:value-of select="format-dateTime(current-dateTime(), 

		'[Y0001]/[M01]/[D01] [h01]:[m01]:[s01] [P] [z] ')"/>
	</xsl:param>
	<xsl:param name="doctype_html">
		<xsl:value-of select="concat('&#060;','!DOCTYPE html&#062;&#010;')"/>
	</xsl:param>
	<xsl:param name="ret">&#010;</xsl:param>
	<xsl:param name="type_process">oa</xsl:param>
	<xsl:param name="num_rows">10</xsl:param>
	<xsl:template match="/doc" xpath-default-namespace="http://namespace.openaire.eu/sygma">
		<xsl:variable name="oa_result_fields" xmlns="http://namespace.openaire.eu/sygma">
			<refactor_item type="oa_result_field" name="n" weight="0"/>
			<refactor_item type="oa_result_field" name="title" weight="10"/>
			<refactor_item type="oa_result_field" name="webresource" weight="11"/>
			<refactor_item type="oa_result_field" name="doi" weight="13"/>
			<refactor_item type="oa_result_field" name="openaireid" weight="14"/>
			<refactor_item type="oa_result_field" name="authors" weight="15" style="display:none;"/>
			<refactor_item type="oa_result_field" name="sourcejournal" weight="16"/>
			<refactor_item type="oa_result_field" name="publicationtype" weight="20"/>
			<refactor_item type="oa_result_field" name="bestlicense" weight="30"/>
			<refactor_item type="oa_result_field" name="dateofacceptance" weight="40"/>
			<refactor_item type="oa_result_field" name="description" weight="90" style="display:none;"/>
		</xsl:variable>
		<xsl:value-of select="$doctype_html" disable-output-escaping="yes"/>
		<html lang="en">
			<head>
				<meta charset="utf-8"/>
				<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
				<title>Responsive Table Super Modal: <xsl:value-of select="concat('nxh_sygma_publications',' : ',$creation_date)"/>
				</title>
				<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"/>
				<meta http-equiv="Pragma" content="no-cache"/>
				<meta http-equiv="Expires" content="0"/>
				<meta name="description" content="Paginated Responsive Table."/>
				<meta name="source" content="https://gist.github.com/sachinrana95/c0c54722b95f98bba0db47441a4601dd"/>
				<!--
				<link href="bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet"/>
				<script src="ajax/libs/jquery/1.7.1/jquery.min.js"/>
				<link rel="stylesheet" href="ajax/libs/jquery/1.10.2/css/jquery.dataTables.min.css"/>
-->
				<meta http-equiv="X-UA-Compatible" content="ie=edge"/>
				<link rel="stylesheet" href="css/supermodal.css"/>
			</head>
			<body>
				<div class="title">
					<xsl:value-of select="concat('nxh_sygma_publications',' : ',$creation_date)"/>
					<br/>
				</div>
				<xsl:choose>
					<xsl:when test="$type_process = 'oa'">
						<xsl:for-each select="/doc/nodes/node[position() &lt;= $num_rows]">
							<xsl:variable name="current_result">
								<xsl:copy-of select="."/>
							</xsl:variable>
							<xsl:call-template name="mk_response_card"/>
						</xsl:for-each>
					</xsl:when>
				</xsl:choose>
			</body>
		</html>
	</xsl:template>
	<!-- MK_RESPONSE_CARD -->
	<xsl:template name="mk_response_card">
		<xsl:element name="a">
			<xsl:attribute name="href"><xsl:value-of select="concat('#modal-opened-',position())"/></xsl:attribute>
			<xsl:attribute name="class">link-1</xsl:attribute>
			<xsl:attribute name="id"><xsl:value-of select="concat('modal-closed-',position())"/></xsl:attribute>
			<!--			<xsl:value-of select="concat(position(),' - ', @title, '&lt;br />DOI:&lt;span class=&quot;link-1&quot;> &lt;a href=&quot;https://doi.org/',@doi,'&quot;>',@doi,'&lt;/a>&lt;/span>')" disable-output-escaping="yes"/> -->
			<xsl:value-of select="concat(position(),' - ', @title, '&lt;br />DOI: ',@doi)" disable-output-escaping="yes"/>
		</xsl:element>
		<xsl:element name="div">
			<xsl:attribute name="class">container</xsl:attribute>
			<xsl:attribute name="id"><xsl:value-of select="concat('modal-opened-',position())"/></xsl:attribute>
			<div class="modal">
				<div class="details">
					<div class="title">
						<xsl:element name="a">
							<xsl:attribute name="href"><xsl:value-of select="@webresource"/></xsl:attribute>
							<xsl:attribute name="target">_blank</xsl:attribute>
							<xsl:attribute name="display">inline</xsl:attribute>
							<xsl:value-of select="concat(position(),' - ', @title)" disable-output-escaping="yes"/>
						</xsl:element>
					</div>
					<p class="description">
						<xsl:value-of select="@authors" disable-output-escaping="yes"/>
					</p>
					<p class="description">
						<xsl:value-of select="concat('&lt;br />&lt;strong>DOI:&lt;/strong> &lt;a href=&quot;https://doi.org/',@doi,'&quot; target=&quot;_blank&quot;>',@doi,'&lt;/a>')" disable-output-escaping="yes"/>
					</p>
				</div>
				<!--
				<p class="txt" style="overflow: auto; height:300px; border: solid 1px rgba(48, 48, 48, .4)">
-->
				<p class="txt">
					<xsl:value-of select="@description" disable-output-escaping="yes"/>
				</p>
				<button class="btn">Button &#8594;</button>
				<xsl:element name="a">
					<xsl:attribute name="href"><xsl:value-of select="concat('#modal-closed-',position())"/></xsl:attribute>
					<xsl:attribute name="class">link-2</xsl:attribute>
				</xsl:element>
			</div>
		</xsl:element>
		<hr/>
		<xsl:value-of select="$ret"></xsl:value-of>
	</xsl:template>
</xsl:stylesheet>
