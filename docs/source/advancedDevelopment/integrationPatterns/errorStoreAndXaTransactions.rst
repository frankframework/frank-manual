.. _advancedDevelopmentIntegrationPatternsErrorStoreXa:

Error Store and XA Transactions
===============================

This section shows how to implement the Fire and Forget integration pattern using an error store and a queue. As a starting point, the application created in section :ref:`advancedDevelopmentIntegrationPatternsTransactions` is taken. It is :download:`available for download <../../downloads/advancedDevelopmentDockerDevelPreJms.zip>`.

Section :ref:`advancedDevelopmentDockerDevelJms` explains how the development environment, files ``docker-compose.yml`` and ``resources.yml``, should be updated to have a queue that can be referenced by Frank configurations. These updates also show that another database driver is needed for PostgreSQL databases that have to support XA transactions. As said, XA transactions are transactions that span multiple data-processing systems, in our case a queue and a database. XA transactions are implemented by the *two phase commit protocol*, see https://en.wikipedia.org/wiki/Two-phase_commit_protocol. This protocol requires a coordinator that drives the data-processing systems. The Frank!Framework uses the Narayana transaction manager for this, which is enabled by setting system property ``transactionmanager.type.default`` to the value ``NARAYANA``. The behavior of the Narayana transaction manager can be fine-tuned by setting properties, see section :ref:`advancedDevelopmentIntegrationPatternsNarayana`.

With the development environment in place, it can be shown how our example configuration can be updated to have the Fire and Forget integration pattern. The changes are shown below:

.. literalinclude:: ../../../../srcSteps/Frank2Transactions/v510/src/main/resources/Configuration.xml
   :language: xml
   :lines: 1-21
   :emphasize-lines: 5, 6, 8, 12, 17, 18, 19
   :linenos:
   :append: ...

Line 5 shows that a new adapter named ``writeDbAsync`` is introduced to hold the ``<ApiListener>``. It has a ``<SenderPipe>`` that enqueues the incoming message, which is processed by the original adapter that is still named ``writeDb``. Enqueueing is done using a ``<JmsSender>`` while dequeueing is done using a ``<JmsListener>`` (lines 12 and 18). These elements are documented in detail in the Frank!Doc. The queue container is accessed using attribute ``queueConnectionFactoryName="jms/qcf-artemis"``. The reference ``jms/qcf-artimis`` is matched in ``resources.yml``, see :ref:`advancedDevelopmentDockerDevelJms`. There is a heading ``jms`` with a list item that has property ``name: "qcf-artemis"``. The ``destinationName`` is the name of the queue being enqueued and dequeued. In our development environment it can be chosen freely because we set sysem property ``jms.createDestination`` to ``true``. In production, it is wise to set this property to ``false`` and then only queues configured by the system administrator can be used.

Preventing that duplicate messages are processed is now done by adapter ``writeDbAsync``. Its receiver has ``checkForDuplicates="true"`` (line 6) and this receiver contains the required message log (line 8). Adapter ``writeDb`` no longer needs a message log because it will not receive duplicate messages anymore. Instead, it has a ``<JdbcErrorStorage>`` that will save messages for which processing fails (line 19). The ``<JdbcErrorStorage>`` stores the failed messages in database table ``IBISSTORE``. That database table also holds data for other error stores and message logs. Records for this ``<JdbcErrorStorage>`` are distinguished because they have the same value for the ``SLOTID`` field; this is configured using the ``slotId`` attribute. Please note that the message log of ``writeDbAsync`` (line 8) and the ``<JdbcErrorStorage>`` have a different ``slotId``.

The ``transactionAttribute`` explained in :ref:`advancedDevelopmentIntegrationPatternsTransactions` works the same for XA transactions as for simple transactions. Adapters ``writeDbAsync`` and ``writeDb`` both have ``transactionAttribute="Required"``. Enqueueing a message happens in a transaction, so a message is either put in the message log *and* enqueued, or the user gets a negative HTTP response from the ``<ApiListener>`` and nothing is done. Dequeueing a message happens in another transaction, but that transaction also spans writing the message in the database. A message is either dequeued and processed, or not dequeued at all.

.. NOTE::

   You may be tempted to set ``transactionAttribute="RequiresNew"`` because enqueuing and dequeuing have to happen in different transactions. This is not needed, however. The receiver of a ``<JmsListener>`` or a ``<MessageStoreListener>`` does not have an existing transaction. We recommend using ``transactionAttribute="Required"`` for the default situation in which a transaction is wanted, and reserving ``transactionAttribute="RequiresNew"`` for special cases where a transaction is present already but a new transaction is needed.

We do not want that a message appears in the error store already when processing fails once. The Frank!Framework retries processing five times because the receiver of adapter ``writeDb`` (line 17) has ``maxRetries="5"``. In production, the system administrator will have control over the time intervals between the retries, because this is part of configuring the queue. When dequeueing and processing fails repeatedly, the Frank!Framework will put the message in the error store and commit the transaction, causing the message to be dequeued permanently. The service manager can check the error store in the Frank!Console and resend the message when the issue with the application has been fixed. See :ref:`managingProcessedMessagesError`. When the message is resent, the receiver of adapter ``writeDb`` is skipped and the message enters the pipeline directly. The transaction attribute of the receiver is inherited by the pipeline, though. Processing the resent message still happens within a transaction.

Exercise
--------

* Download the :download:`Frank application shown in this section <../../downloads/advancedDevelopmentDockerDevelJms.zip>`.
* Start it using ``docker compose up``.
* Start your API client. The HTTP request of section :ref:`advancedDevelopmentIntegrationPatternsOnlyOnce` applies again, the one with HTTP header for the message id.
* Send the request. Observe that the response is different - nothing about updated database rows now, but a response about the enqueued message.
* Send the same request again. Check that you get a HTTP 304 Not Modified.
* In the Frank!Console, stop adapter ``writeTableOtherMessage``, the adapter that does the second modification of the database.
* Send another message with another value for the message id. Check the messages in the Adapter Status page of the Frank!Console. You should see that processing is retried and that finally the message is written to the error store.
* Start adapter ``writeTableOtherMessage`` and resend the message from the Frank!Console. Check that the message is removed from the error store.
* Using JDBC | Execute Query, check that tables "message" and "otherMessage" now have the message you supplied in the HTTP request.
