```none{25, 26, 27, 28, 29, 30}
<Configuration
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
    >
    <Adapter name="First">
        <Receiver name="First">
            <JavaListener name="First" serviceName="First" />
        </Receiver>
        <Pipeline>
            <EchoPipe name="Message" getInputFromFixedValue="Greetings from First"/>
        </Pipeline>
    </Adapter>
    <Adapter name="Second">
        <Receiver name="Second">
            <JavaListener name="Second" serviceName="Listener1b" />
        </Receiver>
        <Pipeline>
            <EchoPipe name="Message" getInputFromFixedValue="Greetings from Second"/>
        </Pipeline>
    </Adapter>
    <Monitoring>
        <SenderMonitorAdapterDestination name="TheDestination">
            <IbisJavaSender name="TheSender" serviceName="OnMonitoringTriggered"></IbisJavaSender>
        </SenderMonitorAdapterDestination>
        <Monitor name="MyMonitor" type="TECHNICAL" destinations="TheDestination">
            <AlarmTrigger severity="WARNING" period="60" threshold="2">
                <Event>Receiver Shutdown</Event>
                <Adapterfilter adapter="First" />
            </AlarmTrigger>
        </Monitor>
    </Monitoring>
</Configuration>
```
