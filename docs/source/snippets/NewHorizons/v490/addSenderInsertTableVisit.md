```xml
...
<FixedQuerySender
    name="insertVisitSender"
    query="INSERT INTO visit VALUES(?, ?, ?, ?, ?, ?, ?)"
    datasourceName="jdbc/${instance.name.lc}">
  <Param name="bookingId" xpathExpression="/destination/bookingId" />
  <Param name="seq" xpathExpression="/destination/seq" />
  <Param name="hostId" xpathExpression="/destination/hostId" />
  <Param name="productId" xpathExpression="/destination/productId" />
  <Param name="startDate" xpathExpression="/destination/startDate" />
  <Param name="endDate" xpathExpression="/destination/endDate" />
  <Param name="price" xpathExpression="/destination/price" />
</FixedQuerySender>
...
```
