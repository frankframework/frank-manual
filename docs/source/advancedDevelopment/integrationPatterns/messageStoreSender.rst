*Under construction*

.. _advancedDevelopmentIntegrationPatternsMessageStoreSender:

Fire and Forget Without Queue
=============================

This page shows how to set up the Fire and Forget integration pattern when you do not want the hassle of introducing a queue and XA transactions. Files ``docker-compose.yml`` and ``src/main/resources/resources.yml`` are taken from the example configuration :download:`example Frank without queue <../../downloads/advancedDevelopmentDockerDevelPreJms.zip>`. We show how the ``Configuration.xml`` that uses a queue (from :download:`example Frank using a queue <../../downloads/advancedDevelopmentDockerDevelJms.zip>`) has to be modified when the queue is replaced database table IBISSTORE:

.. include:: ../../snippets/Frank2Transactions/v520/replaceQueueByIbisStore.txt

In the adapter that enqueues the incoming message, ``writeDbAsync``, the ``<Receiver>`` remains the same. The message log that receives the incoming message is still needed - this has nothing to do with the replaced queue. The only change in this adapter is that the ``<JmsSender>`` is replaced by a ``<MessageStoreSender>``.

In the adapter that processes messages, ``writeDb``, there are more changes. The ``<JdbcErrorStorage>`` is removed because the Frank!Framework automatically puts an error storage in the Frank!Console when a ``<MessageStoreSender>`` / ``<MessageStoreListener>`` pair is used. The ``<JmsListener>`` is replaced by a ``<MessageStoreListener>``.

.. NOTE::

   Attribute ``statusValueInProcess="I"`` makes processing messages more robust. It tells the Frank!Framework to update table IBISSTORE when processing a message is started. The ``TYPE`` field is then updated to value ``I``, telling possilbe parallel instances of the listening adapter not to read the message anymore. This update happens outside the transaction. Without attribute ``statusValueInProcess``, the ``TYPE`` field is not updated when processing starts and you rely on the database to protect the message from parallel instances of the adapter.

It is useful to explain the ``TYPE`` field of table IBISSTORE in more detail. This field plays a role for ``<JdbcMessageLog>`` and ``<JdbcErrorStorage>`` elements and for ``<MessageStoreSender>`` / ``<MessageStoreListener>`` pairs. See the table below:

.. table::
   :widths: auto

   ===== =======
   Value Meaning
   ===== =======
   ``L``   Message is in a message log.
   ``M``   Message is waiting to be read by a ``<MessageStoreListener>``.
   ``I``  Message is in process (only applies if ``statusValueInProcess="I"`` has been set)
   ``A``  Message has been processed successfully.
   ``E``  Message is in error store, processing failed.
   ===== =======

This table implies that a ``<JdbcMessageLog>`` and a ``<JdbcErrorStorage>`` can share the same value for the ``slotId`` attribute.