.. _frankRunnerInstallation:

Frank!Runner Installation
=========================

.. _frankRunnerInstallationInstallation:

Installation and start-up
-------------------------

The Frank!Runner allows you to easily start the Frank!Framework. In this section you will install and start the Frank!Runner. The Frank!Runner contains examples. You will study these examples to get a first impression of the Frank!Framework.

Please do the following:

.. highlight:: none

#. If you do not have git already, download it from https://git-scm.com/downloads.
#. Choose some working directory in which you will install the Frank!Runner and do the exercises of the Frank!Manual, say ``franks``.
#. In a command prompt, go to your ``franks`` directory and clone the Frank!Runner with the following command: ::

     franks> git clone https://github.com/ibissource/frank-runner

#. Check your directory structure. It should look as follows: ::

     franks
     |- frank-runner
        |- ...
        |- examples
           |- Frank2Example1
              |- configurations
                 |- Example1
                    |- Configuration.xml
                    |- StageSpecifics_LOC.properties
                 |- Example2
                    |- Configuration.xml
              |- tests
                 |- ...
           |- Frank2Example2
              |- classes
                 |- ...
              |- configurations
                 |- ...
              |- tests
                 |- ...
        |- ...

#. Check that you do NOT have ``franks/frank-runner/build.properties`` at this point. You will study the default Frank, which is in the directory ``franks/frank-runner/examples/Frank2Example1``.
#. Start the Frank!Runner as explained in its ``README.md`` file, for example by running ``franks/frank-runner/start.bat``.

The main menu
-------------

7. Start a webbrowser and browse to http://localhost. To the left, you see the following menu:

   .. image:: mainMenuExtended.jpg

#. By default, you are in the "Adapter Status" page (number 1). You also see "Testing" (number 2). Please click it to expand it.
#. You see "Larva", "Ladybug", "Test Pipeline" and "Test serviceListener". You will examine the first three of these in this :ref:`gettingStarted`.
#. You also have "JDBC" (number 3), which stands for "Java DataBase Connectivity". This link can also be expanded by clicking it. Here you can find pages to manage your database.
#. You will soon examine the "Webservices" page (number 4). Here you can find some resources that help you to write proper Frank configurations.
#. Finally, the "Environment Variables" page (number 5) is relevant. Here you can find many properties configured within your Frank.

General structure of the example Frank
--------------------------------------

Let us now investigate the general structure of the ``Frank2Example1`` application, or as we say the ``Frank2Example1`` Frank. 

13. Look at the "Adapter Status" page. You see you really do have the ``Frank2Example1`` Frank (number 2 in the figure below):

    .. image:: adapterStatusTopLeft.jpg

#. You also see which version of the Frank!Framework you are using (number 1).

   .. NOTE::

      You will encounter words like Ibis and IAF a lot. WeAreFrank! was recently renamed, which was a good moment to rename their products. Implementing these name changes is not yet finished. The words are related to the old names.

#. You saw earlier that the directory ``franks/frank-runner/examples/Frank2Example1/configurations`` has two subdirectories, namely ``Example1`` and ``Example2``. These appear as tabs (number 3 and number 4). These are Frank configurations.

Frank configurations are meant to be independent of the Frank!Framework instance on which they are deployed. This situation is comparable to software packages in general, which are independent of the specific server on which they are deployed. An example of a software package is Microsoft Word. Everyone who wants this application uses the same installer, independent of the computer on which Microsoft Word is installed.

You as a Frank developer develop a Frank config, which plays the role of a software package in the above metaphor. When you are done, you hand over your Frank config to your customer. The customer has her own production instance of the Frank!Framework, which plays the role of the server. The system administrator deploys your Frank config on the production instance. She can fine-tune the behavior of your Frank config by adding additional configurations on the instance level.

.. NOTE::

   This is a simplified view of the life cycle of a Frank config. Professional Frank developers typically apply Continuous Delivery and Continuous Deploy (CI/CD).

16. To examine the details of a Frank configuration, choose tab "Example2" (number 4 in the figure of step 13). You see the following:

    .. image:: adapterStatusExample2.jpg

#. Please hover over the icons shown as number 1 to number 5. They mean "Started", "Starting", "Stopped", "Stopping", "Error". You see here how many adapters you have and you see for each state how many are in that state. You get a general overview of the health of your configuration.
#. In the row "Adapters", you see "Example2Adapter" (number 6). An adapter is comparable to a subroutine or method in a programming language. An adapter processes an incoming message, typically an XML document, and produces output. The meaning of "Receivers" will be explained in the next section.
#. As a Frank developer, you will be very glad with the following feature. You can reload Frank configs without restarting the Frank!Framework. To do this, press the button labeled with number 1 in the figure below:

   .. image:: adapterStatusTopRight.jpg

#. The button changes while the Frank!Framework is busy reloading. When the icon changes back then the Frank!Framework is done.
#. The button labeled with number 2 is also relevant. It expands all adapters to show you detailed information. You will need it when you work with Larva, see section :ref:`gettingStartedLarva`.

The sources of your Frank configs
---------------------------------

System administrators may want to check the sources of the Frank configs they see. Doing this is also relevant for Frank developers who want to debug their work. Please do the following:

22. In the main menu, choose "Environment Variables" (number 5 in the figure below).

    .. image:: mainMenuExtended.jpg

#. Press Ctrl-F to search on this page. In the search field, type ``configurations.names``. Iterate over the search results until you see the following properties: "configurations.directory", "configurations.Example1.classLoaderType", "configurations.Example2.classLoaderType" and "configurations.names".

   .. NOTE::

      These properties have been set by the Frank!Runner. If you deploy your Frank config another way, you may have to care about these properties yourself.

#. Property "configurations.names" has value "Example1,Example2", confirming that you have these two Frank configs (excluding the predefined configurations).
#. Property "configurations.Example1.classLoaderType" has value "DirectoryClassLoader". This means that configuration "Example1" comes from the file system of the computer running the Frank!Framework. Frank configurations can also be deployed on the database, resulting in a different value for this property. Property "configurations.Example2.classLoaderType" also has value "DirectoryClassLoader", confirming that Frank config "Example2" also comes from the local file system.
#. Property "configurations.directory" has value ``absolute-path-of-directory-franks\frank-runner\..\frank-runner\examples\Frank2Example1\configurations``, the "configurations" directory under the "examples/Frank2Example1" instance. This is the default directory for Frank configs with classLoaderType "DirectoryClassLoader".

Summary
-------

The Frank!Runner allows you to quickly start the Frank!Framework. After starting it, you can visit its Graphical User Interface, the Frank!Console. The Frank!Console shows you what Frank configurations have been deployed and where there sources are located. A Frank configuration can be compared to a computer program which is independent of the computer on which it is deployed. The role of the computer is played by an instance of the Frank!Framework. The Frank!Framework can host multiple Frank configs, each being presented in its own tab on the Adapter Status page. The Adapter Status page shows that a Frank configuration contains adapters. An adapter receives messages and produces output, making it comparable to a subroutine in a programming language. The Adapter Status page shows the status of your adapters and so-called "receivers", which are explained later. Finally, you can use the Adapter Status screen to reload your Frank configs without restarting the Frank!Framework. This will save you a lot of time.