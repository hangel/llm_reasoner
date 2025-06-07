<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2009 (http://www.altova.com) by s0315 (s0315) -->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<!--
==========
2021/11/25
==========
versión 0.0.1
doc2multilevelmenu.xsl
Genera Navegación multinivel partir de 
doc generado desde freemind de 
CustomerJourney_LuisBuscaRemedio.mm
* Usa como plantilla multilevel.xml (versión XML del archivo de documentos de multilevel.html) 
  Archivo parámetro externo. Se accede a él con
		<xsl:copy-of select="document('')/*/my:menu/*"/>
* Usa como datos de contenido el archivo MiObservatorio_mm2doc.xml
==========
-->
	<xsl:output method="html" version="1.0" indent="yes" encoding="UTF-8"/>
	<xsl:param name="brand">Netux®</xsl:param>
	<xsl:param name="retorno">&#xA;</xsl:param>
	<xsl:param name="rssCount">13</xsl:param>
	<xsl:param name="pagename">Mi Observatorio - Nav Multilevel</xsl:param>
	<xsl:param name="pagenamepos">MVP</xsl:param>
	<xsl:param name="version">0.0.1</xsl:param>
	<xsl:param name="tema">Salud</xsl:param>
	<xsl:param name="fecha">
		<!--
		<xsl:value-of select="format-date(current-date(),'[FMn,3-3], [Y0001]/[MNn,3-3]/[D01]','de','AD','DE')"/>&#160;<xsl:value-of select="format-time(current-time(),'[H01]:[m01]  [P] [z]')"/>
-->
		<xsl:value-of select="format-date(current-date(),'[Y0001]/[M01]/[D01]','de','AD','DE')"/>&#160;<xsl:value-of select="format-time(current-time(),'[h01]:[m01]')"/>
	</xsl:param>
	<xsl:template match="/doc">
		<html lang="en">
			<head>
				<meta charset="UTF-8"/>
				<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
				<title>
					<xsl:value-of select="concat($pagename,': ',$fecha)"/>
				</title>
				<link href="https://www.cssscript.com/demo/sticky.css" rel="stylesheet" type="text/css"/>
				<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css" rel="stylesheet" type="text/css"/>
				<link href="https://www.cssscript.com/demo/responsive-multi-level-dropdown-menu-navbar/dist/main.css" rel="stylesheet" type="text/css"/>
				<style>
 div.sticky {
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
}
</style>
			</head>
			<body>
				<header class="sticky" style="position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;">
					<xsl:call-template name="mk_nav_container"/>
				</header>
				<style>
  h1,h2 { text-align: center; }
  h1 { margin-top: 150px; }
  </style>
				<h1>
					<xsl:value-of select="concat($pagename,': ',$fecha)"/>
				</h1>
				<div>
					<h2>Resize The Window To See How It Works On Mobile</h2>
					<hr/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<br/>
					<hr/>
					<br/>
				</div>
				<script src="https://www.cssscript.com/demo/responsive-multi-level-dropdown-menu-navbar/dist/main.js"/>
			</body>
		</html>
	</xsl:template>
	<!-- MK_NAV_CONTAINER -->
	<xsl:template name="mk_nav_container">
		<xsl:element name="div">
			<xsl:attribute name="class">nav__container</xsl:attribute>
			<!-- DIV CLASS MOBILE -->
			<xsl:element name="div">
				<xsl:attribute name="class">nav__mobile</xsl:attribute>
				<div class="nav__logo">
					<img alt="Netux" src="icon_256.png" width="30px"/>
				</div>
				<div class="nav__btn">
					<a aria-label="Nobile menu" class="nav-toggle fade">
						<span/>
						<span class="mrg"/>
						<span class="mrg"/>
					</a>
				</div>
			</xsl:element>
			<!-- DIV MENU-TOGGLE -->
			<xsl:element name="nav">
				<xsl:attribute name="class">menu-toggle</xsl:attribute>
				<ul class="nav__menu">
					<xsl:for-each select="/doc/node[@type='app']/node[@type='pages']/node[@type!='description']">
						<xsl:element name="li">
							<xsl:choose>
								<xsl:when test="count(node[@type!='description'])>0">
									<xsl:attribute name="class">dropdown</xsl:attribute>
									<xsl:element name="a">
										<xsl:attribute name="href">#</xsl:attribute>
										<xsl:value-of select="@text"/>
									</xsl:element>
									<xsl:element name="ul">
										<xsl:for-each select="node[@type!='description']">
											<xsl:element name="li">
												<xsl:element name="a">
													<xsl:attribute name="href"></xsl:attribute>
													<xsl:value-of select="@text"/>
												</xsl:element>
											</xsl:element>
										</xsl:for-each>
									</xsl:element>
								</xsl:when>
								<xsl:otherwise>
									<xsl:element name="a">
										<xsl:attribute name="href"></xsl:attribute>
										<xsl:value-of select="@text"/>
									</xsl:element>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:element>
					</xsl:for-each>
				</ul>
			</xsl:element>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
