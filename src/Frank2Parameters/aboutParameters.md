# About Parameters

*This text is not published on ReadTheDocs. It is for internal use at WeAreFrank!*

On September 15 2022, WeAreFrank! is working on the Frank!Doc documentation about parameters. In particular, on the [page about Param](https://frankdoc.frankframework.org/#!/Other/Param) the explanation of the `type` attribute needs improvement. The behavior of this attribute does not match a programmer's intuition about what data types are. The files in this directory are a Frank application that demonstrates the effect of the `type` attribute. The remainder of this document explains this example and provides its output. After that, Martijn's analysis of the corresponding source code of the Frank!Framework is given. This text should clarify the confusion about the `type` attribute and it should allow discussion about further action.

### Example configuration

The example configuration [configurations/Parameters/Configuration.xml](/configurations/Parameters/Configuration.xml) does the following:

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

### Calculation of parameter values

The value of a parameter is calculated in the Java class that corrsponds with XML tag `<Param>`, namely `nl.nn.adapterframework.parameters.Parameter`. The method that calculates the value has the following signature:

```
public Object getValue(ParameterValueList alreadyResolvedParameters, Message message, PipeLineSession session, boolean namespaceAware) throws ParameterException
```

The behavior of this method can be summarized as follows (some calculations that are not relevant for analyzing `type` are omitted):

1. It calculates a raw value based `<Param>`'s attributes `value`, `sessionKey`, `sessionKeyXPath`, `pattern` and also the input message.
1. If `xpathExpression` is set, create an XSLT stylesheet that includes it.
1. If attribute `styleSheetName` or `xpathExpression` is set, apply the transformation to the raw value. A `styleSheetName` is applied as-is and for an `xpathExpression` the XSLT from the previous step is executed. Based on the `type` attribute, select a part of the result.
1. Based on the `type` attribute, convert the result so far to the desired Java type: a string, a number, a date or an XML document.

Parameters are used in many ways by the Frank!Framework. Martijn did not have the time to check every spot in the source code where parameter values are used. Only some cases of parameter usa are considered here in detail.

### XSLT 2.0 parameters

This section is about pipes and senders that perform XSLT 2.0 transformations. These pipes and senders have parameters that can have `type` value `STRING`, `XML` or `DOMDOC`. These parameters are processed in three steps:

1. The XPath expression of the parameter is transformed into an XSLT stylesheet.
1. The result of the XSLT stylesheet is truncated.
1. The result is taken as a Java String or as a DOM.

The effect of the `type` attribute can be expressed with the following table:

`type` | XPath wrapper | XML truncation | Result type
------ | ------------- | -------------- | -----------
``STRING`` | ``<xsl:value-of>`` | -
``XML`` | ``<xsl:copy-of>`` |
``DOMDOC`` | ``<xsl:copy-of>`` |