<?xml version="1.0" encoding="UTF-8"?>
<!--
...............................................................................
********
20220713
********
* ajustar contenido de @TEXT en mm
...............................................................................

-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:output method="xml" version="1.0" encoding="UTF-8" standalone="yes" omit-xml-declaration="yes" indent="yes"/>
	<xsl:param name="url_base"><xsl:value-of select="/doc/@href"></xsl:value-of></xsl:param>
	<xsl:param name="creation_date">1613996152862</xsl:param>
	<xsl:template match="/doc">
		<xsl:element name="map">
			<xsl:attribute name="version">1.0.1</xsl:attribute>
			<xsl:comment>To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net</xsl:comment>
			<xsl:element name="node">
				<xsl:attribute name="CREATED"><xsl:value-of select="$creation_date"></xsl:value-of></xsl:attribute>
				<xsl:attribute name="ID"><xsl:value-of select="generate-id()"></xsl:value-of></xsl:attribute>
				<xsl:attribute name="TEXT"><xsl:value-of select="concat(@name,'_',@element_text)"/></xsl:attribute>
				<xsl:attribute name="LINK"><xsl:value-of select="@href"></xsl:value-of></xsl:attribute>
				<xsl:for-each select="node">
					<xsl:call-template name="mk_node"/>
				</xsl:for-each>
			</xsl:element>
		</xsl:element>
	</xsl:template>
	<!-- MK_NODE -->
	<xsl:template name="mk_node">
		<!--
<node CREATED="1622817092415" FOLDED="true" ID="ID_425172205" LINK="https://digital-members.weforum.org/intelligence" MODIFIED="1626223567179" POSITION="right" TEXT="WEForum Intelligence">
-->
		<xsl:element name="node">
			<xsl:attribute name="CREATED"><xsl:value-of select="$creation_date"></xsl:value-of></xsl:attribute>
			<xsl:attribute name="FOLDED">true</xsl:attribute>
			<xsl:attribute name="ID"><xsl:value-of select="generate-id()"></xsl:value-of></xsl:attribute>
			<xsl:if test="@href">
				<xsl:attribute name="LINK"><xsl:value-of select="concat($url_base,@href)"></xsl:value-of></xsl:attribute>
			</xsl:if>
			<xsl:attribute name="MODIFIED"><xsl:value-of select="$creation_date"></xsl:value-of></xsl:attribute>
			<xsl:attribute name="POSITION">right</xsl:attribute>
			<xsl:attribute name="TEXT"><xsl:value-of select="@name"></xsl:value-of></xsl:attribute>
			<xsl:if test="count(node)>0">
				<xsl:for-each select="node">
					<xsl:call-template name="mk_node"/>
				</xsl:for-each>
			</xsl:if>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
