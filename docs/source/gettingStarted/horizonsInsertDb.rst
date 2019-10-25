.. _insertDb:

Sending to Database
===================

The frank!framework can send data to external systems.
This is done by pipe ``<SenderPipe>``.
Within this pipe, you add a sender to specify the
destination. We use ``<FixedQuerySender>`` to specify
that we are targeting the database. It is not
necessary to specify what database we
target, because this is configured elsewhere, see
for example https://github.com/ibissource/docker4ibis/.

The ingest booking adapter from the previous section
:ref:`validateBooking` can be appended with the
following pipe:

.. code-block:: XML

   <SenderPipe
       name="insertBooking">
     <FixedQuerySender
         name="insertBookingSender"
         query="INSERT INTO booking VALUES(?, ?, ?, ?)"
         jmsRealm="jdbc">
       <Param name="id" xpathExpression="/booking/@id" />
       <Param name="travelerId" xpathExpression="/booking/travelerId" />
       <Param name="price" xpathExpression="/booking/price" />
       <Param name="fee" xpathExpression="/booking/fee" />
     </FixedQuerySender>
     <Forward name="success" path="Exit" />
     <Forward name="failure" path="ServerError" />
   </SenderPipe>

You see that we send an INSERT query to the database with parameters.
The parameters appear with question marks in the SQL statement.
The values of the parameters are provided through XPath expressions.
These XPath expressions are applied to the incoming message. Xpath is
explained here: https://www.w3schools.com/xml/xpath_intro.asp.

As it stands, the added pipe is never reached. Before this works,
the "success" forward of the pipe with ``name`` attribute "checkInput" has to be
updated. The path of this forward should be changed to "insertBooking".

The intermediate version you have reached now can be tested as follows:

* Copy the booking XML presented in :ref:`horizonsInterfaces` to some file.
* Edit that file to update the ``id`` attribute of the ``<booking>`` element. This corresponds to the primary key of database table "booking". You need a value that differs from the values you applied so far.
* In the console, go to Testing | Test Pipeline. Run the "IngestBooking" adapter with your booking XML.
* In the console, go to JDBC | Execute Query.
* Run the following query: ``SELECT * FROM booking``.
* Check that there is a row with the values you had in your XML.

The presented version of the ingest booking adapter only inserts
in table "booking". In the coming sections, we will extend
our adapter to also insert into table "visit".
