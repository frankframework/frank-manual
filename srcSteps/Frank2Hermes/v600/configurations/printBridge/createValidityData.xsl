<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xsl:output method="xml" omit-xml-declaration="yes"/>
  <xsl:template match="/">
    <report>
      <xsl:apply-templates select="text/right"/>
      <xsl:apply-templates select="text/left"/>
    </report>
  </xsl:template>
  <xsl:template match="right">
    <numRight>
      <xsl:value-of select="count(./line)"/>
    </numRight>
    <right>
      <min>
        <xsl:value-of select="min(for $s in ./line/text() return string-length($s))"/>
      </min>
      <max>
        <xsl:value-of select="max(for $s in ./line/text() return string-length($s))"/>
      </max>
    </right>
  </xsl:template>
  <xsl:template match="left/table">
    <table>
      <xsl:variable name="numCols" as="xs:integer">
        <xsl:value-of select="max(./row/count(field))"/>
      </xsl:variable>
      <numCols><xsl:value-of select="$numCols"/></numCols>
      <xsl:variable name="table" select="." as="element(table)"/>
      <xsl:for-each select="1 to $numCols">
        <xsl:variable name="curCol" as="xs:integer">
          <xsl:value-of select="."/>
        </xsl:variable>
        <column>
          <min>
            <xsl:value-of select="min(for $x in $table/row/field[$curCol]/text() return string-length($x))"/>
          </min>
          <max>
            <xsl:value-of select="max(for $x in $table/row/field[$curCol]/text() return string-length($x))"/>
          </max>
        </column>
      </xsl:for-each>
    </table>
  </xsl:template>
</xsl:stylesheet>