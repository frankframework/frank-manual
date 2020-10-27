.. _advancedDevelopmentMaven:

Advanced configuration management with Maven
============================================

Introduction
------------

This section presents advanced configuration management to Frank developers. In section :ref:`gettingStarted`, you learned how to develop Frank configurations, organizing your files in directories ``configurations``, ``tests`` and ``classes``. You also learned about the Frank!Runner, a tool for developers to quickly start Franks. This section covers the following subjects:

#. Starting the Frank!Runner from within your text editor.
#. The advantages of using Maven.
#. Developing Franks with Maven.

There are two ways to integrate the Frank!Runner with Maven. First, you can develop a single Maven project that holds a Frank. This way, you leave the idea of developing Frank configurations as explained in subsection :ref:`frankRunnerInstallationGeneralStructure`. It was explained there that Frank configs should be developed to be deployed independently from each other. With the simple Maven approach, you create a webapplication that combines the Frank!Framework and all Frank configurations that it should run. The second way to use Maven brings back the idea of independent configurations, but it organizes your files in a more complex way. For details about this second approach, see the documentation of the Frank!Runner at http://github.com/ibissource/frank-runner. We focus here on the fist, simple, approach.

Starting the Frank!Runner from Visual Studio Code
-------------------------------------------------

First, you learn how to start the Frank!Runner from within your text editor. We present the approach for Visual Studio Code, but it also works for Eclipse. Please do the following:

#. Create an empty directory where you can develop a Frank, say ``Frank2Maven``.

   .. WARNING::

      Do not use the same ``Frank2Manual`` directory that you used in :ref:`gettingStarted`. That directory contains a Frank, so you can only create Frank configurations there that are not Maven-based. In this section you are developing a Frank. You cannot fit a Frank within another Frank.

#. Go to the parent directory of ``Frank2Maven`` and clone the Frank!Runner from GitHub. A directory ``frank-runner`` should appear as a brother of ``Frank2Maven``.
#. Start this installation of the Frank!Runner. It will download Ant for you. Then stop it again.
#. Open Visual Studio Code and install the Task Explorer plugin (number 2 in the figure below). To start installing plugins, you first need to press the icon numbered 1.

   .. image:: tasksPlugin.jpg

#. Press the cog wheel (number 3). A pull-down menu appears.
#. Select "Extension Settings".
#. A new window opens in your editor that is named "Settings". It shows many options for the Task Explorer plugin. Check the option "Enable Ant".
#. Lookup "Path to Ant". In that text field, enter the full path of the file ``ant.bat``. You can find that file in your ``frank-runner`` directory.

