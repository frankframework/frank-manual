.. _manageProcessedMessagesStore:

Message Stores
==============

Purpose
-------

When someone accesses one of your web services, she expects a quick reply. If the web service needs to do complex processing, it has to produce a HTTP response before the real processing is done. A positive HTTP response indicates that the request has been received. The opposite is not true: when there is no positive response, the request may have been received nevertheless. Without a positive response, it is not clear whether or not the request has been received.

This situation can be handled as follows. The customer is allowed to send the same request multiple times, until a positive HTTP response is received. The web service then has to ensure that the repeated request is handled exactly once. The web service takes this responsibility by storing each incoming message with a unique id. When the webservice receives the same id again, it does not store a new request. Stored messages appear in a queue that is read by some backend processing system. The backend process removes each processed item from the queue. This way, it is not processed again.

This pattern can also be described in terms of integration patterns. Modifying data is often done with the fire-and-forget integration pattern. Modification is requested by some request, but no response is expected. The sender trusts that the receiving system will handle the request, and that the request will be handled exactly once. Modification is often requested through HTTP requests though, typically HTTP PUT or HTTP POST requests. The HTTP protocol was designed for the request-reply pattern. A bridge is thus needed between the request-reply pattern and the fire-and-forget pattern. This bridge is implementd using a message queue. The request-reply side repeats the same request until a positive response received, which indicates successful receipt of the request. The fire-and-forget side is fed by the message queue. The bridge ensures that each incoming request is stored only once.

The Frank!Framework offers a component for this queuing solution that bridges the request-reply and the fire-and-forget pattern: a message store. The message store uses a database table to queue the requests. Frank configurations write to the message store using a ``<MessageStoreSender>``. Frank configurations read from the message store using a ``<MessageStoreListener>``.

.. NOTE::

   Message logs and message stores are implemented using the database. There is a database table "ibisstore" that holds all database-managed message logs, message stores and error stores. The field "type" distinguishes between a message log, a message store or an error store: The values "L" and "A" indicate a message log; the value "M" indicates a message store and the value "E" indicates an error store. The field "slotid" is used to identify a specific message log, message store or error store.
   
   More information can be accessed through the Frank!Doc. See sender "MessageStoreSender" and listener "MessageStoreListener".

.. NOTE::

   With a message store, what happens when a new copy of a request is received after an earlier copy has been processed by the backend processing system? The message is no longer in the message store, so how does the Frank!Framework know that the request is a duplicate? The answer is that the message is still in the database. The message has been moved from the message store to a message log. This is implemented by changing the type from "M" to "A".

   This analysis demonstrates the difference between a message log with type "L" and a message log with type "A". Message logs intended for auditing, see subsection :ref:`managingProcessedMessagesLog`, use type code "L". Message logs that hold processed messages coming from a message store use type code "A".

.. NOTE::

   If you are a Frank developer, the following may be interesting to you. You introduce a message store by using a ``<MessageStoreSender>`` element in your configuration. This introduces an error store automatically. If you have a ``<MessageStoreSender>``, there is no need to add a ``<JdbcErrorStorage>`` to get the error store for failed messages.

Tutorial
--------

You find an example of a message store in the adapters 02 and 03. Adapter 02 sends to the message store and adapter 03 reads from the message store. Please do the following to study this example:

#. If you did not do the previous subsection, then please use Testing | Test a Pipeline to send a random message to adapter 01.
#. Return to the Adapter Status page.
#. Expand adapter 02. Check that under the "Senders" heading, you see a sender named "Send". It is a "MessageStoreSender".

You have verified that writing to the message store happens in adapter 02. Please continue as follows:

4. Expand adapter 03.
#. Check that under the heading "Receivers", you have a receiver named "03 MessageStoreReceiver". Check that it has a listener of type "MessageStoreListener".

You have verified that reading from the message store happens in adapter 03. Please find the message store on the Frank!Console, as follows:

6. Expand adapter 02 again.
#. Look to the far right next to sender "Send". You should see a green icon as shown below:

   .. image:: theMessageStore.jpg

There are no messages in the message store. There is a number "0" next to the icon. This can be explained as follows. Adapter 01 sends its incoming messages to adapter 02, which puts them in the message store. They are no longer there however, because adapter 03 has read them.

To see something in the message store, you will stop adapter 03. Please continue as follows:

8. Expand adapter 03 and press its stop button. For more information, please see section :ref:`frankConsoleManagement`.
#. Using Test a Pipeline, send some message to Adapter 01. For more information, see the previous subsection :ref:`managingProcessedMessagesLog`. Please do not send the same message, though.
#. Return to the Adapter Status page.
#. Expand adapter 02.
#. You may have to wait a few seconds, but a number "1" should appear at the icon next to sender "Send".

You have verified that messages written to adapter 01 appear in the message store. Please examine the message store as follows:

13. Click the icon of sender Send of adapter 02. You see the contents of the message store as shown below. This page looks like the contents of a message log. There is a table of stored messages. Above that there is an expandable line "Display and Search Filters" (expand icon highlighted). For each message, there are two buttons "View" and "Download". The table holds the storage id of each stored message (highlighted).

    .. image:: managingProcessedMessageMessageStore.jpg

The example frank "Frank2Example3" does not implement that the same message is stored only once. If this were the case, you could return to Test a Pipeline and insert the same message again. The new copy would not appear in the message store. The number of messages would remain one. We cannot demonstrate this here. Please continue as follows:

14. To the top-right, there is a "Back" button. Please press it.
#. Expand adapter 03.
#. Press its adapter start button, a black triangle pointing to the right. It becomes green when you hover over it.
#. Expand adapter 02 again and look at its sender "Send". Look to the icon to the right.
#. Please check that there are no messages anymore in the message store. The number next to the icon should be "0".

You have seen the similarities and the differences between a message log and a message store. A message log is intended for auditing. The messages in a message log are not processed by the Frank!Framework, except that they are removed when their retention period has ended. Messages in a message store are used to bridge a request-reply interface (e.g. HTTP) and a fire-and-forget interface. Messages are removed from a message store when a backend process picks them up.

Message logs and message stores both have icons in the Frank!Console. You can click them to browse the messages. The page looks the same for a message log and a message store. In both cases, each message has a view and a download button, allowing you to see details of the message and to download it.