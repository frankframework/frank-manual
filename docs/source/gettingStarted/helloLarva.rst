.. _gettingStartedLarva:

Automated Tests with Larva
==========================

.. highlight:: none

Introduction
------------

This is the final section about the example Frank configs provided by the Frank!Runner. In application development, it is common to have automated tests. You cannot rely on interactive testing only, because performing these takes much more time than running automated tests. Furthermore, interactive testing is tedious work and therefore error-prone, especially when the same tests have to be performed over and over again for new releases. Automatic tests of Frank configs can be created using the Larva test tool.

Larva in action
---------------

To see what Larva is about, please try it. Please do the following:

#. Install the Frank!Runner and start it as shown in section :ref:`frankRunnerInstallation`.
#. In the main menu of the Frank!Console, expand "Testing" and select "Larva". You see the following page.

   .. image:: runLarva.jpg

#. You see you are in Larva (number 1). Select folder "Example1" (number 2). This is the same name as configuration "Example1", suggesting that these are tests of Frank config "Example1".
#. Press "start" (number 3).
#. Check that all scenarios passed (number 4).
#. Please note the subheading about "Example1\\scenario01" (number 5). There is a hierarchy. You have (nested) groups of scenarios. Each scenario should be independent, which means that the operation of one scenario should not have impact on another. Each scenario consists of steps that are dependent on each other. Scenario "Example1\\scenario01" has two steps, "step1" and "step2" (text above number 5).

Where are the test scripts?
---------------------------

To find test scripts, please do the following:

#. In the main menu, choose "Environment Variables".
#. Press Ctrl-F to search on the page. Search for ``scenariosroot``.
#. Iterate over the results until you see property "scenariosroot1.directory". Check that its value points to ``path-of-directory-franks\frank-runner\examples\Frank2Example1\tests`` (see directory structure at :ref:`frankRunnerInstallationInstallation`).

You selected subdirectory "Example1". You have verified that the test scripts you ran are in the following files: ::

     franks/frank-runner/examples/Frank2Example1/tests/Example1
     |- scenario01.properties
     |- common.properties
     |- scenario01
        |- in.txt
        |- out.txt

.. WARNING::

   It is good practice to give the tests of a Frank config the same name as the Frank config itself, and to group tests about the same Frank config together. This is not enforced in any way however.

Analysis of the test scripts
----------------------------

.. highlight:: none

File ``scenario01.properties`` reads as follows: ::

   scenario.description = Example 1

   include = common.properties

   step1.adapter.Example1.write = scenario01/in.txt
   step2.adapter.Example1.read = scenario01/out.txt

This is a properties file having the keys and the values separated by ``=``. First consider the following line: ::

   step1.adapter.Example1.write = scenario01/in.txt

The right-hand-side references file ``in.txt``. What happens with that file? To see this, you have to know that the left-hand-side consists of three components: ``step1``, ``adapter.Example1`` and ``write``. ``adapter.Example1`` is a service name. Service names always consist of two words separated by a ``.``. In ``step1`` of the scenario, file ``in.txt`` is written to this service.

Now consider the next line: ::

   step2.adapter.Example1.read = scenario01/out.txt

This line has the same syntax as its predecessor. The left-hand-side has components ``step2``, ``adapter.Example1`` and ``read``. The right-hand-side references file ``out.txt``. In ``step2`` of the scenario, data is read from service ``adapter.Example1``. The test verifies that the data equals the contents of file ``out.txt``. The contents of file ``out.txt`` is ``Hello World1``. This is the output of adapter "Example1Adapter" as you verified in section :ref:`helloTestPipeline`. This explains why the test succeeds.

How is service ``adapter.Example1`` defined? To see this, consider the following line: ::

   include = common.properties

This line speaks for itself. When the Frank!Framework interprets the test script, it replaces the line by the contents of file ``common.properties``.  File ``common.properties`` reads as follows: ::

   adapter.Example1.className=nl.nn.adapterframework.senders.IbisJavaSender
   adapter.Example1.serviceName=testtool-Example1Adapter

This means that the shown scripts are equivalent to the following: ::

   scenario.description = Example 1

   adapter.Example1.className=nl.nn.adapterframework.senders.IbisJavaSender
   adapter.Example1.serviceName=testtool-Example1Adapter

   step1.adapter.Example1.write = scenario01/in.txt
   step2.adapter.Example1.read = scenario01/out.txt

The disadvantage of that script is that the lines in ``common.properties`` cannot be reused over multiple scenarios.

Back to ``common.properties``: ::

   adapter.Example1.className=nl.nn.adapterframework.senders.IbisJavaSender
   adapter.Example1.serviceName=testtool-Example1Adapter

These lines define the service ``adapter.Example1``. Consider the first line first: ::

   adapter.Example1.className=nl.nn.adapterframework.senders.IbisJavaSender

The left-hand-side has two components, namely ``adapter.Example1`` and ``className``. This line thus defines the ``className`` property of the ``adapter.Example1`` service. The right-hand-side references Java class ``nl.nn.adapterframework.senders.IbisJavaSender``, which is part of the Java source code of the Frank!Framework. This line links the service ``adapter.Example1`` to the behavior implemented in the mentioned Java class. This class defines what other properties can be configured for the ``adapter.Example1`` service, and it defines the meaning of the ``read`` and ``write`` directives that are applied to it in ``scenario01.properties``.

Services of class ``nl.nn.adapterframework.senders.IbisJavaSender`` communicate with listeners of type ``JavaListener``. Such listeners receive their message through a direct Java call. There are other listeners, for example ``ApiListener`` which gets its message from the body of a RESTful HTTP request. Services of class ``nl.nn.adapterframework.senders.IbisJavaSender`` have an additional property ``serviceName`` that defines the name of the listener to communicate with. The second line on ``common.properties`` gives property ``serviceName`` of service ``adapter.Example1`` the value ``testtool-Example1Adapter``.

Please verify that listener ``testtool-Example1Adapter`` exists by doing the following:

#. In the main menu of the Frank!Console, select the Adapter Status page.
#. Select tab "Example1" (not shown). Then press the "Open All Adapters" button shown below:

   .. image:: larvaExpandButton.jpg

#. Scroll down until you see the following:

   .. image:: larvaReceivers.jpg

#. You see information about adapter "Example1Adapter" (number 1), the only adapter in configuration "Example1". You see a heading that indicates that the receivers of this adapter follow (number 2). There are two receivers (number 3), both having listeners of type "JavaListener" (number 4). One of these listeners is named "testtool-Example1Adapter" (number 6). This is the listener that is accessed by the Larva test. It is connected to adapter "Example1Adapter", which verifies that the Larva test indeed tests the pipeline of this adapter.

We can conclude that the Larva test does the following. It writes the contents of file ``in.txt`` to the "testtool-Example1Adapter" listener, which injects it into the pipeline of adapter "Example1Adapter". Then it reads the output of the pipeline and checks whether it equals the contents of file ``out.txt``, which is ``Hello World1``.

Stubbing
--------

Why does listener "testtool-Example1Adapter" exist? The ``Configuration.xml`` of configuration "Example1" has the following snippet:

.. code-block:: XML

   <Receiver name="Example1Receiver">
     <JavaListener name="Example1" serviceName="Example1"/>
   </Receiver>

This snippet explains the existence of listener "Example1", but not the existance of listener "testtool-Example1Adapter".

The answer can be found in the second file of configuration "Example1", namely ``StageSpecifics_LOC.properties``. This file reads as follows: ::

   stub4testtool.configuration=true

This property instructs the Frank!Framework to create stubs for some listeners and senders. This is a useful feature, because some listeners are difficult to access. For example, to access an ``<ApiListener>``, you need to set up a HTTP connection and you need to do a HTTP request. When stubbing is enabled, pipelines having an ``<ApiListener>`` in front of them automatically get an additional receiver with a ``<JavaListener>``. This allows you to make a Larva test that uses a service of class ``nl.nn.adapterframework.senders.IbisJavaSender``. That service can now access the pipeline through the new listener. Listeners of type ``<JavaListener>`` are copied in the same way when stubbing is enabled.

Stubbing has a different effect for different types of listeners and senders. Some types of listeners are replaced by their stubs instead of being copied. Other listeners are left as-is. Details are beyond the scope of this section.

How to build Larva tests
------------------------

When we reverse the above analysis of our Larva test, we arrive at a receipe to build simple Larva tests:

#. Add file ``StageSpecifics_LOC.properties`` as a brother of ``Configuration.xml``. Ensure it has the following line: ::

     stub4testtool.configuration=true

#. Reload your configuration as explained in section :ref:`frankRunnerInstallation`.
#. Go to the Adapter Status page of the Frank!Console and check whether your adapter has a JavaListener with a name that starts with "testtool".
#. If you have such a listener, you can proceed.
#. Add a file ``common.properties`` with the following contents: ::

     adapter.your-service-name.className=nl.nn.adapterframework.senders.IbisJavaSender
     adapter.your-service-name.serviceName=your-testtool-listener

   .. NOTE::

      We still have to explain how to set up your own instance of the Frank!Framework. The paths required for your test scripts are given in section :ref:`horizonsMultipleFiles`.

   .. NOTE::

      Remember that a service name consists of two words separated by a dot. It is good practice to use ``adapter`` or ``stub`` for the first word. The word ``stub`` is reserved for services that are called by the adapter that you are testing. This does not happen in this hello world example. Therefore the service name starts with ``adapter``. For more information see section :ref:`testingLarva`.

#. Now you can write your scenarios. Each scenario includes your ``common.properties`` file to have access to the service. It has write directives to write data to your service, and the pipeline behind the referenced listener. It also has read directives to the same service to get the responses from the referenced pipeline.

You can write more complicated Larva tests when you apply test services with different behavior. Such services have another value for their ``className`` property. Details will be given in a future version of the Frank!Manual.

More information about Larva is available in section :ref:`testingLarva`.