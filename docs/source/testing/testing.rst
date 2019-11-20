Testing Frank Configurations
============================

This section is about testing Frank configurations. There are two tools to do this,
:ref:`ladybug` and :ref:`larva`. They can be found as follows:

* Open the Frank console in your webbrowser. If you have a configuration named "yourConfig" then go to http://your-server/yourConfig/iaf/gui.
* In the left-hand menu, double-click "Testing" as shown:

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
   larva/larva
