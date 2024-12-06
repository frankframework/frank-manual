```none{8, 9, 10, 11, 12, 13}
...
        </Pipeline>
    </Adapter>
    <Monitoring>
        <Destination name="TheDestination">
            <IbisJavaSender name="TheSender" serviceName="OnMonitoringTriggered"></IbisJavaSender>
        </Destination>
        <Monitor name="MyMonitor" destinations="TheDestination">
            <AlarmTrigger severity="WARNING" period="60" threshold="2">
                <Event>Receiver Shutdown</Event>
                <Adapterfilter adapter="First" />
            </AlarmTrigger>
        </Monitor>
    </Monitoring>
</Configuration>
```
