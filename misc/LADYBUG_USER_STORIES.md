Ladybug User Stories
====================

This document is not meant to be published on ReadTheDocs. It is a starting point for writing user documentation and test cases.

Vision
------

Ladybug is a tool to debug and test Java applications that process messages. The Java application that uses Ladybug is expected to receive or retrieve messages. Each message undergoes a series of transformations to obtain an output message. The Java application has access to a class **TestTool** that is provided by the Ladybug dependency. During the transformation, the Java application uses the methods of class TestTool to produce **checkpoints**. The Java application should also call TestTool to create checkpoints for the input message and the output message. For each input message, the Java application should create a unique **correlation id** that is provided to TestTool for each created checkpoint. TestTool groups all checkpoints by correlation id into a **report**. A **report** thus describes all transformations applied to one input message.

Ladybug can be used as a debug tool. Ladybug provides a user interface that shows a table of all captured reports. When the user clicks a report, it is opened in a tree view. Multiple reports can be shown simultaneously in the tree view. Each checkpoint of each report is a node in the tree. Collapsing and expanding nodes is described in more details in the user stories below. When you click a node, the corresponding message inside the checkpoint is shown. The user can see all intermediate results of processing each message. Each checkpoint has a meaningful name. Therefore the user can relate the checkpoint's message to the debugged/tested source code.

Ladybug can be used as a tool for automated testing. Ladybug reports can act as test cases because they can be rerun. Rerunning a report means that the Java code that produced the report is re-executed. The messages inside the related checkpoints are compared to the messages in the original report. The test succeeds if these new messages are considered equivalent to the original ones; otherwise the test fails. Ladybug's user interface has separate tabs for new reports (Debug) and reports that are meant as test cases (Test). In the Debug tab, the user has a button to copy reports to the test tab. The user has options to edit a report to convert the raw capture to a useful testcase.

Data in Ladybug reports can be confidential. There are userstories to limit access to Ladybug's functions based on the user's role.

Ladybug is included in the Java application Frank!Framework. This document lists user stories for Ladybug in general, and also user stories that apply to Ladybug as part of the Frank!Framework.

This page considers the following user roles:

**Java developer:** The Java developer codes the Java application to be tested with Ladybug. He chooses when the Java code should produce checkpoints and what information should be provided in these checkpoints. He controls what metadata should be extracted from the reports to be shown in the table of captured reports.

**Tester:** The tester debugs or tests the Java code using Ladybug's user interface. He does not interact with Ladybug by writing Java code.

**Frank developer:** Someone who writes Frank application. He wants to configure Ladybug as part of his work.

**Frank tester:** Someone who uses the Ladybug GUI as configured by the Frank!Framework. He tests or debugs Frank configurations using Ladybug.

**System administrator:** Someone who deploys the Java application and has control over the device and the application server on which the Java application is hosted.

This page presents a few main user stories and groups the other userstories as sub-stories. Each main user story is a separate section.

* [I want to find the report I am interested in](#i-want-to-find-the-report-i-am-interested-in)
* [I want to understand how the message captured by a report was processed](#i-want-to-understand-how-the-message-captured-by-a-report-was-processed)
* [I want to turn a report into a test case](#i-want-to-turn-a-report-into-a-test-case)
* [I want to re-run (test) reports to test my Java application](#i-want-to-re-run-test-reports-to-test-my-java-application)
* [I want to configure whether my Java application does produce reports](#i-want-to-configure-whether-my-java-application-does-produce-reports)
* [I do not want unauthorized access to reports](#i-do-not-want-unauthorized-access-to-reports)

# I want to find the report I am interested in

**10:** As a Tester, I want to see a table of reports when I open the Ladybug GUI. Each row of the table should be a report and each column should be a metadata attribute.

**20:** As a Tester, when I click a row in the table I want to see the corresponding report in the tree view.

**100:** As a Frank tester, I want to see at least the following metadata attributes in the report table:

* **Name:** The name of the report, which is the name of the outermost start checkpoint.
* **Correlation id:** See vision.
* **Storage id:** The id assigned to the report when it was stored.
* **End time:** The timestamp at which the outermost end checkpoint was created.
* **Duration:** The time interval between the outermost start checkpoint and the outermost end checkpoint.
* **Status:** The status with which the pipeline ended, should be SUCCESS or ERROR.
* **Number of checkpoints**
* **Estimated memory usage:** TODO: What does this mean?
* **Storage size:** TODO: What does this mean?

**110:** As a Java developer, I want to control what metadata is shown in the table of reports. I want that Ladybug provides Java beans that I can wire together to extract data from reports.

**120:** As a Frank developer, I want to be able to add columns to the report table in addition to the ones shown in story **100**. I am willing to write Spring XML files to achieve this.

TODO: Do I have to specify what metadata extractors we have?

**200:** As a Tester I want to hide reports from the report table in which I am not interested. For each metadata field I want an edit box in which I can write a regular expression. Only if for a report the metadata field satisfies the regex, then the report should be shown in the table.

TODO: What syntax do we support for the filters?

**210:** As a Tester, I want to see the reports ordered by the timestamp of the outer start checkpoint or by the timestamp of the outer end checkpoint. The latest timestamp should be in the topmost table row.

**300:** I want to see whether there are reports-in-progress. There is a report-in-progress if for some correlation id the start checkpoint is not yet matched by a corresponding end checkpoint.

**310:** As a Tester, if a report-in-progress is open for too long, then I want Ladybug to close it such that it can see it as a regular report in the table.

**320:** As a Java developer, I want to configure the time threshold of story **310**.

**330:** As a Frank developer, I want to configure the time threshold of story **310**.

**400:** As a Tester, I want reports to be stored persistently. Reports should not vanish when the Java application is restarted.

**410:** As a System administrator, I want the option to store reports in a shared persistent storage. A shared storage used by multiple instances of the Java application. This is useful when the Java application runs in the cloud and when the Tester does not see easily which node executed a report.

**420:** As a Tester, I want to be able to delete reports permanently from storage.

# I want to understand how the message captured by a report was processed

**1000:** As a Tester, I want to see the name of each checkpoint that is shown in the tree view. Each entry in the tree view shows a checkpoint and part of that entry is the checkpoint's name. The name is not required to be unique.

**1010:** As a Tester I want to see the *type* of each checkpoint in the tree view. The type is shown as an icon. It is one of the following:

* Start point.
* End point.
* Abort point.
* Input point.
* Output point.
* Info point.
* Thread create point.
* Thread start point.
* Thread end point.

**1020:** As a Tester, I want to see a start point as the parent node of the checkpoints that come after it. This applies recursively: a start node inside a start node causes subsequent nodes to be grand children of the first start node. An end point that is a direct child of a start node is also the last child. Subsequent nodes are siblings of the ended start node. This also applies recursively.

**1030:** As a Tester I want to be able to collapse and to expand each parent node in the tree view. Each parent node can be *expanded* which means that the start node and its children, including the end node, are shown. A parent node can also be *collapsed* which means that its descendants are not shown.

**1040:** As a Tester, I want each report to have a single parent node. That parent node does not correspond to a checkpoint. All other nodes correspond to checkpoints and they are descendants of the parent node. This helps me to see which checkpoint belongs to which report. The name of the parent node is the same as the name of the first checkpoint, which is the outer start point.

**1050:** As a Tester, I want to see the message of a checkpoint when I click on it.

TODO: Is there more information than the message here?

**1100:** As a Tester, I want the option to remove a report from the tree view when I am done with it. This does not mean that a report is removed from persistent storage.

# I want to turn a report into a test case

Stubbing.
Edit the message.
XSLT transformation of message.
Is a report XML?

# I want to re-run (test) reports to test my Java application

# I want to configure whether my Java application does produce reports

# I do not want unauthorized access to reports

Capture report
Search in debug tab
View in debug tab
View in test tab
Organize in test tab
Rerun
Edit
Ignore

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