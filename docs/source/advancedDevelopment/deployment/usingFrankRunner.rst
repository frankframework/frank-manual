.. _advancedDevelopmentDeploymentMavenUsingFrankRunner:

Using the Frank!Runner
======================

The webapp of subsection :ref:`advancedDevelopmentDeploymentMavenLarva` has a few drawbacks. As stated in subsection :ref:`advancedDevelopmentDeploymentMavenBasicFrankWebapp`, you cannot refresh the Frank configuration dynamically, because it resides on the classpath. The application server does not update the classpath when the corresponding input files with the configuration are modified. Therefore the Frank!Framework cannot see the modified data. Another drawback is that properties like ``dtap.stage`` have to be configured with the ``jetty-maven-plugin`` while the Frank!Runner can set these properties automatically. Finally, you can integrate the Frank!Runner with your integrated development environment just like you can do with pure Maven projects. Using the Frank!Runner in a Maven project is demonstrated in the examples of the `Frank!Runner <https://github.com/ibissource/frank-runner>`_, Frank2Example4.

In Frank2Example4, the configuration is not in ``src/main/resources`` but in ``src/main/configurations``. This folder is not recognized by Maven, so the configuration is not packaged in the ``.war`` file. The Frank!Framework can be configured to load configurations after the application server has booted. This is the situation shown in the diagram of :ref:`propertiesDeploymentEnvironment`, with both the layer "Frank!Framework + classes" and the layer "Configurations". The first of these is the classpath with which the application server boots. The second stands for configurations loaded by the Frank!Framework after boot (loaded dynamically).

.. NOTE::

   The Java source code of the Frank!Framework finds every Frank configuration on the classpath, also configurations that are loaded dynamically. Java uses class loaders to put files on the classpath. Each class loader sees a different version of the classpath. When a configuration is read dynamically, the Frank!Framework uses a dedicated class loader. This is why dynamically loaded configurations do not share their data. Each of these dedicated class loaders accesses the class loader used to populate the boot class path. Therefore data in layer "Frank!Framework + classes" is available to every configuration. Class loaders search files in their own context first before searching their parent. If a file appears both in a configuration and in the boot classpath, then the file in the configuration is used.

When the Frank!Runner is used, the ``pom.xml`` file can be simplified:

* There is no need to add database drivers like ``h2`` to ``pom.xml``. The Frank!Runner installs them automatically.
* There is no need to add depencency ``geronimo-jms_1.1_spec`` to ``pom.xml``. The Frank!Runner deploys it automatically.
* There is no need to add properties like ``dtap.stage`` to ``pom.xml``. These properties are set automatically by the Frank!Runner.

In this case, the database driver and possibly the JAR of ``geronimo-jms_1.1_spec`` should be deployed manually in the production environment. In every deployment of the Frank!Framework, property ``dtap.stage`` should be configured manually.
