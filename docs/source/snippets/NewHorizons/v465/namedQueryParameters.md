```xml{7, 8}
...
</FixedResultPipe>
<SenderPipe
    name="insertBooking">
  <FixedQuerySender
      name="insertBookingSender"
      query="INSERT INTO booking VALUES(?{id}, ?{travelerId}, ?{price}, ?{fee})"
      useNamedParams="true"
      datasourceName="jdbc/${instance.name.lc}">
    <Param name="id" xpathExpression="/booking/@id" />
    <Param name="travelerId" xpathExpression="/booking/travelerId" />
    <Param name="price" xpathExpression="/booking/price" />
    <Param name="fee" xpathExpression="/booking/fee" />
...
```
