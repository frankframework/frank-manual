.. _configurationSyntaxChecking:

Syntax Checking and the Frank!Doc
=================================

Introduction
------------

In this section, you learn how to reach some additional resources that help you to write correct Frank configs. You will gain access to an additional source of documentation, the Frank!Doc, which you can reach through the Frank!Console. Frank configurations are written in XML. They satisfy an XML Schema, the Frank configuration schema, which can be downloaded from the Frank!Console. You will learn how to use this schema when you type your Frank configuration. You will have automatic code completion and tooltips in your text editor.

Preparation
-----------

Please do the following preparations:

#. If you did not do so, set up your ``Frank2Manual`` instance of the Frank!Framework as explained in the previous section.
#. Ensure that you have a file ``ConfigurationExample1Adapter.xml`` with the following contents:

   .. code-block:: XML

      <Module
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="./FrankConfig.xsd">
        <Adapter name="Example1Adapter">
          <Receiver name="Example1Receiver">
            <JavaListener name="Example1" serviceName="Example1"/>
          </Receiver>
          <Pipeline firstPipe="Example">
            <FixedResultPipe name="Example" returnString="Hello World1">
              <Forward name="success" path="EXIT"/>
            </FixedResultPipe>
            <Exit path="EXIT" state="success"/>
          </Pipeline>
        </Adapter>
      </Module>

   You should have this file if you successfully followed the instructions of the previous section. You will try syntax checking by editing this file in Visual Studio Code or Eclipse.

Frank configuration schema
--------------------------

Please do the following to download the Frank configuration schema:

#. Click "Webservices" as shown in the figure below:

   .. image:: webservicesMenu.jpg

#. Click "IbisDoc":

   .. image:: webservicesPage.jpg

#. Right-click "ibisdoc.xsd" (number 1 in the picture below):

   .. image:: ibisDocFiles.jpg

#. A menu appears that lets you choose what to do with "ibisdoc.xsd".
#. Put file ``ibisdoc.xsd`` in the same directory as ``ConfigurationExample1Adapter.xml``.

Frank!Doc
---------

From the screen shown at step 3, you can access the Frank!Doc, an additional source of documentation. It lets you search pipes, senders and receivers and it gives you detailed information.

6. In the picture of step 3, press "The new ibisdoc application" (number 2). The following screen appears:

   .. image:: frankDoc.jpg

#. As an example, we want to see detailed information about the ``<FixedResultPipe>``. To the top-left, click "Pipes" (number 1). To the bottom-left, all available pipes are listed.
#. Click "FixedResult" (number 2). To the right, a page with detailed information appears. To the top it confirmst that it is about FixedResult (number 3). You see the attribute you know already, "returnString" (number 4).
#. Each pipe, sender or receiver corresponds to a Java class in the source code of the Frank!Framework. You can see the Javadoc documentation of this class by clicking "Javadoc" (number 5). This information is written for Java developers, but it may be useful sometimes for Frank developers.

Try code completion
-------------------

For code completion, you need to configure your text editor. Below, Visual Studio Code and Eclipse are covered.

Visual Studio Code
------------------

Please do the following to configure Visual Studio Code for code completion:

#. Press the plugin menu item (number 1 in the figure below).

   .. image:: visualStudioCodePlugins.jpg

#. Install the two plugins shown (number 2).
#. Open ``ConfigurationExample1Adapter.xml``.
#. Please look at the bottom-right corner. Do you see the following dialog?

   .. image:: vsCodeJava8Required.jpg

#. If you see this dialog, you have to install the Java Development Kit version 8 as is explained in the following steps. If you do not see the dialog, you can proceed to step 9.
#. If you already have Java 8, proceed to step 8.
#. Press the button and follow the instructions to download the Red Hat OpenJDK. Alternatively, you may follow the instructions of https://code.visualstudio.com/docs/java/java-tutorial.
#. The instructions in the previous step should have asked you to set the ``JAVA_HOME`` environment variable. You may have missed that, so we also tell you how to set ``JAVA_HOME`` here. Please do the following:

   a. Figure out the path of your ``java.exe`` executable. This path should end with ``\bin\java.exe``. Please omit this last part to get the value you need for ``JAVA_HOME``. For example, if the path is ``C:\Program Files\Java\jdk1.8.0_251\bin\java.exe``, then the value you need is ``C:\Program Files\Java\jdk1.8.0_251``. Remember this value.
   #. If you have Windows 10, go to Windows Settings. You should see the page shown below. Type "environment" in the search field (if your Windows language is English) and select "Edit the system environment variables".

      .. image:: windowsSettings.jpg

   #. You see the dialog shown below. 

      .. image:: systemProperties.jpg

   #. Click "Environment Variables...". You should see the dialog shown below:

      .. image:: environmentVariables.jpg
   
   #. Select one of the "New..." buttons. You see the dialog shown below:

      .. image:: javaHome.jpg
   
   #. In the "Variable name" field, fill in ``JAVA_HOME``.
   #. In the "Variable value" field, fill in the value you determined in step a).
   #. Press "OK". Close all the dialogs by pressing "OK".
   #. If you are opening Visual Studio Code from a command prompt, please restart that command prompt. Otherwise, your new environment variable is not applied. Also restart Visual Studio Code itself.

#. After the ``</Adapter>`` element close tag, start typing ``<A``. The editor should give you a hint that you mean ``<Adapter>``. You should also see a "i" icon to get more information.

Eclipse
-------

Please do the following to configure Eclipse for code completion:

#. Open Eclipse and choose the workspace you want.
#. In the menu, choose File | New | Project... . The New Project dialog appears (number 1 in the figure below):

   .. image:: eclipseNewProject.jpg

#. Choose "Project" (number 2) and press "Next".
#. Enter a project name (number 1 in the figure below). Uncheck "Use default location" (number 2). Browse (number 3) to ``Frank2Manual``. Press "Finish".

   .. image:: eclipseNewProjectNext.jpg

#. A new project has appeared in your project explorer (number 1 in the fingure below). You may see a cross before your XML files (number 2). If this is the case, you are using the standard XML editor of Eclipse.

   .. image:: eclipseProjectExplorer.jpg

The standard XML editor of Eclipse may crash if you use it with XML schema ``ibisdoc.xsd``. This XML schema may be too large for the XML editor. You can fix this by installing the Wild Web Developer plugin, which enhances the generic text editor to properly process XML. Please continue as follows:

6. Update your Eclipse plugins. If you use outdated plugins, your installation may fail.
#. In the Eclipse main menu, choose Help | Eclipse Marketplace... . The dialog shown below opens.

   .. image:: installWWD.jpg

#. You see your are in the right dialog (number 1). Type ``wild web developer`` in the search field (number 2).
#. You should see the plugin in the search results (number 3). Press "install" (number 4).
#. Follow the dialog to do the installation.
#. Restart Eclipse.
#. In the Eclipse main menu, choose Window | Preferences.
#. You can see you are in the Preferences dialog (number 1). Go to "File Associations" (number 4). You find it under "General" (number 2) and "Editors" (number 3).

   .. image:: goToFileAssociations.jpg

#. You can verify you have the right screen (number 1 in the figure below). Here you can link file types to editors provided by Eclipse. Go to "\*.xml" (number 2). If you do not see it, you can use the "Add..." button (number 3).

   .. image:: fileAssociationsFileTypes.jpg

#. Make the "Generic Text Editor" (number 1 in the figure below) the default using the button (number 2).

   .. image:: chooseDefaultEditor.jpg

#. Restart Eclipse.
#. In your project explorer, you see that the new editor is used for your XML files, see below:

   .. image:: verificationNewEditor.jpg

#. You can see what editor is being used in an editor tab, see below. To use the newly chosen text editor, you have to close all your open XML files and reopen them again.

   .. image:: oldEclipseEditor.jpg

#. Open "ConfigurationExample1Adapter.xml".
#. After the ``</Adapter>`` closing tag, please start typing ``<Ad``. Eclipse should present a hint that you mean ``<Adapter>``.
