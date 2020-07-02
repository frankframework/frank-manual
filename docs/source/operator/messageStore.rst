.. _manageProcessedMessagesStore:

Message Stores
==============

Purpose
-------

When someone accesses one of your web services, she expects a quick reply. If the web service needs to do complex processing, it has to produce a HTTP response before the real processing is done. Such a HTTP response does not provide the answer the customer needs. This situation can be handled as follows. The customer is allowed to send the same request multiple times, until the desired response is received. The web service then has to ensure that the repeated request is handled only once.

The web service takes this responsibility by storing each incoming message with a unique id. When the webservice receives the same id again, it does not start a new calculation. Stored messages appear in a queue that is read by some backend processing system. When the web service gets a request, it checks whether the backend process has produced a result. If no result is available, an empty success response is given. If there is a result, it is included in the body of the response. When that happens, the customer is satisfied.

This pattern can also be described in terms of integration patterns. Modifying data is often done with the fire-and-forget integration pattern. Modification is requested by some request, but no response is expected. The sender trusts that the receiving system will handle the request, and that the request will be handled only once. Modification is often requested through HTTP requests though, typically HTTP PUT or HTTP POST requests. The HTTP protocol was designed for the request-reply pattern. A bridge is thus needed between the request-reply pattern and the fire-and-forget pattern. This bridge is implementd using a message queue. The request-reply side repeats the same request until the desired response is received. The fire-and-forget side is fed by the message queue. The bridge ensures that  each incoming copy of a request is stored only once.

The Frank!Framework offers a component for this queuing solution that bridges the request-reply and the fire-and-forget pattern: a message store. Frank configurations write to a message store using a "MessageStoreSender". Frank configurations read messages from the queue using a "MessageStoreListener".

.. NOTE::

   Frank developers may be confused, because they need to include a ``<messageLog>`` tag with attribute ``className=nl.nn.adapterframework.jdbc.DummyTransactionalStorage``. This has the following background. The sender writes the message to the queue, but the sender does not tell the Frank!Console that the queue exists. In general, ``<messageLog>`` tags are used to define queues and also to write to them. If a normal message log is included next to a sender, writing to the queue happens twice. The ``DummyTransactionalStorage`` is a special kind of message log for which writing to the queue is suppressed. Combining a ``DummyTransactionalStorage`` with a "MessageStoreSender" declares a message store without writing to it twice.

Tutorial
--------

You find an example of a message store in the adapters "02 TestMessageStoreSender" and "03 TestMessageStoreListenerAndErrorStorage". Adapter 2 sends to the message store and adapter 3 reads from the message store. Please do the following to study this example:

#. If you did not do the previous subsection, then please use Testing | Test Pipeline to send a random message to adapter 1.
#. Return to the Adapter Status page.
#. Expand adapter 2. Check that under the "Senders" heading, you see a sender named "Send". It is a "MessageStoreSender".

You have verified that writing to the message store happens in adapter 2. Please continue as follows:

4. Expand adapter 3.
#. Check that under the heading "Receivers", you have a receiver named "TestMessageStoreListenerAndErrorStorage". Check that it has a listener of type "MessageStoreListener".

You have verified that reading from the message store happens in adapter 3. Please find the message store on the Frank!Console, as follows:

6. Expand adapter 2 again.
#. Look to the far right next to sender "Send". You should see the envelope again as shown below:

   .. image:: theEnvelope.jpg

Please note that a message log looks the same as a message store, even though they have a very different purpose. You see also that there are no messages in the message log. There is a number "0" next to the envelope. This can be explained as follows. Adapter 1 sends its incoming messages to adapter 2, which puts them in the message store. They are no longer there however, because adapter 3 reads them.

To see something in the message log, you will stop adapter 3. Please continue as follows:

8. Expand adapter 3 and press its stop button. For more information, please see section :ref:`frankConsoleManagement`.
#. Using Test Pipeline, send some message to Adapter 1. For more information, see the previous subsection :ref:`managingProcessedMessagesLog`. Please do not send the same message, though.
#. Return to the Adapter Status page.
#. Expand adapter 2.
#. You may have to wait a few seconds, but a number "1" should appear at the envelope next to sender "Send".

You have verified that messages written to adapter 1 appear in the message store. Please examine the message store as follows:

13. Click the envelope of the expanded adapter 2. You see the contents of the message store as shown below. This page looks like the contents of a message log. There is a table of stored messages. Above that, you have edit fields for filtering (number 1). For each message, there are two buttons for viewing and downloading the message (number 2). And you see the id of the stored message (number 3).

    .. image:: managingProcessedMessageMessageStore.jpg

The example frank "Frank2Example3" does not implement that the same message is stored only once. If this were the case, you could return to Test Pipeline and insert the same message again. The new copy would not appear in the message store. The number of messages would remain one. We cannot demonstrate this here. Please continue as follows:

14. To the top-right, there is a "Back" button (not shown). Please press it.
#. Expand adapter 3.
#. Press its adapter start button, a black triangle pointing to the right. It becomes green when you hover over it.
#. Expand adapter 2 again and browse to its sender "Send". Look to the envelope to the right.
#. Please check that there are no messages anymore in the message store. The number next to the envelope should be "0".

You have seen the similarities and the differences between a message log and a message store. A message log is intended for auditing. The messages in a message log are not processed by the Frank!Framework, except that they are removed when their retention period has ended. Messages in a message store are used to bridge a request-reply interface (e.g. HTTP) and a fire-and-forget interface. Messages are removed from a message store when a backend process picks them up.

Message logs and message stores both appear in the Frank!Console as an envelope. In both cases you can click the envelope to browse the messages. The page looks the same for a message log and a message store. In both cases, each message has a view and a download button, allowing you to see details of the message and to download it.