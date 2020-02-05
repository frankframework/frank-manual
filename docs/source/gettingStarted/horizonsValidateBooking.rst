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
should check that this document is valid. In this section you will write a first version of the ingest booking adapter that only does that. Please do the following:

#. The validity of an XML documents is usually checked using an XML schema, see https://www.w3schools.com/xml/schema_intro.asp. Please make a document ``projects/gettingStarted/configurations/NewHorizons/booking.xsd`` and give it the following contents:

   .. literalinclude:: ../../../src/gettingStarted/configurations/NewHorizons/booking.xsd
      :language: xml

#. We will write our adapter in its own file that will be named ``ConfigurationIngestBooking.xml``. The Frank!Framework will read file ``Configuration.xml``, so that file needs to include ``ConfigurationIngestBooking.xml``. Please open ``projects/gettingStarted/configurations/NewHorizons/Configuration.xml`` and give it the following contents (highlighted lines are new):

   .. code-block:: XML
      :emphasize-lines: 4, 8

      <?xml version="1.0" encoding="UTF-8" ?>
      <!DOCTYPE configuration [
        <!ENTITY Hello SYSTEM "ConfigurationHello.xml">
        <!ENTITY IngestBooking SYSTEM "ConfigurationIngestBooking.xml">
      ]>
      <Configuration name="NewHorizons">
        &Hello;
        &IngestBooking;
      </Configuration>

#. Please create file ``projects/gettingStarted/configurations/NewHorizons/ConfigurationIngestBooking.xml``. Start editing it by putting the following contents:

   .. code-block:: XML

      <Module
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="./ibisdoc.xsd">
        <Adapter name="IngestBooking">
          <Receiver name="input">
            <ApiListener
               name="inputListener"
               uriPattern="booking"
               method="POST"/>
          </Receiver>
        </Adapter>
      </Module>

You start with a ``<Module>`` tag. It is there to satisfy XML schema ``ibisdoc.xsd``, which allows your text editor to provide automatic code completion.

This adapter starts with a ``<Receiver>`` that contains an ``<ApiListener>``.
The choice for ``<ApiListener>`` makes the adapter listen to REST HTTP requests. The attribute
``method="POST"`` makes it listen to HTTP POST requests. The ``uriPattern="booking"`` attribute
defines the relative path to which the adapter listens.
The Frank!Framework extends this path to be http://localhost/ibis/api/booking.

4. The Frank!Framework defines a pipe ``<XmlValidatorPipe>`` that checks the incoming message against an XML Schema. We use it in our adapter. Please extend ``ConfigurationIngestBooking.xml`` as follows:

.. code-block:: XML

   ...
       </Receiver>
       <Pipeline firstPipe="checkInput">
         <Exit path="Exit" state="success" code="201" />
         <Exit path="ServerError" state="failure" code="500" />
         <XmlValidatorPipe
             name="checkInput"
             root="booking"
             schema="booking.xsd">
           <Forward name="success" path="Exit" />
         </XmlValidatorPipe>
       </Pipeline>
     </Adapter>
   </Module>

The attributes ``root`` and ``schema`` are used to reference the expected root element of the incoming XML and to reference the XML schema file ``booking.xsd`` presented in step 1. A ``<Forward>`` tag links a forward name to a path. On success, we go to the pipeline exit having path ``Exit``, finishing execution. The ``<Pipeline>`` tag contains an ``<Exit>`` tag that links path ``Exit`` to exit state ``success`` and code ``201``.

5. The ``<XmlValidatorPipe>`` echos its input message to its output message, both if validation succeeds and if validation fails. We want an error message if we receive an invalid booking message. The ``<XmlValidatorPipe>`` supports another forward name ``failure`` that is followed in this case. Please extend ``ConfigurationIngestBooking.xml`` as follows:

   .. code-block:: XML
      :emphasize-lines: 7, 9, 10, 11, 12, 13

      ...
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
      </Module>

Forward name ``failure`` is linked to the pipe named ``makeInvalidBookingError``. This pipe replaces the incoming message
by an error message. The fixed result pipe never fails and follows its (predefined) forward name ``success``. That forward points to
path ``ServerError``, corresponding to exit state ``failure`` and code ``500``.

Testing (Windows)
-----------------

Your adapter listens to REST HTTP requests. If you are working under Windows, you can use Postman to send HTTP requests to your adapter. Please do the following:

#. Install Postman from https://www.getpostman.com/downloads/ if you do not have it.
#. Start Postman.
#. Go to File | Settings, select tab General.
#. Ensure that "SSL certificate verification" is not checked, see figure below:

   .. image:: postmanSettings.jpg

#. Close this dialog.
#. Select method POST (number 1 in the figure below) and type URL ``http://localhost/ibis/api/booking`` (number 2).

   .. image:: postmanUrl.jpg

#. Select tab "Headers" (number1 in the figure below). Add header ``Content-Type`` (number 2) with value ``application/xml`` (number 3) and select it (number 1):

   .. image:: postmanHeaders.jpg

#. Select tab "Body" (number 1 in the figure below).

   .. image:: postmanSend.jpg

#. In the message field (number 2), copy/paste the following XML:

   .. literalinclude:: ../../../src/gettingStarted/tests/CheckBooking/scenario01/validBooking.xml
      :language: XML

#. Press "Send" (number 3 in the figure).
#. Check the response. Go to the "Body" tab (number 1 in the figure below). You should see that the response equals the original XML message (number 2). You should have status code ``201`` (number 3).

   .. image:: postmanResponse.jpg

Testing (Linux)
---------------

Under Linux, you can test your adapter as follows:

#. Copy the valid booking XML listed above and (subsection "Testing (Windows)") to some file on your computer, say ``validBooking.xml``.
#. Execute the following Linux shell command: ::

     curl -i -X POST -H 'Content-Type: application/xml' -d @validBooking.xml http://localhost/ibis/api/booking

#. The output will be something like the following: ::

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

The HTTP status code ``201`` is the ``code`` attribute defined with exit state ``success``.
To the bottom, you see that the incoming XML is echoed in the body of the response.

Final remarks (Windows and Linux)
---------------------------------

The HTTP request includes a HTTP header ``Content-Type: application/xml``. You need this header because the ingest booking adapter uses listener ``<ApiListener>``. Use another listener if you want to omit the header from the request.

The exit path ``Exit`` corresponds to code ``201`` and state ``success``. This exit state ``success`` does not appear in the HTTP response. You can see it if you use the "Test Pipeline" page in the console, see section :ref:`helloTestPipeline`.

Please test your adapter with XML documents that do not satisfy ``booking.xsd`` or with text that is not valid XML. You should see the message ``Input booking does not satisfy booking.xsd`` and HTTP status code ``500``.

