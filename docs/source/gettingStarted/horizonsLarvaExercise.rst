Exercise: Write Larva tests to test booking.xsd
===============================================

As an exercise, please write Larva tests to test your XML Schema ``booking.xsd``. You should test the following:

* When you validate a valid booking XML like presented in section :ref:`horizonsInterfaces` against your XSD, then validation should succeed.
* Booking XML messages can have multiple destinations. Test that validation succeeds both for bookings with one destination and for bookings with two destinations.
* When you validate a booking that is invalid because there are no destinations, then validation against your XSD should fail.
* When you validate a non-xml text against your XSD, then validation should fail.

Here are a few hints:

#. If you did not do the previous sections, you can :download:`download <../downloads/configurations/NewHorizonsValidate.zip>` that work and use it as a starting point.
#. First figure out what directory to use. Remember that there is a root directory where all your configurations and all your tests are deployed. That root directory has a subdirectory ``tests``. You need to work in a subdirectory of that ``tests`` directory.
#. Remember the forward names that the ``<XmlValidatorPipe>`` defines: ``success`` and ``failure``.
#. Write a new adapter around the ``XmlValidatorPipe``. The adapter you already have may do the job now, but you will extend it later. Your new adapter should produce a meaningful output for valid bookings, invalid bookings that are valid XML and also for non-XML input messages.
#. Please review section :ref:`gettingStartedLarva`. Write a test that reads a valid booking and checks that the same message is returned as output.
#. Add additional write and read statements to do the other tests required in this exercise. You also need to write input files for these tests and files with expected output.

We provide a solution for this exercise. You should have :download:`updated your configuration <../downloads/configurations/NewHorizonsLarva.zip>` and you should have written :download:`tests <../downloads/tests/NewHorizonsLarva.zip>`