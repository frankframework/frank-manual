.. _advancedDevelopmentDeploymentMavenExecuteJar:

Execute jar
===========

1. Please save the example project of the previous subsection somewhere. In the next subsection, you will start again from the code you have now.
#. Add a plugin to your ``pom.xml`` that can execute Java programs using the Java Virtual Machine. Update ``pom.xml`` as shown below:

   .. include:: ../../snippets/mavenWebapp/v510/addPlugin.txt

References to plugins are nested within XML tags ``<build>`` and ``<plugins>`` instead of ``<dependencies>``. The plugin added is org.codehaus.mojo:exec-maven-plugin:3.0.0. This is a little program that needs additional information. That information appears within the ``<configuration>`` tag. The tags that can appear within ``<configuration>`` are plugin specific. Information about them can be found on the internet. For the plugin added here, see for example `https://www.mojohaus.org/exec-maven-plugin/ <https://www.mojohaus.org/exec-maven-plugin/>`_.

The plugin has goal ``exec``. This goal is not linked to a build phase, so it will not execute when you execute a phase in Maven. You have to execute the ``exec`` goal explicitly. You might do this like ``mvn org.codehaus.mojo:exec-maven-plugin:exec``, but the plugin allows for a shorthand notation: ``mvn exec:exec``.

3. On a command prompt, do ``mvn clean install exec:exec``. Check that the output includes the line ``HELLO WORLD!``, the output of our program.

Maven has two command-line options: ``-e`` to show errors and ``-X`` to show debug information.

4. Do ``mvn -e -X exec:exec``.

The output should include:

.. code-block:: none

   [DEBUG] Executing command line: [C:\Program Files (x86)\Common Files\Oracle\Java\javapath\java.exe, -classpath, C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v510\target\classes;C:\Users\martijn\.m2\repository\org\apache\commons\commons-lang3\3.12.0\commons-lang3-3.12.0.jar, org.wearefrank.maven.webapp.example.Main]

The output is a comma-separated list of the arguments used to start ``java.exe``. You see here that ``java.exe`` was executed like this:

.. code-block:: none

   C:\Program Files (x86)\Common Files\Oracle\Java\javapath\java.exe -classpath C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v510\target\classes;C:\Users\martijn\.m2\repository\org\apache\commons\commons-lang3\3.12.0\commons-lang3-3.12.0.jar org.wearefrank.maven.webapp.example.Main

5. Please run this command directly on a command prompt. You may have to quote some words and you may have to adjust some directory names depending on your operating system and your work directory.

The ``java.exe`` executable that starts the JVM has an option ``-classpath``. That option takes a list of directories that are used to populate the classpath. The classpath is obtained by merging the ``classes`` directory of our artifact and the extracted ``.jar`` file of artifact ``org.apache.commons:commons-lang3:3.12.0``. Finally, the name of the class is given that has the ``main`` method to be executed.

Java webapplications are not executed by the JVM directly. Instead, an application server like Apache Tomcat is run in which webapplications are deployed. An application server offers additional services that allow operators to configure the webapplication without the need to rebuild it. This is the subject of the next subsection.
