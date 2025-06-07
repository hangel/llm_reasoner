<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2009 (http://www.altova.com) by s0315 (s0315) -->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<!--
...............................................................................
********
20220717
********
- Generar código Python Streamlit para NxOBS
 ...............................................................................
-->
	<xsl:output method="text" encoding="utf-8" omit-xml-declaration="yes" indent="yes"/>
	<xsl:param name="url_base">
		<xsl:value-of select="/doc/@href"/>
	</xsl:param>
	<xsl:param name="creation_date">
		<xsl:value-of select="(xs:dateTime(current-dateTime()) - xs:dateTime('1970-01-01T00:00:00')) 
div xs:dayTimeDuration('PT0.001S')"/>
	</xsl:param>
	<xsl:template match="/doc">
<xsl:value-of select="concat('&#010;# ', 'FECHA: ',$creation_date,':',$url_base,'&#010;')"/>
		<xsl:for-each select="node">
			<xsl:sort order="ascending" select="@n"/>
			<xsl:call-template name="mk_node"/>
		</xsl:for-each>
	</xsl:template>
	<!-- MK_NODE -->
	<xsl:template name="mk_node">
		<xsl:param name="pos"/>
		<xsl:choose>
			<xsl:when test="@type='comment'">
				<xsl:value-of select="concat('&#010;# ',@n,':',@params,'&#010;')"/>
			</xsl:when>
			<xsl:when test="@type='libraries'">
				<xsl:value-of select="concat(.,'&#010;')"/>
			</xsl:when>
			<xsl:when test="@type='decorator'">
				<xsl:value-of select="concat('&#010;@',@name,'(',@params,')&#010;')"/>
			</xsl:when>
			<xsl:when test="@type='def'">
				<xsl:value-of select="concat('&#010;def ',@name,'(',@params,'):&#010;')"/>
			</xsl:when>
			<xsl:when test="@type='function_body'">
				<xsl:value-of select="concat(.,' # ',@n,' &#010;')"/>
			</xsl:when>
			<xsl:when test="@type='direct'">
				<xsl:value-of select="concat('&#010;',normalize-space(@params),' #: ',@n,'&#010;')"/>
			</xsl:when>
			<xsl:when test="@type='execute'">
				<xsl:value-of select="."/>
			</xsl:when>
			<xsl:when test="@type='no'">
</xsl:when>
			<xsl:when test="@type='assign'">
				<xsl:value-of select="concat(@var,' = ',@params,'# ',@n,' ',@type,' &#010;')"/>
			</xsl:when>
			<xsl:when test="@type='python'">
				<xsl:value-of select="concat(@var,' = ',@name,'(',@params,')','# ',@n,' ',@type,' &#010;')"/>
			</xsl:when>
			<xsl:when test="@type='return'">
				<xsl:value-of select="concat('    return ',@name,'(',@params,')&#010;')"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="."/>&#010;</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>
