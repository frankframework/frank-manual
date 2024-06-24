```none{1, 2, 3}
<Module xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
    >
    <Adapter name="myAdapter">
        <Receiver name="myReceiver">
            <JavaListener name="myListener" serviceName="myService" />
        </Receiver>
        <Pipeline firstPipe="myPipe">
            <FixedResultPipe name="myPipe" returnString="Hello World"/>
...
```
