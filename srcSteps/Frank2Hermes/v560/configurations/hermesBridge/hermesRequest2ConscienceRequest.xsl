<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match = "/">
    <addressRequest>
      <xsl:apply-templates select="/addressRequest/relationId"/>
    </addressRequest>
  </xsl:template>
  <xsl:template match="relationId">
    <id>
      <xsl:value-of select="text()"/>
    </id>
  </xsl:template>
</xsl:stylesheet>
