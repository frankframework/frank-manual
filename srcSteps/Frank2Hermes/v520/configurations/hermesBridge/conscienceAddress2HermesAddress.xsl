<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match = "/">
    <address>
      <xsl:apply-templates select="/address/id"/>
      <name>
        <xsl:apply-templates select="/address/firstName"/>
        <xsl:apply-templates select="/address/lastName"/>
      </name>
      <xsl:apply-templates select="/address/address"/>
      <xsl:apply-templates select="/address/city"/>
      <xsl:apply-templates select="/address/postalCode"/>
      <xsl:apply-templates select="/address/country"/>
    </address>
  </xsl:template>
  <xsl:template match="id">
    <relationId>
      <xsl:value-of select="."/>
    </relationId>
  </xsl:template>
  <xsl:template match="firstName">
    <xsl:copy>
      <xsl:value-of select="."/>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="lastName">
    <surName>
      <xsl:value-of select="."/>
    </surName>
  </xsl:template>
  <xsl:template match="address">
    <address>
      <street>
        <xsl:value-of select="
            substring(
              text(),
              1,
              index-of(
                string-to-codepoints(text()),
                string-to-codepoints(' ')
              )[last()] - 1)"/>
      </street>
      <houseNumber>
        <xsl:value-of select="
            substring(
              text(),
              index-of(
                string-to-codepoints(text()),
                string-to-codepoints(' ')
              )[last()] + 1)"/>
      </houseNumber>
    </address>
  </xsl:template>
  <xsl:template match="city">
    <xsl:copy>
      <xsl:value-of select="."/>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="postalCode">
    <xsl:copy>
      <dutch>
        <digids>
          <xsl:value-of select="substring(text(), 1, 4)"/>
        </digids>
        <letters>
          <xsl:value-of select="substring(text(), 6, 2)"/>
        </letters>
      </dutch>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="country">
    <xsl:copy>
      <xsl:value-of select="."/>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>