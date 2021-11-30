.. _frankConsolePreparations:

Preparations 
============

.. highlight:: none

As said in section :ref:`frankConsoleNewHorizons`, this chapter on the Frank!Console is a tutorial, allowing you to practice. Before you dive into the Frank!Console, you need to install the Frank!Framework. The Frank!Framework can be executed in different ways. The simplest way to execute the Frank!Framework is to use the Frank!Runner. Please do the following to prepare yourself for this tutorial:

#. If you do not have git already, download it from https://git-scm.com/downloads.
#. Choose some working directory in which you will install the Frank!Runner and do the exercises of the Frank!Manual, say ``franks``.
#. In a command prompt, go to your ``franks`` directory and clone the Frank!Runner with the following command: ::

     franks> git clone https://github.com/ibissource/frank-runner

#. Check that your directory ``franks`` has a subdirectory ``frank-runner``. 
#. Within ``franks``, create a subdirectory ``Frank2Manual``.
#. Within ``franks/Frank2Manual``, create subdirectory ``configurations``.
#. Within directory ``franks/frank-runner``, create text file ``build.properties`` and give it the following contents: ::

     project.dir=Frank2Manual

#. Download the :download:`Frank config <../downloads/configurations/forFrankConsole.zip>` that you will deploy on the Frank!Framework. Save it as ``franks/Frank2Manual/configurations/forFrankConsole.zip``.
#. Right-click this file and choose "Extract All...". You see the dialog shown below:

   .. image:: extractOmittingComponentForFrankConsole.jpg

#. Within this dialog, remove the last path component ``forFrankConsole`` like indicated with number 1. The zipfile itself already contains subdirectory "NewHorizons".

   .. WARNING::

      Many zipfiles you download from other places in the Frank!Manual are different. Those others do not wrap their files within a root directory. In those cases you do not remove the last path component. In this chapter we use download zips with a root directory because we need them that way in section :ref:`frankConsoleConfigsUploading`.

#. Press "Extract" (number 2).
#. Check your directory structure. It should be as shown: ::

     franks
     |- Frank2Manual
        |- configurations
           |- NewHorizons
              |- Configuration.xml
              |- ConfigurationDatabase.xml
              ...
     |- frank-runner
        |- build.properties
        ...

As said in section :ref:`frankConsoleNewHorizons`, the Frank config you are deploying processes ``.csv`` files. The directory in which they are expected is configurable by setting a property named ``work``. You will set property ``work`` to the value ``work``, a directory relative to ``franks/frank-runner``. When you do this, the example Frank configuration expects input files in directory ``work/input``. The example configuration expects that this directory exists, and also that some other directories exist.

14. Create the following directories:

    * ``franks/frank-runner/work/input``
    * ``franks/frank-runner/work/processing``
    * ``franks/frank-runner/work/processed``
    * ``franks/frank-runner/work/error``

When you start the Frank!Runner you also need to set a property named ``jdbc.migrator.active``, indicating that the Frank!Framework should create initial data. With this property set, the example configuration will create table ``product``.

15. Start the Frank!Runner with the following command: ::

      > start.bat -Djdbc.migrator.active=true -Dwork=work

    .. NOTE::

       The Frank!Runner is using Apache Tomcat under the hood. Apache Tomcat is a Java application. The arguments ``-Djdbc.migrator.active=true`` and  ``-Dwork=work`` are added to a shell command that starts up the Java Virtual Machine (JVM). If you are not using the Frank!Runner to start the Frank!Framework, there may be a different way to set properties.

#. Open a webbrowser and browse to http://localhost.
