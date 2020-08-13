<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xsl:import href="../../../configurations/printBridge/formatTableRow.xsl"/>
  <xsl:param name="columnWidths" as="xs:string*"/>
  <xsl:output method="xml" omit-xml-declaration="yes"/>
  <xsl:variable name="integerColumnWidths" as="xs:integer*">
    <xsl:for-each select="$columnWidths">
      <xsl:value-of select="round(number(.))"/>
    </xsl:for-each>
  </xsl:variable>
  <xsl:template match="/">
    <xsl:apply-templates select="row">
      <xsl:with-param name="columnWidths" select="$integerColumnWidths" as="xs:integer*"/>
    </xsl:apply-templates>
  </xsl:template>
</xsl:stylesheet>