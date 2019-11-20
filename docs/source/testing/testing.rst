Testing Frank Configurations
============================

This section is about testing Frank configurations. There are two tools to do this,
:ref:`ladybug` and :ref:`larva`. They can be as follows:

* Open the Frank console in your webbrowser. If you have a configuration named "yourConfig" then go to http://your-server/yourConfig/iaf/gui.
* In the left-hand menu, double-click "Testing" as shown:

  .. image:: frankConsoleFindTestTool.jpg

Larva is intended to test new functionality of your adapter. It provides a simple
programming language in which tests can be scripted. Ladybug is intended for
regression testing. If you run an adapter, a report appears in Ladybug. You can
capture this report into a test scripts. Ladybug allows you to rerun these test
scripts later. Ladybug also provides features to organize these test scripts.

Here is the table of contents of this section.

.. toctree::
   :maxdepth: 3

   ladybug/ladybug
   larva/larva
