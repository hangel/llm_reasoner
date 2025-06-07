<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2009 (http://www.altova.com) by s0315 (s0315) -->
<!-- 
## nxh_sygma2PaginatedResponsiveTable.xsl -->
<!-- 
#### 20221014

* Convert OpenAIRE Search Result converts nxh_sygma_publications_yyymmdd_hhmmss.xml
  into nxh_sygma_publications_yyymmdd_hhmmss.html
  HTML basic for Spy local test
  SOURCE: [sachinrana95/responsive_table.md](https://gist.github.com/sachinrana95/c0c54722b95f98bba0db47441a4601dd)
-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" exclude-result-prefixes="fo" xmlns="">
	<xsl:output method="html" encoding="utf-8" omit-xml-declaration="yes" indent="yes" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xpath-default-namespace="http://namespace.openaire.eu/sygma"/>
	<xsl:param name="creation_date">
		<xsl:value-of select="format-dateTime(current-dateTime(), 
		'[Y0001]/[M01]/[D01] [h01]:[m01]:[s01] [P] [z] ')"/>
	</xsl:param>
	<xsl:param name="doctype_html">
		<xsl:value-of select="concat('&#060;','DOCTYPE html&#062;&#010;')"/>
	</xsl:param>
	<xsl:param name="type_process">oa</xsl:param>
	<xsl:param name="oa_result_fields">
		<refactor_item type="oa_result_field" name="n" weight="0"/>
		<refactor_item type="oa_result_field" name="title" weight="10"/>
		<refactor_item type="oa_result_field" name="webresource" weight="11"/>
		<refactor_item type="oa_result_field" name="doi" weight="13"/>
		<refactor_item type="oa_result_field" name="openaireid" weight="14"/>
		<refactor_item type="oa_result_field" name="authors" weight="15"/>
		<refactor_item type="oa_result_field" name="sourcejournal" weight="16"/>
		<refactor_item type="oa_result_field" name="publicationtype" weight="20"/>
		<refactor_item type="oa_result_field" name="bestlicense" weight="30"/>
		<refactor_item type="oa_result_field" name="dateofacceptance" weight="40"/>
		<refactor_item type="oa_result_field" name="description" weight="90"/>
	</xsl:param>
	<xsl:template match="/doc" xpath-default-namespace="http://namespace.openaire.eu/sygma">
		<xsl:value-of select="$doctype_html" disable-output-escaping="yes"/>
		<html lang="en">
			<head>
				<meta charset="utf-8"/>
				<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
				<title>Responsive Table</title>
				<meta name="description" content="Paginated Responsive Table."/>
				<meta name="source" content="https://gist.github.com/sachinrana95/c0c54722b95f98bba0db47441a4601dd"/>
				<link href="bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet"/>
				<script src="ajax/libs/jquery/1.7.1/jquery.min.js"/>
				<link rel="stylesheet" href="ajax/libs/jquery/1.10.2/css/jquery.dataTables.min.css"/>
				<script type="text/javascript" src="ajax/libs/jquery/1.10.2/js/jquery.dataTables.min.js"/>
				<script type="text/javascript" src="bootstrap/3.2.0/js/bootstrap.min.js"/>
			</head>
			<body style="margin:20px auto">
				<div class="container">
					<div class="row header" style="text-align:center;color:green">
						<h3>
							<xsl:value-of select="concat('nxh_sygma_publications',' : ',$creation_date)"/>
						</h3>
					</div>
					<table id="openaire_result" class="table table-striped table-bordered table-responsive table-hover">
						<thead>
							<tr>
								<xsl:for-each select="/doc/nodes/node[1]/@*">
									<th>
										<xsl:value-of select="name()"/>
									</th>
								</xsl:for-each>
							</tr>
						</thead>
						<tbody>
							<xsl:for-each select="/doc/nodes/node">
								<xsl:element name="tr">
									<xsl:for-each select="@*">
										<td>
											<xsl:value-of select="."/>
										</td>
									</xsl:for-each>
								</xsl:element>
							</xsl:for-each>
						</tbody>
					</table>
				</div>
			</body>
			<script>
$(document).ready(function(){
    $('#openaire_result').dataTable();
});
</script>
		</html>
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
