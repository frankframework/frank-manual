```xml{5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
<Configuration
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
    >
    <Adapter name="writeDbAsync">
        <Receiver checkForDuplicates="true" processResultCacheSize="0" transactionAttribute="Required">
            <ApiListener uriPattern="/write" method="POST" allowAllParams="false"/>
            <JdbcMessageLog slotId="write-db-req"/>
        </Receiver>
        <Pipeline>
            <SenderPipe name="enqueue">
                <JmsSender name="enqueue" destinationName="myQueue" messageClass="TEXT" queueConnectionFactoryName="jms/qcf-artemis"></JmsSender>
            </SenderPipe>
        </Pipeline>
    </Adapter>
    <Adapter name="writeDb">
        <Receiver transactionAttribute="Required" maxRetries="5">
            <JmsListener name="dequeue" destinationName="myQueue" messageClass="TEXT" queueConnectionFactoryName="jms/qcf-artemis" />
            <JdbcErrorStorage slotId="write-db"/>
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
