.. _advancedDevelopmentCustomJavaCode:

Custom Java code
================

Frank configurations reference building blocks (pipes, senders, receivers, listeners) that are combined into an enterprise application. The Frank!Framework provides many types of building blocks as you can see in the Frank!Doc, see section :ref:`configurationSyntaxChecking`. In advanced integration projects, you may have user requirements that you cannot implement only with the existing building blocks. In this case, you can add custom building blocks to the Frank!Framework. You can code these custom building blocks in Java.

To program custom building blocks for the Frank!Framework, you need an understanding of the Java source code of the Frank!Framework. You can find this source code at https://github.com/ibissource/iaf. You can also study the Javadocs, which are HTML documents that are generated from Java sources. You can find these on the Nexus repository of WeAreFrank! at https://nexus.ibissource.org. This subsection does not explain how to write custom Java code. It focuses on the build environment you need. You learn how you can combine custom Java code with Frank configs. You learn to do this in such a way that you can easily develop, test and package your projects.

Both your custom code and the Frank!Framework are written in the programming language Java. Java programs often depend on many libraries and they often involve many lines of source code. Java programs need to be compiled and packaged before they can be executed. This complexity can be managed using Apache Maven, see https://maven.apache.org/. Maven expects a file ``pom.xml`` in the root directory of your project. This XML file contains the Project Object Model (POM), which is a central piece of information that describes how your Java project should be compiled and packaged. Maven projects are typically organized in a standardized way. For example, Java source files typically appear in directory ``src/main/java`` while Java source files with unit tests appear in ``src/test/java``.

WeAreFrank! has developed two standardized approaches to organize Frank configs with custom Java code: :ref:`advancedDevelopmentCustomJavaCodeOneProjectPerConfig` and :ref:`advancedDevelopmentCustomJavaCodeSingleProject`. The first keeps each Frank configuration in its own Maven project. Each Frank configuration can be deployed independently on an instance of the Frank!Framework. Independent deployment of Frank configs is advocated in subsection :ref:`horizonsMultipleFiles`. You learned there that an instance of the Frank!Framework manages directories ``configurations`` and ``tests``. Each Frank config is deployed by copying it to become a subdirectory of ``configurations``. These directories are supported by the Frank!Runner, but they may be different in a production environment. The :ref:`advancedDevelopmentCustomJavaCodeOneProjectPerConfig` approach adheres to the same idea, though.

The :ref:`advancedDevelopmentCustomJavaCodeOneProjectPerConfig` approach is complicated, however. The second approach, :ref:`advancedDevelopmentCustomJavaCodeSingleProject`, is simpler. All Frank configurations and all custom Java code is kept in a single Maven project. As a result, a single output file is produced that holds the entire webapplication. This single webapplication should then be deployed to an application server (for example Apache Tomcat) to run all your configurations. You loose the flexibility to deploy your Frank configs independently, but your files are organized in a simpler way.

As a Frank developer, you have to write Maven POM files. For each of the two approaches, you will learn how your POM should look like. The approaches are also supported by the Frank!Runner, which you can use during development. You learn how to integrate the Frank!Runner within your development environment.

Here is the table of contents:

.. toctree::
   :maxdepth: 3

   mavenCourse
   singleProject
   oneProjectPerConfig
   customCodeDependencies