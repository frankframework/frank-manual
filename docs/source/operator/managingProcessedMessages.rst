.. _operatorManagingProcessedMessages:

Processed Messages
==================

The Frank!Framework operates by processing messages. In section :ref:`frankConsoleAdapterStatus`, you learned that receivers receive messages, which are then processed by adapters. Adapters often send messages to external systems or queues. The Frank!Framework sometimes saves copies of these messages. Messages are stored in there are three kinds of containers: :ref:`managingProcessedMessagesLog`, :ref:`manageProcessedMessagesStore` and :ref:`managingProcessedMessagesError`. In this section you learn the purpose of these containers and you learn how to browse and manage them.

You will study processed messages using an example that is shipped with the Frank!Runner. Please prepare yourself as follows if you want to do this tutorial:

#. In the ``build.properties`` file within your ``frank-runner`` directory, put the following line:

   .. code-block:: none

      project.dir=frank-runner/examples/Frank2Example3

#. Ensure that other lines starting with ``project.dir`` are removed or commented out with a ``#`` sign.
#. Restart the Frank!Runner.

You will study each type of storage for processed messages in turn. Here is the table of contents:

.. toctree::

   messageLog
   messageStore
   errorStore