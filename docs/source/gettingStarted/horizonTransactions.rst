.. _transactions:

Transactions
============

This section will finish the implementation of :ref:`horizonsInterfaces`.
So far we have inserted a booking in the two tables "booking" and "visit".
In this section we add transactionality. The inserts in these two
tables should either all succeed, or all fail.

This last requirement can be implemented very easily. To the
``<Pipeline>`` tag, you can add the attribute
``transactionAttribute="RequiresNew"``. With this update,
file "AdapterIngestBooking.xml" becomes:

.. code-block:: XML
   :emphasize-lines: 9

   <Adapter name="IngestBooking">
     <Receiver name="input">
       <ApiListener
           name="inputListener"
           uriPattern="booking"
           method="POST"/>
     </Receiver>
     <Pipeline firstPipe="checkInput"
         transactionAttribute="RequiresNew" >
       <Exit path="Exit" state="success" code="201" />
       <Exit path="ServerError" state="failure" code="500" />
       ...
     </Pipeline>
   </Adapter>

The value ``RequiresNew`` means that a new transaction is started
for executing the ``<Pipeline>``. There are other possible values.
The value ``Mandatory`` for example requires that a transaction
is expected to exist when pipeline execution starts; the pipeline
will fail otherwise. This value is useful when
you want to execute multiple adapters within a single transaction.
See https://ibis4example.ibissource.org/iaf/ibisdoc/ for details.

This completes the implementation of the requirements of section
:ref:`horizonsInterfaces` . We have a REST HTTP service listening
to booking XML documents. The XML is validated and all data
is written to the database. To do this, multiple INSERT
statements are needed. These are executed within a transaction,
which means that either all inserts succeed or all inserts fail.

There is one open end: security. Ingest booking is not the right user
story to explain security, because it is part of a larger interaction
with the user. Before a booking is accepted, the user logs in and
searches destinations. That functionality would be needed before
restricting access would make sense.

Security is easy to implement using the Frank!Framework. This manual will be extended with another
user story of New Horizons to cover this topic.
