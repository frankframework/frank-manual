.. _deploymentTomcat4Frank:

Frank!Runner
============

Frank!Runner allows you to run a Frank right from the command line. It automates downloading Apache Tomcat, deploying your Frank configs and booting the Frank!Framework. Your Frank is expected to have directories ``classes``, ``configurations`` and ``tests``, your Frank configurations being deployed as subdirectories of ``configurations``. Test suites are deployed as subdirectories of ``tests``. Directory ``classes`` holds XML files and property files that are applied to all deployed configurations. For further instructions and downloading, see http://www.github.com/ibissource/frank-runner

Alternatively, a Maven-style directory structure is supported for backward compatibility. To see which directories are then equivalent with ``classes``, ``configurations`` and ``tests``, check the README.md file on GitHub.