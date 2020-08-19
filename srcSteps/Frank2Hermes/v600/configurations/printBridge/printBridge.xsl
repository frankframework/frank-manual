<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <!-- <xsl:param name="statistics" as="xs:element(report)"/> -->
  <xsl:import href="formatTableRow.xsl"/>
  <xsl:param name="statistics"/>
  <xsl:template match="/">
    <document>
      <xsl:call-template name="envelope"/>
      <content>
        <xsl:apply-templates select="statementOfAccount/text/right">
          <xsl:with-param name="maxWidth" select="xs:integer(number($statistics/report/right/max))" as="xs:integer"/>
        </xsl:apply-templates>
        <line/>
        <line/>
        <xsl:apply-templates select="statementOfAccount/text/left/table/row">
          <xsl:with-param name="columnWidths" select="for $x in $statistics/report/table/column/max return xs:integer(number($x))"/>
        </xsl:apply-templates>
      </content>
    </document>
  </xsl:template>
  <xsl:template name="envelope">
    <paper>A4</paper>
    <envelope>
      <envelopeSize>A4</envelopeSize>
      <postage>0,70</postage>
      <address>
        <xsl:call-template name="envelopeAddressLines"/>
      </address>
    </envelope>
  </xsl:template>
  <xsl:template name="envelopeAddressLines">
    <xsl:for-each select="statementOfAccount/text/right/line[not(position() = 1)]">
      <line><xsl:value-of select="."/></line>
    </xsl:for-each>
  </xsl:template>
  <xsl:template match="right">
    <xsl:param name="maxWidth" as="xs:integer"/>
    <xsl:for-each select="line">
      <line>
        <xsl:attribute name="spaces">
          <xsl:value-of select="80 - $maxWidth"/>
        </xsl:attribute>
        <xsl:value-of select="."/>
      </line>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>