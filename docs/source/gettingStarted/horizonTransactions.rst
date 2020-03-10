.. _transactions:

Transactions
============

This section will finish the implementation of :ref:`horizonsInterfaces`.
So far we have inserted a booking in the two tables "booking" and "visit".
In this section we add transactionality. The inserts in these two
tables should either all succeed, or all fail.

This last requirement can be implemented very easily. In file ``projects/gettingStarted/configurations/NewHorizons/ConfigurationIngestBooking.xml``,  please update the ``<Pipeline>`` tag by inserting the attribute ``transactionAttribute="RequiresNew"``. Here is the update:

.. include:: ../snippets/NewHorizons/v500/addTransactionAttribute.txt

The value ``RequiresNew`` means that a new transaction is started
for executing the ``<Pipeline>``. There are other possible values.
The value ``Mandatory`` for example requires that a transaction
exists when pipeline execution starts; the pipeline
will fail otherwise. This value is useful when
you want to execute multiple adapters within a single transaction.
See the Frank!Doc (section :ref:`horizonsMultipleFiles`) for details.

This completes the implementation of the requirements of section
:ref:`horizonsInterfaces` . We have a REST HTTP service listening
to booking XML documents. The XML is validated and all data
is written to the database. To do this, multiple INSERT
statements are needed. These are executed within a transaction,
which means that either all inserts succeed or all inserts fail. If you are having troubles, you can download the solution. Please find the download link at the beginning of this chapter: :ref:`gettingStarted`.

At this point, please test your work with the tools you found in this Getting Started tutorial. Windows users can use Postman to send HTTP requests to the adapter and Linux users can use ``curl`` as explained in section :ref:`validateBooking`. You can also use the Test Pipeline screen as explained in section :ref:`helloTestPipeline`. Mind the primary key constraint of the database. Either give each booking document a unique ``id``, or apply SQL query ``DROP ALL OBJECTS`` to clean your database (requires restarting the Frank!Framework).

There is one open end: security. Ingest booking is not the right user
story to explain security, because it is part of a larger interaction
with the user. Before a booking is accepted, the user logs in and
searches destinations. That functionality would be needed before
restricting access would make sense.

Security is easy to implement using the Frank!Framework. This manual will be extended with another
user story of New Horizons to cover this topic.
