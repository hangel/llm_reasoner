<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:output method="text" encoding="utf-8" omit-xml-declaration="yes" indent="yes" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xpath-default-namespace="http://namespace.openaire.eu/sygma"/>
	<xsl:template match="/doc" xpath-default-namespace="http://namespace.openaire.eu/sygma">
		<xsl:for-each select="//node/@*" xmlns="http://namespace.openaire.eu/sygma">
			<xsl:value-of select="concat(local-name(),'&#010;')"/>
		</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>
