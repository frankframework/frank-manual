.. _organize:

Organize Test Scripts
=====================

In subsection :ref:`capture` you learned how to capture test scripts and how to run them. If you have many test scripts, it is useful to organize them. This section explains how to add a description to a test script, and shows you how to organize test scripts into folders.

Please do the following:

.. highlight:: none

#. Ensure that the Frank!framework is set up according to :ref:`preparations` and that it is running. Go to Ladybug. Ensure that the report generator is enabled. See :ref:`useWebInterfaceWindows` or :ref:`useWebInterfaceLinux`.
#. Ensure that you have a captured test script of running adapter "sutGet". This should be the case if you did subsection :ref:`downloadUpload`. In this case, you can proceed to :ref:`here <afterPrepared>`.
#. If you do not have a test script of running "sutGet", continue with this step. Click "Testing" in the picture below:

   .. image:: ../../frankConsoleFindTestTools.jpg

#. Click "Test Pipeline". The following screen appears:

   .. image:: ../useTestPipeline/testPipeline.jpg

#. Select adapter "sutGet" (number 1)
#. Enter the following text in the message field (number 2): ::

     <docid>docid-12345</docid>

#. Press "Send" (number 3).
#. The result is shown below the send button:

   .. image:: ../testPipeline/testPipelineResult.jpg

#. Go back to Ladybug.
#. Select the line corresponding to the execution of "sutGet". This is shown with number 1 in the picture below:

   .. image:: ../capture/doCapture.jpg

#. Select the upper-most "Pipeline" node (number 2).
#. Select stub strategy "Never" in the pull down menu with number 3.
#. Press "Copy" (number 4).
#. Go to tab "Test" (number 5). This changes the screen as shown:

   .. image:: ../capture/afterCapture.jpg

#. You see you are in tab "Test" (number 1). Press "Refresh" (number 2). This causes your captured test script to appear (number 3).

This step finishes your preparations.

.. _afterPrepared:

Now that you are prepared, you can learn how to organize your test scripts. Please do the following:

#. We capture another test script first. Click "Test Pipeline". Select adapter "sutArchive" (number 1 of the picture below):

   .. image:: sutArchiveInTestPipeline.jpg

#. In the message field (number 2), enter the following XML:

   .. code-block:: XML

      <document>This is the document</document>

#. Press Send (number 3). Below the send button, the following XML should appear:

   .. code-block:: XML

      <docid>docid-12345</docid>

#. Press "Ladybug", then button "Refresh":

   .. image:: ../useWebInterface/ladybugRefresh.jpg

#. Select the line reporting about "sutArchive" (number 1 of picture below). Select the upper-most "Pipeline" node (number 2). Set the stub strategy to "Never" (number 3) and press "Copy" (number 4). Then press tab "Test" (number 5).

   .. image:: captureArchive.jpg

#. You see that you are in tab "Test" (number 1 of picture below). Press Refresh (number 2). You see two test scripts now, one about "sutGet" and one about "sutArchive" (number 3).

   .. image:: afterCapture.jpg

#. Press the "Open" button of "sutArchive" (number 4). You see the following:

   .. image:: afterOpen.jpg

#. A new tab has been created (number 1). Select the uppermost "Pipeline" node (number 2). You can see that the stub strategy was "Never" when the test script was captured (number 3). Press "Edit" (number 4). The following screen appears:

   .. image:: editDescriptionSutArchive.jpg

#. The tab name stays the same (number 1). Edit the description field (number 2). Write the following text: ::

     sutArchive, call to real archive not stubbed

   .. NOTE::

      This description references the architecture of the simplified electronic archive as introduced in :ref:`introduction`. It emulates a real archive combined with a portal, the portal servicing the user and delegating user calls to the real archive. This set-up allows us to demonstrate the impact of the stub strategy in subsection TODO.

#. Press Save (number 3) and Close (number 4). You go back to the "Test" tab as shown with number 1 in the picture below:

   .. image:: descriptionAdded.jpg

#. Press Refresh (number 2) to see the new description (number 3).
#. Now we will move the "sutArchive" test to a new folder "sutArchive", see the figure below:

   .. image:: prepareMove.jpg

#. Select the "sutArchive" test. Enter the following for the destination folder (number 2): ::

     /sutArchive/

#. Press "Move" (number 3). The new folder is selected as shown in the figure below.

   .. image:: afterMove.jpg

#. As shown in the figure below, select the top node of the tree view (number 1). Now you see all test cases again. You see the folder names as part of the test script names (number 2).

   .. image:: afterMoveSeeAll.jpg

#. Finally, you can remove test scripts. Ensure that "sutGet" is selected and "sutArchive" is deselected as shown. Then press "Delete" (number 3).
#. You get a confirmation dialog. After proceeding, you see that test script "sutGet" is gone:

   .. image:: afterDelete.jpg

#. If you want to pause, you may do "Download all". Then you can upload later when you have time to continue.
