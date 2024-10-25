```xml{7}
<Configuration
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
    >
    <Adapter name="Server">
        <Receiver>
            <ApiListener name="server" uriPattern="/server/ADMIN/PASSWORD1234" />
        </Receiver>
        <Pipeline>
            <EchoPipe name="showMessage" getInputFromFixedValue="Hello World" />
        </Pipeline>
    </Adapter>
</Configuration>
```