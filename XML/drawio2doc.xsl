<?xml version="1.0" encoding="UTF-8"?>
<!--
...............................................................................
DRAWIO2DOC.xsl
********
20221006
********
* Convertir versión XML de DRAW.io en Doc para observarlo y prteparar la real conversión de ff2drawio.xsl

...............................................................................
-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:output method="xml" version="1.0" encoding="UTF-8" standalone="yes" indent="yes"/>
	<xsl:param name="file_name">NxOBS® Doc version-Draw.io</xsl:param>
	<xsl:template match="/">
		<xsl:element name="doc">
			<xsl:attribute name="name"><xsl:value-of select="$file_name"/></xsl:attribute>
			<xsl:attribute name="date"><xsl:value-of select="current-dateTime()"/></xsl:attribute>
			<xsl:for-each select="@*">
				<xsl:sort select="@parent"/>
				<xsl:call-template name="mk_attribute">
					<xsl:with-param name="name">
						<xsl:value-of select="local-name()"/>
					</xsl:with-param>
					<xsl:with-param name="value">
						<xsl:value-of select="."/>
					</xsl:with-param>
					<xsl:with-param name="element_pos">
						<xsl:value-of select="position()"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
			<xsl:if test="count(*)>0">
				<xsl:for-each select="*">
					<xsl:sort select="@parent"/>
					<xsl:call-template name="mk_node">
						<xsl:with-param name="name">
							<xsl:value-of select="local-name()"/>
						</xsl:with-param>
						<xsl:with-param name="value">
							<xsl:value-of select="position()"/>
						</xsl:with-param>
						<xsl:with-param name="element_pos">
							<xsl:value-of select="position()"/>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:for-each>
			</xsl:if>
		</xsl:element>
	</xsl:template>
	<!-- MK_NODE -->
	<xsl:template name="mk_node">
		<xsl:param name="name"/>
		<xsl:param name="value"/>
		<xsl:param name="element_pos"/>
		<xsl:param name="element_text"/>
		<xsl:element name="node">
			<xsl:attribute name="element_type"><xsl:value-of select="$name"/></xsl:attribute>
			<xsl:attribute name="element_pos"><xsl:value-of select="$element_pos"/></xsl:attribute>
			<xsl:if test="$element_text != ''">
				<xsl:attribute name="element_text"><xsl:value-of select="$element_text"/></xsl:attribute>
			</xsl:if>
			<xsl:for-each select="@*">
				<xsl:sort select="@parent"/>
				<xsl:sort select="local-name()"/>
				<xsl:call-template name="mk_attribute">
					<xsl:with-param name="name">
						<xsl:value-of select="local-name()"/>
					</xsl:with-param>
					<xsl:with-param name="value">
						<xsl:value-of select="."/>
					</xsl:with-param>
					<xsl:with-param name="element_pos">
						<xsl:value-of select="position()"/>
					</xsl:with-param>
					<xsl:with-param name="element_text">
						<xsl:value-of select="text()"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
			<xsl:for-each select="@LINK">
				<xsl:attribute name="{lower-case(local-name())}"><xsl:value-of select="."/></xsl:attribute>
			</xsl:for-each>
			<xsl:if test="count(*)>0">
				<xsl:for-each select="*">
					<xsl:sort select="@parent"/>
					<xsl:call-template name="mk_node">
						<xsl:with-param name="name">
							<xsl:value-of select="local-name()"/>
						</xsl:with-param>
						<xsl:with-param name="value">
							<xsl:value-of select="attribute/@value"/>
						</xsl:with-param>
						<xsl:with-param name="element_pos">
							<xsl:value-of select="position()"/>
						</xsl:with-param>
						<xsl:with-param name="element_text">
							<xsl:value-of select="text()"/>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:for-each>
			</xsl:if>
		</xsl:element>
	</xsl:template>
	<!-- MK_ATTRIBUTE -->
	<xsl:template name="mk_attribute">
		<xsl:param name="name"/>
		<xsl:param name="value"/>
		<xsl:param name="element_pos"/>
		<xsl:param name="element_text"/>
		<xsl:choose>
			<xsl:when test="$name='class'"/>
			<xsl:when test="$name='style'"/>
			<xsl:otherwise>
				<xsl:attribute name="{$name}"><xsl:value-of select="$value"/></xsl:attribute>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>
