<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xsl:apply-templates select="result/rowset/row"/>
  </xsl:template>
  <xsl:template match="row">
    <message>
        <xsl:apply-templates select="field[@name='CUSTOMER']"/>
        <xsl:apply-templates select="field[@name='SUBJECT']"/>
        <xsl:apply-templates select="field[@name='MESSAGE']"/>
    </message>
  </xsl:template>
  <xsl:template match="field[@name='CUSTOMER']">
      <customer>
          <xsl:value-of select="."/>
      </customer>
  </xsl:template>
  <xsl:template match="field[@name='SUBJECT']">
    <subject>
        <xsl:value-of select="."/>
    </subject>
  </xsl:template>
  <xsl:template match="field[@name='MESSAGE']">
    <message>
        <xsl:value-of select="."/>
    </message>
  </xsl:template>
</xsl:stylesheet>
