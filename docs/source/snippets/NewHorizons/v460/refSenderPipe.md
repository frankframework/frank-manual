```xml{4}
...
    root="booking"
    schema="booking.xsd">
  <Forward name="success" path="insertBooking" />
  <Forward name="failure" path="makeInvalidBookingError" />
</XmlValidatorPipe>
...
```
