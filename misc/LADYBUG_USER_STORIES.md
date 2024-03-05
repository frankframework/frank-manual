Ladybug User Stories
====================

This document is not meant to be published on ReadTheDocs. It is a starting point for writing user documentation and test cases.

Debugging
---------

Story | Test plan
----- | ---------
I want to see the flow of a message through the receier and the pipes (tree view) | ladybug-ff-cypress-test
When a pipeline calls other adapters by Java calls, the flow through these other adapters should be shown in the same report | ladybug-ff-cypress-test
Right after opening a report in the tree view, calls to other adapters should be collapsed nodes | ladybug-ff-cypress-test
I want the option to delete reports from the table to keep the number of reports limited | ladybug-ff-cypress-test
I can disable report generation to limit the number of reports in the table and to reduce execution time | ladybug-ff-cypress-test
I can configure a regular expression such that reports are only stored if their name matches the regular expression | ladybug-ff-cypress-test

Searching
---------

Story | Test plan
----- | ---------
Above the tree view there is a table that has one row for each report | ladybug-ff-cypress-test
The columns of the table are metadata fields. It should be possible put a filter in each metadata field to reduce the number of rows shown | ladybug-ff-cypress-test, details about possible filters in ladybug-frontend or component test
I can open reports in the tree view that I choose from the table, and I should be able to close them again | ladybug-ff-cypress-test

Testing
-------

Story | Test plan
----- | ---------
Reports are put in the debug tab when created. When I want to use a report as a test case, I want to put it in the test tab. | ladybug-ff-cypress-test
I can rerun a report. This can be with stubbed responses of external systems or without stubbing | ladybug-ff-cypress-test
I can rerun both in the test tab and in the debug tab | ladybug-ff-cypress-test
When a rerun produces a different result, I can compare the original and the new result.
I can configure irrelevant differences (e.g. time stamps) to be ignored | ladybug-ff-cypress-test
In the test tab, I can select multiple reports to be rerun in one go | ladybug-ff-cypress-test
I can download reports and upload them later, allowing them to be backed up | ladybug-ff-cypress-test
Downloading and uploading reports should be available both in the debug tab and the test tab | ladybug-ff-cypress-test

Reports in progress
-------------------

Story | Test plan
----- | ---------
Each message the F!F is currently processing results in a report-in-progress. I want to see the number of reports-in-process | ladybug-ff-cypress-test
If a report remains in-process for more than five minutes, I want to see an alert in Ladybug | ladybug-ff-cypress-test

Security and storage
--------------------

Ladybug has different security categories for functions. Most functions are accessible with F!F security role "Observer", which implies accessibility with DataAdmin role. Some functions are only accessible with the "DataAdmin" role. Other functions are only available with the Tester role.

The following features should only be available with the DataAdmin role.

* Enabling or disabling the report generator.
* Configuring a regex that determines whether reports are stored.
* Deleting reports-in-progress.
* Deleting reports.
* Updating reports.
* Copy reports.
* Move reports.
* Upload report.
* Move report.
* Run report.
* TODO: Something about resetting a ReportRunner.

The following features should be available with the Tester role (and not necessarily the DataAdmin role):

* Running a report.

Reports are saved by the ladybug backend. The backend provides different storages:

* Memory storage.
* File storage.
* Database storage.
* TODO: Make this overview complete.

Some storages provide the option to delete specific reports. Others only provide the option to clear all reports. If a storage provides the option to clear all reports, then the user should have the option to clear all reports at once.

It should be possible to configure what storage is used in the ladybug backend, although this does not need to be controllable through the GUI.

TODO: Tester role not properly described.
TODO: Include white box, grey box, black box. What is it?