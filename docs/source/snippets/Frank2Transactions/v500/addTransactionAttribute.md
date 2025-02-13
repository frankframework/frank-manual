```xml{6, 21, 33}
<Configuration
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
    >
    <Adapter name="writeDb">
        <Receiver checkForDuplicates="true" processResultCacheSize="0" transactionAttribute="Required">
            <ApiListener uriPattern="/write" method="POST" allowAllParams="false"/>
            <JdbcMessageLog slotId="write-db"/>
        </Receiver>
        <Pipeline>
            <SenderPipe name="writeTableMessage">
                <FrankSender name="writeTableMessage" target="writeTableMessage" />
            </SenderPipe>
            <EchoPipe name="originalMessage" getInputFromSessionKey="originalMessage" />
            <SenderPipe name="writeTableOtherMessage">
                <FrankSender name="writeTableOtherMessage" target="writeTableOtherMessage" />
            </SenderPipe>
        </Pipeline>
    </Adapter>
    <Adapter name="writeTableMessage">
        <Receiver transactionAttribute="Mandatory">
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
        <Receiver transactionAttribute="Mandatory">
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
