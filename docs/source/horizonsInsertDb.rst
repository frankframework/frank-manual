Sending to Database
===================

The frank!framework can send data to external systems.
This is done by pipe "GenericMessageSendingPipe".
Within this pipe, you add a sender to specify the
destination. We use "FixedQuerySender" to specify
that we are targeting the database. It is not
necessary to specify what database we
target, because this configured elsewhere, see
:ref:`installationLinux` .

The ingest booking adapter from the previous section
:ref:`validateBooking` can be appended with the
following pipe:

.. code-block:: XML

   <pipe className="nl.nn.adapterframework.pipes.GenericMessageSendingPipe"
       name="insertBooking">
     <sender className="nl.nn.adapterframework.jdbc.FixedQuerySender"
         name="insertBookingSender"
         query="INSERT INTO booking VALUES(?, ?, ?, ?)"
         jmsRealm="jdbc">
       <param name="id" xpathExpression="/booking/@id" />
       <param name="travelerId" xpathExpression="/booking/travelerId" />
       <param name="price" xpathExpression="/booking/price" />
       <param name="fee" xpathExpression="/booking/fee" />
     </sender>
     <forward name="success" path="Exit" />
     <forward name="failure" path="ServerError" />
   </pipe>

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

