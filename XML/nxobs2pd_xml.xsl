<!--<?xml version="1.0" encoding="UTF-8"?>-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xmlns:a="http://namespace.openaire.eu/sygma" xmlns:jats="http://namespace.openaire.eu/jats">
	<!--
========
20220818
++++++++
Evitar el error de buúsqueda con CERO resultados
========
-->
	<!--
========
20220720
++++++++
Generar una versión XML del archivo respuesta que permita se importada por Pandas de manera natural
========
<!DOCTYPE inline_dtd[
<!ENTITY nbsp "&#160;">
]>
-->
	<xsl:param name="html5">
		<xsl:text>&lt;!DOCTYPE html SYSTEM "entities.dtd" &gt;</xsl:text>
	</xsl:param>
	<xsl:param name="inlinedtd">
		<xsl:text>&lt;!DOCTYPE inline_dtd [
&lt;!ENTITY nbsp "&amp;#160;" &gt;
]&gt;</xsl:text>
	</xsl:param>
	<xsl:param name="newline">
		<xsl:text>&#10;</xsl:text>
	</xsl:param>
	<xsl:character-map name="a">
		<xsl:output-character character="&lt;" string="&lt;"/>
		<xsl:output-character character="&gt;" string="&gt;"/>
		<xsl:output-character character="&#160;" string="&amp;nbsp;"/>
	</xsl:character-map>
	<xsl:output encoding="utf-8" indent="yes" method="xml" omit-xml-declaration="yes" include-content-type="no" use-character-maps="a" exclude-result-prefixes="jats"/>
	<xsl:strip-space elements="*"/>
	<xsl:template match="/a:doc" xpath-default-namespace="http://namespace.openaire.eu/sygma">
		<root>
		<xsl:choose>
			<xsl:when test="count(nodes/node)>0"></xsl:when>
			<xsl:otherwise><node n="0" description="No results available"/></xsl:otherwise>
		</xsl:choose>
			<xsl:if test="count(nodes/node)>0">
				<xsl:for-each select="nodes/node">
					<xsl:call-template name="mk_register">
					</xsl:call-template>
				</xsl:for-each>
			</xsl:if>
		</root>
	</xsl:template>
	<!-- MK_CARD -->
	<xsl:template name="mk_register">
		<xsl:element name="row">
			<xsl:for-each select="@*">
				<xsl:if test=". != ''">
					<xsl:element name="{local-name()}">
						<xsl:value-of select="concat('&#060;![CDATA[',.,']]>')"/>
					</xsl:element>
				</xsl:if>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
