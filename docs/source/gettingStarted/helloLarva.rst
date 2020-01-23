.. _gettingStartedLarva:

Console Larva
=============

This is the final section about the Hello World adapter presented
in section :ref:`helloIbis`. In application development,
it is common to have automated tests. You cannot rely
on interactive testing only, because performing these
takes much more time than running automated tests.
Furthermore, interactive testing is tedious work and
therefore error-prone, especially when the same
tests have to be performed over and over again
for new releases.

We present a tutorial here about the Larva service in which you update the example Frank studied in the previous sections. You will add a trivial Larva test to that Frank config. If you have any problems, please compare your results with the :download:`solution <../downloads/gettingStartedExample-SolutionLarva.zip>`.

Please do the following:

#. If you did not download and unzip the example Frank config, please :download:`download <../downloads/gettingStartedExample.zip>` and unzip it. In the remainder of this page, we assume you have a directory ``gettingStartedExample`` with the unzipped text.
#. Create ``gettingStartedExample/classes/StageSpecifics_LOC.properties`` with the following contents: ::

     stub4testtool.configuration=true

   This file tells the Frank!Framework to add stubs for some receivers and some senders. Details on what stubs are added exactly are beyond the scope of this Getting Started guide.

   .. NOTE::

      The Frank!Framework internally applies an XSLT stylesheet to the original Frank if ``stub4testtool.configuration`` is true. You can find it with the source code on GitHub, URL http://www.github.com/ibissource/iaf. The file you need is ``ibis-adapterframework-core/src/main/resources/xml/xsl/stub4testtool.xsl``.

   .. NOTE::

      The properties set in ``StageSpecifics_LOC.properties`` only apply in your local development environment. You use other property files for properties specific to a DTAP stage. Use ``StageSpecifics_DEV.properties`` for D, ``StageSpecifics_TST.properties`` for T,``StageSpecifics_ACC.properties`` for A and ``StageSpecifics_PRD.properties`` for P. See sub-subsection :ref:`propertiesDeploymentEnvironmentLogicalCharacteristics` for an explanation of DTAP stages.

#. Check what stubs have been created, as follows. Start the Frank!Framework using ``tomcat4ibis.bat``. Browse http://localhost/ibis/iaf/gui/. Yôu are in the Adapter Status page. Press the expand all button as shown below:

   .. image:: expandAll.jpg

#. Then enter Ctrl-F in your browser and search for "testtool". You get the following screen:

   .. image:: testtoolHello.jpg

#. Check that the HelloDockerWorld adapter now has two receivers. One of them should be named ``testtool-HelloDockerWorld``.
#. Create a text file ``gettingStartedExample/tests/Hello/scenario01.properties``. You will edit this file in the next steps. Directory ``tests`` is the directory in which all Larva tests are stored. Directory ``Hello`` groups some tests. The scenario name ``scenario01`` can be chosen freely.
#. Within your scenario, you need a service that writes to the ``testtool-HelloDockerWorld`` receiver and reads responses from it. For  historic reasons, a service has a name consisting of two words separated by a dot. Please enter the following in ``scenario01.properties``: ::

     scenario.description = Hello world test, made to see how to configure Larva

     ijs.hello.className = nl.nn.adapterframework.senders.IbisJavaSender
     ijs.hello.serviceName = testtool-HelloDockerWorld

   We choose the service name ``ijs.hello``. The string ``nl.nn.adapterframework.senders.IbisJavaSender`` is the name of a Java class within the source code of the Frank!Framework. This line thus specifies which Java class should be used to implement the test service. The line ``ijs.hello.serviceName = testtool-HelloDockerWorld`` specifies the receiver to connect to.
   
   The string ``ijs`` is an abbreviation of ``IbisJavaSender``. It is common to name the service after the Java class name being used. Alternatively, many developers write ``java`` instead of ``ijs``.

   .. NOTE::

      The next section, :ref:`horizonsMultipleFiles`, tells about another source of documentation, the Frank!Doc. You can find the name of a Java class (e.g ``nl.nn.adapterframework.senders.IbisJavaSender``) by searching a pipe, receiver or sender in the Frank!Doc and by following the "Javadoc" link you will find there.
 
#. The rest is simpler. We have to direct our service to write a message and read the response back. The read response is then compared to the expected value we configure. Please append the following to ``scenario01.properties``: ::

     step1.ijs.hello.write = scenario01/step01.xml
     step2.ijs.hello.read = scenario01/step02.txt

   .. NOTE ::

      Although we are formally writing a properties file, it is better to see this as a simple programming language. The first of these   two lines for example should be interpreted as follows. ``step1`` means this is the first step in the scenario. ``ijs.hello`` is the service name to use, defined earlier to interact with the receiver stub ``testtool-HelloDockerWorld``. ``write`` means we want to write data. On the other side of the "=" sign, we find a filename that references the data we want to write.

#. Create text file ``gettingStartedExample/tests/Hello/scenario01/step01.xml`` and give it the following contents: ::

     xxx

   This is a dummy text. Remember that our adapter applies a ``<FixedResultPipe>``, which ignores the incoming text.
#. Create text file ``gettingStartedExample/tests/Hello/scenario01/step02.txt``. This holds the expected response. Give it the following text: ::

     Hello Docker World

#. Go back to your browser with the Frank!Console. Go to the Adapter Status page using the left-hand menu.

   .. image:: adapterStatusInMenu.jpg

#. Press the refresh button shown below.

   .. image:: adapterStatusRefresh.jpg

#. Go to Larva by expanding "Testing" and then pressing Larva.

   .. image:: frankConsoleFindTestTools.jpg

#. You see you are in the Larva page (number 1 in the figure below). Enter ``/`` or ``\`` to run all tests (number 2). Press "start" (number 3).

   .. image:: runLarva.jpg

#. Check that the tests succeed (number 4).

This was the last section about the Hello World adapter. The rest of :ref:`gettingStarted`
will consider a more interesting example.
