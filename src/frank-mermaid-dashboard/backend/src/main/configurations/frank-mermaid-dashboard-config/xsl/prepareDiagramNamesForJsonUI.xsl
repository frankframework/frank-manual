<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output omit-xml-declaration="yes" method="text" media-type="text/plain"></xsl:output>
	<xsl:template match="/">
		<xsl:text>[</xsl:text>
		<xsl:for-each select="result/rowset/row/field[@name='DIAGRAMNAME']">
			<xsl:text>"</xsl:text>
			<xsl:value-of select="."/>
			<xsl:text>"</xsl:text>
			<xsl:if test="position() &lt; last()">
				<xsl:text>,</xsl:text>
			</xsl:if>
			</xsl:for-each>
		<xsl:text>]</xsl:text>
	</xsl:template>
</xsl:stylesheet>