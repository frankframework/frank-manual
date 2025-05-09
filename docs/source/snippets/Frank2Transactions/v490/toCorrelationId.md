```xml{6, 7, 12, 13, 14, 15, 16, 17, 20}
<Configuration
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
    >
    <Adapter name="writeDb">
        <Receiver checkForDuplicates="true"
            checkForDuplicatesMethod="CORRELATIONID" correlationIDXPath="/input/@correlationId">
            <ApiListener uriPattern="/write" method="POST" allowAllParams="false"/>
            <JdbcMessageLog slotId="write-db"/>
        </Receiver>
        <Pipeline>
            <XmlInputValidator schema="input.xsd" root="input" throwException="true"></XmlInputValidator>
            <XsltPipe name="extractMessage" xpathExpression="/input/@message"></XsltPipe>
            <PutInSessionPipe name="Safe message">
                <Param name="inputMessage" />
            </PutInSessionPipe>
            <SenderPipe name="writeTableMessage" getInputFromSessionKey="inputMessage">
                <FrankSender name="writeTableMessage" target="writeTableMessage" />
            </SenderPipe>
            <EchoPipe name="originalMessage" getInputFromSessionKey="inputMessage" />
            <SenderPipe name="writeTableOtherMessage">
                <FrankSender name="writeTableOtherMessage" target="writeTableOtherMessage" />
            </SenderPipe>
        </Pipeline>
    </Adapter>
...
```
