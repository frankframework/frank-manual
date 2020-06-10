.. _capture:

Capture test reports
====================

In the preceeding subsections, two ways were demonstrated to access the simplified electronic archive introduced in :ref:`introduction`. In subsection :ref:`useWebInterface`, the HTTP interface of the System Under Test was accessed. In :ref:`useTestPipeline`, the HTTP interface was bypassed such that the input message was given directly to the business logic. We saw reports of these actions in Ladybug. In this subsection, we capture these reports and demonstrate how they can be run again. In subsection :ref:`edit`, you will change captured test reports.

Please do the following:

#. Ensure that the Frank!Framework is set up according to :ref:`preparations` and that it is running. Go to Ladybug. Ensure that the report generator is enabled. See :ref:`useWebInterfaceWindows` or :ref:`useWebInterfaceLinux`.
#. Ensure that you have a report in Ladybug for running adapter "sutGet". If it misses, repeat the steps of :ref:`useTestPipeline`.
#. Select the line corresponding to the execution of "sutGet". This is shown with number 1 in the picture below:

   .. image:: doCapture.jpg

#. Select the upper-most "Pipeline" node (number 2).
#. Select stub strategy "Never" in the pull down menu with number 3.
#. Press "Copy" (number 4).
#. Go to tab "Test" (number 5). This changes the screen as shown:

   .. image:: afterCapture.jpg

#. You see you are in tab "Test" (number 1). Press "Refresh" (number 2). This causes your captured test reports to appear (number 3).
#. Select your test (number 4).
#. Run your test by pressing "Run" (number 6). The other "Run" (button 5) can be used to run individual tests.
#. Press "Refresh". A message appears showing that the test succeeded (number 1 in the figure below):

   .. image:: successfulRun.jpg

#. Go back to tab "Debug", number 1 in the figure below. Press "Refresh" (number 2).

   .. image:: seeRunOfCaptured.jpg

#. Numbers 3 and 4 show the impact of running a captured test. Number 3 was the run of "sutGet" that was captured. Number 4 was introduced by running the captured test. Every execution of an adapter results in a table row.
