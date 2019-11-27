.. _downloadUpload:

Save and Load Test Scripts
==========================

The previous subsection :ref:`capture` explained how reports in Ladybug can be captured into test scripts. Test scripts can be run any time, allowing you to do regression tests. This section explains how to save test scripts to your PC and how to upload saved tests again.

Please do the following:

.. highlight:: none

#. Ensure that the Frank!framework is set up according to :ref:`preparations` and that it is running. Go to Ladybug. Ensure that the report generator is enabled. See :ref:`useWebInterfaceWindows` or :ref:`useWebInterfaceLinux`.
#. Ensure that you have captured test scripts in tab "Test". If not, you can redo subsection :ref:`capture`.
#. Go to tab "Test". Press "Download all" (number 2 of the picture below):

   .. image:: ../capture/successfulRun.jpg

#. A save file dialog appears allowing you to save a zip file. Press OK.
#. Go to your Downloads folder and sort by creation date to see the downloaded file.
#. Stop the Frank!framework. You will restore your captured scripts soon.
#. Sometimes the Frank!framework saves test scripts automatically, but you can not rely on this. In this tutorial we make sure that all test scripts are lost, such that we can properly demonstrate uploading.
#. Please open a command prompt (Windows) or a terminal (Linux) and enter the issue the following command: ::

     docker container rm ladybug

#. Restart the Frank!framework.
#. Browse to http://localhost/ladybug/iaf/gui.
#. Click "Testing":

   .. image:: ../../frankConsoleFindTestTools.jpg

#. Click Ladybug and tab "Test".
#. There are no tests, see picture:

   .. image:: ladybugUpload.jpg

#. Press Upload.
#. A dialog appears. Select your saved zip file and upload.
#. Your saved test script should be back:

   .. image:: uploadedSuccessfully.jpg
