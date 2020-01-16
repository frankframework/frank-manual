.. _horizonsMultipleFiles:

Configuration Management
========================

Introduction
------------

In subsections :ref:`helloIbis` to :ref:`gettingStartedLarva`, you got a basic understanding of the Frank!Framework. You used the Tomcat4Ibis project to run the Frank!Framework and you worked with the example configurations in that project. You learned the basic concepts by studying these configurations. You ran the framework and learned how configurations can be executed and tested.

In this section you start your own project and you build your first configuration. Frank configurations are written in XML. They satisfy an XML Schema that can be downloaded from the Frank!Framework. You will learn how to use this schema when you type your Frank configuration. You will have automatic code completion and tooltips in your text editor.

Initialize your project
-----------------------

.. highlight:: none

After installing Tomcat4Ibis, you should have a folder ``projects`` with a folder ``tomcat4ibis`` inside. This ``tomcat4ibis`` folder is your checkout of Tomcat4Ibis. Please continue as follows:

#. Within the ``projects`` directory, create a subdirectory ``gettingStarted``. Please create subdirectories of ``gettingStarted`` to arrive at the following directory structure: ::

     projects
     |- tomcat4ibis
     |- gettingStarted
        |- classes
        |- configurations
        |- tests

#. The directory ``classes`` contains code that is common to all Frank configurations within your Frank. The ``tests`` folder holds Larva tests while each configuration is within a subdirectory of ``configurations``.
#. You want the Frank!Framework to run ``gettingStarted`` when you start it. To achieve this, create file ``build.properties`` within the ``tomcat4ibis`` directory. Give ``build.properties`` the following contents: ::

     project.dir=gettingStarted

#. The Frank!Framework expects a Frank configuration within the ``classes`` directory for historical reasons. You do not want your real Frank configurations there because the ``classes`` folder is for common code of all your configurations. Within your ``classes`` directory, add a ``Configuration.xml`` file with the following contents:

   .. code-block:: XML

      <Configuration name="${instance.name}">
        <jmsRealms>
          <jmsRealm datasourceName="jdbc/${instance.name.lc}" realmName="jdbc"/>
        </jmsRealms>
      </Configuration>

#. The Frank!Framework does not automatically detect what configurations you have. In your ``classes`` directory, please add property file ``DeploymentSpecifics.properties`` with the following contents: ::

     instance.name=gettingStarted
     configurations.names=${instance.name}
   
   .. NOTE::

      There is much to know about properties, which is explained in section :ref:`properties`. If you read this chapter for the first time, please finish it first. For now, just note that property ``configuration.names`` contains a list of all your configurations. The empty configuration you just added is referenced as ``${instance.name}``, the value of property ``instance.name``.

#. The Frank!Framework can be configured differently for different stages in your development cycle (local, development, test, acceptance and production). During development, you want to initialize your database automatically. To do this, introduce file ``classes\StageSpecifics_LOC.properties``. Add the following line: ::

     jdbc.migrator.active=true

#. During development, you also want to run Larva tests. To run Larva tests, the Frank!Framework needs to process changed versions of your Frank configurations (your files are not changed; they are changed in memory after the Frank!Framework reads them). Please extend ``classes\StageSpecifics_LOC.properties`` to tell the Frank!Framework you want this. The file should be updated to: ::

     jdbc.migrator.active=true
     stub4testtool.configuration=true

#. You will download the Frank configuration schema now. Please start the Frank!Framework by running ``tomcat4ibis\tomcat4ibis.bat`` (Windows) or ``tomcat4ibis/tomcat4ibis.sh`` (Linux).
#. Click "Webservices" as shown in the figure below:

   .. image:: webservicesMenu.jpg

#. Click "IbisDoc":

   .. image:: webservicesPage.jpg

#. Right-click "ibisdoc.xsd" as shown below:

   .. image:: ibisDocFiles.jpg

#. A menu appears that lets you choose what to do with "ibisdoc.xsd". Please choose to download it. You will need it later.

Add your configuration
----------------------

Now that you have your project, you can add your real Frank configuration to your ``gettingStarted`` project. Please proceed as follows:

#. Update your file ``classes\DeploymentSpecifics.properties`` to list a new configuration ``NewHorizons``. It should become as follows: ::

     instance.name=gettingStarted
     configurations.names=${instance.name},NewHorizons

#. Within your ``configurations`` directory, please add subdirectory ``NewHorizons``.
#. A configuration usually requires many lines of XML. It is good practice to split a configuration over multiple files. This is done using entity references. Please create ``configurations\NewHorizons\Configuration.xml`` with the following contents:

   .. code-block:: XML

      <?xml version="1.0" encoding="UTF-8" ?>
      <!DOCTYPE configuration [
        <!ENTITY Hello SYSTEM "ConfigurationHello.xml">
      ]>
      <Configuration name="NewHorizons">
        &Hello;
      </Configuration>

#. This Configuration.xml does a literal include of file ``ConfigurationHello.xml``. Please add ``configurations\NewHorizons\ConfigurationHello.xml`` with the following contents:

   .. literalinclude:: ../../../src/gettingStarted/configurations/NewHorizons/ConfigurationHello.xml
      :language: xml
      :emphasize-lines: 1, 2, 3, 9

#. Please look at ``ConfigurationHello.xml`` for a moment. Line 1 wraps your adapter in the ``<Module>`` tag. This tag does not have a meaning. Its purpose is to arrive at valid XML, also if your include file has multiple adapters. The ``<Module>`` tag is also expected by the XML schema ``ibisdoc.xsd``. Code completion will not work without the ``<Module>`` tag.
#. Lines 2 and 3 are needed to tell your text editor to check against XML schema file ``ibisdoc.xsd``. You downloaded that file earlier. Please copy it now to ``configurations\NewHorizons\ibisdoc.xsd``, making it a brother of ``ConfigurationHello.xml``.
#. Line 9 (also highlighted) holds the output string of your Hello World adapter. It reads ``Hello Docker World``.
#. Please restart Tomcat4Ibis. Run your "HelloDockerWorld" adapter in the Test Pipeline screen and check that the output is ``Hello Docker World``. If this is the case, you succeeded doing this tutorial.
#. If something is wrong, please compare your files with the examples of docker4ibis, or with the :download:`solution <../downloads/gettingStarted.zip>`.

Try code completion
-------------------

For code completion, you need to configure your text editor. Below, Visual Studio Code and Eclipse are covered.

Visual Studio Code
------------------

Please do the following to configure Visual Studio Code for code completion:

#. Press the plugin menu item (number 1 in the figure below).

   .. image:: visualStudioCodePlugins.jpg

#. Install the two plugins shown (number 2).
#. Open ``ConfigurationHello.xml``. After the ``</Adapter>`` element close tag, start typing ``<A``. The editor should give you a hint that you mean ``<Adapter>``. You should also see a "i" icon to get more information.

Eclipse
-------

Please do the following to configure Eclipse for code completion:

#. Open Eclipse and choose the workspace you want.
#. In the menu, choose File | New | Project... . The New Project dialog appears (number 1 in the figure below):

   .. image:: eclipseNewProject.jpg

#. Choose "Project" (number 2) and press "Next".
#. Enter a project name (number 1 in the figure below). Uncheck "Use default location" (number 2). Browse to the folder you want to edit (number 3), for example ``projects\gettingStarted``. Press "Finish".

   .. image:: eclipseNewProjectNext.jpg

#. A new project has appeared in your project explorer (number 1 in the fingure below). Please open ``ConfigurationHello.xml`` (number 2).

   .. image:: eclipseProjectExplorer.jpg

#. After the ``</Adapter>`` closing tag, please start typing ``<Ad``. Eclipse should present a hint that you mean ``<Adapter>``.
