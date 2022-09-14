<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="2.0">
    <xsl:param name="parString"></xsl:param>
    <xsl:param name="parXml"></xsl:param>
    <xsl:param name="parDomDoc"></xsl:param>
    <xsl:template match="/">
        <root>
            <parameterTypeString>
                <xsl:copy-of select="$parString" />
            </parameterTypeString>
            <parameterTypeXml>
                <xsl:copy-of select="$parXml" />
            </parameterTypeXml>
            <parameterTypeDomDoc>
                <xsl:copy-of select="$parDomDoc" />
            </parameterTypeDomDoc>
        </root>
    </xsl:template>
</xsl:stylesheet>