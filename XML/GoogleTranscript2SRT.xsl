<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:param name="mask">
		<xsl:value-of select="'00:00:00'"/>
	</xsl:param>
	<xsl:param name="end_time">
		<xsl:value-of select="'01:37:41'"/>
	</xsl:param>
	<xsl:output method="text" version="1.0" standalone="yes" omit-xml-declaration="yes"/>
	<xsl:template match="/div">
		<xsl:element name="doc">
			<xsl:attribute name="name">NVidia GTC 2022</xsl:attribute>
			<xsl:attribute name="date">2022/09/20</xsl:attribute>
			<xsl:attribute name="lan">en</xsl:attribute>
			<xsl:for-each select="ytd-transcript-segment-renderer">
				<xsl:call-template name="mk_time_ok">
					<xsl:with-param name="in_time">
						<xsl:value-of select="normalize-space(div/div/div[@class='segment-timestamp style-scope ytd-transcript-segment-renderer'])"/>
					</xsl:with-param>
					<xsl:with-param name="next_position">
						<xsl:value-of select="position() + 1"/>
					</xsl:with-param>
				</xsl:call-template>
				<xsl:value-of select="concat(normalize-space(.//yt-formatted-string[@class='segment-text style-scope ytd-transcript-segment-renderer']),'&#010;')"/>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>
	<xsl:template name="mk_time_ok">
		<xsl:param name="in_time"/>
		<xsl:param name="next_time"/>
		<xsl:param name="next_position"/>
		<xsl:variable name="next_time_ok">
			<xsl:choose>
				<xsl:when test="$next_position = last()">
					<xsl:value-of select="$end_time"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="normalize-space(//ytd-transcript-segment-renderer[position() = $next_position]/div/div/div[@class='segment-timestamp style-scope ytd-transcript-segment-renderer'])"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>
		<xsl:value-of select="concat('&#010;',position(),'&#010;',substring($mask,1,string-length($mask)-string-length($in_time)),$in_time,',000 --> ',substring($mask,1,string-length($mask)-string-length($next_time_ok)),$next_time_ok,',000&#010;')"/>
	</xsl:template>
</xsl:stylesheet>
