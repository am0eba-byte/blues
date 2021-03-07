<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    <xsl:output method="text"/>
    <!-- 2021-03-06 ebb: XSLT to take some very weird old HTM made in 1999-2001 and output the texts of blues lyrics inside. 
    Source .HTM files scraped from https://blueslyrics.tripod.com/bluessongs1.htm
    
    Text retrieved via the following XPaths
    (//table[@border="0"]//string())[1], 
    //table[@border="0"]/following::text()[not(parent::b)][not(parent::font[@size="-1"])]
    -->
    
    <xsl:variable name="htmcoll" as="node()+" select="collection('../sourceHTM/')//body"/>
    
    <xsl:template match="body">
        <xsl:for-each select="$htmcoll">
            <xsl:value-of select="(descendant::table[@border='0']//string())[1]"/>
            
            <xsl:apply-templates select="descendant::table[@border='0']/following::text()[not(parent::b)][not(parent::font[@size='-1'])]"/>
            
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>