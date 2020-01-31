Exercise: Write Larva tests to test booking.xsd
===============================================

As an exercise, please write Larva tests to test your XML Schema ``booking.xsd``. You should test the following:

* When you validate a valid booking XML like presented in section :ref:`horizonsInterfaces` against your XSD, then validation should succeed.
* Booking XML messages can have multiple destinations. Test that validation succeeds both for bookings with one destination and for bookings with two destinations.
* When you validate a booking that is invalid because there are no destinations, then validation against your XSD should fail.
* When you validate a non-xml text against your XSD, then validation should fail.

Here are a few hints:

#. First lookup the ``XmlValidatorPipe`` in the Frank!Doc. What forward names does it have (you may need the Javadoc link)?
#. Write an adapter around the ``XmlValidatorPipe``. It should produce a meaningful output for valid bookings, invalid bookings that are valid XML and also for non-XML input messages.
#. Please review section :ref:`gettingStartedLarva`. Write a test that reads a valid booking and checks that the same message is returned as output.
#. Add additional write and read statements to do the other tests required in this exercise. You also need to write input files for these tests and files with expected output.
