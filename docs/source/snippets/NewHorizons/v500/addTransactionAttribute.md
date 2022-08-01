```xml{7, 8}
...
  <ApiListener
      name="inputListener"
      uriPattern="booking"
      method="POST"/>
</Receiver>
<Pipeline firstPipe="checkInput"
    transactionAttribute="RequiresNew" >
  <Exit path="Exit" state="SUCCESS" code="201" />
  <Exit path="BadRequest" state="ERROR" code="400" />
  <XmlValidatorPipe
      name="checkInput"
      root="booking"
      schema="booking.xsd">
    <Forward name="success" path="insertBooking" />
    <Forward name="failure" path="makeInvalidBookingError" />
...
```
