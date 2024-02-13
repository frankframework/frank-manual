.. _testingLarvaProperties:

Properties
==========

Section :ref:`propertiesReference` explains how to use properties within Frank configurations. Can you also reference properties within Larva tests? The answer is yes, but there is a caveat.

The steps below show you how to work with properties within Larva.

#. Start from your work for section :ref:`testingLarvaServices`.
#. Introduce a property in ``Frank2Manual/classes/StageSpecifics_LOC.properties`` as shown:

   .. include:: ../../snippets/Frank2Hermes/v560/defineProperty.txt

#. Update ``Frank2Manual/tests/hermesBridge/scenario01.properties`` to reference the property:

   .. include:: ../../snippets/Frank2Hermes/v560/useProperty.txt

#. Run the Larva tests again. They should still succeed.

Here is the caveat. Larva does not know properties that are defined in layer "Configurations" shown in subsection :ref:`propertiesDeploymentEnvironment`. These are typically defined in a subdirectory of directory ``configurations``, or in a subdirectory of ``src/main/configurations`` in case of a Maven project. Only system properties and properties in layer "Frank!Framework + classes" are known.
