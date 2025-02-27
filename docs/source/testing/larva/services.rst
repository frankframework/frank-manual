.. _testingLarvaServices:

Services
========

In subsection :ref:`testingLarvaStubbing`, you learned that the Frank!Framework can alter adapters such that they can easily be unit tested. You were introduced to an example Frank "Frank2Hermes". You saw that its HTTP interfaces were replaced by a JavaListener and an IbisJavaSender, which work with direct Java calls. In this subsection you will write the test. This will introduce you to Larva services.

Defining your services
----------------------

Please start writing your Larva test by doing the following:

#. Create file ``Frank2Manual/tests/hermesBridge/common.properties`` and open it in a text editor.
#. Give this file the following contents:

   .. literalinclude:: ../../../../srcSteps/Frank2Hermes/v505/tests/hermesBridge/common.properties

You have defined a service that can interact with listener "testtool-adapterToConscience". Your service writes to a listener, so it has to be a sender. The listener is of type "JavaListener", so your sender should issue direct Java calls. Therefore, your sender needs to be of type "IbisJavaSender". To define the sender, you reference the Java class that implements it. In the Frank!Framework source code, class ``org.frankframework.senders.IbisJavaSender`` implements senders of type "IbisJavaSender".

Services are defined by assigning properties. Services of type "IbisJavaSender" have two properties, namely ``className`` and ``serviceName``. You are defining a service named ``adapter.toConscience``, so you have to set the properties ``adapter.toConscience.className`` and ``adapter.toConscience.serviceName``.

The values of these properties appear after the ``=`` sign. You already learned why the value of the ``className`` property is ``org.frankframework.senders.IbisJavaSender``. In ``serviceName`` you set the destination to which your IbisJavaSender is writing. This is the service name of the "JavaListener" you are accessing, which is ``testtool-adapterToConscience``.

3. Add your ``testtool-pipeCallConscience`` service to ``common.properties``. Extend this file as shown:

    .. include:: ../../snippets/Frank2Hermes/v510/completeCommonProperties.txt

Your service ``testtool-pipeCallConscience`` is accessed by your system under test "Frank2Hermes". "Frank2Hermes" writes to your test service, so your service should be a listener. "Frank2Hermes" calls your service through direct Java calls, so your service should be of type "JavaListener". This type of service is implemented by Java class ``org.frankframework.receivers.JavaListener``. You name your service ``stub.conscience``, so your Java class name should be the value of property ``stub.conscience.className``. This explains the first line you added.

Services of type "JavaListener" also have a property ``serviceName``, but it has a different meaning. The service name of a JavaListener identifies it for senders of type "IbisJavaSender". An IbisJavaSender references the destination to write to by the service name. We explained earlier that the Frank!Framework modified the sender within Frank2Hermes to access listener ``testtool-pipeCallConscience``. This is the ``serviceName`` we need for our service. To set the ``serviceName`` of service ``stub.conscience``, we have to set property ``stub.conscience.serviceName``. This explains the second line.

Writing your test
-----------------

Now that you have your services, you can use them to write a unit test. Please continue as follows:

4. Create file ``Frank2Manual/tests/hermesBridge/scenario01.properties`` and open it in a text editor.
#. Give this file the following contents:

   .. literalinclude:: ../../../../srcSteps/Frank2Hermes/v515/tests/hermesBridge/scenario01.properties
      :language: none

It is wise to give your scenario a description. When you have multiple tests, you will see all their descriptions when you run them. This shows you what features of your adapters are covered by your tests. When there are failing tests, the descriptions will help you to spot the issue.

Your scenario needs the services you have defined in ``common.properties``. Please do the following to include this file:

6. Extend your file ``scenario01.properties`` as shown:

   .. include:: ../../snippets/Frank2Hermes/v520/scenario01AddInclude.txt

Next, you will write a Hermes-formatted address request to your system-under-test "Frank2Hermes". This is message 1 in the figure to the bottom of the previous subsection :ref:`testingLarvaStubbing`. To the top of that subsection in Figure 1, you already saw an example Hermes-formatted address request. Please continue as follows:

7. Create file ``Frank2Manual/tests/hermesBridge/scenario01/hermesAddressRequest.xml``.
#. Fill it with the text of Figure 1 of subsection :ref:`testingLarvaStubbing`.
#. Extend your file ``scenario01.properties`` as shown:

   .. include:: ../../snippets/Frank2Hermes/v525/scenario01Message1.txt

You see a new syntax here that needs explanation. The file you are writing appears to the right of the ``=`` sign. The property name before the ``=`` sign has to: (a) command that the mentioned file is to be written; (b) specify the service that has to do the writing; and (c) specify when the write has to happen. Point (c) is expressed by the first word ``step1``. Point (b) is pressed by the next two words ``adapter.toConscience``. Point (a) is expressed by the last word ``write``.

You will continue with message 2 of the figure of subsection :ref:`testingLarvaStubbing`. Now a message is coming from your system-under-test, and you have to ``read`` this message. The ``read`` command compares the read text with the file mentiond to the right of the ``=`` sign. You test here that "Frank2Hermes" transforms a Hermes address request correctly into a Conscience address request. The reading has to be done by service ``stub.conscience`` and it is ``step2`` of your scenario. Please continue as follows:

10. Extend ``scenario01.properties`` as shown:

    .. include:: ../../snippets/Frank2Hermes/v530/scenario01Message2.txt

#. Create file ``Frank2Manual/tests/hermesBridge/scenario01/conscienceAddressRequest.xml``. Fill it with the example Conscience address request Figure 2.

You have seen all Larva syntax you need to finish your test. You need to write message 3, the response to "Frank2Hermes" that is the Conscience-formatted address. The writing has to be done by service ``stub.conscience``. Finally your test needs to read message 4, the Hermes-formatted address, comparing it with the address you expect. Please continue as follows:

12. Create file ``Frank2Manual/tests/hermesBridge/scenario01/conscienceAddressResponse.xml``. Fill it with Figure 3.
#. Create file ``Frank2Manual/tests/hermesBridge/scenario01/hermesAddressResponse.xml``. Fill it with Figure 4.
#. Finish ``scenario01.properties`` as shown:

    .. include:: ../../snippets/Frank2Hermes/v550/scenario01Complete.txt

.. _testingLarvaServicesRunningYourTest:

Running your test
-----------------

Please try your test as follows:

15. In the main menu of the Frank!Console, go to Testing | Larva. Your screen should look like shown below:

    .. image:: runRequestReplyTest.jpg

#. You see you are in Larva (number 1). Select that you want to run all your tests ("\\" in number 2) and press "start" (number 3).
#. All your tests should succeed. Please check this (see number 4).
#. A test scenario is a sequence of steps that depend on each other. You should have one scenario named "hermesBridge/scenario01". Please check that you see the decription you entered earlier.
#. You see all four steps of your scenario (number 6 shows step 1). If a step fails it becomes red, showing you where the problem occurs.

Summary of Larva syntax
-----------------------

You have seen how to write a Larva test for integrations that use the request-reply integration pattern. You have learned most of the syntax of writing Larva tests. Here is a summary:

Service definition
  Service definition lines have properties with three words, like ``service.name.propertyName``. A service name always has two words. It is good practice to use ``adapter`` or ``stub`` for the first word, making clear the role this service plays in your tests. Each service has a property ``className`` that identifies the kind of service by a Java classname. Each kind of service defines different properties.

Scenario description
  Each scenario defines property ``scenario.description``, providing a description of the scenario. This description is shown in the user interface of Larva.

Include statement
  Each scenario can include files using the syntax ``include = <file name>``. The file name is a relative path, relative to the directory of your scenario properties file (e.g. ``scenario01.properties``). You can have multiple lines like ``include =`` to include multiple files.

Test command
  Your test consists of commands like ``step<n>.service.name.<read or write> = <file name>``. The file name is either the file to write, or the file to compare with the read result. The file name is a relative path, relative to the scenario properties file.