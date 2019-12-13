.. _horizonsMultipleFiles:

Configuration Management (1)
============================

We do not want to throw away the Hello World adapter explained
in section :ref:`helloIbis`, so we will have two adapters.
We use XML entity references to store our Frank in
multiple files. Each of the two adapters gets its own file,
and in Configuration.xml they are referenced.

You can make a file "<project directory>/classes/AdapterHello.xml
and copy from Configuration.xml the ``<Adapter>`` element and its
contents. This results in:

.. literalinclude:: ../../../src/gettingStartedAndDeploy/classes/AdapterHello.xml
   :language: xml

Then you can change Configuration.xml to be:

.. code-block:: XML

   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE configuration [
     <!ENTITY Hello SYSTEM "AdapterHello.xml">
     <!ENTITY IngestBooking SYSTEM "AdapterIngestBooking.xml">
   ]>
   <Configuration
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:noNamespaceSchemaLocation="./ibisdoc.xsd"
       name="Ibis4DockerExample">
     <jmsRealms>
       <jmsRealm realmName="jdbc" datasourceName="jdbc/${instance.name.lc}"/>
     </jmsRealms>
     &Hello;
     &IngestBooking;
   </Configuration>

Our New Horizons adapter, the ingest booking adapter, now appears in
"<project directory>/classes/AdapterIngestBooking.xml".
This adapter should read XML documents like the one presented in :ref:`horizonsInterfaces` and
use them to fill the data model described there.
