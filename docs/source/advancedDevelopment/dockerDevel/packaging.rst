.. _advancedDevelopmentDockerDevelSingleConfig:

Packaging configurations
========================

In section :ref:`advancedDevelopmentDockerDevelBasics` it was explained how to run Frank configurations using Docker. Within the container derived from the Frank!Framework Docker image, a directory ``/opt/frank/configurations/my-config`` was created with ``Configuration.xml`` inside. This was fine to get started, but for real projects it is wise to package configurations in .zip or .jar files (extension does not matter, both work). There are two reasons for packaging configurations:

* When the customer manages his own deployment environment, Frank developers can deliver a single file to the customer when there is a new release.
* Without packaging, it is not possible to include Java .class files that are specific for the configuration.

Please follow the following rules when building the package:

* The name of each configuration should be different from the name of the instance (``${instance.name}``).
* Metadata should be provided in either ``BuildInfo.properties`` or the manifest file of the generated .jar file, see below.
* File ``Configuration.xml`` and other files of the configuration should live under a top-level directory. The name of the top-level directory is the name of the configuration.
* When frontend code is included as explained in :ref:`gettingStartedWebcontent`, it should live in a subdirectory ``<configuration name>/webcontent``.
* When there are Java .class files, their directory tree is a *brother* of the configuration's root directory.

Here is the contents of an example archive:

.. code-block:: none

   frank-mermaid-dashboard-config/BuildInfo.properties
   frank-mermaid-dashboard-config/Configuration.xml
   frank-mermaid-dashboard-config/Data.xml
   ...
   frank-mermaid-dashboard-config/webcontent/chunk-2D4RQQEM.js
   frank-mermaid-dashboard-config/webcontent/chunk-2VCO5H7P.js
   ...
   frank-mermaid-dashboard-config/webcontent/favicon.ico
   frank-mermaid-dashboard-config/webcontent/index.html
   frank-mermaid-dashboard-config/webcontent/main-2JFPUTB3.js
   ...
   frank-mermaid-dashboard-config/xsd/parsedTemplate.xsd
   ...
   frank-mermaid-dashboard-config/xsl/prepareDbLineStatusForJsonUI.xsl
   ...
   org/wearefrank/mermaid/dashboard/Analysis.class
   ...

About the metadata
------------------

As said, there are two ways to add the metadata to the .jar file that is needed by the Frank!Framework. First, a file ``BuildInfo.properties`` can be added to the configuration. Here is an example:

.. code-block:: none

   configuration.version=1
   configuration.timestamp=20250807-163000

The second approach is to add the metadata in ``META-INF/MANIFEST.MF``. This can easily be automated with Maven, which integrates well with CI/CD pipelines. Please use a parent ``pom.xml`` file provided by the maintainers of the Frank!Framework and add the data that has to appear in the manifest, as follows:

.. code-block:: xml

   ...
   <groupId>...</groupId>
   <artifactId>...</artifactId>
   <name>...</name>
   <description>...</description>
   <version>...</version>
   <packaging>jar</packaging>

   <parent>
       <groupId>org.frankframework</groupId>
       <artifactId>configuration-parent</artifactId>
       <version>9.3.0-20250927.042333</version>
   </parent>

   <properties>
       <framework.version>9.2.0</framework.version>
       ...
   </properties>
   ...


The parent ``pom.xml`` implements this by configuring the maven-jar-plugin.

.. WARNING::

   If you have some knowledge of Maven, you may be tempted to configure the maven-jar-plugin in your ``pom.xml`` without using the mentioned parent ``pom.xml``. The maintainers of the Frank!Framework discourage this approach. They carefully crafted this parent ``pom.xml`` to write the correct ``MANIFEST.MF`` and to do a few checks on your project.

At the time of writing, the parent ``pom.xml`` has not been released on Maven Central. To fetch it from the nightly builds, please add the following to your ``pom.xml``.

.. code-block:: xml

   <repositories>
     <repository>
       <id>frankframework</id>
       <name>frankframework</name>
       <url>https://nexus.frankframework.org/repository/public</url>
     </repository>
   </repositories>

Exercise
--------

Try to package an example configuration and upload it in the Frank!Console. For instructions on uploading configurations see :ref:`frankConsoleConfigsUploading`.
