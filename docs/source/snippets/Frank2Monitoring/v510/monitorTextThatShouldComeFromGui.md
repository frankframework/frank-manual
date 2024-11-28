```none{17, 18, 19, 20, 21}
<Configuration
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
    >
    <Adapter name="MonitorContainer">
        <Receiver name="MonitorContainer">
            <JavaListener name="MonitorContainer" serviceName="MonitorContainer" />
        </Receiver>
        <Pipeline>
            <EchoPipe name="Message" getInputFromFixedValue="Greetings from MonitorContainer"/>
        </Pipeline>
    </Adapter>
    <Monitoring>
        <SenderMonitorAdapterDestination name="TheDestination">
            <IbisJavaSender name="TheSender" serviceName="OnMonitoringTriggered"></IbisJavaSender>
        </SenderMonitorAdapterDestination>
        <Monitor name="MyMonitor" type="TECHNICAL" destinations="TheDestination">
            <AlarmTrigger>
                <Event>Receiver Shutdown</Event>
            </AlarmTrigger>
        </Monitor>
    </Monitoring>
</Configuration>
```
