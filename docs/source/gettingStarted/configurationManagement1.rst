.. _horizonsMultipleFiles:

Configuration Management
========================

Introduction
------------

In subsections :ref:`helloIbis` to :ref:`gettingStartedLarva`, you got a basic understanding of the Frank!Framework. You used the Frank!Runner with its example Frank configurations to run the Frank!Framework. You learned the basic concepts by studying these configurations. You also learned how configurations can be tested.

It was explained that Frank configurations are independent of the Frank!Framework instance on which they are deployed. In this section you setup your own instance of the Frank!Framework for development, resulting in a common directory tree for everything you do while studying the Frank!Manual. You will test your setup by deploying the "Example1" configuration of the Frank!Runner on your instance. This "Example1" config has all XML in one file, namely ``Configuration.xml``. For larger Frank configs it is better to divide the XML of a config over multiple files, such that each adapter has its own XML file. You will practice this by modifying your deployment of "Example1".

.. _horizonsMultipleFilesSetUpYourInstance:

Set up your instance
--------------------

.. highlight:: none

To set up your instance, please do the following:

#. If you did not do so, install the Frank!Runner as explained in :ref:`frankRunnerInstallation`.
#. Create the root directory of your instance, ``Frank2Manual`` as a brother of your ``frank-runner`` directory. Give it two subdirectories ``configurations`` and ``tests``. You should arrive at the following directory tree: ::

     franks
     |- frank-runner
        |- examples
           |- Frank2Example1
              |- configurations
                 |- Example1
                    |- ...
                 |- ...
              |- tests
                 |- Example1
                    |- ...
                 |- ...
           |- ...
        |- ...
     |- Frank2Manual
        |- configurations
        |- tests

   .. NOTE::

      WeAreFrank! encourages you to name all your instances like "Frank2Something". You express that you are frank, honest, open to the subject of your work.

#. Create file ``franks/frank-runner/build.properties`` and give it the following contents: ::

     project.dir=Frank2Manual

#. Deploy configuration "Example1" of the Frank!Runner on your instance by copying ``franks/frank-runner/examples/Frank2Example1/configurations/Example1`` to ``franks/Frank2Manual/configurations/Example1``.
#. Deploy the corresponding tests by copying ``franks/frank-runner/examples/Frank2Example1/tests/Example1`` to ``franks/Frank2Manual/tests/Example1``. After this step, your ``Frank2Manual`` directory should look as follows: ::

     Frank2Manual
     |- configurations
        |- Example1
           |- ...
     |- tests
        |- Example1
           |- ...

#. Start the Frank!Runner as explained before. You may use ``franks/frank-runner/start.bat``.
#. Browse to http://localhost. You should see the Adapter Status page as shown:

   .. image:: configurationManagementVerifyInstance.jpg

#. Verify that the name of your instance is "Frank2Manual" (number 1).
#. Verify that you have configuration "Example1" (number 2).
#. In the main menu, expand "Testing" and select "Larva". You see the shown page:

   .. image:: runLarva.jpg

#. You see you are in Larva (number 1). Select directory "Example1" (number 2).
#. Press "start" (number 3).
#. Verify that your tests succeeded (number 5).

.. _horizonsMultipleFilesEntityReference:

Give Example1Adapter its own XML file
-------------------------------------

You will split ``Frank2Manual/configurations/Example1/Configuration.xml`` now such that each adapter gets its own file. Please do the following:

#. Create file ``Frank2Manual/configurations/Example1/ConfigurationExample1Adapter.xml``. Fill it by copying a part of ``Frank2Manual/configurations/Example1/Configuration.xml``. You need the text of the ``<Adapter>`` element, including the opening ``<Adapter>``, the closing ``</Adapter>`` and everything in between.
#. Before this text, add the following:

   .. code-block:: XML

      <Module
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="./ibisdoc.xsd">

   You need this text in the next section to have syntax checking in our text editor. It does not influence the way the Frank config works.
   
   .. NOTE::

      These lines mean the following. First comes a namespace declaration to define namespace prefix "xsi". Then the attribute "noNamespaceSchemaLocation" within namespace "http://www.w3.org/2001/XMLSchema-instance" is set to reference an XML schema file named "./ibisdoc.xsd". In the next section you will download this schema file. For more information on XML namespaces see http://www.xmlmaster.org/en/article/d01/c10/#declaration.

#. To the end, add the closing ``</Module>`` tag.

   .. WARNING..

      Do not add an ``<?xml ... ?>`` declaration. The ``ConfigurationExample1Adapter.xml`` will be included literally, which would result in invalid syntax for the total XML.

#. Replace the contents of ``Frank2Manual/configurations/Example1/Configuration.xml`` with the following:

   .. code-block:: XML

      <?xml version="1.0" encoding="UTF-8" ?>
      <!DOCTYPE configuration [
        <!ENTITY ConfigurationExample1Adapter SYSTEM "ConfigurationExample1Adapter.xml">
      ]>
      <Configuration name="Example1">
        &ConfigurationExample1Adapter;
      </Configuration>

   You see an XML entity declaration and a reference to it. For more information see https://xmlwriter.net/xml_guide/entity_declaration.shtml.

#. Refresh your configuration in the Adapter Status screen with the button annotated with number 1:

   .. image:: adapterStatusTopRight.jpg

#. Using Testing | Test Pipeline (see section :ref:`helloTestPipeline`), check that adapter "Example1Adapter" still works.
#. You can lookup the source code loaded by the Frank!Runner to check that refreshing succeeded. In the main menu, expand "Configuration" (number 1 in the figure below) and select "Show Configuration" (number 2).

   .. image:: mainMenuConfiguration.jpg

#. You see the page shown below. You get confirmation that you are on the right page (number 1). Please select the tab of configuration "Example1" (number 2).

   .. image:: configurationModifiedExample1.jpg

#. Select "Original Configuration" (number 3).
#. Check that there is a ``<Module>`` tag (number 4). The original "Example1" configuration does not have this tag, so the ``<Module>`` tag confirms that your modifications have been loaded.

   .. NOTE::

      You see here the result of replacing the entity reference ``&ConfigurationExample1Adapter;`` with the included file. The entity declaration has been removed. If file ``ConfigurationExample1Adapter.xml`` had an ``<?xml ... ?>`` declaration, then the expanded XML would have this declaration twice, corrupting the XML syntax.
