<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:param name="columnWidths"/>
  <xsl:output method="xml" omit-xml-declaration="yes"/>
  <xsl:template match="/">
    <xsl:apply-templates select="row">
      <xsl:with-param name="columnWidths" select="$columnWidths"/>
    </xsl:apply-templates>
  </xsl:template>
  <xsl:template match="row">
    <xsl:param name="columnWidths"/>
    <line>
      <xsl:variable name="first">
        <xsl:value-of select="field[position() = 1]/text()"/>
      </xsl:variable>
      <xsl:variable name="second">
        <xsl:call-template name="padString">
          <xsl:with-param name="value" select="field[position() = 2]/text()"/>
          <xsl:with-param name="length" select="subsequence($columnWidths, 2, 1)"/>
          <xsl:with-param name="align" select="'left'"/>
        </xsl:call-template>
      </xsl:variable>
      <xsl:variable name="third">
        <xsl:call-template name="padString">
          <xsl:with-param name="value" select="field[position() = 3]/text()"/>
          <xsl:with-param name="length" select="subsequence($columnWidths, 3, 1)"/>
          <xsl:with-param name="align" select="'right'"/>
        </xsl:call-template>
      </xsl:variable>
    <xsl:value-of select="string-join(($first, $second, $third), ' ')"/>
    </line>
  </xsl:template>
  <xsl:template name="padString">
    <xsl:param name="value"/>
    <xsl:param name="length"/>
    <xsl:param name="align"/>
    <xsl:choose>
      <xsl:when test="string-length($value) &gt;= number($length)">
        <xsl:value-of select="$value"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:variable name="appended">
          <xsl:call-template name="generalAppend">
            <xsl:with-param name="in" select="$value"/>
          </xsl:call-template>
        </xsl:variable>
        <xsl:call-template name="padString">
          <xsl:with-param name="value" select="$appended/append/*[local-name()=$align]/text()"/>
          <xsl:with-param name="length" select="$length"/>
          <xsl:with-param name="align" select="$align"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <xsl:template name="generalAppend">
    <xsl:param name="in"/>
    <append>
      <left><xsl:value-of select="concat($in, ' ')"/></left>
      <right><xsl:value-of select="concat(' ', $in)"/></right>
    </append>
  </xsl:template>
</xsl:stylesheet>