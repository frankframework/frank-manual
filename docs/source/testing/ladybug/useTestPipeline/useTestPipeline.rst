.. _useTestPipeline:

Use Test Pipeline
=================

In section :ref:`useWebInterface`, the electronic archive introduced in :ref:`introduction` was accessed. The electronic archive offers a HTTP interface and therefore HTTP requests were issued. We had to take care to provide the right HTTP headers along with the message we wanted to pass (header "Content-Type"). In general, satisfying the requirements of the interface can sometimes be complicated.

This section explains an alternative way to access the System Under Test, the Test Pipeline screen of the Frank!framework. This way, you skip the interface of your Frank adapter (the HTTP interface of the electronic archive) and pass your message directly to the business logic.

Please call the the electronic archive as follows:

.. highlight:: none

#. Ensure that the Frank!framework is set up according to :ref:`preparations` and that it is running. Go to Ladybug. Ensure that the report generator is enabled. See :ref:`useWebInterfaceWindows` or :ref:`useWebInterfaceLinux`.
#. Click "Testing":

   .. image:: ../../frankConsoleFindTestTools.jpg

#. Click "Test Pipeline". The following screen appears:

   .. image:: testPipeline.jpg

#. Select adapter "sutGet" (number 1)

   .. NOTE::

     The abbreviation SUT stands for "System Under Test".

#. Enter the following text in the message field (number 2): ::

     <docid>docid-12345</docid>

#. Press "Send" (number 3).
#. The result is shown below the send button:

   .. image:: testPipelineResult.jpg

   .. NOTE::

      This result is fixed as motivated in :ref:`introduction`.

#. Go back to Ladybug and press Refresh:

   .. image:: ../useWebInterface/ladybugRefresh.jpg

#. You see a table in which your HTTP call appears (number 1):

   .. image:: ladybugReport.jpg

#. Click the line corresponding to your call to the electronic archive. You see a tree view of the execution of this Frank adapter (number 2). To the right, you see information about the selected node (number 3). In this case, it is the output XML message you saw before after pressing "Send" in Test Pipeline.
