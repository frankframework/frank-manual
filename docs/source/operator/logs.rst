.. _frankConsoleLogs:

Logs
====

Introduction
------------

In section :ref:`frankConsoleAdapterStatus`, you learned how to monitor the general state of the Frank!Framework. In the previous section :ref:`frankConsoleLadybug`, you learned about the Ladybug debugger. Ladybug produces test reports. A test report is a tree view, and each time you open a node, you see more details on the way the incoming message was processed. The present section provides an additional source of information you can use for monitoring and debugging. The Frank!Framework produces many messages during its operation that are written to text files with extension ".log". These are the logfiles, the subject of this section.

To follow the instructions of this section, you should first have done section :ref:`frankConsoleAdapterStatus`. In particular, you should have processed files ``example.csv`` and ``example2.csv``. You should still have the Frank!Runner open.

.. WARNING::

   At the time of writing, you cannot do this section when you are viewing the Frank!Console with Microsoft Edge. See the following issue of the Frank!Framework: https://github.com/ibissource/iaf/issues/628. If this issue has been closed by the time you are reading this, you may be able to do this section with Microsoft Edge again.

General information
-------------------

In the main menu, please click "Logging" as shown below:

.. image:: mainMenuLogging.jpg

Your screen should look like shown below. You see the version of the Frank!Framework you are using (number 1), like you do in every screen of the Frank!Console. You also see the instance name of your deployment (number 2). You have it confirmed that you are looking to the logging (number 3). All logfiles appear in the same directory on the server and the full path of this directory is shown (number 4).

.. image:: loggingOverview.jpg

Below this general information, a directory listing follows. To the top of this listing, you see a file with prefix ``catalina`` (number 5). The name ``catalina`` is used by Apache Tomcat, the application server on which the Frank!Framework is deployed. Apache Tomcat is used under the hood when you use the Frank!Runner, like you are doing in this tutorial. The contents of the ``catalina`` files equals the output you see when you start the Frank!Runner: on Windows, look at the new command window that is created when the Frank!Framework boots. If your production site is not set up using the Frank!Runner, you may be using aother application server. In that case there are no ``catalina`` files. More information on the role of the application server can be found in chapter :ref:`deploying`.

There are also files with prefix ``frank2manual`` (number 6). This name is derived from the instance name of your deployment, which is "Frank2Manual" (number 2). On your production site, you will probably use another instance name, resulting in another prefix. The general rule is that the capitals in the instance name are replaced by lower-case letters to get the prefix. The files with prefix ``frank2manual`` are written by the Frank!Framework, not by the application server on which the Frank!Framework has been deployed.

In the figure, you also see that the file size is shown (number 7). This information is quite relevant, because some logfiles can grow very rapidly. During your career, you will probably see problems caused by full disks. Later in this manual you will see instructions on how to limit the size of your logfiles. Finally, you see a date column (number 8). This is the last date that the file was written, but this date is not updated in real time. To update the modification dates, you have to refresh your browser. Seeing the modification in the directory listing simplifies searching a lot, because the same information is often spread over multiple logfiles. When you are searching for a specific time, you can quickly see which file to open.

Here are a few logfiles that were present when this manual page was written:

* catalina.2020-04-23.log
* frank2manual-heartbeat.log
* frank2manual-messages.log
* frank2manual.log
* frank2manual_xml.log
* frank2manual_xml.log.1

You see that the filename "catalina.2020-04-23.log" contains a data. No more text is written to this file when April 23 2020 ends. On April 24, a new file "catalina.2020-04-24.log" will be written, etc. You also see "frank2manual_xml.log.1". This file was created because "frank2manual_xml.log" became too large. When the size of "frank2manual_xml.log" passed a certain threshold, it was copied to "frank2manual_xml.log.1". Then "frank2manual_xml.log" was recreated to hold the additional text. When "frank2manual_xml.log" would again grow beyond the threshold, file "frank2manual_xml.log.1" would be copied to "frank2manual_xml.log.2" and then "frank2manual_xml.log" would be copied to "frank2manual_xml.log.1". Then "frank2manual_xml.log" would be recreated to hold the additional data. This approach is called log rotation.

In the remainder of this section, you will examine "frank2manual-heartbeat.log", "frank2manual-messages.log" and "frank2manual.log".

Messages 
--------


TODO: General information, centered around the list of filenames.

TODO: Relating messages log to Ladybug.

TODO: The logfile. Log levels. Relate to Ladybug.

TODO: Logfiles can be connected to monitoring tool.