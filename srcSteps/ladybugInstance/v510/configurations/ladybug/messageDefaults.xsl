<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <message>
      <xsl:if test="/message[not(customer)]">
        <customer>No customer</customer>
      </xsl:if>
      <xsl:if test="/message[not(subject)]">
        <subject>No subject</subject>
      </xsl:if>
      <xsl:apply-templates select="message/*"/>
    </message>
  </xsl:template>
  <xsl:template match="*|text()">
    <xsl:copy>
      <xsl:apply-templates/>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>