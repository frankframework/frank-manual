.. _useWebInterfaceWindows:

Windows
=======

This subsection explains how to do a HTTP call to
the electronic archive introduced in :ref:`introduction`
outside the Frank!framework. This subsection gives the
instructions Windows users need to follow.

Please do the following:

.. highlight:: none

#. Open the Frank!framework by browsing to http://localhost/ladybug/iaf/gui.
#. Open Ladybug by clicking "Testing" and then clicking "Ladybug":

   .. image:: ../../frankConsoleFindTestTools.jpg

#. Enable the report generator as shown:

   .. image:: ladybugEnableReportGenerator.jpg

#. Start Postman.
#. Go to File | Settings, select tab General.
#. Ensure that "SSL certificate verification" is not checked, see figure below:

   .. image:: postmanSettings.jpg

#. Close this dialog.
#. Select tab Params. Select method POST and type URL "localhost/ladybug/api/archive" (without quotes). See figure below:

   .. image:: postmanParams.jpg

#. Add header "Content-Type" with value "application/xml" and select it, as shown:

   .. image:: postmanHeaders.jpg

#. Enter the following XML for the body: ::

     <document>This is the document</document>

  .. image:: postmanBody.jpg

#. Press "Send".
#. To the bottom, you should see the following response:

   .. image:: postmanResponse.jpg

   There are tabs that allow you to see different features of the response (number 1). The body tab is selected, so you see the body of the response (number 2). And you see that the HTTP status code is 200 (number 3), which indicates success.

#. Switch back to Ladybug. Press "Refresh":

   .. image:: ladybugRefresh.jpg

#. You see a table in which your HTTP call appears (number 1):

   .. image:: ladybugReport.jpg

#. Click this line. You see a tree view of the execution of this Frank adapter (number 2). To the right, you see information about the selected node (number 3). In this case, it is the arbitrary XML message you passed through the body of your HTTP request.

.. NOTE::

   In the tree view you see the abbreviation SUT. This stands for System Under Test.

