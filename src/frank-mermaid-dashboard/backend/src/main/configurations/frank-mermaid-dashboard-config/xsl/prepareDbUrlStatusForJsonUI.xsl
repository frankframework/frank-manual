<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<urls>
			<xsl:apply-templates select="result/rowset/row"/>
		</urls>
	</xsl:template>
	<xsl:template match="row">
		<url>
			<xsl:apply-templates select="field"/>
		</url>
	</xsl:template>
	<xsl:template match="field[@name='URL']">
		<url>
			<xsl:value-of select="text()" />
		</url>
	</xsl:template>
	<xsl:template match="field[@name='ISFAKE']">
		<isFake>
			<xsl:value-of select="text()" />
		</isFake>
	</xsl:template>
	<xsl:template match="field[@name='HTTPRESPONSEOK']">
		<httpResponseOk>
			<xsl:value-of select="text()" />
		</httpResponseOk>
	</xsl:template>
</xsl:stylesheet>