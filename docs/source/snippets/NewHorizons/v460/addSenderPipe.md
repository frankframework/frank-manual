```xml{4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
...
      <Forward name="success" path="BadRequest"/>
    </EchoPipe>
    <SenderPipe
        name="insertBooking">
      <FixedQuerySender
          name="insertBookingSender"
          query="INSERT INTO booking VALUES(?, ?, ?, ?)"
          datasourceName="jdbc/${instance.name.lc}">
        <Param name="id" xpathExpression="/booking/@id" />
        <Param name="travelerId" xpathExpression="/booking/travelerId" />
        <Param name="price" xpathExpression="/booking/price" />
        <Param name="fee" xpathExpression="/booking/fee" />
      </FixedQuerySender>
      <Forward name="success" path="Exit" />
    </SenderPipe>
  </Pipeline>
</Adapter>
...
```
