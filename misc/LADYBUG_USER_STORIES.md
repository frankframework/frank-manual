Ladybug User Stories
====================

This document is not meant to be published on ReadTheDocs. It is a starting point for writing user documentation and test cases.

Vision
------

Ladybug is a tool to debug and test Java applications that process messages. It is included in the Frank!Framework. This document provides user stories for Ladybug as a part of the Frank!Framework.

Ladybug is not limited to work with the Frank!Framework; it is a tool that can be used with other Java applications as well. The Java application that uses Ladybug is expected to receive or retrieve messages. Each message undergoes a series of transformations to obtain an output message. The Java application has access to a class **TestTool** that is provided by the Ladybug dependency. During the transformation, the Java application uses the methods of class TestTool to produce **checkpoints**. The Java application should also call TestTool to create checkpoints for the input message and the output message. For each input message, the Java application should create a unique **correlation id** that is provided to TestTool for each created checkpoint. TestTool groups all checkpoints by correlation id into a **report**. A **report** thus describes all transformations applied to one input message.

The Frank!Framework creates a Ladybug checkpoint for each pipe and each pipeline. Frank developers can thus see how each pipe transforms the message going through the pipeline.

Ladybug can be used as a debug tool. Ladybug provides a user interface that shows a table of all captured reports. When the user clicks a report, it is opened in a tree view. Each checkpoint is a node in the tree. Collapsing and expanding nodes is described in more details in the user stories below. When you click a node, the corresponding message inside the checkpoint is shown.

In the tree view, the user can see all intermediate results of processing each message. Each checkpoint has a meaningful name. The Frank!Framework names each checkpoint after the adapter or pipe name. Therefore the user can relate the checkpoint's message to the debugged/tested source code, or to the Frank application being tested.

Ladybug can be used as a tool for automated testing. Ladybug reports can act as test cases because they can be rerun. Rerunning a report means that the Java code that produced the report is re-executed. The messages inside the related checkpoints are compared to the messages in the original report. The test succeeds if these new messages are considered equivalent to the original ones; otherwise the test fails. Ladybug's user interface has separate tabs for new reports (Debug) and reports that are meant as test cases (Test). In the Debug tab, the user has a button to copy reports to the test tab. The user has options to edit a report to convert the raw capture to a useful testcase.

Data in Ladybug reports can be confidential. There are userstories to limit access to Ladybug's functions based on the user's role.

This document focuses on user stories for Ladybug as a part of the Frank!Framework. The following user roles are considered:

**Frank developer:** Someone who writes Frank application. He wants to configure Ladybug as part of his work.

**Frank tester:** Someone who tests or debugs Frank configurations using Ladybug.

**System administrator:** Someone who deploys the Java application and has control over the device and the application server on which the Java application is hosted.

This page presents a few main user stories and groups the other userstories as sub-stories. Each main user story is a separate section.

* [I want to find the report I am interested in](#i-want-to-find-the-report-i-am-interested-in)
* [I want to understand how the message captured by a report was processed](#i-want-to-understand-how-the-message-captured-by-a-report-was-processed)
* [I want to turn a report into a test case](#i-want-to-turn-a-report-into-a-test-case)
* [I want to re-run (test) reports to test my Frank application](#i-want-to-re-run-test-reports-to-test-my-frank-application)
* [I want to configure whether my Frank application does produce reports](#i-want-to-configure-whether-my-frank-application-does-produce-reports)
* [I do not want unauthorized access to reports](#i-do-not-want-unauthorized-access-to-reports)
* [Miscelaneous](#miscelaneous)

# I want to find the report I am interested in

**10:** As a Frank tester, I want to see a table of reports when I open the Ladybug GUI. Each row of the table should be a report and each column should be a metadata attribute. In this table I can search the report of the adapter run that I want to examine.

**20:** As a Frank tester, when I click a row in the table I want to see the corresponding report in the tree view. This allows me to examine it in more detail.

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

**120:** As a Frank developer, I want to be able to add columns to the report table in addition to the ones shown in story **100**. This way I can support the customer's tester who wants to search reports based on customer-specific data (see story **10**). As a Frank developer I am willing to write Spring XML files to achieve this for the customer. Customer specific data appears in the checkpoints of the reports, so I need Java Beans that together provide flexible search capabilities.

**200:** As a Frank tester I want to hide reports from the report table in which I am not interested. This way I can find the report I need more easily. For each metadata field I want an edit box in which I can write a regular expression. Only if for a report all the metadata fields satisfy their regex, then the report should be shown in the table.

TODO: What syntax do we support for the filters?

**210:** As a Frank tester, I want to see the reports ordered by the timestamp of the first start checkpoint or by the timestamp of the last end checkpoint. The latest timestamp should be in the topmost table row.

**220:** As a Frank tester, I want to be able to sort both ascending and descending with respect to the timestamp of story **210**. This helps me to find reports more easily.

**300:** As a Frank tester I want to see how many reports-in-progress there are. There is a report-in-progress if for some correlation id the start checkpoint is not yet matched by a corresponding end checkpoint.

**310:** As a Frank tester, if a report-in-progress is open for too long, then I want Ladybug to close it such that I can see it as a regular report in the table.

**330:** As a Frank developer, I want to be able to configure the time threshold of story **310**.

**400:** As a Frank tester, I want reports to be stored persistently. Reports should not vanish when the Frank!Framework is restarted.

**410:** As a System administrator, I want the option to store reports in a shared persistent storage. A shared storage used by multiple instances of the Frank!Framework. This is useful when the Framk!Framework runs in the cloud and when the Frank tester does not see easily which node executed a report.

**420:** As a Frank tester, I want to be able to delete reports permanently from storage. This helps me to search more easily within the remaining reports.

# I want to understand how the message captured by a report was processed

**1000:** As a Frank tester, I want to see the name of each checkpoint that is shown in the tree view. The name is not required to be unique.

**1010:** As a Frank tester I want to see the *type* of each checkpoint in the tree view. The type is shown as an icon. It is one of the following:

* Start point.
* End point.
* Abort point.
* Input point.
* Output point.
* Info point.
* Thread create point.
* Thread start point.
* Thread end point.

**1020:** As a Frank tester, I want to see a start point as the parent node of the checkpoints that come after it. This applies recursively: a start node inside a start node causes subsequent nodes to be grand children of the first start node. An end point that is a direct child of a start node is also the last child. Subsequent nodes are siblings of the ended start node. This also applies recursively.

**1030:** As a Frank tester I want to be able to collapse and to expand each parent node in the tree view. Each parent node can be *expanded* which means that the start node and its children, including the end node, are shown. A parent node can also be *collapsed* which means that its descendants are not shown. This way I can hide details of how a message was processed.

**1033:** As a Frank tester, I want to have a checkpoint for each pipe such that I can see how each pipe transformed the incoming message.

**1037:** As a Frank tester, I want a single report when my adapter calls another adapter via a JavaListener. This way, I do not have to browse multiple reports to examine how my incoming message was processed. The sub-adapter checkpoints should have a common ancestor. When I collapse that ancestor, I want to see only one node for everything done in the sub-adapter.

**1040:** As a Frank tester, I want each report to have a single parent node. That parent node does not correspond to a checkpoint. All other nodes correspond to checkpoints and they are descendants of the parent node. This helps me to see which checkpoint belongs to which report. The name of the parent node is the same as the name of the first checkpoint, which is the outer start point.

**1050:** As a Frank tester, I want to see the message of a checkpoint when I click on it.

TODO: Is there more information than the message here?

**1100:** As a Frank tester, I want the option to remove a report from the tree view when I am done with it. This does not mean that a report is removed from persistent storage.

# I want to turn a report into a test case

**2000:** Given is that I am viewing a report as a Frank tester. I want the option to edit the message within each checkpoint. When the report is rerun, the produced message will be compared to the edited message instead of the message originally captured. This allows me to update reports as test cases when my Frank application is changed.

**2010:** Given is that I am viewing a report as a Frank tester. I want the option to configure an XSLT transformation that is applied to each message inside each checkpoint. When a report is rerun, the XSLT transformation is applied to the produced messages and it is applied to the messages inside the checkpoints. For each checkpoint, the two transformation results are compared. This way, irrelevant differences can be ignored. Irrelevant differences are produced for example if the current time is used by a Frank application.

**2020:** Given is that I am viewing a report as a Frank tester. I want the option to declare some checkpoints **stubbed**, checkpoints that correspond to calls to external systems. When the report is rerun, the Frank!Framework should not call the external systems again but it should return the results already stored in the stubbed checkpoints. This way, only the logic within the Frank configuration captured in the report is tested, not the behavior of the external system. Stubbing allows Frank testers to work with a simpler test environment, because the test do not require access to external systems.

**2030:** Given is that I am viewing a report as a Frank tester. I want the option to base parameterized tests upon my report. This means that I introduce variable references in my report. I can create a new report by specifying values for the variables. I can do this for multiple possibilities to set the variables, all resulting in a new clone of the report.

**2040:** Given is that I am viewing a report as a Frank tester. I want the option to add a *description* to my report. In the description I can document what the report viewed as a test case should test.

# I want to re-run (test) reports to test my Frank application

**3000:** As a Frank tester, when I enter the test tab I want to see all reports that I have prepared as test cases for my Frank application.

**3010:** As a Frank tester, I want the option to *rerun* reports. Rerunning a report means that the Frank adapter that produced the report is re-executed. The same input message is supplied. For each pipe, the produced output is compared with the value stored with the corresponding checkpoint. The test succeeds if the new messages are the same after applying the configured XSLT transformation (user story **2010**).

**3020:** As a Frank tester, I want the option to rerun a single report. I should have that option for every report, whether it is in the Debug tab or in the Test tab. This way, I am not obliged to edit reports before they can act as automated tests.

**3030:** As a Frank tester, I want the option to organize the reports in the Test tab. I want to create groups of tests that can have sub-groups. A tree structure in which the composite nodes are test groups and the leaf nodes are reports. This structure gives me an overview of the tests I have.

**3040:** As a Frank tester, I want the option to select test cases and groups of test cases. I want the option to rerun the tests I selected. This gives me fine-grained control over my test runs when I want to test parts of my Frank application.

**3050:** As a Frank tester, I want the option to rerun all reports that are in the Test tab, allowing me to test my Frank application with a single click.

**3100:** As a Frank tester, when I have rerun a report I want the option to compare the original capture to the new results. I want to see the two datasets next to each other such that I can see what is the same and what is different.

**3200:** As a Frank tester, I want the option to download reports and upload them later. This allows me to save reports if I do not trust the persistent storage provided by the Frank!Framework. It also allows me to remove tests from my test cases without losing the test permanently.

**3210:** As a Frank tester, I want downloading and uploading to be available both in the Debug tab and in the Test tab. This way I am not obliged to copy reports to the Test tab before I can use these functions.

# I want to configure whether my Frank application does produce reports

**4000:** As a System administrator I want the option to turn off the report generator. When the report generator is off, my Frank application should not invoke Ladybug when processing messages. This might reduce the execution time.

**4010:** As a System administrator I want the option to create reports for only some adapter executions that match my search criterion. The search criterion is a regex that is applied to the name of the outer start checkpoint.

# I do not want unauthorized access to reports

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

# Miscelaneous

### Running a report.

Reports are saved by the ladybug backend. The backend provides different storages:

* Memory storage.
* File storage.
* Database storage.
* TODO: Make this overview complete.

Some storages provide the option to delete specific reports. Others only provide the option to clear all reports. If a storage provides the option to clear all reports, then the user should have the option to clear all reports at once.

It should be possible to configure what storage is used in the ladybug backend, although this does not need to be controllable through the GUI.

TODO: Tester role not properly described.
TODO: Include white box, grey box, black box. What is it?