.. _useWebInterface:

Use Web Interface
=================

As explained in :ref:`introduction`, this tutorial demonstrates Ladybug
by testing a simplified electronic archive. Subsection :ref:`preparations`
explains how the electronic archive is installed. In this section we access
the electronic archive outside the Frank!framework.

The electronic archive, or more precisely its portal (see :ref:`introduction`)
provides a HTTP interface. Windows users can access it using Postman, while Linux users use curl.
This is the only section that requires these tools. If you do not have them, you can
skip this section or install them as explained in :ref:`preparations`.

The instructions are different for Windows and for Linux. Windows users
go to :ref:`useWebInterfaceWindows` while Linux users go to
:ref:`useWebInterfaceLinux`.

.. toctree::
   :maxdepth: 3

   useWebInterfaceWindows
   useWebInterfaceLinux
   

#. Start the Frank framework. You will see the following screen:

   .. image:: startLadybug.png

#. Start ladybug by clicking the ladybug icon, as highlighted by an arrow.
#. In tab Debug, use the Options... button to ensure that "Report generator enabled" is "Yes".

   .. image:: reportGeneratorEnabledYes.png

#. Adjust the stub strategy to "NEVER". By default it is "Stub all sender" (number 6)

   .. image:: stubStrategyNever.png

#. Execute one of your adapters.
#. Click "Refresh" in tab Debug (number 1).
#. A new line is added to the top table to show the execution of your adapter (number 3). You can also use "Test Pipeline" to have a new line in this table. TODO: Reference text.
#. Select the line about the execution of your adapter in the table.
#. Click "Copy" (number 7). This will save the job you did as a test script, to be shown in tab "Test". See the next figure.
#. Click the second tab, which is named "Test".
#. Expand the tree view and select the highest level of subtree "Reports".
#. Click "Refresh". You see a new item as shown below:

   .. image:: treeViewRefresh.png

#. You just captured a test script. Using the "Move" button, you can organize test scripts in a folder structure. You can press the "Run" button to rerun a test script. On success a green text will be put behind the script name, on failure a red text will be shown.
#. After capturing a test set, you can see the items within as shown in the picture below

   .. image:: capturedTestSetItems.png

#. You can add a description to every script. You can do this as follows:

   #. Click the folder that contains your script in the tree view to the left.
   #. Click the "Open" button of the script.
   #. In the tree view to the left, click on the line like [pipeline xxx] having the highest level.
   #. Click "Edit". A screen appears allowing you to add your description as shown below

   .. image:: testscriptAddDescription.png

   #. Click Save.
   #. Done.

