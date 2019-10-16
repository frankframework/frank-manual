Validating XML against Schema
=============================

In this section we start coding the Frank
needed by the imaginary company New Horizons
as introduced in section :ref:`newHorizons`. In
section :ref:`horizonsInterfaces`, the requirements
for our adapter are introduced.

We do not want to throw away the Hello adapter explained
in section :ref:`helloIbis`, so we will have two adapters.
We use XML entity references to store our Frank in
multiple files. Each of the two adapters gets its own file,
and in Configuration.xml they are referenced.

You can make a file "<project directory>/classes/AdapterHello.xml
and copy from Configuration.xml the ``<adapter>`` element and its
contents. This results in:

.. literalinclude:: ../../classes/AdapterHello.xml

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
       name="ibis4manual">
     <jmsRealms>
       <jmsRealm realmName="jdbc" datasourceName="jdbc/${instance.name.lc}"/>
     </jmsRealms>
     &Hello;
     &IngestBooking;
   </Configuration>

Our New Horizons adapter, the ingest booking adapter, now appears in
"<project directory>/classes/AdapterIngestBooking.xml".
This adapter should read XML documents like the one presented in :ref:`horizonsInterfaces` and
use them to fill the data model described there. Before doing something with the XML, we want
to check that it is valid. This can be done using an XML Schema, see
https://www.w3schools.com/xml/schema_intro.asp. You can make a document
"<project directory>/classes/booking.xsd and give it the following contents:

.. literalinclude:: ../../classes/booking.xsd

The frank!framework defines a pipe that checks the incoming message against
an XML Schema. Using this pipe, we can can produce an intermediate version
of the ingest booking adapter:

.. code-block:: XML

   <adapter name="IngestBooking">
     <receiver name="input">
       <ApiListener
           name="inputListener"
           uriPattern="booking"
           method="POST"/>
     </receiver>
     <pipeline firstPipe="checkInput">
       <exits>
         <exit path="Exit" state="success" code="201" />
         <exit path="ServerError" state="failure" code="500" />
       </exits>
       <pipe className="nl.nn.adapterframework.pipes.XmlValidator"
           name="checkInput"
           root="booking"
           schema="booking.xsd">
         <forward name="success" path="Exit" />
         <forward name="failure" path="makeInvalidBookingError" />
       </pipe>
       <pipe className="nl.nn.adapterframework.pipes.FixedResult"
           name="makeInvalidBookingError"
           returnString="Input booking does not satisfy booking.xsd">
         <forward name="success" path="ServerError"/>
       </pipe>
     </pipeline>
   </adapter>

This adapter starts with a ``<receiver>`` that contains an ``<ApiListener>``.
The adapter thus listens to REST HTTP requests. The ingest booking
adapter listens to HTTP POST requests to the path "http://localhost/docker/api/booking".
See also section :ref:`helloRest`.

Then comes a pipe with the name "XmlValidator". The attributes ``root`` and
``schema`` are used to reference the expected root element of the incoming
XML and to reference the XML schema file "booking.xsd" presented earlier
in this section.

In section :ref:`helloIbis`, the concept of a forward was introduced.
We see here an example of a pipe that can exit with two different
forward names. Forward name "success" is followed if the incoming XML
satisfies "booking.xsd". Otherwise, forward "failure" is followed.
This is predefined behavior of the "XmlValidator" pipe.

The ``<forward>`` tags link the forward names to paths. On success,
we go to the pipeline exit having path "Exit", finishing execution.
The ``<pipeline>`` tag contains an ``<exit>`` tag that links
path "Exit" to exit state "success". The "XmlValidator" pipe always echos
its input message to its output message. Therefore, the output
message of the ingest booking adapter equals the incoming XML in this case.

For testing, it is wise to produce an error message if validation fails.
Therefore, forward name "failure" is linked to the pipe named
"makeInvalidBookingError". This pipe replaces the incoming message
by an error message. The "FixedResult" pipe never fails and
follows the (predefined) forward name "success". It points to path "ServerError",
corresponding to exit state "failure".
