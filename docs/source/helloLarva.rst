Console Larva
=============

This is the final page about the Hello adapter presented
in :ref:`installationLinux` . In application development,
it is common to have automated tests. You cannot rely
on interactive testing only, because performing these
takes much more time than running automated tests.
Furthermore, interactive testing is tedious work and
therefore error-prone, especially when the same
tests have to be performed over and over again
for new releases.

The frank!framework offers the Larva service that runs
automated tests. You can configure a Larva test of the 
Hello adapter as follows:

#. In the "tests" directory of your project, add a directory "Hello".
#. In the Hello directory, put a file "scenario01.properties" with the following contents. ::

   scenario.description = Hello Test, made to see how to configure Larva
   
   hello.default.className = nl.nn.adapterframework.senders.IbisJavaSender
   hello.default.serviceName = testtool-Hello
   
   step1.hello.default.write = scenario01/step01.xml
   step2.hello.default.read = scenario01/step02.txt

#. In the Hello directory, create file "scenario01/step01.xml with the following contents: ::

     <message>Hello</message>

#. In the Hello directory, create file "scenario01/step02.txt" with some text.
#. In the Adapter Status screen, press the refresh button (see the arrow)

   .. image:: reloadConfiguration.jpg

#. Run the Larva tests by pressing the Start button, as shown:

   .. image:: larvaRun.jpg

