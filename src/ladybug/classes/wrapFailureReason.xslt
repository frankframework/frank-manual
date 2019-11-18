<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output omit-xml-declaration="yes" />
  <xsl:param name="failureReason" />
  <xsl:template match="node()">
    <result>
      <status>invalid</status>
      <message><xsl:value-of select='$failureReason' /></message>
    </result>
  </xsl:template>
</xsl:stylesheet>