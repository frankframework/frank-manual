
Ibis Framework
==============


Startup
-------


1e editie IBISSource Framework
------------------------------
The IAF is a framework to build integration solutions and backend applications that will run on any cloud or java 
application server. It consists of 100+ building blocks that can be configured and chained together without any programming.

Introduction
------------
Ibis is an application and an implementation of the IAF (Ibis Adapter Framework) and can be used to build backend 
applications or integration components which will run on any java machine.

Install
-------
Before you can start with the installation of the IBISSOURCE repository you need to install several tools. But very 
first of all: make a backup! Install Eclipse IDE for Java EE Developers. (64-bit Eclipse doesn't work with 32-bit JRE/JDK it will fail without any 
error message)

    `Eclipse https://www.eclipse.org/downloads/` (download 64 bit)

* Install JRE/JDK (use Java 7 or higher)

   `JRE/JDK https://www.oracle.com/technetwork/java/javase/downloads/index.html`

* Install Git and/orSourceTree

   `GIT https://git-scm.com/downloads`
   `SourceTree https://www.sourcetreeapp.com`

*Install for local use Tomcat 8.5 and Maven (is not explicitly necessary but can be very handy)

   `Tomcat 8.5 https://tomcat.apache.org/download-70.cgi`
   `Tomcat 8.5 http://maven.apache.org/download.cgi/`

Install Visual Code Studio for local use(is not explicitly necessary but can also be very handy)
   `VISUAL CODE https://code.visualstudio.com/Download`

* Create a URL link to the IBISSOURCE Java directory

   `IbisSource https://javadoc.ibissource.org/latest/`

Add the following param  use -vm in eclipse.ini 
On Windows, edit the eclipse.ini file in the program directory
On MAC Open package content of the Eclipse.app and change eclipse.ini as mentioned

Start Eclipse
-------------

Close "Welcome" screen
----------------------
* On Windows, Open Perspective, Other..., Java EE. On MAC leave it as is

* Newline settings

Make sure that the default text file line delimiter is set to Unix and default 
encoding is set to UTF-8
On Windows, Preferences, General, Workspace, New text file line delimiter: Unix, Text file encoding: UTF-8.
On Linux/MAC, idem dito

* Maven

Make sure Maven is able to access the internet. E.g. when behind a proxy
On Windows, Preferences, Maven, User Settings, settings.xml should exist and contain proxy configuration.
On MAC, idem dito

* AWS-Git, logon AWS (use id and username/password) via a browser

* Switch to AWS-CodeCommit

* Search for the repository you need/want to download

* Choose HTTPS option

Download with a GIT tool (SourceTree is a simple and handy option)
On Window, Open Perspective, Other..., Git, OK

Start working
-------------
The following tips/tricks and command are necessary to load a project and start working with it.

Start Eclipse
-------------
Be sure Tomcat is installed and reachable via eclipse
* Chose for version 8.5
Double click Tomcat v8.5 Server at localhost, 
Open launch configuration, Arguments, VM arguments, add -Dotap.stage=LOC, OK (your working and testing environment for Ibis4 Frameworks applications is now LOC. If you want to work in PRD please change the dot.stage)

Load project
------------
Be sure that the .project info is sufficient
* Switch to Navigator tab

Right-mouse click
Choose import

* Switch to the directory where the project or git repository is stored

Adjust the code where needed and save

Before compiling and Running
----------------------------
* Set proper project settings

Double click on project in Navigator tab
* Click on Properties

* Click on Project Facets

Choose Active Dynamic Web Module (2.3 / 3.0)(needed for WEB)
And choose Java (1.8)

Set proper Tomcat settings
--------------------------
Double click Tomcat v8.5 Server at localhost,
Choose the module tab
Add Web Module (add module and choose the added project)

the POM.XML
-----------
Compile and build project (use pom and maven)
Start the project on your local machine via starting Tomcat in servers map
Open a webbrowser and go to http://localhost:8080/ibis4project/ to check if ibis4project is running

Troubleshooting
---------------
In some cases you might want/need to:

Right click ibis4project, Maven, Update Project..., OK.
Enable Project, Build Automatically
Right click Tomcat 8.5 Server at localhost, Clean...
Change newlines in .classpath and org.eclipse.wst.common.component files back to Unix newlines.
Rightclick pom.xml (in ibis4project), Run As, Maven build..., JRE, make sure a JDK (not a JRE) is used, 
Refresh, Refresh resources upon completion,
The local Maven repository might contain corrupt jar files which for example will result in java.lang.NoClassDefFoundError: org/aspectj/lang/ProceedingJoinPoint when starting Tomcat. Remove the jar file from the repository to make Maven download the file again.
Sometimes the m2e tool crashes during the download resulting in corrupted overlays. You can resolve this by cleaning the target/m2e-wtp/overlays directory.

Command-line interface
----------------------
If the user wants to perform the mentioned commands and action o  the prompt (Linux or Mac OSx) the following commands are needed:

* git clone https://github.com/ibissource/ibis4template
* mvn package
* mvn jetty:run

browser> http://localhost:8080/

After modifying a project (pom.xml) file:
* ctrl-c
* cd .. ; mvn clean install ; cd example ; mvn jetty:run
