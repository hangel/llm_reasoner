<?xml version="1.0" encoding="UTF-8"?>
<!-- 
## nxh_sygma_response2pdLoad.xsl -->
<!-- 
#### 20221017
* Converts the sygma_response to a Pandas compatible <root><row>...<fields...</row></root>
  Field ata into <CDATA containers
-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" exclude-result-prefixes="fo" xmlns="">
	<xsl:output method="xml" encoding="utf-8" omit-xml-declaration="yes" indent="yes" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xpath-default-namespace="http://namespace.openaire.eu/sygma"/>
	<xsl:param name="creation_date">
		<xsl:value-of select="format-dateTime(current-dateTime(), 
		'[Y0001]/[M01]/[D01] [h01]:[m01]:[s01] [P] [z] ')"/>
	</xsl:param>
	<xsl:param name="cdata_prefix">
		<xsl:value-of select="concat('&#060;','![CDATA[&#010;')"/>
	</xsl:param>
	<xsl:param name="cdata_suffix">
		<xsl:value-of select="concat(']]&#062;','&#010;')"/>
	</xsl:param>
	<xsl:param name="type_process">oa</xsl:param>
	<xsl:param name="num_rows">100</xsl:param>
	<xsl:template match="/doc" xpath-default-namespace="http://namespace.openaire.eu/sygma">
		<xsl:variable name="oa_result_fields" xmlns="http://namespace.openaire.eu/sygma">
			<refactor_item type="oa_result_field" name="n" weight="0"/>
			<refactor_item type="oa_result_field" name="title" weight="10"/>
			<refactor_item type="oa_result_field" name="webresource" weight="11"/>
			<refactor_item type="oa_result_field" name="doi" weight="13"/>
			<refactor_item type="oa_result_field" name="openaireid" weight="14"/>
			<refactor_item type="oa_result_field" name="authors" weight="15" style="display:none;"/>
			<refactor_item type="oa_result_field" name="sourcejournal" weight="16"/>
			<refactor_item type="oa_result_field" name="publicationtype" weight="20"/>
			<refactor_item type="oa_result_field" name="bestlicense" weight="30"/>
			<refactor_item type="oa_result_field" name="dateofacceptance" weight="40"/>
			<refactor_item type="oa_result_field" name="description" weight="90" style="display:none;"/>
		</xsl:variable>
		<xsl:element name="root">
			<xsl:for-each select="@*">
				<xsl:attribute name="{local-name()}"><xsl:value-of select="."></xsl:value-of></xsl:attribute>
			</xsl:for-each>
			<xsl:for-each select="nodes/node">
				<xsl:element name="row">
					<xsl:for-each select="@*">
						<xsl:element name="{local-name()}">
							<xsl:value-of select="$cdata_prefix" disable-output-escaping="yes" />
							<xsl:value-of select="." disable-output-escaping="yes"/>
							<xsl:value-of select="$cdata_suffix" disable-output-escaping="yes"/>
						</xsl:element>
					</xsl:for-each>
				</xsl:element>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>
	<xsl:template name="mk_response_card">
		<xsl:element name="span">
			<xsl:attribute name="class">popuptext</xsl:attribute>
			<xsl:attribute name="id"><xsl:value-of select="concat('myPopUp_',position())"/></xsl:attribute>
			<xsl:element name="a">
				<xsl:attribute name="href"><xsl:value-of select="@webresource"/></xsl:attribute>
				<xsl:attribute name="target">_blank</xsl:attribute>
				<strong>
					<xsl:value-of select="@title"/>
				</strong>
			</xsl:element>
			<br/>
			<xsl:element name="div">
				<xsl:attribute name="class">popup_description</xsl:attribute>
				<xsl:value-of select="@description" disable-output-escaping="yes"/>
			</xsl:element>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
