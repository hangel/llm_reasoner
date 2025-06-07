<?xml version="1.0" encoding="UTF-8"?>
<!--
...............................................................................
********
20221121
********
#okmaps_papers_list2doc.xsl
* Ajuste de links con target="_blank"
...............................................................................
********
20211206
********
Pendiente de agregar atributo "icon" a cada nodo, que vendrá del FreMind
...............................................................................
********
20211122
********
Validar procesamiento de atributos de FreeMind como atributos de nodo de salida
...............................................................................
Simplificar el documento quitando atributos de estilo de FreeMind
...............................................................................

-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:output method="xml" version="1.0" encoding="UTF-8" standalone="yes" indent="yes"/>
	<xsl:param name="creation_date">
		<xsl:value-of select="format-dateTime(current-dateTime(),
                          '[Y0001]/[M01]/[D01] [h01]:[m01]:[s01] [P] [z] ')"/>
	</xsl:param>
	<xsl:template match="/div[@id='papers_list']">
		<xsl:element name="doc">
			<xsl:attribute name="name"><xsl:value-of select="@TEXT"></xsl:value-of></xsl:attribute>
			<xsl:attribute name="date"><xsl:value-of select="$creation_date"></xsl:value-of></xsl:attribute>
			<xsl:for-each select="@*">
				<xsl:call-template name="mk_attribute">
					<xsl:with-param name="name">
						<xsl:value-of select="local-name()"/>
					</xsl:with-param>
					<xsl:with-param name="value">
						<xsl:value-of select="."/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
			<xsl:for-each select="attribute">
				<xsl:call-template name="mk_attribute">
					<xsl:with-param name="name">
						<xsl:value-of select="@NAME"/>
					</xsl:with-param>
					<xsl:with-param name="value">
						<xsl:value-of select="@VALUE"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
			<xsl:if test="count(*)>0">
				<xsl:for-each select="*">
					<xsl:call-template name="mk_node">
						<xsl:with-param name="name">
							<xsl:value-of select="attribute/@name"/>
						</xsl:with-param>
						<xsl:with-param name="value">
							<xsl:value-of select="attribute/@value"/>
						</xsl:with-param>
						<xsl:with-param name="type">
							<xsl:value-of select="local-name()"/>
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
		<xsl:param name="type"/>
		<xsl:element name="node">
			<xsl:attribute name="type"><xsl:value-of select="$type"></xsl:value-of></xsl:attribute>
			<xsl:for-each select="@TEXT">
				<xsl:attribute name="{lower-case(local-name())}"><xsl:value-of select="."></xsl:value-of></xsl:attribute>
			</xsl:for-each>
			<xsl:for-each select="@*">
				<xsl:choose>
					<xsl:when test="local-name() = 'd'"/>
					<xsl:when test="local-name() = 'x'"/>
					<xsl:when test="local-name() = 'y'"/>
					<xsl:when test="local-name() = 'width'"/>
					<xsl:when test="local-name() = 'height'"/>
					<xsl:when test="local-name() = 'style'"/>
					<xsl:otherwise>
						<xsl:call-template name="mk_attribute">
							<xsl:with-param name="name">
								<xsl:value-of select="local-name()"/>
							</xsl:with-param>
							<xsl:with-param name="value">
								<xsl:value-of select="."/>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:for-each>
			<xsl:for-each select="attribute">
				<xsl:call-template name="mk_attribute">
					<xsl:with-param name="name">
						<xsl:value-of select="@NAME"/>
					</xsl:with-param>
					<xsl:with-param name="value">
						<xsl:value-of select="@VALUE"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
			<xsl:for-each select="@LINK">
				<xsl:attribute name="{lower-case(local-name())}"><xsl:value-of select="."></xsl:value-of></xsl:attribute>
			</xsl:for-each>
			<xsl:choose>
				<xsl:when test="count(*)>0">
					<xsl:for-each select="*">
						<xsl:call-template name="mk_node">
							<xsl:with-param name="type">
								<xsl:value-of select="local-name()"/>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:for-each>
				</xsl:when>
				<xsl:otherwise>
					<xsl:attribute name="text"><xsl:value-of select="."></xsl:value-of></xsl:attribute>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:element>
	</xsl:template>
	<!-- MK_ATTRIBUTE -->
	<xsl:template name="mk_attribute">
		<xsl:param name="name"/>
		<xsl:param name="value"/>
		<xsl:choose>
			<xsl:when test="$name = 'COLOR'"/>
			<xsl:when test="$name = 'FOLDED'"/>
			<xsl:when test="$name = 'CREATED'"/>
			<xsl:when test="$name = 'POSITION'"/>
			<xsl:when test="$name = 'MODIFIED'"/>
			<xsl:otherwise>
				<xsl:attribute name="{$name}"><xsl:value-of select="$value"></xsl:value-of></xsl:attribute>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>
