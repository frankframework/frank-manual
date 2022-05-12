.. _advancedDevelopmentDeploymentMavenLarva:

Larva
=====

Larva is a tool to test Frank configurations in isolation, see section :ref:`testingLarva`. When property ``stub4testtool.configuration`` is true, the Frank!Framework creates stub services that can be used instead of interacting with external systems. In this section, a Larva test is added that is only available in DTAP stage ``LOC``. Larva tests are not useful in the other DTAP stages, because in those the external systems are usually available.

Here is the code for the Larva test itself:

#. Create file ``work/src/test/testtool/scenario01.properties`` with the following contents:

   .. literalinclude:: ../../../../srcSteps/Frank2Webapp/v520/src/test/testtool/scenario01.properties
      :language: none

#. Create file ``work/src/test/testtool/scenario01/in.txt`` with the following contents:

   .. literalinclude:: ../../../../srcSteps/Frank2Webapp/v520/src/test/testtool/scenario01/in.txt

#. Create file ``work/src/test/testtool/scenario01/out.txt`` with the following contents:

   .. literalinclude:: ../../../../srcSteps/Frank2Webapp/v520/src/test/testtool/scenario01/out.txt

Larva reads these files **from the file system of the host**, not the classpath! It needs a property that points to the right directory. Please do the following:

4. Create file ``work/src/main/resources/StageSpecifics_LOC.properties`` with the following contents:

   .. literalinclude:: ../../../../srcSteps/Frank2Webapp/v520/src/main/resources/StageSpecifics_LOC.properties

   Properties in this file are only applied in DTAP stage ``LOC``. See subsection :ref:`propertiesInitialization` as intended.

The Larva tests have to work independently of the path to the checkout directory. This is achieved by referencing a Maven property: ``${project.build.testSourceDirectory}``. Now we must instruct Maven to replace that property by its value.

5. Modify ``work/pom.xml`` as shown:

   .. include:: ../../snippets/Frank2Webapp/v520/pomFiltering.txt

   .. NOTE::

      This will substitute Maven properties in every file in ``work/src/main/resources``. You can organize your resources such that some are filtered and some are not. See for example `https://maven.apache.org/plugins/maven-resources-plugin/examples/filter.html <https://maven.apache.org/plugins/maven-resources-plugin/examples/filter.html>`_.

#. Verify that the Larva test can be executed by browsing to `http://localhost:8080/iaf/gui <http://localhost:8080/iaf/gui>`_ and selecting Testing | Larva in the main menu.

.. NOTE::

   The fact that the Larva tests are not read from the classpath has an interesting consequence. If you modify the Larva tests, the modifications are applied the next time that the tests are run. There is no need to reboot the application server or refresh a configuration.
