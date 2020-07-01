.. _managingProcessedMessagesLog:

Message Logs
============

Many companies are legally required to prove that their internal control and financial reporting systems are adequate. They are required to prove this to external auditors. In the United State, this legal requirement is stated in the Sarbanes-Oxley Act, and other countries have similar laws. The adequacy of financial systems can be proved by retaining messages. When a system processes a message by routing it through a chain of subsystems, then each subsystem must save a copy of the message it sends. These messages do not have to be stored forever; only retaining messages for a finite time period, for example 30 days, is required.

The Frank!Framework supports this kind of requirements through a message log. Frank developers can add a ``<messageLog>`` element to a sender. As a result, all message sent by the chosen sender are stored. They are removed when their configured retention period is over. You as a site owner get the option to browse the stored messages. In this section you learn how to do this. Please do the following:

#. Please remember to do the preparations of :ref:`operatorManagingProcessedMessages`.
#. Start the Frank!Runner.
#. Browse to http://localhost. You enter the Adapter Status page.
#. Please check that your are in Frank "Frank2Example3", as shown:

   .. image:: managingProcessedMessagesTheRightFrank.jpg

#. Minimize all adapters by clicking on expanded adapters. You should see the four adapters shown below: "TestMessageLog", "TestMessageStoreSender", "TestMessageStoreListenerAndErrorStorage" and "TestFailureAndSuccess".

   .. image:: managingProcessedMessagesTheExampleAdapters.jpg

#. Expand adapter "TestMessageLog" again, see below. You see a heading "Senders" and below it the sender named "TestMessageStoreSender". Next to this, you see an envelope. As indicated by the blue line, the envelope appears to the far right of the screen; in reality, the ends of the blue line are at the same height.

   .. image:: managingProcessedMessageMessageLogEnvelope.jpg

Next to the envelope you see the number "0", indicating that there are no stored messages. Please proceed as follows to see a stored message:

7. In the main menu, go to Testing | Test Pipeline.
#. Choose adapter "01 TestMessageLog".
#. In the message field, enter ``<message>Some message</message>``.
#. Press "Send".  You should see the output ``<id>1</id>``. You should also see a green bar to the top with the word "success".
#. Go back to the adapter status page and expand adapter "TestMessageLog". Your screen should look again like the figure at step 6, but next to the envelope you should see the number "1".
#. Click the envelope. Your screen should look as shown below. You see a table with all stored messages (only one message in your case). There is a row with filter fields (number 1). For each message row, there are two buttons (number 2) for viewing and downloading the message. The message has been stored with id "2" (number 3). Note that this value differs from the value you saw in Test Pipeline.

   .. image:: managingProcessedMessageMessageLog.jpg

#. Please click the "View" button. Your screen looks as shown below. You see the id used with the message log (number 1) and the original message (number 2). There is also a Download button (not shown).

   .. image:: managingProcessedMessagesMessageLogViewed.jpg

Finally, remember that messages in a message log are automatically deleted when their retention period has ended. This retention period is configured by the Frank developer in the Frank configuration.

.. NOTE::

   If you are a Frank developer yourself, look in the Frank!Doc under "MessageLogs". When you select that heading, you can for example select "JdbcTransactionalStorage". This element has an attribute "retention", the number of days that the retention period lasts.
