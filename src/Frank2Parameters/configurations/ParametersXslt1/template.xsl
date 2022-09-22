<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.0"
    xmlns:fn="http://www.w3.org/2005/xpath-functions">
    <xsl:param name="parNode"></xsl:param>
    <xsl:template match="/">
        <root>
            <parameterTypeNode>
                <xsl:copy-of select="$parNode" />
            </parameterTypeNode>
        </root>
    </xsl:template>
</xsl:stylesheet>