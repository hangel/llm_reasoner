<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<!--
...............................................................................
********
20220717
********
- Simplificar el mm quitando div atravesando el elemento
...............................................................................
-->
	<xsl:output method="text" version="1.0" encoding="UTF-8" standalone="yes" omit-xml-declaration="yes" indent="no"/>
	<xsl:param name="url_base">
		<xsl:value-of select="/doc/@href"/>
	</xsl:param>
	<xsl:param name="creation_date">
		<xsl:value-of select="(xs:dateTime(current-dateTime()) - xs:dateTime('1970-01-01T00:00:00')) 
div xs:dayTimeDuration('PT0.001S')"/>
	</xsl:param>
	<xsl:template match="/doc">
		<xsl:for-each select="node">
			<xsl:value-of select="."/>
		</xsl:for-each>
	</xsl:template>
	<!-- MK_NODE -->
	<xsl:template name="mk_node">
		<xsl:param name="parent_id"/>
		<xsl:choose>
			<xsl:when test="@element_type='script'"/>
			<xsl:when test="@element_type='style'"/>
			<xsl:when test="@element_type='head'"/>
			<xsl:when test="@element_type = 'div'">
				<xsl:if test="count(*)  > 0">
					<xsl:if test="count(node)>0">
						<xsl:for-each select="node">
							<xsl:call-template name="mk_node">
								<xsl:with-param name="parent_id">
									<xsl:value-of select="@id"/>
								</xsl:with-param>
							</xsl:call-template>
						</xsl:for-each>
					</xsl:if>
				</xsl:if>
			</xsl:when>
			<xsl:otherwise>
				<xsl:element name="node">
					<xsl:attribute name="CREATED"><xsl:value-of select="$creation_date"/></xsl:attribute>
					<xsl:attribute name="FOLDED">true</xsl:attribute>
					<xsl:attribute name="ID"><xsl:value-of select="generate-id()"/></xsl:attribute>
					<xsl:if test="@href">
						<xsl:attribute name="LINK"><xsl:value-of select="concat($url_base,@href)"/></xsl:attribute>
					</xsl:if>
					<xsl:attribute name="MODIFIED"><xsl:value-of select="$creation_date"/></xsl:attribute>
					<xsl:attribute name="POSITION">right</xsl:attribute>
					<!--				<xsl:attribute name="TEXT"><xsl:value-of select="@name"/></xsl:attribute> -->
					<xsl:attribute name="TEXT"><xsl:value-of select="@element_type"/></xsl:attribute>
					<!--			<xsl:attribute name="TEXT"><xsl:value-of select="concat(@element_type,'_',@element_pos)"/></xsl:attribute> -->
					<xsl:if test="count(@*)>0">
						<xsl:call-template name="mk_attribute_layout">
							<xsl:with-param name="parent_id">
								<xsl:value-of select="$parent_id"/>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:if>
					<xsl:if test="count(node)>0">
						<xsl:for-each select="node">
							<xsl:call-template name="mk_node">
								<xsl:with-param name="parent_id">
									<xsl:value-of select="@id"/>
								</xsl:with-param>
							</xsl:call-template>
						</xsl:for-each>
					</xsl:if>
				</xsl:element>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	<!-- MK_ATTRIBUTE -->
	<xsl:template name="mk_attribute">
		<xsl:param name="parent_id"/>
		<xsl:param name="parent_pos"/>
		<xsl:element name="attribute">
			<xsl:attribute name="NAME"><xsl:value-of select="local-name()"/></xsl:attribute>
			<xsl:attribute name="VALUE"><xsl:value-of select="."/></xsl:attribute>
		</xsl:element>
		<!--
			<attribute_layout NAME_WIDTH="73" VALUE_WIDTH="319"/>
			<attribute NAME="page" VALUE="menu"/>
			<attribute NAME="enabled" VALUE="True"/>
			<attribute NAME="link" VALUE="https://graph.openaire.eu/develop/api.html"/>
			<attribute NAME="name" VALUE="OpenAIRE Research Graph"/>
			<attribute NAME="description" VALUE="https://graph.openaire.eu/develop/changelog.html"/>
			<attribute NAME="version" VALUE="2022-05-11T10:01:33.969973Z"/>
-->
	</xsl:template>
	<!-- MK_ATTRIBUTE_LAYOUT -->
	<xsl:template name="mk_attribute_layout">
		<xsl:param name="parent_id"/>
		<xsl:param name="parent_pos"/>
		<xsl:element name="attribute_layout">
			<xsl:attribute name="NAME_WITH">87</xsl:attribute>
			<xsl:attribute name="VALUE_WITH">119</xsl:attribute>
		</xsl:element>
		<xsl:for-each select="@*">
			<xsl:call-template name="mk_attribute">
				<xsl:with-param name="parent_id"/>
				<xsl:with-param name="parent_pos"/>
			</xsl:call-template>
		</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>
