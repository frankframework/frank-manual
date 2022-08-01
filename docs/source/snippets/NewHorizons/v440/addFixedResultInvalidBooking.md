```xml{7, 9, 10, 11, 12, 13}
...
      <XmlValidatorPipe
          name="checkInput"
          root="booking"
          schema="booking.xsd">
        <Forward name="success" path="Exit" />
        <Forward name="failure" path="makeInvalidBookingError" />
      </XmlValidatorPipe>
      <FixedResultPipe
          name="makeInvalidBookingError"
          returnString="Input booking does not satisfy booking.xsd">
        <Forward name="success" path="BadRequest"/>
      </FixedResultPipe>
    </Pipeline>
  </Adapter>
</Configuration>
```
