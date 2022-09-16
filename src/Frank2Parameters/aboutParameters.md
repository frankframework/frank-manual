# About Parameters

*This text is not published on ReadTheDocs. It is for internal use at WeAreFrank!*

On September 15 2022, WeAreFrank! is working on the Frank!Doc documentation about parameters. In particular, on the [page about Param](https://frankdoc.frankframework.org/#!/Other/Param) the explanation of the `type` attribute needs improvement. The behavior of this attribute does not match a programmer's intuition about what data types are. The files in this directory are a Frank application that demonstrates the effect of the `type` attribute. The remainder of this document explains this example and provides its output. After that, Martijn's analysis of the corresponding source code of the Frank!Framework is given. This text should clarify the confusion about the `type` attribute and it should allow discussion about further action.

### Example configurations

There are two example configurations. The example configuration [configurations/Parameters/Configuration.xml](/configurations/Parameters/Configuration.xml) does the following:

* It executes an SQL query with a parameter.
* It executes a pipe that needs parameters with specific names.
* It executes an XSLT stylesheet with parameters.

First, the SQL query reads `INSERT INTO WithTimestamp VALUES(?)`. The parameter is of type `XMLDATETIME` and its value is `2022-09-14T15:00:00`. In file [configurations/Parameters/DatabaseChangelog.xml](/configurations/Parameters/DatabaseChangelog.xml) the manipulated database table is created (H2 database). The table being inserted has one column of data type `TIMESTAMP`.

Second, a `CompareIntegerPipe` is executed. It compares the values of parameters `operand1` and `operand2`. These parameters are considered as integers even though they do not have a `type` attribute`.

Third, the XSLT stylesheet [configurations/Parameters/template.xsl](/configurations/Parameters/template.xsl) is executed. It takes three parameters and includes their values in its output. The values are included using `<xsl:copy-of>`. In the configuration, each parameter is given the value `<xmlRoot>This is the value</xmlRoot>`, the contents of file [configurations/Parameters/fileXmlParameter.xml](/configurations/Parameters/fileXmlParameter.xml). They are passed with different `type` attributes however, namely `STRING`, `XML` and `DOMDOC`. The result is as follows:

```<?xml version="1.0" encoding="UTF-8"?>
<root xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<parameterTypeString>This is the value</parameterTypeString>
	<parameterTypeXml>&lt;xmlRoot&gt;This is the value&lt;/xmlRoot&gt;</parameterTypeXml>
	<parameterTypeDomDoc>
		<xmlRoot>This is the value</xmlRoot>
	</parameterTypeDomDoc>
</root>
```

The second example is very much like the XSLT part of the first example. The difference is that the XSLT transformation produces a node set without a common root. This does not work with `type=DOMDOC` (that case produces an error) and hence only `type=STRING` and `type=XML` are tried. The output is:

```
<?xml version="1.0" encoding="UTF-8"?>
<root xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<parameterTypeString>
        Value first child
     
        Value second child
    </parameterTypeString>
	<parameterTypeXml>&lt;xmlChild&gt;
        Value first child
    &lt;/xmlChild&gt;&lt;xmlChild&gt;
        Value second child
    &lt;/xmlChild&gt;</parameterTypeXml>
</root>
```

This comes from applying XPath expression `xmlRoot/xmlChild` to an XML document in which root element `<xmlRoot>` haw two child elements `<xmlChild>`.

### Calculation of parameter values

The value of a parameter is calculated in the Java class that corrsponds with XML tag `<Param>`, namely `nl.nn.adapterframework.parameters.Parameter`. The method that calculates the value has the following signature:

```
public Object getValue(ParameterValueList alreadyResolvedParameters, Message message, PipeLineSession session, boolean namespaceAware) throws ParameterException
```

The behavior of this method can be summarized as follows (some calculations that are not relevant for analyzing `type` are omitted):

1. It calculates a raw value based `<Param>`'s attributes `value`, `sessionKey`, `sessionKeyXPath`, `pattern` and also the input message.
1. If `xpathExpression` is set, create an XSLT stylesheet that includes it.
1. If attribute `styleSheetName` or `xpathExpression` is set, apply the transformation to the raw value. A `styleSheetName` is applied as-is and for an `xpathExpression` the XSLT from the previous step is executed.
1. Based on the `type` attribute, convert the result so far to the desired Java type: a string, a number, a date or an XML document.

Parameters are used in many ways by the Frank!Framework. Martijn did not have the time to check every spot in the source code where parameter values are used. Only some cases of parameter usa are considered here in detail.

### XSLT 2.0 parameters

This section is about pipes and senders that perform XSLT 2.0 transformations. These pipes and senders have parameters that can have `type` value `STRING`, `XML` or `DOMDOC`. In this case, the value of the `type` attribute influences the parameter's value in two ways:

1. It influences how the parameter`s XPath expression is transformed to an XSLT stylesheet.
1. It influences the Java type to which the parameter value is finally transformed.

The effect of the `type` attribute can be expressed with the following table:

`type` | XPath wrapper | Result type
------ | ------------- | -----------
``STRING`` | ``<xsl:value-of>`` | String
``XML`` | ``<xsl:copy-of>`` | String
``DOMDOC`` | ``<xsl:copy-of>`` | XML document

The consequences of this table are examined for the first example (configuration `Parameters`). For each tested value for `type`, the produced result is explained:

**STRING:** To calculate the parameter value, the string `<xmlRoot>This is the value</xmlRoot>` is transformed with XPath expression `xmlRoot`. This XPath expression is first converted to an XSLT stylesheet. That stylesheet contains something like `<xsl:value-of select="xmlRoot" />`. The XSLT element `<xsl:value-of>` selects the text inside the selected node set without the surrounding tags. This produces parameter value `This is the value`. This value is passed as a parameter when `template.xsl` is executed. The following snippet of `template.xsl` uses the parameter: `<parameterTypeString><xsl:copy-of select="$parString" /></parameterTypeString>`. The `xsl:copy-of` is applied to the parameter value and hence the parameter value is just wrapped here inside the `<parameterTypeString>` element.

**XML:** The XSLT stylesheet contains something like `<xsl:copy-of select="xmlRoot" />`. The `<xsl:copy-of>` tag takes the select result including the XML tags. This is the string `<xmlRoot>This is the value</xmlRoot>`, but that string is not passed down as an XML document. This lets the Frank!Framework escape the `<` and `>` characters by default. The parameter is applied in `template.xsl` using the snippet `<parameterTypeXml><xsl:copy-of select="$parXml" /></parameterTypeXml>`. It would not work to give this `<xsl:copy-of>` a `select` attribute, because the engine would not recognize the input as XML.

**DOMDOC:** The parameter value becomes the XML document `<xmlRoot>This is the value</xmlRoot>`. When `template.xsl` is applied, the input is an XML document that is properly formatted.

### SQL query parameters

The Frank!Framework executes SQL queries using the JDBC protocol. The Frank!Framework has to pass parameter values using setter methods defined by JDBC. The `type` attribute influences in two ways how query parameters are set:

1. The `type` attribute determines how the raw parameter value is converted into a Java object.
1. The `type` attribute determines the chosen setter method provided by the JDBC protocol. This setter has to match the data type within the underlying database engine.

It is interesting to compare `type=DATETIME` and `type=XMLDATETIME`. If a paramter has `type=DATETIME`, the raw value should match date format `yyyy-MM-dd HH:mm:ss` (according to the JavaDoc, Martijn did not test this). If the raw value matches this format, the parameter value is a Java object of type `Date`. It is passed to the underlying database engine using JDBC setter `setTimestamp()`. This will only work if the related database field has a vendor-specific data type that matches JDBC setter `setTimestamp()`.

If `type=XMLDATETIME`, the raw value should match date format that is something like `yyyy-mm-ddThh:mm:ss`. The resulting parameter value becomes a Java `Date` that is passed with JDBC setter `setTimestamp()`. The allowed database field types for Frank!Framework parameters having `type=DATETIME` or having `type=XMLDATETIME` are the same.

### A case where `type` is ignored

The `<CompareIntegerPipe>` ignores the `type` attribute of parameters. It converts everything integers and compares those. I can imagine that there are some edge cases with rounding. What if parameters of type `NUMBER` are used? Martijn would expect that these are first parsed as Java variables of type `double`. If two `double` values are different but are rounded to the same integer, the comparison may produce equality.
