.. _operatorManagingProcessedMessages:

Processed Messages
==================

The Frank!Framework operates by processing messages. In section :ref:`frankConsoleAdapterStatus`, you learned that receivers receive messages, which are then processed by adapters. Adapters often send messages to external systems or queues. The Frank!Framework sometimes saves copies of these messages. Messages are stored in three kinds of containers: :ref:`managingProcessedMessagesLog`, :ref:`manageProcessedMessagesStore` and :ref:`managingProcessedMessagesError`. In this section you learn the purpose of these containers and you learn how to browse and manage them.

You will study processed messages using an example that is shipped with the Frank!Runner, Frank2Example3. You can start it by executing ``frank-runner\examples\Frank2Example3\restart.bat`` (Windows) or ``frank-runner/examples/Frank2Example3/restart.sh`` (Linux). Each type of storage for processed messages is studied in a separate subsection. Here is the table of contents:

.. toctree::

   messageLog
   messageStore
   errorStore