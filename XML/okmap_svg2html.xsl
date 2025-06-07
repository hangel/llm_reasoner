<?xml version="1.0" encoding="UTF-8"?>
<!-- 
## okmap_svg2html.xsl -->
<!-- 
#### 20221121

* Convert OKMap SVG (BASE/PubMed) 
  into OKMaps_DataSource_yyyymmdd_svg.html
  HTML basic for Spy local test
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
	<xsl:template match="/doc" xpath-default-namespace="http://namespace.openaire.eu/sygma">
		<xsl:value-of select="$doctype_html" disable-output-escaping="yes"/>
		<html>
			<head>
				<meta charset="UTF-8"/>
				<meta name="viewport" content="width=device-width, initial-scale=1"/>
				<meta name="description" content="Convert OpenAIRE Search Result converts nxh_sygma_publications_yyymmdd_hhmmss.xml"/>
				<meta name="source" content=""/>
				<title>
					<xsl:value-of select="concat('nxh_sygma_publications',' : ',$creation_date)"/>
				</title>
				<style>
:root, body {
    --mdn-color-white: #fff;
    --mdn-color-black: #000;
    --mdn-color-dark-grey: #4e4e4e;
    --mdn-background-dark: #1b1b1b;
    --mdn-background-light: #fff;
    --mdn-background-light-grey: #e2e2e2;
    --color-announcement-banner-accent: #ff6d91;
}

/* DEFAULT */
body, a, li, ul, ol {
font-family: sans;
font-size: 1.1em;
}

/* Popup container - can be anything you want */
.popup {
  position: relative;
  display: inline-block;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  margin: 10x; 
  padding: 5px; 
  border: solid 1px #aaa; 
  background-color: #f0fff0;
}

/* The actual popup */
.popup .popuptext {
  visibility: hidden;
  width: inherit;
  background-color: #ccc;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 8px 0;
  position: absolute;
  z-index: 1;
  bottom: 125%;
  left: 50%;
  top: 20px;
  bottom: 125%;
  left: 5%;
  margin-left: -80px;
}

/* PopUp Description */
.popup_description {
  background-color: #eee;
  color: #339;
  font-weight: 450;
  text-align: justify;
  margin-top: 10px;
  padding: 10px;
  width: 90%
  top: 20px;
  bottom: 125%;
  left: 5%;
  margin-left: 5%;
 }
 
 /* Popup arrow */
.popup .popuptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #555 transparent transparent transparent;
}

/* Toggle this class - hide and show the popup */
.popup .show {
  visibility: visible;
  -webkit-animation: fadeIn 1s;
  animation: fadeIn 1s;
}

/* Add animation (fade in the popup) */
@-webkit-keyframes fadeIn {
  from {opacity: 0;} 
  to {opacity: 1;}
}

@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity:1 ;}
}
</style>
</head>
<body>
				<h2>
					<xsl:value-of select="concat('nxh_sygma_publications',' : ',$creation_date)"/>
				</h2>
				<p>
					<xsl:value-of select="name()"/>
					<br/>
					<xsl:for-each select="@*">
						<xsl:value-of select="concat(name(),': ',.)"/>
						<br/>
					</xsl:for-each>
				</p>
				<ol>
					<xsl:for-each select="/doc/nodes/node">
						<xsl:element name="li">
							<xsl:attribute name="n"><xsl:value-of select="@n"/></xsl:attribute>
							<xsl:element name="div">
								<xsl:attribute name="class">popup</xsl:attribute>
								<xsl:attribute name="onclick"><xsl:value-of select="concat('myFunction(',position(),')')"></xsl:value-of></xsl:attribute>
								<xsl:attribute name="style"></xsl:attribute>
								[Detalle]&#160;<xsl:value-of select="@title"/>
								<xsl:call-template name="mk_response_card"/>
							</xsl:element>
						</xsl:element>
					</xsl:for-each>
				</ol>
				<script>
// When the user clicks on div, open the popup
function myFunction(id) {
  var popup = document.getElementById("myPopUp_"+id);
  popup.classList.toggle("show");
}
function HideFunction(id) {
  var popup = document.getElementById("myPopUp_"+id);
  popup.classList.toggle("hide");
}
</script>
			</body>
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
			<br />
			<xsl:element name="div">
			<xsl:attribute name="class">popup_description</xsl:attribute>
				<xsl:value-of select="@description" disable-output-escaping="yes"/>
			</xsl:element>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
