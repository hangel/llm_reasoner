<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:output method="text" encoding="utf-8" omit-xml-declaration="no" indent="yes" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions"/>
	<xsl:param name="creation_date">
		<xsl:value-of select="format-dateTime(current-dateTime(), 
                          '[Y0001]/[M01]/[D01] [h01]:[m01]:[s01] [P] [z] ')"/>
	</xsl:param>
	<xsl:param name="pad">
		<xsl:text>    </xsl:text>
	</xsl:param>
	<xsl:param name="ret">
		<xsl:value-of select="'&#010;'"/>
	</xsl:param>
	<xsl:param name="tab">
		<xsl:value-of select="'&#009;'"/>
	</xsl:param>
	<xsl:param name="indent"/>
	<xsl:param name="src">https://stackoverflow.com/questions/50819390/processing-an-xslt-input-file-to-remove-particular-content-from-xslt</xsl:param>
	<xsl:template match="*">
		<xsl:choose>
			<xsl:when test="count(*) > 0">
				<xsl:call-template name="mk_element">
					<xsl:with-param name="indent">
						<xsl:value-of select="concat($indent,$pad)"/>
					</xsl:with-param>
					<xsl:with-param name="node_name">
						<xsl:value-of select="local-name()"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise/>
		</xsl:choose>
	</xsl:template>
	<!-- MK_ELEMENT -->
	<xsl:template name="mk_element">
		<xsl:param name="indent"/>
		<xsl:param name="node_name"/>
		<xsl:choose>
			<xsl:when test="local-name() = 'param'"/>
			<xsl:when test="local-name() = 'with-param'"/>
			<xsl:when test="local-name() = 'value-of'"/>
			<xsl:when test="local-name() = 'variable'"/>
			<xsl:when test="local-name() = 'choose'"/>
			<xsl:when test="local-name() = 'when'"/>
			<xsl:when test="local-name() = 'otherwise'"/>
			<xsl:when test="local-name() = 'text'"/>
			<xsl:when test="local-name() = 'if'"/>
			<xsl:otherwise>
				<xsl:value-of select="concat($ret,$indent,local-name(),': ',@name)"/>
				<xsl:if test="count(@*) > 0">
					<xsl:for-each select="@*">
						<xsl:call-template name="mk_attribute">
							<xsl:with-param name="indent">
								<xsl:value-of select="$indent"/>
							</xsl:with-param>
							<xsl:with-param name="attrib_name">
								<xsl:value-of select="local-name()"/>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:for-each>
				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:if test="count(*) > 0">
			<xsl:for-each select="*">
				<xsl:call-template name="mk_element">
					<xsl:with-param name="indent">
						<xsl:value-of select="concat($indent,$pad)"/>
					</xsl:with-param>
					<xsl:with-param name="node_name">
						<xsl:value-of select="local-name()"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>
	<!-- MK_ATTRIBUTE -->
	<xsl:template name="mk_attribute">
		<xsl:param name="indent"/>
		<xsl:param name="attrib_name"/>
		<!--
		<xsl:value-of select="concat($ret,$indent,$pad,$attrib_name,':: ',.)"/>
-->
	</xsl:template>
</xsl:stylesheet>
