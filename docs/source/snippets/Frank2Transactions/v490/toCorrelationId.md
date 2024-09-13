```none{6, 7, 13, 14, 15, 16, 17, 18, 21}
<Configuration
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
    >
    <Adapter name="writeDb">
        <Receiver checkForDuplicates="true"
            checkForDuplicatesMethod="CORRELATIONID" correlationIDXPath="/input/@correlationId">
            <ApiListener uriPattern="/write" method="POST" />
            <!-- <JdbcErrorStorage slotId="write-db"/> -->
            <JdbcMessageLog slotId="write-db"/>
        </Receiver>
        <Pipeline>
            <XmlInputValidator schema="input.xsd" root="input" throwException="true"></XmlInputValidator>
            <XsltPipe name="extractMessage" xpathExpression="/input/@message"></XsltPipe>
            <PutInSessionPipe name="Safe message">
                <Param name="inputMessage" />
            </PutInSessionPipe>
            <SenderPipe name="writeTableMessage" getInputFromSessionKey="inputMessage">
                <IbisLocalSender name="writeTableMessage" javaListener="writeTableMessage" />
            </SenderPipe>
            <EchoPipe name="originalMessage" getInputFromSessionKey="inputMessage" />
            <SenderPipe name="writeTableOtherMessage">
                <IbisLocalSender name="writeTableOtherMessage" javaListener="writeTableOtherMessage" />
            </SenderPipe>
        </Pipeline>
    </Adapter>
    <Adapter name="writeTableMessage">
        <Receiver>
            <JavaListener name="writeTableMessage" serviceName="writeTableMessage" />
        </Receiver>
        <Pipeline>
            <SenderPipe name="writeTableMessage">
                <FixedQuerySender query="INSERT INTO &quot;message&quot;(message) VALUES(?)">
                    <Param name="message" type="string" defaultValueMethods="input" />
                </FixedQuerySender>
            </SenderPipe>
        </Pipeline>
    </Adapter>
    <Adapter name="writeTableOtherMessage">
        <Receiver>
            <JavaListener name="writeTableOtherMessage" serviceName="writeTableOtherMessage" />
        </Receiver>
        <Pipeline>
            <SenderPipe name="writeTableOtherMessage">
                <FixedQuerySender query="INSERT INTO &quot;otherMessage&quot;(message) VALUES(?)">
                    <Param name="message" type="string" defaultValueMethods="input" />
                </FixedQuerySender>
            </SenderPipe>
        </Pipeline>
    </Adapter>
</Configuration>
```
