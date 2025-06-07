<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2009 (http://www.altova.com) by s0315 (s0315) -->
<!--
==========
2021/11/25
==========
versión 0.0.1
doc2pico.xsl
Genera Monopágina en PicoCSS a partir de 
doc generado desde freemind de 
CustomerJourney_LuisBuscaRemedio.mm
* Usa como plantilla de PicoCSS el archivo PicoCSS_Documents.xml (versión XML del archivo de documentos de PicoCSS) 
  Archivo parámetro externo. Se accede a él con
		<xsl:copy-of select="document('')/*/my:menu/*"/>
* Usa como datos de contenido el archivo MiObservatorio_mm2doc.xml
==========
-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" exclude-result-prefixes="fo xs fn">
	<xsl:output method="html" version="1.0" indent="yes" encoding="UTF-8"/>
	<xsl:param name="retorno">&#xA;</xsl:param>
	<xsl:param name="rssCount">13</xsl:param>
	<xsl:param name="pagename">Mi Observatorio</xsl:param>
	<xsl:param name="pagenamepos">MVP</xsl:param>
	<xsl:param name="version">0.0.1</xsl:param>
	<xsl:param name="tema">Salud</xsl:param>
	<xsl:param name="fecha">
		<xsl:value-of select="format-date(current-date(),'[FMn,3-3], [Y0001]/[MNn,3-3]/[D01]','de','AD','DE')"/>&#160;<xsl:value-of select="format-time(current-time(),'[H01]:[m01]  [P] [z]')"/>
	</xsl:param>
	<!--
   <xsl:value-of select="format-date(xs:date('1960-12-25'), 
                          '[D] [MNn,3-3] [Y0001]', 'de', 
                          'AD', 'DE')"/>
-->
	<xsl:template match="/doc">
		<xsl:element name="html">
			<xsl:attribute name="lang">en</xsl:attribute>
			<xsl:element name="head">
				<meta charset="UTF-8"/>
				<meta name="viewport" content="width=device-width, initial-scale=1"/>
				<meta name="description" content="A starter RSS aggregator example with elements and components used in Pico design system. Built with Pico CSS."/>
				<meta name="source" content="https://picocss.com/"/>
				<meta name="version" content="Netux"/>
				<title><xsl:value-of select="$pagename"/> v<xsl:value-of select="$version"/>. <xsl:value-of select="$pagenamepos"/></title>
				<link rel="shortcut icon" href="https://uploads-ssl.webflow.com/5d66946a1b07767aacb25958/5d7f89574cc8597b44871504_nx%20ico%2032.png" type="image/x-icon"/>
				<link rel="canonical" href="https://j.mp/nxobs"/>
				<link rel="image_src" href="https://uploads-ssl.webflow.com/5d66946a1b07767aacb25958/5d66a65a071de8b2d1f132e0_Logo%20v5%20t-n.png"/>
				<link rel="stylesheet" href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css"/>
				<style type="">
				/* Deep-orange Light scheme (Default) */
/* Can be forced with data-theme="light" */
[data-theme="light"],
:root:not([data-theme="dark"]) {
  --primary: #f4511e;
  --primary-hover: #e64a19;
  --primary-focus: rgba(244, 81, 30, 0.125);
  --primary-inverse: #FFF;
}

/* Deep-orange Dark scheme (Auto) */
/* Automatically enabled if user has Dark mode enabled */
@media only screen and (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --primary: #f4511e;
    --primary-hover: #ff5722;
    --primary-focus: rgba(244, 81, 30, 0.25);
    --primary-inverse: #FFF;
    --font-size: 14px;
  }
}

/* Deep-orange Dark scheme (Forced) */
/* Enabled if forced with data-theme="dark" */
[data-theme="dark"] {
  --primary: #f4511e;
  --primary-hover: #ff5722;
  --primary-focus: rgba(244, 81, 30, 0.25);
  --primary-inverse: #FFF;
  --font-size: 14px;
}

/* Deep-orange (Common styles) */
:root {
  --form-element-active-border-color: var(--primary);
  --form-element-focus-color: var(--primary-focus);
  --switch-color: var(--primary-inverse);
  --switch-checked-background-color: var(--primary);
  --font-size: 14px;
}
				</style>
			</xsl:element>
			<xsl:element name="body">
				<header class="container">
					<hgroup>
						<h2><xsl:value-of select="$pagename"/> v<xsl:value-of select="$version"/>. <xsl:value-of select="$pagenamepos"/></h2>
						<h3>
							<strong>Agregador de canales RSS *** DIFERENTES **** de <xsl:value-of select="upper-case($tema)"/>
							</strong>
						</h3>
						<h3>Generado el <xsl:value-of select="$fecha"/>
						</h3>
					</hgroup>
					<nav>
						<ul>
							<li>Estilo:</li>
							<li>
								<a href="#" data-theme-switcher="auto">Auto</a>
							</li>
							<li>
								<a href="#" data-theme-switcher="light">Claro</a>
							</li>
							<li>
								<a href="#" data-theme-switcher="dark">Oscuro</a>
							</li>
						</ul>
					</nav>
				</header>
				<main class="container">
					<xsl:for-each select="node[@tema!=$tema][position()&lt;=$rssCount]">
						<xsl:sort select="@tema"/>
						<xsl:call-template name="mk_details">
							<xsl:with-param name="rss_url">
								<xsl:value-of select="@rss"/>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:for-each>
				</main>
				<footer class="container">
					<small>Built with <a href="https://picocss.com">Pico</a> • <a href="https://github.com/picocss/examples/blob/master/preview/index.html">Source code</a>
					</small>
				</footer>
				<script src="https://picocss.com/examples/js/minimal-theme-switcher.js"/>
				<script>
    // Set indeterminate progress bar
    document.getElementById('progress-2').indeterminate = true;
    </script>
			</xsl:element>
		</xsl:element>
	</xsl:template>
	<!-- MK_DETAILS -->
	<xsl:template name="mk_details">
		<xsl:param name="rss_url"/>
		<xsl:variable name="rssChannel">
			<xsl:copy-of select="document($rss_url)/."/>
		</xsl:variable>
		<xsl:element name="details">
			<xsl:attribute name="id"><xsl:value-of select="concat('article_',position())"></xsl:value-of></xsl:attribute>
			<summary>
				<h4>
					<xsl:element name="a">
						<xsl:attribute name="href"><xsl:value-of select="$rss_url"/></xsl:attribute>
						<xsl:attribute name="target">_blank</xsl:attribute>
						<xsl:value-of select="concat(position(),'/',last(),': ',upper-case(@tema))"/>: <xsl:value-of select="$rssChannel/rss/channel/title" disable-output-escaping="yes"/>
					</xsl:element>
					<br/>
				</h4>
				<h5>
				ORIGINAL: <xsl:element name="a">
						<xsl:attribute name="href"><xsl:value-of select="@url"/></xsl:attribute>
						<xsl:attribute name="target">_blank</xsl:attribute>
						<xsl:value-of select="@nombre"/>&#160;
					</xsl:element>
					<xsl:value-of select="$rssChannel/rss/channel/lastBuildDate"/>&#160;
				</h5>
				<p><xsl:value-of select="$rssChannel/rss/channel/description" disable-output-escaping="yes"/></p>
			</summary>
			<ol>
				<xsl:for-each select="$rssChannel/rss/channel/item">
					<xsl:call-template name="mk_item"/>
				</xsl:for-each>
			</ol>
			<!--				<xsl:copy-of select="$rssChannel"/> -->
		</xsl:element>
	</xsl:template>
	<!-- MK_RSSCARD -->
	<!-- <xsl:value-of select="document('file:///D:/Data/Test.xml')/Report/Doc/DName"/> -->
	<xsl:template name="mk_rssCard">
		<xsl:param name="rss_url"/>
		<xsl:variable name="rssChannel">
			<xsl:copy-of select="document($rss_url)/."/>
		</xsl:variable>
		<xsl:element name="article">
			<xsl:attribute name="id"><xsl:value-of select="concat('article_',position())"></xsl:value-of></xsl:attribute>
			<h4>
				<xsl:element name="a">
					<xsl:attribute name="href"><xsl:value-of select="$rss_url"/></xsl:attribute>
					<xsl:attribute name="target">_blank</xsl:attribute>
					<xsl:value-of select="upper-case(@tema)"/>: <xsl:value-of select="$rssChannel/rss/channel/title" disable-output-escaping="yes"/>
				</xsl:element>
				<br/>
			</h4>
			<h5>
				ORIGINAL: <xsl:element name="a">
					<xsl:attribute name="href"><xsl:value-of select="@url"/></xsl:attribute>
					<xsl:attribute name="target">_blank</xsl:attribute>
					<xsl:value-of select="@nombre"/>
				</xsl:element>
			</h5>
			<ul>
				<xsl:for-each select="$rssChannel/rss/channel/item">
					<xsl:call-template name="mk_item"/>
				</xsl:for-each>
			</ul>
			<!--				<xsl:copy-of select="$rssChannel"/> -->
		</xsl:element>
	</xsl:template>
	<!-- MK_ITEM -->
	<xsl:template name="mk_item">
		<li>
			<xsl:element name="a">
				<xsl:attribute name="href"><xsl:value-of select="link"></xsl:value-of></xsl:attribute>
				<xsl:attribute name="target">_blank</xsl:attribute>
				<xsl:value-of select="title"/>
				<i style="color:#eee;">&#160;(<xsl:value-of select="pubDate"/>)</i>
			</xsl:element>
			<p>
				<xsl:value-of select="description" disable-output-escaping="yes"/>
			</p>
			<xsl:if test="count(category)>0">
				<xsl:call-template name="mk_hashtags">
				<xsl:with-param name="hashCount"><xsl:value-of select="count(category)"></xsl:value-of></xsl:with-param></xsl:call-template>
			</xsl:if>
		</li>
	</xsl:template>
	<!-- MK_HASHTAGS -->
	<xsl:template name="mk_hashtags">
	<xsl:param name="hashCount"/>
		<xsl:for-each select="category">
			<xsl:value-of select="concat('#',translate(.,' ','_'))" disable-output-escaping="yes"/><xsl:if test="position() &lt; $hashCount">, </xsl:if>
		</xsl:for-each>
	</xsl:template>
	<!-- MK_ARTICLE -->
	<xsl:template name="mk_article">
		<xsl:element name="article">
			<xsl:attribute name="id"><xsl:value-of select="concat('article_',position())"></xsl:value-of></xsl:attribute>
			<h3>
				<xsl:element name="a">
					<xsl:attribute name="href"><xsl:value-of select="node/rss/channel/link"/></xsl:attribute>
					<xsl:attribute name="target">_blank</xsl:attribute>
					<xsl:value-of select="node/rss/channel/title" disable-output-escaping="yes"/>
				</xsl:element>
			</h3>
			<figure>
				<xsl:element name="img">
					<xsl:attribute name="src"><xsl:value-of select="node/rss/channel/image/url"></xsl:value-of></xsl:attribute>
					<xsl:attribute name="alt"><xsl:value-of select="node/rss/channel/image/title"></xsl:value-of></xsl:attribute>
				</xsl:element>
				<!-- 
					<img src="https://source.unsplash.com/a562ZEFKW8I/2000x1000" alt="Minimal landscape"/>
					<a href="https://unsplash.com">unsplash.com</a>
				 -->
				<figcaption>
					<xsl:element name="a">
						<xsl:attribute name="href"><xsl:value-of select="node/rss/channel/image/link"/></xsl:attribute>Original: <xsl:value-of select="node/rss/channel/image/title"/>
					</xsl:element>
				</figcaption>
			</figure>
			<p>
				<xsl:value-of select="concat(@nombre,': ',node/rss/channel/description)"/>.</p>
			<xsl:if test="count(node/rss/channel/item)>0">
				<ul>
					<xsl:for-each select="node/rss/channel/item">
						<xsl:element name="li">
							<xsl:element name="a">
								<xsl:attribute name="href"><xsl:value-of select="link"></xsl:value-of></xsl:attribute>
								<xsl:attribute name="target">_blank</xsl:attribute>
								<xsl:value-of select="title" disable-output-escaping="yes"/>
								<br/>
							</xsl:element>
							<strong>
								<xsl:value-of select="pubDate"/>: </strong>
							<xsl:value-of select="description" disable-output-escaping="yes"/>
						</xsl:element>
					</xsl:for-each>
				</ul>
			</xsl:if>
			<footer>
				<small>
					<xsl:value-of select="node/rss/channel/image/title" disable-output-escaping="yes"/>: <xsl:value-of select="pubDate"/>
				</small>
			</footer>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>
<!--
<article>
<aside>
<details>
<figcaption>
<figure>
<footer>
<header>
<main>
<mark>
<nav>
<section>
<summary>
<time>
-->
<!--
        <title>xslt - Extract data from External XML file using XSL - Stack Overflow</title>
        <link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
        <link rel="apple-touch-icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
        <link rel="image_src" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a"> 
        <link rel="search" type="application/opensearchdescription+xml" title="Stack Overflow" href="/opensearch.xml">
        <link rel="canonical" href="https://stackoverflow.com/questions/16812192/extract-data-from-external-xml-file-using-xsl" />
        <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
        <meta property="og:type" content= "website" />
        <meta property="og:url" content="https://stackoverflow.com/questions/16812192/extract-data-from-external-xml-file-using-xsl"/>
        <meta property="og:site_name" content="Stack Overflow" />
        <meta property="og:image" itemprop="image primaryImageOfPage" content="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded" />
        <meta name="twitter:card" content="summary"/>
        <meta name="twitter:domain" content="stackoverflow.com"/>
        <meta name="twitter:title" property="og:title" itemprop="name" content="Extract data from External XML file using XSL" />
        <meta name="twitter:description" property="og:description" itemprop="description" content="I am using given below code in XSL file Both xsl and Results.xml are at same location but it cant give output.actually i want to access nodes of Results.xml file to extract data.&#xA;&#xA;&amp;lt;xsl:variable ..." />

-->
