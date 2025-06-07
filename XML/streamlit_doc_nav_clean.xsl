<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:output method="html" encoding="UTF-8"/>
	<xsl:param name="class_filter">class</xsl:param>
	<xsl:param name="creation_date">
		<xsl:value-of select="format-dateTime(current-dateTime(), 
		'[Y0001]/[M01]/[D01] [h01]:[m01]:[s01] [P] [z] ')"/>
	</xsl:param>
	<xsl:param name="doctype_html">
		<xsl:value-of select="concat('&#060;','DOCTYPE html&#062;&#010;')"/>
	</xsl:param>
	<xsl:param name="url_base">https://docs.streamlit.io/</xsl:param>
	<xsl:template match="/nav">
		<xsl:value-of select="$doctype_html"/>
		<html lang="en">
			<head>
				<meta charset="utf-8"/>
				<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
				<title>Streamli Docs Index <xsl:value-of select="$creation_date"/>
				</title>
			</head>
			<body>
				<xsl:for-each select="*">
					<xsl:call-template name="mk_node"/>
				</xsl:for-each>
			</body>
		</html>
	</xsl:template>
	<!-- MK_NODE -->
	<xsl:template name="mk_node">
		<xsl:element name="node">
			<xsl:attribute name="name"><xsl:value-of select="local-name()"/></xsl:attribute>
			<xsl:for-each select="@*[local-name() != $class_filter]">
				<xsl:attribute name="{local-name()}"><xsl:value-of select="."/></xsl:attribute>
			</xsl:for-each>
			<xsl:attribute name="elem_value"><xsl:value-of select="text()"/></xsl:attribute>
			<xsl:if test="count(*) > 0">
				<xsl:for-each select="*">
					<xsl:call-template name="mk_node"/>
				</xsl:for-each>
			</xsl:if>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
