.. _validateBooking:

Validating XML against Schema
=============================

.. highlight:: none

In this section we start coding the Frank
needed by the imaginary company New Horizons
as introduced in section :ref:`newHorizons`. In
section :ref:`horizonsInterfaces`, the requirements
for our adapter are introduced.

The ingest booking adapter
--------------------------

Before doing something with a booking XML, the ingest booking adapter
should check that this document is valid.
This can be done using an XML Schema, see
https://www.w3schools.com/xml/schema_intro.asp. You can make a document
"<project directory>/classes/booking.xsd" and give it the following contents:

.. literalinclude:: ../../../src/gettingStarted/classes/booking.xsd
   :language: xml

The frank!framework defines a pipe that checks the incoming message against
an XML Schema. Using this pipe, we can can produce an intermediate version
of the file AdapterIngestBooking.xml:

.. code-block:: XML

   <Adapter name="IngestBooking">
     <Receiver name="input">
       <ApiListener
           name="inputListener"
           uriPattern="booking"
           method="POST"/>
     </Receiver>
     <Pipeline firstPipe="checkInput">
       <Exit path="Exit" state="success" code="201" />
       <Exit path="ServerError" state="failure" code="500" />
       <XmlValidatorPipe
           name="checkInput"
           root="booking"
           schema="booking.xsd">
         <Forward name="success" path="Exit" />
         <Forward name="failure" path="makeInvalidBookingError" />
       </XmlValidatorPipe>
       <FixedResultPipe
           name="makeInvalidBookingError"
           returnString="Input booking does not satisfy booking.xsd">
         <Forward name="success" path="ServerError"/>
       </FixedResultPipe>
     </Pipeline>
   </Adapter>

This adapter starts with a ``<Receiver>`` that contains an ``<ApiListener>``.
The choice for ``<ApiListener>`` makes the adapter listen to REST HTTP requests. The attribute
``method="POST"`` makes it listen to HTTP POST requests. The ``uriPattern="booking"`` attribute
defines the relative path to which the adapter listens.
The frank!framework extends this path to be http://localhost/docker/api/booking.

After the receiver comes an ``<XmlValidatorPipe>`` . The attributes ``root`` and
``schema`` are used to reference the expected root element of the incoming
XML and to reference the XML schema file "booking.xsd" presented earlier
in this section.

In section :ref:`helloIbis`, the concept of a forward was introduced.
We see here an example of a pipe that can exit with two different
forward names. Forward name "success" is followed if the incoming XML
satisfies "booking.xsd". Otherwise, forward "failure" is followed.
This is predefined behavior of the ``<XmlValidatorPipe>`` .

The ``<Forward>`` tags link the forward names to paths. On success,
we go to the pipeline exit having path "Exit", finishing execution.
The ``<Pipeline>`` tag contains an ``<Exit>`` tag that links
path "Exit" to exit state "success" and code 201. The ``<XmlValidatorPipe>`` echos
its input message to its output message, both if validation succeeds and
if validation fails. Therefore, the output
message of the ingest booking adapter equals the incoming booking if it is valid.

For testing, it is wise to produce an error message if validation fails.
Therefore, forward name "failure" is linked to the pipe named
"makeInvalidBookingError". This pipe replaces the incoming message
by an error message. The fixed result pipe never fails and
follows its (predefined) forward name "success". That forward points to
path "ServerError", corresponding to exit state "failure" and code 500.

You can test your adapter as follows. Copy the valid booking XML to some file
on your computer, say ``validBooking.xml``. Then execute the following
Linux shell command: ::

  curl -i -X POST -H 'Content-Type: application/xml' -d @validBooking.xml http://localhost/docker/api/booking

The output will be something like the following: ::

  HTTP/1.1 201 Created
  Server: Apache-Coyote/1.1
  Last-Modified: Wed, 16 Oct 2019 12:39:06 GMT
  Cache-Control: no-store, no-cache, must-revalidate, max-age=0, post-check=0, pre-check=0
  Pragma: no-cache
  Allow: OPTIONS, POST
  Content-Type: */*;charset=UTF-8
  Content-Length: 247
  Date: Wed, 16 Oct 2019 12:39:06 GMT

  <booking id="1">  <travelerId>2</travelerId>  <price>500.00</price>  <fee>100.00</fee>  <destination hostId="3" productId="4">    <price>400.00</price>    <startDate>2018-12-27</startDate>    <endDate>2019-01-02</endDate>  </destination></booking>

The HTTP status code "201" is the ``code`` attribute defined with exit state "success".
To the bottom, you see that the incoming XML is echoed in the body of the response.

.. NOTE::

   The HTTP request includes a HTTP header "Content-Type: application/xml". You need
   this header because the ingest booking adapter uses listener ``<ApiListener>``. Use
   another listener if you want to omit the header from the request.

.. NOTE::

   The exit path "Exit" corresponds to code 201 and state "success". This exit
   state "success" does not appear in the HTTP response. You can see it
   if you use the "Test Pipeline" page in the console, see section
   :ref:`helloTestPipeline`.

You can also test what happens with an invalid input, as follows: ::

  curl -i -X POST -H 'Content-Type: application/xml' -d "xxx" http://localhost/docker/api/booking

This results in the following output: ::

  HTTP/1.1 500 Internal Server Error
  Server: Apache-Coyote/1.1
  Last-Modified: Wed, 16 Oct 2019 12:48:43 GMT
  Cache-Control: no-store, no-cache, must-revalidate, max-age=0, post-check=0, pre-check=0
  Pragma: no-cache
  Allow: OPTIONS, POST
  Content-Type: */*;charset=UTF-8
  Content-Length: 42
  Date: Wed, 16 Oct 2019 12:48:43 GMT
  Connection: close

  Input booking does not satisfy booking.xsd

From the HTTP status code 500, we see that processing exited with exit state
"failure". This exit state has path "ServerError", which is reached through
the pipe named "makeInvalidBookingError". The adapter thus detected that
the incoming message did not satisfy XML schema "booking.xsd". This is also
clear from the body of the HTTP response.
