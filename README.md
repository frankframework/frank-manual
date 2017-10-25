# IBIS starterkit
=====================

## Purpose
The ibis4example project is meant as a starterkit for creating a new ibis applications. 
## What is ibis
An ibis is an application is an implementation of the IAF (Ibis Adapter Framework) and can be used to build backend applications or integration component wich will run on any java machine

## Getting started
Eclipse
=======

- Download and unzip
  [Eclipse Kepler SR2](http://eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/keplersr2)
  (64-bit Eclipse doesn't work with 32-bit JRE/JDK (doesn't start without any
  message)).
- Start Eclipse with Java 7. You might want to
  [use -vm in eclipse.ini](http://wiki.eclipse.org/Eclipse.ini#Specifying_the_JVM).
- Close Welcome.
- _Feel free to use other versions of eclipse and Java but you might run into unexpected issues (maven version, cvs support etc)_ 
- Make sure that the default text file line delimiter is set to Unix and
  default encoding is set to UTF-8: Window, Preferences, General, Workspace,
  New text file line delimiter: Unix, Text file encoding: UTF-8.
- Make sure Maven is able to access the internet. E.g. when behind a proxy:
  Window, Preferences, Maven, User Settings, settings.xml should exist and
  contain proxy configuration.
- Window, Open Perspective, Other..., Git, OK, Clone a Git repository,
  URI: https://github.com/ibissource/ibis4example.git, Next, Next, Finish.
- Window, Open Perspective, Other..., Java EE.
- Servers, No servers are available. Click this link to create a new server...,
  Apache, Tomcat v7.0 Server, Next, Browse..., select the root folder of a
  Tomcat installation (when not available download
  [Tomcat](http://tomcat.apache.org/) (version 7.0.22 is known to work, but
  other version are expected to work too)), OK, Finish.
- Double click Tomcat v7.0 Server at localhost, Open launch configuration,
  Arguments, VM arguments, add ```-Dotap.stage=LOC```, OK, Modules, Add Web Module...,
  iaf-example, OK, File, Save
- Right click Tomcat v7.0 Server at localhost, Start.
- Browse the IAF console at
  [http://localhost:8080/ibis4example/](http://localhost:8080/ibis4example/).

In some cases you might want/need to:

- Rightclick ibis4example, Maven, Update Project..., OK.
- Enable Project, Build Automatically
- Right click Tomcat v7.0 Server at localhost, Clean...
- Change newlines in .classpath and org.eclipse.wst.common.component files
  back to Unix newlines.
- Rightclick pom.xml (in ibis4example), Run As, Maven build..., JRE, make sure a JDK
  (not a JRE) is used (use Java 1.6 to compile with the minimal Java version for
  the IAF project), Refresh, Refresh resources upon completion,
  Specific resources, Specify Resources..., iaf (Using "The project containing
  the selected resource" doesn't seem to work), Finish, Run.
- The local Maven repository might contain corrupt jar files which for example
  will result in java.lang.NoClassDefFoundError:
  org/aspectj/lang/ProceedingJoinPoint when starting Tomcat. Remove the jar file
  from the repository to make Maven download the file again.



IntelliJ
========

- Clone this any way you like. E.g. at the commandline: git clone git@github.com:ibissource/ibis4example.git
- File -> Open project, and select the pom.xml which just appeared.
- To use git via intellij you need to install the git and/or github plugin.
- You can add a tomcat configuration via Run-> Edit Configuration -> + -> Tomcat Server -> Local -> Add example webapp under deployments tab.
- Run it



Command-line interface
======================

Initial:

- git clone https://github.com/ibissource/ibis4example
- cd ibis4example
- mvn
- cd example
- mvn jetty:run
- [http://localhost:8080/](http://localhost:8080/)


After modifying a project file:

- ctrl-c
- cd .. ; mvn clean install ; cd example ; mvn jetty:run

The jetty-maven-plugin requires Maven 3 and Java 1.7.
