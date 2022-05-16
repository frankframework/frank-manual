.. _advancedDevelopmentDeploymentMavenMavenBasics:

Maven basics
============

Write program
-------------

Maven can best be introduced using a simple Hello World application. Please do the following:

1. Choose some work directory, say ``work``.
#. Within ``work``, create folder ``src/main/java``. This is where Maven expects Java sources.
#. Within ``work/src/main/java``, open ``org/wearefrank/maven/webapp/example/Main.java``. Populate it with the following text:

   .. literalinclude:: ../../../../srcSteps/mavenWebapp/v500/src/main/java/org/wearefrank/maven/webapp/example/Main.java

This is a program that should be started from the command line. It simply prints "HELLO WORLD!". To demonstrate Maven, a dependency has been introduced. This program needs Java class ``org.apache.commons.lang3.StringUtils``.

In the next steps, a file ``pom.xml`` is added that tells Maven how to compile this program.

4. Within ``work``, open a file ``pom.xml``. Start it as follows:

   .. literalinclude:: ../../../../srcSteps/mavenWebapp/v480/pom.xml
      :language: XML

The first two lines are the same for every ``pom.xml`` file. Next come three lines with tags ``<groupId>``, ``<artifactId>`` and ``<version>``. These are collectively referenced as **Maven coordinates**. The Maven coordinates are the unique identifier of an **artifact**. Artifacts are the basic building blocks that are combined by Maven during compilation and linking. The three lines identify the artifact that is built by this project. Use the ``<groupId>`` as a common name for all artifacts produced by your organization or your team. It is used to distinguish your artifact from artifacts produced by other organizations. The ``<artifactId>`` distinguishes your artifact from the ohter artifacts with the same ``<groupId>``. Finally, the ``<version>`` is the version of your artifact.

5. Extend ``pom.xml`` as shown:

   .. include:: ../../snippets/mavenWebapp/v490/pomAddJavaVersion.txt

   This tells Maven that the Java sources were written with Java 8, and that the code is to be executed with Java 8.
#. Conclude ``pom.xml`` by adding a dependency. You add the dependency that references the artifact that holds class ``org.apache.commons.lang3.StringUtils``:

   .. include:: ../../snippets/mavenWebapp/v500/pomDependencies.txt

Build program
-------------

The program is complete. Start building it as follows:

7. Open a command prompt and browse to your ``work`` directory.
#. Type ``mvn clean``.

The output should look like this:

.. code-block:: none

   C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v500>mvn clean
   [INFO] Scanning for projects...
   [INFO]
   [INFO] -----------------< org.ibissource:mavenWebappExample >------------------
   [INFO] Building mavenWebappExample 1.0-SNAPSHOT
   [INFO] --------------------------------[ jar ]---------------------------------
   [INFO]
   [INFO] --- maven-clean-plugin:2.5:clean (default-clean) @ mavenWebappExample ---
   [INFO] Deleting C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v500\target
   [INFO] ------------------------------------------------------------------------
   [INFO] BUILD SUCCESS
   [INFO] ------------------------------------------------------------------------
   [INFO] Total time:  0.204 s
   [INFO] Finished at: 2022-05-10T18:06:56+02:00
   [INFO] ------------------------------------------------------------------------

   C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v500>

Maven distinguishes build phases. The ``mvn clean`` command tells maven to execute build phase ``clean``. Maven delegates everything it does to plugins. By default, Maven executes plugin ``maven-clean-plugin`` when it executes phase ``clean``. Maven plugins are artifacts themselves that can be referenced by Maven coordinates. You can change the version of this plugin by adding a reference to this plugin in your ``pom.xml``. You will see how to do this in a later subsection. Maven plugins are little programs that may have multiple functions. These are named ``goals``. The output says that goal ``clean`` of ``maven-clean-plugin`` version ``2.5`` has been executed. This action deleted directory ``target`` which probably did not exist at this moment. All output of Maven appears in the ``target`` directory, so all output from previous runs of Maven has been removed as was intended.

9. Within the same command prompt, enter ``mvn compile`` to execute build phase ``compile``.

The output should look as follows:

.. code-block:: none

   C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v500>mvn compile
   [INFO] Scanning for projects...
   [INFO]
   [INFO] -----------------< org.ibissource:mavenWebappExample >------------------
   [INFO] Building mavenWebappExample 1.0-SNAPSHOT
   [INFO] --------------------------------[ jar ]---------------------------------
   [INFO]
   [INFO] --- maven-resources-plugin:2.6:resources (default-resources) @ mavenWebappExample ---
   [WARNING] Using platform encoding (Cp1252 actually) to copy filtered resources, i.e. build is platform dependent!
   [INFO] skip non existing resourceDirectory C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v500\src\main\resources
   [INFO]
   [INFO] --- maven-compiler-plugin:3.1:compile (default-compile) @ mavenWebappExample ---
   [INFO] Changes detected - recompiling the module!
   [WARNING] File encoding has not been set, using platform encoding Cp1252, i.e. build is platform dependent!
   [INFO] Compiling 1 source file to C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v500\target\classes
   [INFO] ------------------------------------------------------------------------
   [INFO] BUILD SUCCESS
   [INFO] ------------------------------------------------------------------------
   [INFO] Total time:  0.838 s
   [INFO] Finished at: 2022-05-10T18:22:50+02:00
   [INFO] ------------------------------------------------------------------------

   C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v500>

Build phase ``compile`` is part of the default life cycle. All preceding phases, like ``process-resources``, of the default life cycle are executed as well. Phase ``process-resources`` is linked to plugin ``maven-resources-plugin`` and its goal ``resources``. Phase ``compile`` executes goal ``compile`` of plugin ``maven-compiler-plugin``.

10. Check what files have been produced. Enter command ``tree``.

The output should look like this:

.. code-block:: none

   C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v500>tree
   Folder PATH listing
   Volume serial number is D8AD-6F85
   C:.
   ├───src
   │   └───main
   │       └───java
   │           └───org
   │               └───wearefrank
   │                   └───maven
   │                       └───webapp
   │                           └───example
   └───target
       ├───classes
       │   └───org
       │       └───wearefrank
       │           └───maven
       │               └───webapp
       │                   └───example
       ├───generated-sources
       │   └───annotations
       └───maven-status
           └───maven-compiler-plugin
               └───compile
                   └───default-compile

   C:\Users\martijn\frank-manual\srcSteps\mavenWebapp\v500>

All generated files appear in the ``target`` directory. Within that directory, there is a directory ``classes``. This directory holds everything that this artifact will put on the classpath when the linked application executes. There is a path ``org/wearefrank/maven/webapp/example``. This path resembles the path to file ``Main.java``. The directory holds file ``Main.class``, the byte code produced by compiling source file ``Main.java`` (not shown).

11. Assemble the artifact of this project, which has ``<groupId>`` ``org.ibissource``, ``<artifactId>`` ``mavenWebappExample`` and ``<version>`` ``1.0-SNAPSHOT``. Do so by entering ``mvn install``.
#. Check that you have file ``mavenWebappExample-1.0-SNAPSHOT.jar``. This is a ZIP file that holds all data that this artifact should put on the classpath.
#. Check that your home directory has a folder named ``.m2``. Check that this folder contains directory ``repository\org\ibissource\mavenWebappExample\1.0-SNAPSHOT``.
#. Check that that directory contains the same JAR file: ``mavenWebappExample-1.0-SNAPSHOT.jar``.

Maven has stored the artifact in the local repository on your computer. If you would build some other project that references ``org.ibissource:mavenWebappExample:1.0-SNAPSHOT`` as a dependency, then the corresponding directory in the ``.m2`` folder would be accessed.

15. Check that your ``.m2`` folder has directory ``repository\org\apache\commons\commons-lang3\3.12.0``.

Maven has downloaded the artifact that was referenced as ``<dependency>``. Please note that this version does not end with ``SNAPSHOT``. Version numbers that end with ``SNAPSHOT`` are development versions that will change. Versions without ``SNAPSHOT`` are expected not to change anymore. Anytime that such an artifact is used, the data should be the same.

Conclusion
----------

Maven is a tool that automates compiling and linking Java programs. It distinguishes build phases like ``clean``, ``process-resources``, ``compile`` and ``install`` that each belong to a lifecycle. When Maven executes a phase, it automatically executes the preceding phases of the lifecycle first. Maven delegates its work to plugins, little programs that can have multiple functions that are named goals. Each phase is linked to plugin goals, which appear in the console output when Maven executes. If your Maven build fails or if you have to update the build process, you probably need information about specific Maven plugins. Maven plugins are usually documented quite well on the internet. Maven plugins and dependencies in your ``pom.xml`` are Maven artifacts. Each artifact is referenced by three Maven coordinates: the group id, the artifact id and the version. Maven can download artifacts automatically and stores them in a central repository on your computer.

In the next subsection, you will use Maven to execute the Java program you wrote.