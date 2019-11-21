.. _useWebInterfaceLinux:

Linux
=====

.. highlight:: none

This subsection explains how to do a HTTP call to
the electronic archive introduced in :ref:`introduction`
outside the Frank!framework. This subsection gives the
instructions Linux users need to follow.

Please do the following:

#. Open the Frank!framework by browsing to http://localhost/ladybug/iaf/gui.
#. Open Ladybug by clicking "Testing" and then clicking "Ladybug":

   .. image:: ../../frankConsoleFindTestTools.jpg

#. Enable the report generator as shown:

   .. image:: ladybugEnableReportGenerator.jpg

#. Open a command prompt.
#. Enter the following command:

   .. code-block:: bash

      curl -i -X POST -H "Content-Type: application/xml" -d '<document>This is the document</document>' localhost/ladybug/api/archive

#. The result will be something like this: ::

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

.. include:: commonWindowsLinux.rst
