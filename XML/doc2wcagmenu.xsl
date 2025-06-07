<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2009 (http://www.altova.com) by s0315 (s0315) -->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<!--
==========
2021/11/30
==========
versión 0.0.1
* Revisar recursión de nivel 2 [OK]
* Revisar ADMNISTRAR > Tesauros en mm
* Integrar con 
	+ picocss
	+ cssscripts
	+ w3scholls
* Crear Blog Home
* Crear Forma para Acceso a Open Semantic Search
	+ Incialmente con iframe
	+ Buscar acceso por rss / json
==========
2021/11/29
==========
versión 0.0.1
doc2wcagmenu.xsl
Genera Navegación multinivel partir de 
doc generado desde freemind de 
CustomerJourney_LuisBuscaRemedio.mm
* Usa como plantilla wcag.xml (versión XML del archivo de documentos de multilevel.html) 
  Archivo parámetro externo. Se accede a él con
		<xsl:copy-of select="document('')/*/my:menu/*"/>
* Usa como datos de contenido el archivo MiObservatorio_mm2doc.xml
==========
-->
	<xsl:output method="html" version="1.0" indent="yes" encoding="UTF-8"/>
	<xsl:param name="brand">Netux®</xsl:param>
	<xsl:param name="retorno">&#xA;</xsl:param>
	<xsl:param name="rssCount">13</xsl:param>
	<xsl:param name="pagename">Mi Observatorio Netux®- Nav WCAG</xsl:param>
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
				<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
				<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
				<title>
					<xsl:value-of select="concat($pagename,': ',$fecha)"/>
				</title>
				<link href="https://www.cssscript.com/demo/sticky.css" rel="stylesheet" type="text/css"/>
				<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css" rel="stylesheet" type="text/css"/>
				<link href="https://www.cssscript.com/demo/responsive-multi-level-dropdown-menu-navbar/dist/main.css" rel="stylesheet" type="text/css"/>
				<link rel="preconnect" href="https://fonts.googleapis.com"/>
				<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""/>
				<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;600&amp;display=swap" rel="stylesheet"/>
				<style>
* {
  box-sizing: border-box; margin: 0; padding: 0; }
  *:focus {
    outline: 2px dotted #000;
    outline-offset: -2px;
    box-shadow: 0 0 2px 0 inset #fff; }
    *:focus:not(:focus-visible) {
      outline: none;
      box-shadow: none; }
.lead { font-size: 24px; font-weight: 300; }
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: 'Inter'; }

main {
  padding: 1rem 6rem; }

nav {
  background-color: #293345;
  color: #3bc993; }
  nav > button {
    min-width: 44px;
    min-height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: auto;
    border: 0;
    background-color: #293345;
    color: #3bc993;
    font-size: 2.5rem; }
  nav ul {
    display: none;
    margin: 0;
    padding: 0;
    background-color: #293345;
    color: #3bc993;
    list-style: none; }
    nav ul.show {
      display: grid;
      grid-auto-flow: row;
      grid-auto-rows: max-content; }
  nav a {
    min-width: 44px;
    min-height: 44px;
    display: flex;
    align-items: center;
    padding: 0.75rem 1.5rem;
    transition: background-color 150ms ease-in-out;
    color: #3bc993;
    text-decoration: none; }
    nav a:hover {
      background-color: #3bc993;
      color: #293345; }
  nav li {
    padding: 0.25rem; }
  nav li.dropdown {
    position: relative; }
    nav li.dropdown > a::after {
      content: "▼";
      display: block;
      margin-left: 0.5rem;
      transition: transform 250ms linear;
      font-size: 0.5em; }
    nav li.dropdown > a[aria-expanded="true"]::after {
      transform: rotate(-180deg); }
    nav li.dropdown ul a {
      padding-left: 2.25rem; }
    nav li.dropdown ul li.dropdown ul a {
      padding-left: 3.375rem; }

@media screen and (min-width: 1080px) {
  nav button {
    display: none; }
  nav > ul,
  nav > ul.show {
    display: grid;
    grid-auto-columns: max-content;
    grid-auto-flow: column; }
  nav .dropdown ul.show {
    position: absolute; }
  nav .dropdown ul ul {
    top: 0;
    left: 100%; } }
    </style>
				<!-- sticky -->
				<style>
 div.sticky {
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
}
</style>
			</head>
			<body style="font-family:sans;">
				<header class="sticky" style="position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;">
					<xsl:call-template name="mk_nav_container"/>
				</header>
				<main>
					<h1>
						<xsl:value-of select="concat($pagename,': ',$fecha)"/>
					</h1>
					<div style="margin:30px auto">
						<div id="carbon-block"/>
						<div>
							<style>
  h1,h2 { text-align: center; }
  h1 { margin-top: 150px; }
  </style>
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
						</div>
					</div>
				</main>
				<script type="text/javascript" src="dist/disclosure-menu.min.js"/>
				<script>
    document.addEventListener("DOMContentLoaded", () => {
  const containerElement = document.querySelector("nav");
  const controllerElement = containerElement.querySelector("button");
  const menuElement = containerElement.querySelector("ul");

  const menu = new DisclosureMenu({
    menuElement,
    submenuItemSelector: ".dropdown",
    containerElement,
    controllerElement,
    optionalKeySupport: true,
  });
});
</script>
			</body>
		</html>
	</xsl:template>
	<!-- MK_NAV_CONTAINER -->
	<xsl:template name="mk_nav_container">
		<xsl:element name="nav">
			<button id="toggle-0" aria-label="Toggle main menu">
				<a href="https://netux.com" target="_blank">
					<img alt="Netux®" src="/favicon.png" width="30px" style="text-align:left;"/>
				</a>

☰</button>
			<xsl:if test="count(/doc/node[@type='app']/node[@type='pages']/node[@type!='description'])>0">
				<ul id="menu-0">
					<li id="toggle-1">
						<a href="https://netux.com" target="_blank">
							<img alt="Netux®" src="/favicon.png" width="30px"/>
						</a>
					</li>
					<xsl:for-each select="/doc/node[@type='app']/node[@type='pages']/node[@type!='description']">
						<xsl:choose>
							<xsl:when test="count(node[@type!='description'])>0">
								<xsl:call-template name="mk_dropdown_line">
									<xsl:with-param name="menu_pos">
										<xsl:value-of select="position()"/>
									</xsl:with-param>
									<xsl:with-param name="line_pos">0</xsl:with-param>
								</xsl:call-template>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="mk_single_line">
									<xsl:with-param name="menu_pos">
										<xsl:value-of select="position()"/>
									</xsl:with-param>
									<xsl:with-param name="line_pos">0</xsl:with-param>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:for-each>
				</ul>
			</xsl:if>
		</xsl:element>
	</xsl:template>
	<!-- MK_DROPDOWN -->
	<xsl:template name="mk_dropdown_line">
		<xsl:param name="menu_pos"/>
		<xsl:param name="line_pos"/>
		<xsl:element name="li">
			<xsl:attribute name="id"><xsl:value-of select="concat('item-',$menu_pos,'-',$line_pos,'-0')"></xsl:value-of></xsl:attribute>
			<xsl:attribute name="class">dropdown</xsl:attribute>
			<xsl:element name="a">
				<xsl:attribute name="id"><xsl:value-of select="concat('link-',$menu_pos,'-',$line_pos,'-0')"></xsl:value-of></xsl:attribute>
				<xsl:attribute name="href">#</xsl:attribute>
				<xsl:value-of select="@text"/>
			</xsl:element>
			<xsl:element name="ul">
				<xsl:attribute name="id"><xsl:value-of select="concat('menu-',$menu_pos)"></xsl:value-of></xsl:attribute>
				<xsl:for-each select="node[@type!='description']">
					<xsl:choose>
						<xsl:when test="count(node[@type!='description'])>0">
							<xsl:call-template name="mk_dropdown_line">
								<xsl:with-param name="menu_pos">
									<xsl:value-of select="position()"/>
								</xsl:with-param>
								<xsl:with-param name="line_pos">0</xsl:with-param>
							</xsl:call-template>
						</xsl:when>
						<xsl:otherwise>
							<xsl:call-template name="mk_single_line">
								<xsl:with-param name="menu_pos">
									<xsl:value-of select="position()"/>
								</xsl:with-param>
								<xsl:with-param name="line_pos">0</xsl:with-param>
							</xsl:call-template>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:for-each>
			</xsl:element>
		</xsl:element>
	</xsl:template>
	<!-- MK_SINGLE_LINE -->
	<xsl:template name="mk_single_line">
		<xsl:param name="menu_pos"/>
		<xsl:param name="line_pos"/>
		<xsl:element name="li">
			<xsl:attribute name="id"><xsl:value-of select="concat('item-',$menu_pos,'-',$line_pos,'-0')"></xsl:value-of></xsl:attribute>
			<xsl:element name="a">
				<xsl:attribute name="id"><xsl:value-of select="concat('link-',$menu_pos,'-',$line_pos,'-0')"></xsl:value-of></xsl:attribute>
				<xsl:attribute name="href">#</xsl:attribute>
				<xsl:value-of select="@text"/>
			</xsl:element>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
