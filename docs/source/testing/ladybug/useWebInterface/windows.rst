.. _useWebInterfaceWindows:

Windows
=======

This sub-subsection explains how to do a HTTP call to
the electronic archive introduced in :ref:`introduction`
outside the Frank!Framework. This subsection gives the
instructions Windows users need to follow.

Please do the following:

.. highlight:: none

#. Open the Frank!Framework by browsing to http://localhost.
#. Open Ladybug by clicking "Testing" and then clicking "Ladybug":

   .. image:: ..\\..\\frankConsoleFindTestTools.jpg

#. Enable the report generator as shown:

   .. image:: ladybugEnableReportGenerator.jpg

#. Start Postman.
#. Go to File | Settings, select tab General.
#. Ensure that "SSL certificate verification" is not checked, see figure below:

   .. image:: postmanSettings.jpg

#. Close this dialog.
#. Select tab Params. Select method POST and type URL ``localhost/api/archive``. See figure below:

   .. image:: postmanParams.jpg

#. Go to tab "Headers".
#. Add header ``Content-Type`` with value ``application/xml`` and select it, as shown:

   .. image:: postmanHeaders.jpg

#. Go to tab "Body".
#. Select radio button "raw". Then enter the following XML for the body:

   .. code-block:: xml
     
      <document>This is the document</document>

   See the figure below:

   .. image:: postmanBody.jpg

#. Press "Send".
#. To the bottom, you should see the following response:

   .. image:: postmanResponse.jpg

   There are tabs that allow you to see different features of the response (number 1). The body tab is selected, so you see the body of the response (number 2). And you see that the HTTP status code is 200 (number 3), which indicates success.

#. Switch back to Ladybug and press Refresh:

   .. image:: ladybugRefresh.jpg

#. You see a table in which your HTTP call appears (number 1):

   .. image:: ladybugReport.jpg

#. Click the line corresponding to your call to the electronic archive (number 1). You see a tree view of the execution of this Frank adapter (number 2). To the right, you see information about the selected node (number 3). In this case, it is the XML message you passed through the body of your HTTP request.

.. NOTE::

   In the tree view you see the abbreviation SUT. This stands for System Under Test.

