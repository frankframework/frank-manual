```xml{12, 18}
...
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
>
<Adapter name="writeDbAsync">
    <Receiver checkForDuplicates="true" processResultCacheSize="0" transactionAttribute="Required">
        <ApiListener uriPattern="/write" method="POST" />
        <JdbcMessageLog slotId="write-db-req"/>
    </Receiver>
    <Pipeline>
        <SenderPipe name="enqueue">
            <MessageStoreSender slotId="write-db"></MessageStoreSender>
        </SenderPipe>
    </Pipeline>
</Adapter>
<Adapter name="writeDb">
    <Receiver transactionAttribute="Required" maxRetries="5">
        <MessageStoreListener slotId="write-db" statusValueInProcess="I" />
    </Receiver>
    <Pipeline>
        <SenderPipe name="writeTableMessage">
            <IbisLocalSender name="writeTableMessage" javaListener="writeTableMessage" />
        </SenderPipe>
        <EchoPipe name="originalMessage" getInputFromSessionKey="originalMessage" />
        <SenderPipe name="writeTableOtherMessage">
            <IbisLocalSender name="writeTableOtherMessage" javaListener="writeTableOtherMessage" />
        </SenderPipe>
    </Pipeline>
...
```
