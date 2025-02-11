```xml{4, 5, 6, 7, 8, 9, 10, 11, 12}
<Configuration
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../FrankConfig.xsd">
  <Adapter name="IngestBooking">
    <Receiver name="input">
      <ApiListener
          name="inputListener"
          uriPattern="booking"
          allowAllParams="false"
          method="POST"/>
    </Receiver>
  </Adapter>
</Configuration>
```
