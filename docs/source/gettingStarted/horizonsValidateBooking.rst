.. _validateBooking:

Validating XML against Schema
=============================

Introduction
------------

In this section you start developing the adapter that the imaginary company New Horizons needs, continuing the case study started in section :ref:`newHorizons`. The adapter will process an XML document with a valid booking, see section :ref:`horizonsInterfaces` for an example. It will write the booking to the database tables "booking" and "visit" you created in section :ref:`databaseInitialization`. If you did not do the previous sections, you can :download:`download <../downloads/configurations/NewHorizonsDatabase.zip>` that work and continue here from your download.

The ingest booking adapter
--------------------------

Before doing something with a booking XML, the ingest booking adapter should check that this document is valid. In this section you will write a first version of the ingest booking adapter that only does that. Please do the following:

#. The validity of an XML documents is usually checked using an XML schema, see https://www.w3schools.com/xml/schema_intro.asp. Please make a document ``NewHorizons/booking.xsd`` and give it the following contents:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v430/configurations/NewHorizons/booking.xsd
      :language: xml

   .. NOTE::

      This schema does not check all possible requirements for a booking to be valid. It does not check that the start date of a visit is before its end date. More advanced checks are possible, but then you need features that are new in XML Schema version 1.1. These features are explained at https://www.altova.com/blog/what-s-new-in-xml-schema-11/. The Frank!Framework supports XML Schema 1.1, but you need a commercial text editor to use the new features. With a free text editor, you will not have syntax checking while working on your advanced XSD file.

      To have syntax checking with a free text exitor, you have to stick to XML Schema version 1.0. We do so in this tutorial.

#. Extend ``Configuration.xml`` as shown below:

   .. include:: ../snippets/NewHorizons/v420/snippetAddAdapterAndReceiver.txt

The adapter starts with a ``<Receiver>`` that contains an ``<ApiListener>``. The choice for ``<ApiListener>`` makes the adapter listen to REST HTTP requests. The attribute ``method="POST"`` makes it listen to HTTP POST requests. The ``uriPattern="booking"`` attribute defines the relative path to which the adapter listens. The Frank!Framework extends this path to be http://localhost/api/booking.

4. The Frank!Framework defines a pipe ``<XmlValidatorPipe>`` that checks the incoming message against an XML Schema. We use it in our adapter. Please update ``Configuration.xml`` as shown:

   .. include:: ../snippets/NewHorizons/v430/addPipeline.txt

The attributes ``root`` and ``schema`` are used to reference the expected root element of the incoming XML and to reference the XML schema file ``booking.xsd`` presented in step 1. A ``<Forward>`` tag links a forward name to a path. On success, we go to the pipeline exit having name ``Exit``, finishing execution. The ``<Pipeline>`` tag contains an ``<Exit>`` tag that links path ``Exit`` to exit state ``SUCCESS`` and HTTP status code ``201``.

The ``<XmlValidatorPipe>`` supports another forward name ``failure`` that is followed when validation fails. It is linked to forward name "BadRequest" at this point, corresponding to exit state ``ERROR`` and code ``400``.

5. The ``<XmlValidatorPipe>`` echos its input message to its output message, both if validation succeeds and if validation fails. We want an error message if we receive an invalid booking message. Please update ``Configuration.xml`` as follows:

   .. include:: ../snippets/NewHorizons/v440/addFixedResultInvalidBooking.txt

Forward name ``failure`` is linked to the pipe named ``makeInvalidBookingError``. This pipe replaces the incoming message by an error message. The fixed result pipe never fails and follows its (predefined) forward name ``success``. That forward points to path ``BadRequest``.

.. _validateBookingTestWindows:

Testing (Windows)
-----------------

Your adapter listens to REST HTTP requests. If you are working under Windows, you can use Postman to send HTTP requests to your adapter. Please do the following:

#. Install Postman from https://www.getpostman.com/downloads/ if you do not have it.
#. Start Postman.
#. Go to File | Settings, select tab General.
#. Ensure that "SSL certificate verification" is not checked, see figure below:

   .. image:: postmanSettings.jpg

#. Close this dialog.
#. Select method POST (number 1 in the figure below) and type URL ``http://localhost/api/booking`` (number 2).

   .. image:: postmanUrl.jpg

#. Select tab "Headers" (number1 in the figure below). Add header ``Content-Type`` (number 2) with value ``application/xml`` (number 3) and select it (number 1):

   .. image:: postmanHeaders.jpg

#. Select tab "Body" (number 1 in the figure below).

   .. image:: postmanSend.jpg

#. In the message field (number 2), copy/paste the following XML:

   .. literalinclude:: validBooking.xml
      :language: XML

#. Press "Send" (number 3 in the figure).
#. Check the response. Go to the "Body" tab (number 1 in the figure below). You should see that the response equals the original XML message (number 2). You should have status code ``201`` (number 3).

   .. image:: postmanResponse.jpg

Testing (Linux)
---------------

Under Linux, you can test your adapter as follows:

#. Copy the valid booking XML listed above (subsection :ref:`validateBookingTestWindows`) to some file on your computer, say ``validBooking.xml``.
#. Execute the following Linux shell command: ::

     curl -i -X POST -H 'Content-Type: application/xml' -d @validBooking.xml http://localhost/api/booking

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

The HTTP status code ``201`` is the ``code`` attribute defined with exit state ``SUCCESS``. To the bottom, you see that the incoming XML is echoed in the body of the response.

Final remarks (Windows and Linux)
---------------------------------

The HTTP request includes a HTTP header ``Content-Type: application/xml``. You need this header because the ingest booking adapter uses listener ``<ApiListener>``. Use another listener if you want to omit the header from the request.

The exit name ``Exit`` corresponds to code ``201`` and state ``SUCCESS``. This exit state ``SUCCESS`` does not appear in the HTTP response. You can see it if you use the "Test Pipeline" page in the console, see section :ref:`gettingStartedTestPipelines`.

Please test your adapter with XML documents that do not satisfy ``booking.xsd`` or with text that is not valid XML. You should see the message ``Input booking does not satisfy booking.xsd`` and HTTP status code ``400``.

Solution
--------

If you are having troubles, you can :download:`download <../downloads/configurations/NewHorizonsValidate.zip>` the solution for the work presented so far.