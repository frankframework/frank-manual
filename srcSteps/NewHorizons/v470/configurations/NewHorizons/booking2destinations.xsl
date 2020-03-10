<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <destinations>
      <xsl:apply-templates select="booking/destination">
        <xsl:with-param name="bookingId" select="booking/@id"></xsl:with-param>
      </xsl:apply-templates>
    </destinations>
  </xsl:template>
  <xsl:template match="destination">
    <xsl:param name="bookingId" />
    <destination>
      <bookingId><xsl:value-of select="$bookingId"/></bookingId>
      <seq><xsl:value-of select="position()"/></seq>
      <hostId><xsl:value-of select="@hostId"/></hostId>
      <productId><xsl:value-of select="@productId"/></productId>
      <startDate><xsl:value-of select="startDate"/></startDate>
      <endDate><xsl:value-of select="endDate"/></endDate>
      <price><xsl:value-of select="price"/></price>
    </destination>
  </xsl:template>
</xsl:stylesheet>