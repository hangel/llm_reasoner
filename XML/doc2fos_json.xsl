<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
<!-- https://explore.openaire.eu/search/find/research-outcomes?fos=%22060201%2520languages%2520%2526%2520linguistics%22 -->
<!--
Pendiente reeemplazar en @text para fos
- espacios  %2520
- ampersand %2526
-->
	<xsl:output encoding="utf-8" method="text" indent="yes"/>
	<xsl:param name="fill">
		<xsl:text>&#09;</xsl:text>
	</xsl:param>
	<xsl:param name="ret">
		<xsl:text>&#xA;</xsl:text>
	</xsl:param>
	<xsl:param name="nbsp">
		<xsl:text>&#160;</xsl:text>
	</xsl:param>
	<xsl:template match="/">
		<xsl:for-each select="/doc">#
<xsl:for-each select="node">
				<xsl:call-template name="mk_widget">
					<xsl:with-param name="nudge">#</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:for-each>
	</xsl:template>
	<!-- MK_WIDGET -->
	<xsl:template name="mk_widget">
		<xsl:param name="nudge"/>
		<xsl:param name="pos"/>
		<xsl:variable name="indent"/>
		<xsl:value-of select="concat($nudge,'[',@n,' ',@text,']','(','https://explore.openaire.eu/search/find/research-outcomes?fos=%22',@n,'%2520',@text,'%22)',$ret)"/>
		<xsl:choose>
			<xsl:when test="@widget='checkbox'"><xsl:call-template name="mk_widget_checkbox"/></xsl:when>
		</xsl:choose>
		<xsl:if test="count(node)>0">
			<xsl:for-each select="node">
				<xsl:call-template name="mk_widget">
					<xsl:with-param name="nudge">
						<xsl:value-of select="concat($nudge,$fill)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="position()"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>
	<xsl:template name="mk_widget_checkbox">
	</xsl:template>
</xsl:stylesheet>
