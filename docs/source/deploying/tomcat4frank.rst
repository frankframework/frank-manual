.. _deploymentTomcat4Frank:

Frank!Runner
============

Frank!Runner allows you to run a Frank right from the command line. It automates downloading Apache Tomcat, deploying your Frank configs and booting the Frank!Framework. Your Frank is expected to have directories ``classes``, ``configurations`` and ``tests``, your Frank configurations being deployed as subdirectories of ``configurations``. Test suites are deployed as subdirectories of ``tests``. Directory ``classes`` holds XML files and property files that are applied to all deployed configurations.

Alternatively, a Maven-style directory structure is supported for backward compatibility. See https://github.com/ibissource/iaf/tree/master/example for an example of this directory structure. You can download Frank!Runner from GitHub. For further instructions, see http://www.github.com/ibissource/frank-runner and chapter :ref:`gettingStarted`.