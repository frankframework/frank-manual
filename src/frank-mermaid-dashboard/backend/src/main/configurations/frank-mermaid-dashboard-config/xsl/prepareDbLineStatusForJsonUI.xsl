<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:param name="diagramName"/>
	<xsl:template match="/">
		<lines>
			<diagramName><xsl:value-of select="$diagramName"></xsl:value-of></diagramName>
			<xsl:apply-templates select="result/rowset/row"/>
		</lines>
	</xsl:template>
	<xsl:template match="row">
		<line>
			<xsl:apply-templates select="field"/>
		</line>
	</xsl:template>
	<xsl:template match="field[@name='LINENUMBER']">
		<lineNumber>
			<xsl:value-of select="text()" />
		</lineNumber>
	</xsl:template>
	<xsl:template match="field[@name='ISOK']">
		<isOk>
			<xsl:value-of select="text()" />
		</isOk>
	</xsl:template>
	<xsl:template match="field"/>
</xsl:stylesheet>