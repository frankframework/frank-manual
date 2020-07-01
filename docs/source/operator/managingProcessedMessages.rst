.. _operatorManagingProcessedMessages:

Processed Messages
==================

The Frank!Framework operates by processing messages. In section :ref:`frankConsoleAdapterStatus`, you learned that receivers receive messages, which are then processed by adapters. Adapters often send messages to external systems or queues. As a site owner, you have to deal with three kinds of processed messages: :ref:`managingProcessedMessagesLog`, :ref:`manageProcessedMessagesStore` and :ref:`managingProcessedMessagesError`.

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