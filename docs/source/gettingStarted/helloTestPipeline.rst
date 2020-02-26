.. _helloTestPipeline:

Run and Debug an Adapter
========================

Introduction
------------

In section :ref:`frankRunnerInstallation` you installed the Frank!Runner, a tool to quickly start the Frank!Framework. You examined the Frank!Console, which was populated with two example configs that came with the Frank!Runner. In the previous section you examined one of these in detail. It had name "Example2" and consisted of one file, ``Configuration.xml``. You saw that Frank configuration "Example2" had one adapter named "Example2Adapter". The output of that adapter was produced by a ``<FixedResultPipe>`` XML element. This element had attribute ``returnString="Hello World2"``. In this section we will run this adapter and verify that the output is "Hello World2". We will also show how to debug adapters with our debugger Ladybug.

Running with Test Pipeline
--------------------------

#. If you did not install the Frank!Runner, do so.
#. Start the Frank!Framework: ::

     franks\frank-runner> start.bat

#. Browse to http://localhost. You see the Frank!Console as explained in section :ref:`frankRunnerInstallation`.
#. In the main menu, click "Testing" to expand it.
#. In the main menu, click "Test Pipeline". You see the page shown below:

   .. image:: frankTestPipeline.jpg

The Test Pipeline screen allows you to run the pipeline within an adapter directly, disregarding the receiver of the pipeline. You need this behavior, because your receiver ``Example2Receiver`` contains a ``<JavaListener>``. Therefore you would need to call Java code to access the receiver. In general, accessing receivers is often more complicated than using the Test Pipeline page.

6. Select adapter "Example2Adapter" (number 1). Enter some arbitrary message in the Message field (number 2). Then Click "Send" (number 3).
#. Verify that the output is "Hello World2" (number 4). This is the value of the ``returnString`` attribute of the ``<FixedResultPipe>`` within adapter ``Example2Adapter``.
#. Check that to the top, you see a green bar with the word "success" (number 5). "success" is the state you configured in the ``<Exit>`` tag.
#. Select "Example1Adapter" (number 1). This adapter is very similar to "Example2Adapter" but produces a slightly different output.
#. Ensure you have some message (number 2) and press "Send" (number 3).
#. Check that the output is now "Hello World1" (number 4).

Debugging with Ladybug
----------------------

You have run the "Example2Adapter" and the "Example1Adapter". The Ladybug debugger presents detailed reports of these runs, showing for each pipe its inputs and its outputs. Please do the following to examine them:

#. In the main menu, click "Testing" and then "Ladybug". You see you are in Ladybug (number 1 in the picture below).

   .. image:: ladybugAnnotated.jpg

#. Click "Refresh" (number 2) to see the reports of running your adapters (number 3).
#. Select the uppermost line of Example2Adapter (one of the lines of number 3). The bottom-left of the page becomes as shown.

   .. image:: ladybugExample2AdapterBottomLeft.jpg

#. You have a tree view of the pipeline of the Example2Adapter. You can expand or collapse with the + or - buttons. Expand all nodes.
#. Number 1 is the input of the pipeline and number 2 is its output. Number 3 is the input of the pipe "Example" while number 4 is the output of that pipe.

   .. NOTE::

      In the tree view you see session keys (not annotated). These are used to store information that complements the incoming message, for example "tsReceived" for the time that the input message was received (timezone UTC!). If you want to learn more about Ladybug, you can study section :ref:`ladybug`. This tool also has features to automate testing.

#. Please select node number 1. The bottom-right of your page becomes as shown:

   .. image:: ladybugExample2AdapterBottomRight.jpg

#. Number 1 confirms that you are seeing the pipeline input of the Example2Adapter. Number 2 shows the arbitrary input message you entered in the Test Pipeline page.
#. Select the node annotated with number 2 in the figure of step 3. Check that the bottom-right becomes "Hello World2" as shown. This is the output you saw in the Test Pipeline page.

   .. image:: ladybugExample2AdapterBottomRightOut.jpg

#. In the figure of step 1, select the upper-most row of running adapter "Example1Adapter" (one of the lines of number 3).
#. To the bottom-left, select the output of the pipeline (number 2 in the figure of step 3).
#. Check that the output is "Hello World1" (like the figure of step 8).
