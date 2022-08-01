```xml{7, 9, 10, 11, 12, 13, 14}
...
          <Param name="id" xpathExpression="/booking/@id" />
          <Param name="travelerId" xpathExpression="/booking/travelerId" />
          <Param name="price" xpathExpression="/booking/price" />
          <Param name="fee" xpathExpression="/booking/fee" />
        </FixedQuerySender>
        <Forward name="success" path="getDestinations" />
      </SenderPipe>
      <XsltPipe
          name="getDestinations"
          styleSheetName="booking2destinations.xsl"
          getInputFromSessionKey="originalMessage">
        <Forward name="success" path="Exit"/>
      </XsltPipe>
    </Pipeline>
  </Adapter>
</Configuration>
```
