.. _transform:

Transformation with XSLT
========================

In this section, we extend the ingest booking adapter of section
:ref:`insertDb`. Our aim is to not only insert into table
"booking", but also in table "visit", see :ref:`horizonsInterfaces`.
Table "visit" has a field "bookingId" that references the "id"
field of table "booking". Furthermore, the "visit" table has a
field "seq". This field should contain the sequence number
of the ``<destination>`` tag in the incoming booking XML.
We want to transform the incoming booking, such that the
values intended for each row are grouped together.

The example booking of section :ref:`horizonsInterfaces` should
be transformed to the following:

.. code-block:: XML

   <?xml version="1.0" encoding="UTF-8"?>
   <destinations>
     <destination>
       <bookingId>1</bookingId>
       <seq>1</seq>
       <hostId>3</hostId>
       <productId>4</productId>
       <startDate>2018-12-27</startDate>
       <endDate>2019-01-02</endDate>
       <price>400.00</price>
     </destination>
   </destinations>

In this example, only ``<seq>1</seq`` appears because there is only one destination.
If there were multiple destinations, the second ``<destination>`` would contain
``<seq>2</seq>``, the third would contain ``<seq>3</seq>``, etc.

This can be done with an XSLT transformation, see https://www.w3schools.com/xml/xsl_intro.asp.
The frank!framework defines a pipe ``<XsltPipe>`` that does XSLT transformations.
You can make an XSLT stylesheet "<project directory>/classes/booking2destinations.xsl"
and give it the following contents:

.. literalinclude:: ../../classes/booking2destinations.xsl
   :language: xml

Then you can append the ingest booking adapter with the following:

.. code-block:: XML

   <XsltPipe
       name="getDestinations"
       styleSheetName="booking2destinations.xsl"
       getInputFromSessionKey="originalMessage">
     <Forward name="success" path="Exit"/>
     <Forward name="failure" path="ServerError"/>
   </XsltPipe>

.. NOTE::

   The pipe shown above has attribute ``getInputFromSessionKey="originalMessage"``.
   You may remeber session keys from section :ref:`gettingStartedLadyBug`. They are
   name/value pairs that accompany the message flowing throug the pipeline.
   The ``<XsltPipe>`` should not use the output of its predecessor with
   ``name`` attribute "insertBooking". The output of that pipe is
   an XML coming from the database that expresses the result of
   the INSERT query. Session key "originalMessage" points to
   the original input message of the pipeline, which is what we need.

Finally, update the pipe with ``name`` attribute "insertBooking".
Update its "success" forward to have ``path`` "getDestinations".
