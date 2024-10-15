```xml{12, 13, 14, 15}
...
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
    >
    <Adapter name="Client">
        <Receiver>
            <JavaListener name="client" />
        </Receiver>
        <Pipeline>
            <SenderPipe name="callServer">
                <HttpSender name="callServer"
                    urlParam="urlParam">
                    <Param name="urlParam" authAlias="myAlias"
                      pattern="http://frank-authorization-server:8080/api/server/{username}/{password}"
                      hidden="true"/>
                </HttpSender>
            </SenderPipe>
        </Pipeline>
    </Adapter>
</Configuration>
```
