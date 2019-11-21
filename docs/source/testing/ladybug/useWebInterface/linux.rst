.. _useWebInterfaceLinux:

Linux
=====

This subsection explains how to do a HTTP call to
the electronic archive introduced in :ref:`introduction`
outside the Frank!framework. This subsection gives the
instructions Linux users need to follow.

Please do the following:

#. Open a command prompt.
#. Enter the following command:

   .. code-block:: bash

      curl -i -X POST -H "Content-Type: application/xml" -d '<xxx/>' localhost/ladybug/api/archive

#. The result will be something like this:

   .. code-block: none

      HTTP/1.1 200 OK
      Server: Apache-Coyote/1.1
      Last-Modified: Thu, 21 Nov 2019 10:29:55 GMT
      Cache-Control: no-store, no-cache, must-revalidate, max-age=0, post-check=0, pre-check=0
      Pragma: no-cache
      Allow: OPTIONS, POST
      Content-Type: */*;charset=UTF-8
      Content-Length: 26
      Date: Thu, 21 Nov 2019 10:29:55 GMT

      <docid>docid-12345</docid>

#. Open a webbrowser and open URL "localhost/ladybug/iaf/gui".
#. Open Ladybug by clicking "Testing" and then clicking "Ladybug":

   .. image:: ../../frankConsoleFindTestTools.jpg

#. In Ladybug, you see a table in which your HTTP call appears (number 1):

   .. image:: ladybugReport.jpg

#. Click this line. You see a tree view of the execution of this Frank adapter (number 2). To the right, you see information about the selected node (number 3). In this case, it is the arbitrary XML message you passed through the body of your HTTP request.

.. NOTE::

   In the tree view you see the abbreviation SUT. This stands for System Under Test.

