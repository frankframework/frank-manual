Ladybug User Stories
====================

This document is not meant to be published on ReadTheDocs. It is a starting point for writing user documentation and test cases.

Vision
------

Ladybug is a tool to debug and test Java applications that process messages. It is included in the Frank!Framework. This document provides user stories for Ladybug as a part of the Frank!Framework.

Ladybug is not limited to work with the Frank!Framework; it is a tool that can be used with other Java applications as well. The Java application that uses Ladybug is expected to receive or retrieve messages. Each message undergoes a series of transformations to obtain an output message. The Java application has access to a class **TestTool** that is provided by the Ladybug dependency. During the transformation, the Java application uses the methods of class TestTool to produce **checkpoints**. The Java application should also call TestTool to create checkpoints for the input message and the output message. For each input message, the Java application should create a unique **correlation id** that is provided to TestTool for each created checkpoint. TestTool groups all checkpoints by correlation id into a **report**. A **report** thus describes all transformations applied to one input message. The Frank!Framework creates a Ladybug checkpoint for each pipe and each pipeline. Frank developers can thus see how each pipe transforms the message going through the pipeline.

When a report has been captured it is a Java object managed by Ladybug. Ladybug then extracts metadata from the report. This helps for searching and browsing reports because the amount of metadata is much less than the amount of data of all reports. The users should have options to define what information captured in reports should be treated as metadata. Ladybug should also be able to transform reports into XML format. Then users can interact with the reports through Xpath and XSLT.

Ladybug can be used as a debug tool. Ladybug provides a user interface that shows a table of all captured reports. When the user clicks a report, it is opened in a tree view. Each checkpoint is a node in the tree. Collapsing and expanding nodes is described in more detail in the user stories below. In the tree view, the user can see all intermediate results of processing each message. Each checkpoint has a meaningful name. The Frank!Framework names each checkpoint after the adapter or pipe name. Therefore the user can relate the checkpoint's message to the debugged/tested source code, or to the Frank application being tested. When you click a node in the tree, the corresponding message inside the checkpoint should be shown.

Ladybug can be used as a tool for automated testing. Ladybug reports can act as test cases because they can be rerun. Rerunning a report means that the Java code that produced the report is re-executed. The messages inside the related checkpoints are compared to the messages in the original report. The test succeeds if these new messages are considered equivalent to the original ones; otherwise the test fails. Ladybug's user interface has separate tabs for new reports (Debug) and reports that are meant as test cases (Test). In the Debug tab, the user has a button to copy reports to the test tab. The user has options to edit a report to convert the raw capture to a useful testcase.

Data in Ladybug reports can be confidential. There are userstories to limit access to Ladybug's functions based on the user's role.

This document focuses on user stories for Ladybug as a part of the Frank!Framework. The following user roles are considered:

**Frank developer:** Someone who writes Frank applications. He wants to configure Ladybug as part of his job to develop the application for the customer. He also uses Ladybug for debugging or testing purposes, typically before the application is deployed to the customer's production environment. There is little risk that he will see confidential information of the customer.

**Support engineer:** Someone hired by the customer to debug issues in the production environment. He can use ladybug but the customer expects that he does not modify data. He should respect the confidentiality of the customer's data.

**Service manager:** Employee of the customer who uses Ladybug to manage the Frank application. He wants to see whether the app is working correctly and whether there are messages that have not been processed as expected. He typically wants to resend messages when their processing failed (resending messages is not done by Ladybug but by another part of the Frank!Framework).

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

**5:** Given is that I am developing an application and that I did some test. As a Frank developer, I want to see a table of my reports in which I can search for the report about my test. This helps me to produce regression tests.

**10:** Given is that some messages have been processed. As a service manager I want to see a table of my reports that shows me what messages were succesfully processed and what messages could not be processed correctly. I want to see the status for each message and also some metadata that gives me a hint where to look for problems.

**15:** Given is that some messages have been processed. As a support engineer I want to see a table of my reports that gives me an overview of how the system is operating: how many errors? how many messages? what are the general characteristics of the messages? I want to use this table as a starting point for more detailed research. This goal is achieved when the following metadata fields are supplied as table columns:

* **Name:** The name of the report, which is the name of the outermost start checkpoint.
* **Correlation id:** See vision.
* **Storage id:** The id assigned to the report when it was stored.
* **End time:** The timestamp at which the last checkpoint was created.
* **Duration:** The duration of processing the message.
* **Status:** The status with which the pipeline ended, should be SUCCESS or ERROR.
* **Number of checkpoints**
* **Estimated memory usage:** Estimated amount of memory needed to work with this report (size when the data is not compressed).
* **Storage size:** Estimated number of bytes needed to store this report (size needed after possible data compression).

**20:** As a Frank developer, support engineer or service manager, when I click a row in the table I want to see the corresponding report in the tree view so that I can examine it in more detail.

**120:** Given is that a service manager wants to see customer-specific data in the table of reports (story **10**). As a Frank developer, I want tools to define meta data items that are calculated from reports (input and output data, also data captured in arbitrary checkpoints). I want simple building blocks that I can combine, similar to building Frank configurations from pipes, senders and listeners. I want the option to configure the Frank!Framework to add the custom meta data items as columns in the table of reports. This way I can satisfy the requirements given to me by the service manager within a limited timeframe.

NOTE: We implement story **120** because Frank developers can write Spring configuration files (XML). These files define what Java beans are used as metadata extractors and what metadata is used to produce the table of reports. Instructions are in the Frank!Manual but they also require some knowledge of the Java source code of Ladybug.

**200:** Given is that Frank developers are working simultaneously with the same development or test environment. As a Frank developer I want to filter the rows in the report table such that I am seeing only the work I am doing. This helps me to write automated tests more quickly (story **5**).

**203:** Given is that there are many reports in the production environment. As a service manager, I want user-friendly options to omit reports from the report table such that I can analyze the remaining rows. This way I can answer specific questions about the status of the system. This can be implemented as follows. For each column there is an edit field in which I can choose the value required for that column. A report is only shown if every column has the required value. Some metadata items take their value from a limited set (e.g. either SUCCESS or ERROR). In these cases, Ladybug should provide a drop-down list with all possible values to choose from.

**204:** As a Frank developer I want the option to customize in which cases story **203** is implemented with drop-down lists. I do not want to bother the customer with such  detailed configurations.

**207:** Given is that there are many reports in the production environment. As a support engineer, I want flexible options to filter the rows in the report table such that I can do complicated analyses of the reports. This flexibility can be implemented by allowing filter options with regexes.

**210:** As a user I want to see the reports ordered by end time in descending order in the report table when I open Ladybug. This is because I am usually most interested in recent reports.

**212:** Given is that I am busy with some analysis that involves the report table, and that I am also curious whether there are new reports (any user role). When I press the refresh button, I want that the row that was previously selected remains selected so that I am not distracted unnecessarily from the work I was doing.

**220:** As a user I want to have standard sorting options in the table of reports. This means at least sorting on any column and both ascending and descending.

**300:** Given is that messages are being processed in the production environment. As a service manager I want to see how many reports-in-progress there are. There is a report-in-progress if for some correlation id the start checkpoint is not yet matched by a corresponding end checkpoint.

**310:** Given is that processing a message is taking long - after a long time there is no end checkpoint that corresponds to the start checkpoint (this is a report-in-progress, see story **300**). As a service manager I want Ladybug to forcibly produce a report after a timeout so that I can examine what is happening.

**330:** As a Frank developer, I want to be able to configure the time threshold of story **310** so that the customer is not bothered by such a detailed configuration setting.

**400:** As a service manager, I want reports to be stored persistently. Reports should not vanish when the Frank!Framework is restarted.

**405:** Given is that my app runs in the cloud and that because of that data stored in a local file system is not persistent. As a service manager, I want reports to be stored persistently also in this configuration. This can be implemented by storing reports in a database.

**410:** As a Frank developer or system administrator I want control over the kind of storage I am using. Depending on whether I have a database and whether data on my local file system is really persistent, I want the choice to use a database storage or storage on the local file system. I also want the option to store my reports as XML such that I can read them.

**415:** As a Frank developer I want the option to store my reports in memory (not persistent) so that automated tests are not influenced by reports captured during earlier test runs.

**420:** As a Frank developer, I want to be able to delete reports permanently from storage so that I can limit the number of reports I have to consider.

**500:** Given is that multiple users with multiple interests use the report table. As a Frank developer, I want a languague that allows me to create *views*. I want to configure for each view what metadata is in the report table. It should be possible to do this differently for different views.

**510:** Given is that multiple users with multiple interests use the report table. As a user, I want to select a view provided by the Frank developer such that I see the metadata I want in the report table.

NOTE: Story **500** is implemented in the ladybug backend because you can create views in Spring configuration files. Story **510** is implemented because the debug tab has a dropdown box in which you can select a view from the list of available views.

# I want to understand how the message captured by a report was processed

**1000:** As a support engineer or Frank developer, I want to see the name of each checkpoint that is shown in the tree view. The name is not required to be unique.

**1010:** As a support engineer or Frank developer, I want to see the *type* of each checkpoint in the tree view. The type is shown as an icon. It is one of the following:

* Start point.
* End point.
* Abort point.
* Input point.
* Output point.
* Info point.
* Thread create point.
* Thread start point.
* Thread end point.

**1020:** As a support engineer or Frank developer, I want to see a start point as the parent node of the checkpoints that come after it. This applies recursively: a start node inside a start node causes subsequent nodes to be grand children of the first start node. An end point that is a direct child of a start node is also the last child. Subsequent nodes are siblings of the ended start node. This also applies recursively.

**1030:** As a support engineer or Frank developer, I want to be able to collapse and to expand each parent node in the tree view. Each parent node can be *expanded* which means that the start node and its children, including the end node, are shown. A parent node can also be *collapsed* which means that its descendants are not shown. This way I can hide details of how a message was processed.

**1033:** As a support engineer or Frank developer, I want to have a checkpoint for each pipe such that I can see how each pipe transformed the incoming message.

**1037:** As a support engineer or Frank developer, I want a single report when my adapter calls another adapter via a JavaListener. This way, I do not have to browse multiple reports to examine how my incoming message was processed. The sub-adapter checkpoints should have a common ancestor. When I collapse that ancestor, I want to see only one node for everything done in the sub-adapter.

**1050:** As a support engineer or Frank developer, I want to see the message and the metadata of a checkpoint when I click on it.

**1100:** As a support engineer or Frank developer, I want the option to remove a report from the tree view when I am done with it. This does not mean that a report is removed from persistent storage.

**1200:** As a user I want the option to have multiple reports in the tree view simultaneously so that I can easily switch between a few reports I am interested in.

**1210:** As a user I want the option to enforce that the tree view holds only one report at a time, so that I will not get confused about the report I am looking at.

**1220:** As a service manager I want a user-friendly way to switch between requirements **1200** or **1210**.

**1230:** As a service manager I want my choice regarding to **1220** to be persistent, so that I can know by heart whether my Ladybug works like **1200** or like **1210**.

**1240:** Story **1200** has as a consequence that each report in the tree view should have a single root node, otherwise you could not see which node belonged to each report.

NOTE: Presently, some features of Ladybug are attached to the root node of a report.

* In the old Echo2 GUI, there is an "Edit" button in the tree view that puts the report in "edit mode". In edit mode, you have an editable message when you click a node in the tree view. There are also metadata fields, some of them editable and some of them read-only. When you select the top level node, you can edit a description. This way you can add a description of a report that exists in the debug tab.
* In the test tab you can "open" a report. This is the user interface for main user story [I want to turn a report into a test case](#i-want-to-turn-a-report-into-a-test-case). Doing so opens a new tab with a tree view with editable node information next to it, like "edit mode" in the debug tab's tree view. Also in this case the root node of a report is relevant in the current implementation of Ladybug.
* When you click the root node of a report you see it as XML. This combines nicely with an edit field to enter an XSLT transformation (story **2010**)
* When you click the root node of a report you have the option there to enter the description (story **2040**).

**1300:** Given is that I as a service manager am investigating an issue with my application. I want the option to see only checkpoints about communicating with external systems for reports I open in the debug tree. This is currently known as the black box view.

**1310:** Given is that I as a support engineer or Frank developer am investigating an issue. I want the option to see all checkpoints within a report for reports I open in the debug tree. This is known as the white box view.

**1320:** Given is that I as a user am investigating an issue. I want the option to see a selection of checkpoints within a report for reports I open in the debug tree. More checkpoints than the black box view. This is known as the gray box view.

**1330:** Given is that multiple users with multiple interests use the debug tree. As a user I want that the view I select (story **510**) also determines which checkpoints of my reports are shown: **1300**, **1310** or **1320**, in other words white box, gray box or black box.

# I want to turn a report into a test case

**2000:** Given is that I am building an automated test from a report. As a Frank developer I want the option to edit the message within each checkpoint. When the report is rerun, the produced message will be compared to the edited message instead of the message originally captured.

**2010:** Given is that I am building an automated test from a report. As a Frank developer I want the option to configure an XSLT transformation that is applied to each message inside each checkpoint. When a report is rerun, the XSLT transformation is applied to the produced messages and it is applied to the messages inside the checkpoints. For each checkpoint, the two transformation results are compared. This way, irrelevant differences can be ignored. Irrelevant differences are produced for example if the current time is used by a Frank application.

**2020:** Given is that I am building an automated test from a report. As a Frank developer I want the option to declare some checkpoints **stubbed**, checkpoints that correspond to calls to external systems. When the report is rerun, the Frank!Framework should not call the external systems again but it should return the results already stored in the stubbed checkpoints. This way, only the logic within the Frank configuration captured in the report is tested, not the behavior of the external systems. Stubbing allows Frank developers to work with a simpler test environment, because the test does not require access to external systems.

**2030:** Given is that I am building an automated test from a report. As a Frank developer I want the option to base parameterized tests upon my report. This means that I introduce variable references in my report. I can create a new report by specifying values for the variables. I can do this for multiple possibilities to set the variables, all resulting in a new clone of the report.

**2040:** Given is that I am building an automated test from a report. As a Frank developer I want the option to add a *description* to my report. In the description I can document what the report viewed as a test case should test.

# I want to re-run (test) reports to test my Frank application

**3000:** Given is that I am testing my application as a Frank developer. When I enter the test tab I want to see all reports that I have prepared as test cases.

**3010:** Given is that I am testing my application as a Frank developer. I want the option to *rerun* reports. Rerunning a report means that the Frank adapter that produced the report is re-executed. The same input message is supplied. For each pipe, the produced output is compared with the value stored with the corresponding checkpoint. The test succeeds if the new messages are the same after applying the configured XSLT transformation (user story **2010**).

**3020:** Given is that I am testing my application as a Frank developer. I want the option to rerun a single report.

**3030:** Given is that I am testing my application as a Frank developer. I want the option to organize the reports in the Test tab. I want to create groups of tests that can have sub-groups. A tree structure in which the composite nodes are test groups and the leaf nodes are reports. This structure gives me an overview of the tests I have.

**3040:** Given is that I am testing my application as a Frank developer. I want the option to select test cases and groups of test cases. I want the option to rerun the tests I selected. This gives me fine-grained control over my test runs when I want to test parts of my Frank application.

**3050:** Given is that I am testing my application as a Frank developer. I want the option to rerun all reports that are in the Test tab, allowing me to test my Frank application with a single click.

**3060:** Given is that I have reran a few reports and that I want to do new tests. As a user I want the option to reset the report generator, which means that all shown test results are cleared. When I rerun my tests after resetting the report generator, I want that all test results I see come from test started after the moment of resetting.

NOTE: Story **3060** is not trivial because rerunning reports happens in the background.

**3100:** Given is that I have rerun a report as a Frank developer and that this test failed. I want the option to compare the original capture to the new results. I want to see the two datasets next to each other such that I can see what is the same and what is different.

**3110:** Given is that I have rerun a report and that this test failed. Given is also that the number of checkpoints at both sides is different. As a user I want that Ladybug chooses intelligently what checkpoints to the left belong to what checkpoints to the right. When I look at one checkpoint I want to see the corresponding checkpoint next to it. I do not want to search on the other side for the corresponding checkpoint.

**3120:** Given is the context of story **3110**. I want that checkpoints corresponding to the same inputs and outputs to external systems are matched. This statement is intended to clarify the "intelligent choice" of story **3110**.

NOTE: Details of the algorithm implied in **3110** and **3120** are not needed here. We can make Cypress tests to test that the user will be happy with the algorithm.

**3200:** As a Frank developer I want the option to download reports and upload them later. This allows me to save reports if I do not trust the persistent storage provided by the Frank!Framework. It also allows me to remove tests from my test cases without losing the test permanently.

**3210:** As a Frank developer I want to use reports as a means to communicate with my colleagues. I want to construct a report and send it to someone else, asking him to update our application such that the test will pass.

NOTE: Jaco suggested that there should be an edit button in the debug tab. A disadvantage is that if reports can be edited in the debug tab, then you cannot be sure that all reports in the debug tab are original captures. Jaco is also satisfied if there is a disabled edit button in the debug tab. This button can have a mouse-over text that suggests copying to the test tab first.

TODO: Discuss whether we want that reports can be downloaded and uploaded in the debug tab. It may be better to only have this in the test tab.

# I want to configure whether my Frank application does produce reports

**4000:** As a service manager I want the option to turn off the report generator, so that I can reduce the execution time of my application.

**4002:** Given is that my application is not performing well. As a service manager I want the option to turn on the report generator, so that I will get reports that allow me to investigate my issue.

**4004:** As a Frank developer, I want to include in my Frank application whether the report generator is on or off when my Frank configuration is deployed, so that the service manager does not have to check whether the report generator is off to save resources or whether it is on to provide information about potential problems.

**4010:** Given is that my application is not performing well. As a service manager or support engineer I want the option to create reports for only some adapter executions that match my search criterion. This allows me to reduce execution time and memory usage and also get reports to investigate my issue. This can be implemented by an edit field where the user can enter a regular expression. The regular expression is applied to the name of the report, which can be derived from the first checkpoint that will create the report if the report generator is enabled. If the regular expression matches, subsequent checkpoints are used to produce a report. Otherwise no report is created. This implementation provides the desired trade-off between saving resources and providing debug information.

**4100:** Given is that a service manager may distinguish multiple categories of reports. An example is Tibet2. Some reports are about failed messages and indicate that messages should be resend. As a Frank developer, I want the option to route reports to different storages. TODO: Make this a bit more specific.

**4110:** Given is that reports appear in multiple storages as described in **4100**. As a Frank developer, I want to configure for each view (story **500:**) what storage is used to populate the report table.

**4120:** Given is that I am as a service manager investigating an issue with my application. Given is also that reports appear in multiple storages. I want that the view I select (story **510**) determines what storage is used to populate the report table.

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

**5000:** As a service manager I want Ladybug to be self-explanatory. The user interface should help me to understand what is going on, for example by providing mouse-over texts.

TODO: Tester role not properly described.
TODO: Include white box, grey box, black box. What is it?