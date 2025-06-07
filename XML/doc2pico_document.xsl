<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2009 (http://www.altova.com) by s0315 (s0315) -->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<!--
==========
2021/11/25
==========
versión 0.0.1
doc2pico_document.xsl
Genera Monopágina en PicoCSS a partir de 
doc generado desde freemind de 
CustomerJourney_LuisBuscaRemedio.mm
* Usa como plantilla de PicoCSS el archivo PicoCSS_Documents.xml (versión XML del archivo de documentos de PicoCSS) 
  Archivo parámetro externo. Se accede a él con
		<xsl:copy-of select="document('')/*/my:menu/*"/>
* Usa como datos de contenido el archivo MiObservatorio_mm2doc.xml
==========
-->
	<xsl:output method="html" version="1.0" indent="yes" encoding="UTF-8"/>
	<xsl:param name="brand">Netux®</xsl:param>
	<xsl:param name="retorno">&#xA;</xsl:param>
	<xsl:param name="rssCount">13</xsl:param>
	<xsl:param name="pagename">Mi Observatorio</xsl:param>
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
				<title>
					<xsl:value-of select="concat($brand,' ',$pagename,' v',$version,'. ',$pagenamepos,' ',$fecha)"/>
				</title>
				<xsl:call-template name="mk_head"/>
				<xsl:call-template name="mk_poshead"/>
			</head>
			<body>
				<xsl:call-template name="mk_top_nav"/>
				<main class="container" id="docs">
					<xsl:call-template name="mk_aside"/>
					<xsl:call-template name="mk_documents"/>
				</main>
				<xsl:call-template name="mk_scripts">
				</xsl:call-template>
				<footer>
				</footer>
				<xsl:call-template name="mk_end_script"/>
			</body>
		</html>
	</xsl:template>
	<!-- MK_HEAD -->
	<xsl:template name="mk_head">
		<xsl:copy-of select="document('PicoCSS_Documents.xml')/html/head/*"/>
	</xsl:template>
	<!-- MK_POSHEAD -->
	<xsl:template name="mk_poshead"/>
	<!-- MK_TOP_NAV -->
	<xsl:template name="mk_top_nav">
		<nav class="container-fluid">
			<ul>
				<li>
					<a href="https://netux.com" aria-label="Back home">
						<img alt="Netux" src="icon_256.png"/>
					</a>
				</li>
				<li>
					<xsl:value-of select="$pagename"/>
				</li>
			</ul>
			<ul>
				<xsl:for-each select="node[@type='app']/node[@nav='top']/node">
					<xsl:element name="li">
						<xsl:element name="a">
							<xsl:attribute name="class">secundary</xsl:attribute>
							<xsl:attribute name="href">#<xsl:value-of select="lower-case(replace(@text,' ','_'))"/></xsl:attribute>
							<xsl:value-of select="@text"/>
						</xsl:element>
					</xsl:element>
				</xsl:for-each>
			</ul>
		</nav>
		<!--<xsl:copy-of select="document('PicoCSS_Documents.xml')/html/body/nav"/>-->
		<!--
		<nav class="container-fluid">
			<ul>
				<li>
					<a href="https://netux.com" aria-label="Back home">
						<img alt="Netux" src="icon_256.png"/>
					</a>
				</li>
				<li><xsl:value-of select="$pagename"></xsl:value-of></li>
			</ul>
			<ul>
				<li>
					<a href="https://netux.com#examples" class="secondary">Examples</a>
				</li>
				<li>
					<a href="#docs" class="secondary">Docs</a>
				</li>
				<li>
					<a href="https://github.com/netux/pico" class="contrast" aria-label="PicoCSS GitHub repository">
						<svg aria-hidden="true" focusable="false" role="img" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 496 512" height="16px">
							<path fill="currentColor" d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/>
						</svg>
					</a>
				</li>
			</ul>
		</nav>
-->
	</xsl:template>
	<!-- MK_TOP_aside -->
	<xsl:template name="mk_aside">
		<!-- format-date($date,'The [D1o] of [MNn], [YWw]') -->
		<aside>
			<nav>
				<small>@&#160;<xsl:value-of select="$fecha"/>
				</small>
				<xsl:for-each select="node[@type='app']/node[@nav='aside']/node[@type='page']">
					<details>
						<summary>
							<xsl:value-of select="@text"/>
							<xsl:if test="count(node[@type='page'])>0">&#160;&#x2192;</xsl:if>
						</summary>
						<xsl:if test="count(node[@type='page'])>0">
							<ul>
								<xsl:for-each select="node[@type='page']">
									<li>
										<xsl:element name="a">
											<xsl:attribute name="href">#<xsl:value-of select="lower-case(replace(@text,' ','_'))"/></xsl:attribute>
											<xsl:attribute name="class">secondary</xsl:attribute>
											<xsl:value-of select="@text"/>
											<xsl:if test="count(node[@type='page'])>0">&#160;&#x2192;</xsl:if>
										</xsl:element>
									</li>
								</xsl:for-each>
							</ul>
						</xsl:if>
					</details>
				</xsl:for-each>
			</nav>
		</aside>
	</xsl:template>
	<!-- MK_SCRIPTS -->
	<xsl:template name="mk_scripts"/>
	<!-- MK_END_SCRIPT -->
	<xsl:template name="mk_end_script">
		<xsl:copy-of select="document('PicoCSS_Documents.xml')/html/body/script[1]"/>
		<xsl:copy-of select="document('PicoCSS_Documents.xml')/html/body/script[2]"/>
		<!--
		<xsl:copy-of select="document('PicoCSS_Documents.xml')/html/body/footer"/>
-->
		<xsl:copy-of select="document('PicoCSS_Documents.xml')/html/body/script[3]"/>
		<!--
-->
	</xsl:template>
	<!-- MK_DOCUMENTS -->
	<xsl:template name="mk_documents">
		<div role="documents">
			<xsl:for-each select="node[@type='app']/node[@nav='aside']/node[@type='page']">
				<xsl:call-template name="mk_sections"/>
			</xsl:for-each>
		</div>
	</xsl:template>
	<!-- MK_SECTIONS -->
	<xsl:template name="mk_sections">
		<xsl:element name="section">
			<xsl:attribute name="id"><xsl:value-of select="lower-case(replace(@text,' ','_'))"></xsl:value-of></xsl:attribute>
			<h3>
				<xsl:value-of select="@text"/>
			</h3>
			<p>
				<xsl:value-of select="node[@type='description']/@text"/>
			</p>
		</xsl:element>
		<xsl:if test="count(node[@type='page'])+count(node[@type='form'])>0">
			<xsl:for-each select="node[@type='page']|node[@type='form']">
				<xsl:call-template name="mk_sections"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>
</xsl:stylesheet>
