.. _advancedDevelopmentDeploymentMavenExecuteJar:

Execute program
===============

1. Please save the example project of the previous subsection somewhere. In the next subsection, you will start again from the code you have now.
#. Add a plugin to your ``pom.xml`` that can execute Java programs using the Java Virtual Machine. Update ``pom.xml`` as shown below:

   .. include:: ../../snippets/mavenWebapp/v510/addPlugin.txt

References to plugins are nested within XML tags ``<build>`` and ``<plugins>`` instead of ``<dependencies>``. The plugin added is org.codehaus.mojo:exec-maven-plugin:3.0.0. This is a little program that needs additional information. That information appears within the ``<configuration>`` tag. The tags that can appear within ``<configuration>`` are plugin specific. Information about them can be found on the internet. For the plugin added here, see for example `https://www.mojohaus.org/exec-maven-plugin/ <https://www.mojohaus.org/exec-maven-plugin/>`_.

The plugin has goal ``java``. This goal is not linked to a build phase, so it will not execute when you execute a phase in Maven. You have to execute the ``java`` goal explicitly. You might do this like ``mvn org.codehaus.mojo:exec-maven-plugin:java``, but the plugin allows for a shorthand notation: ``mvn exec:java``.

.. NOTE::

   You saw a group id ``org.codehaus.mojo``. The letters "MOJO" stand for "Maven Old Java Object". Maven plugins are coded in Java themselves, and a MOJO is a Java class that satisfies additional requirements; these requirements allow it to be a Maven plugin. A Java class that does not satisfy any additional requirements is named a "Plain Old Java Object" (POJO). The term POJO was coined when application servers (see subsection :ref:`advancedDevelopmentDeploymentMavenMavenWebapp`) matured. In the past, application servers could only interact with Java classes that satisfied additional requirements. Modern application servers can work with POJOs.

3. On a command prompt, do ``mvn clean install exec:java``. Check that the output includes the line ``HELLO WORLD!``, the output of our program.

   .. NOTE::

      This command does not invoke the JVM directly. Maven is itself a Java program, so Maven is running on a JVM. That execution of the JVM loads our Java classes on the classpath and then executes them. If you want to know more, you can search the internet to learn about class loaders.
