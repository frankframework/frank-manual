.. _ignorePreparations:

Preparations
============

In this sub-subsection of :ref:`ignore`, we set the stage for examining this functionality. You will learn nothing new. If you are not following the instructions but are just reading, you can skip this sub-subsection.

Please do the following:

.. highlight:: none

#. Stop the Frank!framework.
#. Edit :code:`classes/Configuration.xml` to become:

   .. code-block:: XML

      <?xml version="1.0" encoding="UTF-8" ?>
      <!DOCTYPE configuration [
          <!ENTITY external SYSTEM "externalTime.xml">
      ]>
      ...

#. Restart the Frank!framework.
#. Open Ladybug by clicking "Testing" and then "Ladybug" as shown below:

   .. image:: ../../frankConsoleFindTestTools.jpg

#. We delete all existing texts because they are no longer relevant. Click tab "Test" (number 1 in the picture below). Select the top node in the tree view (number 2). Press "Select all" (number 3) to select all tests (number 4). Then press "Delete" (number 5).

   .. image:: prepareDeleteOld.jpg

#. A confirmation dialog appears, proceed. Press "Refresh" (number 6). All test scripts should be gone.
#. Go to "Test Pipeline". To the top, you see you are indeed in the Test Pipeline screen (number 1 in the picture below). Select adapter "sutGet" (number 2). In the message field (number 3), enter the following XML: :code:`<docid>docid-12345</docid>`. Then press "Send" (number 4). You see that execution was successful (number 5) and you see a result (number 6).

   .. image:: sutGetTestPipeline.jpg

#. The result should be:

   .. code-block:: XML

      <result>
          <document>
              This is the document
          </document>
          <retrievalTime>
              2019-11-26T10:57:37UTC
          </retrievalTime>
      </result>

   You see that the current time is part of the result. This will be different each time the "sutGet" adapter is run.
#. Go back to Ladybug. Click tab "Debug" (number 1 in the picture below). Click "Refresh" (number 2). Select the topmost row with a report about running "sutGet" (number 3). Select the topmost "Pipeline" node in the tree view (number 4). Select stub strategy "Never" (number 5). Then press "Copy" (number 6).

   .. image:: capture.jpg