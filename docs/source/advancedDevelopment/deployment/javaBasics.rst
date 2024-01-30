.. _advancedDevelopmentDeploymentMavenJavaBasics:

Java basics
===========

Maven has been designed for the programming language Java and the Frank!Framework has been written in that programming language. Therefore a basic understanding of Java is needed.

Java has been developed to be platform independent. A compiled Java program is meant to work on any processor and any operating system. This has been achieved by introducing the Java Virtual Machine (JVM). Source code files with extension ``.java`` are not compiled into machine code but in so-called byte code. Byte code files are binary files that have extension ``.class``. To run a compiled program, the user starts the Java Virtual Machine. Like a physical processor, the JVM executes the instructions that appear in the ``.class`` files. The JVM can do so reasonable fast because byte code is similar to machine code. For different platforms the implementation of the JVM is different, but all these implementations can read the same byte code.

A key concept with Java development is the **classpath**. When the JVM starts, it populates its own file system by reading ``.class`` files and other resources. It is important to distinguish the classpath from the file system of the host computer. The JVM does this based on the command-line arguments it gets. If you have Java installed, you can learn about the command-line arguments by opening a command prompt and typing ``java -h``. You do not need to know these details however. Maven can take care of them.

The remainder of this section presents instructions to give you hands-on experience. To follow them, you need Java and Maven. There are two ways to get started:

#. Download the Frank!Runner. Execute the ``cmd.bat`` script in the checkout directory. This starts a command prompt with Maven at your disposal. Please keep in mind that you do not have Maven anymore after closing this command prompt. Start ``cmd.bat`` again to resume using Maven.
#. Prepare yourself manually. Download the Java Development Kit (JDK). It is not so important what version you take because you will work with very simple Java programs. We recommend version 11 or later. You do not need the Oracle JDK. An open JDK is sufficient; At the Frank!Framework organisation the `AdoptOpenJdk <https://adoptopenjdk.net/>`_ is used. Second, you have to download `Apache Maven <https://maven.apache.org/download.cgi>`_. It is important to set system variable ``JAVA_HOME`` to reference the JDK you downloaded. Maven uses this variable to access Java.

In both cases, the installation can be tested by typing ``mvn -v``. The output should show a Maven version and a Java version.