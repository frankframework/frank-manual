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
        xsi:noNamespaceSchemaLocation="./ibisdoc.xsd">
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

From the screen shown at step 2, you can access the Frank!Doc, an additional source of documentation. It lets you search pipes, senders and receivers and it gives you detailed information.

6. In the picture of step 3, press "The new ibisdoc application" (number 2). The following screen appears:

   .. image:: frankDoc.jpg

#. As an example, we want to see detailed information about the ``<FixedResultPipe>``. To the top-left, click "Pipes" (number 1). To the bottom-left, all available pipes are listed.
#. Click "FixedResultPipe" (number 2). To the right, a page with detailed information appears. To the top it confirmst that it is about FixedResultPipe (number 3). You see the attribute you know already, "returnString" (number 4).
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
#. Open ``ConfigurationExample1Adapter.xml``. After the ``</Adapter>`` element close tag, start typing ``<A``. The editor should give you a hint that you mean ``<Adapter>``. You should also see a "i" icon to get more information.

Eclipse
-------

Please do the following to configure Eclipse for code completion:

#. Open Eclipse and choose the workspace you want.
#. In the menu, choose File | New | Project... . The New Project dialog appears (number 1 in the figure below):

   .. image:: eclipseNewProject.jpg

#. Choose "Project" (number 2) and press "Next".
#. Enter a project name (number 1 in the figure below). Uncheck "Use default location" (number 2). Browse (number 3) to ``Frank2Manual``. Press "Finish".

   .. image:: eclipseNewProjectNext.jpg

#. A new project has appeared in your project explorer (number 1 in the fingure below). Please open ``ConfigurationExample1Adapter.xml`` (number 2).

   .. image:: eclipseProjectExplorer.jpg

#. After the ``</Adapter>`` closing tag, please start typing ``<Ad``. Eclipse should present a hint that you mean ``<Adapter>``.
