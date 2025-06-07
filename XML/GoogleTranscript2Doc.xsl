<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:output method="xml" version="1.0" standalone="yes" omit-xml-declaration="yes"/>
	<xsl:template match="/div">
		<xsl:element name="doc">
			<xsl:attribute name="name">NVidia GTC 2022</xsl:attribute>
			<xsl:attribute name="date">2022/09/20</xsl:attribute>
			<xsl:attribute name="lan">en</xsl:attribute>
			<xsl:value-of select="'&#010;'"/>
			<xsl:for-each select="ytd-transcript-segment-renderer">
				<xsl:value-of select="concat(normalize-space(.//div[@class='segment-timestamp style-scope ytd-transcript-segment-renderer']), '&#009;', normalize-space(.//yt-formatted-string[@class='segment-text style-scope ytd-transcript-segment-renderer']),'&#010;')"/>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
