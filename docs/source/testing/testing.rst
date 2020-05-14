.. _testing:

Testing Frank Configurations
============================

This section is about testing Frank configurations. There are two tools to do this,
:ref:`ladybug` and. These tools have been introduced in :ref:`gettingStarted`. You can study Ladybug without studying :ref:`gettingStarted` before.

Larva and Ladybug can be found as follows:

* Open the Frank console in your webbrowser. The URL depends on the way your Frank has been deployed. If the Frank!Runner is used, it is just http://your-server in which "your-server" is the name or ip address of your host. The Frank!Runner running on your development computer can be reached at http://localhost. The URL may also be http://your-server/yourConfig/iaf/gui if your configuration is named ``yourconfig``.
* In the left-hand menu, click "Testing" as shown:

  .. image:: frankConsoleFindTestTools.jpg

Larva is intended for Frank developers who want to test functionality in the
development environment or the test environment. It provides a simple
programming language in which tests can be scripted. Ladybug is intended for
the acceptance environment or the production environment. If you run an adapter,
a report appears in Ladybug. You can
capture this report into a test script. Ladybug allows you to rerun these test
scripts later. Ladybug also provides features to organize test scripts.

Here is the table of contents of this section.

.. toctree::
   :maxdepth: 3

   ladybug/ladybug
