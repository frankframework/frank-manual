.. _advancedDevelopmentCustomCodeBackend:

Writing Custom Backend Code in Java
===================================

The Frank!Framework provides building blocks to develop solutions for system integration projects. These are mainly pipes, senders, receivers and listeners that are configured in XML files, typically ``Configuration.xml``. Sometimes, Frank developers need logic that is difficult to implement with the standard building blocks. In these cases, custom Java code can be added to the project that acts like a standard building block. The custom code can then be referred to in Frank adapters in the same way as standard building blocks are referenced.

Before you begin
----------------

If you are tempted to write much custom code, please consider the following:

* Think twice whether there are really no standard building blocks that can do what you want. The Frank!Framework has many building blocks. For manipulating XML and JSON for example you can often use XSLT or DataSonnet transformations.
* You can write a separate application and treat it like the other applications that are communicating through the Frank!Framework as intermediary. This typically requires your application to provide HTTP interfaces. Your Frank application can use standard senders and standard listeners to exchange data with the application you write.
* If the logic you need is a useful extension to a standard building block, consider copying the Java code of that standard building block from the Frank!Framework sources. If you put your version of the building block on the classpath it overrides the standard implementation implemented in the Frank!Framework. In this case it is wise to store the original copy of the Java code somewhere. When the Frank!Framework evolves, you can see how the original file is updated by the maintainers of the Frank!Framework. You can apply the same updates to your custom code to retain the integrity of the Frank!Framework. Keep in touch with the maintainers of the Frank!Framework to allow them to implement the functionality you are proposing. Hopefully you can throw away your copy eventually to use the standard building block again.

Compiling
---------

Your custom code should work with the same Java version as is used by your version of the Frank!Framework. Use the Frank!Framework components you need as compile-time dependencies. If your custom code lives in a Maven project, this may look like the following:

.. code-block:: xml

   <dependencies>
       <dependency>
           <groupId>org.frankframework</groupId>
           <artifactId>frankframework-core</artifactId>
           <version>${ff.version}</version>
           <scope>compile</scope>
       </dependency>
       ... other dependencies ...
    </dependencies>

Because of the way the Frank!Framework loads custom code, take care with package-private classes when you have your code in multiple .java files. The Frank!Framework may load different .class files in different Java modules, see :ref:`qaFailedToAccesClassJavaException`.

Code example -- a simple calculation
------------------------------------

In general, writing custom classes requires a close understanding of the architecture of the Frank!Framework sources. That subject is beyond the scope of this manual, but we explain here how to write and use a specific type of custom pipes. If you follow these instructions, your pipe will integrate well with the other features of the Frank!Framework, e.g. Ladybug reports and drawings of flowcharts in the Frank!Console.

Derive your custom pipe from ``org.frankframework.pipes.FixedForwardPipe`` and implement your logic in method ``PipeRunResult doPipe(Message message, PipeLineSession session) throws PipeRunException``. Class ``org.frankframework.stream.Message`` holds the input message taken by a pipe or the output message produced by a pipe. Your method should return a ``org.frankframework.core.PipeRunResult``, which wraps the combination of a forward name (e.g. ``success``) and the output message. The forward name is referenced in Frank configurations with a ``<Forward>`` XML tag to link the forward to a target pipe or pipeline exit. You can return ``PipeRunResult`` instances with other forward names to raise error conditions. To use the custom pipe, you have to reference it in a Frank configuration. This looks like: ``<Pipe name="pipe-name" className="full.path.of.MyClass"> ... </Pipe>`` with ``pipe-name`` replaced by the name you choose.

Here is a template for the .java code to start from:

.. code-block:: java

   package org.wearefrank.mermaid.dashboard;

   import org.frankframework.core.PipeLineSession;
   import org.frankframework.core.PipeRunException;
   import org.frankframework.core.PipeRunResult;
   import org.frankframework.pipes.FixedForwardPipe;
   import org.frankframework.stream.Message;

   ... other imports ...

   public class MyCustomPipe extends FixedForwardPipe {
       ...
       public PipeRunResult doPipe(Message message, PipeLineSession session) throws PipeRunException {
           try {
               String template = message.asString();
               ...
               String result = ...;
               Message m = new Message(result);
               return new PipeRunResult(getSuccessForward(), m);
           }
           catch(SomeException e) {
               throw new PipeRunException(this, "Some exception encountered", e);
           }
       }
   }

.. NOTE::

   You are encouraged to examine the Frank!Framework sources of class ``FixedForwardPipe`` and code surrounding it to get more understanding of what you are doing.

.. _advancedDevelopmentCustomCodeBackendPackaging:

Packaging
---------

It is strongly advised to package your compiled custom code, either along with your configuration or in a dedicated archive. You have two options regarding packaging and deploying. You can build your Java code as a library that should be available to all configurations of the Frank application. In this case you should build a dedicated .jar file for the custom Java code and deploy that in ``/opt/frank/resources`` in the Frank!Framework Docker container (container based on the image provided by the maintainers of the Frank!Framework). The other option is to package the custom code in the same archive as the configuration. This way the custom code is only accessible by the configuration. Archives with configurations with or without custom Java code are deployed in ``/opt/frank/configurations``.

When you package a configuration with custom code, DO NOT have a top-level directory in the archive that is named after the configuration. There is no need to have a common root folder. Just put the relevant files in the archive. Here is an example list for the files in the archive (from ``jar -tvf <filename>`` and then edited by hand to make it more clear):

.. code-block:: none

   META-INF/MANIFEST.MF
   META-INF/maven/org.wearefrank/frank-mermaid-dashboard/pom.xml
   META-INF/maven/org.wearefrank/frank-mermaid-dashboard/pom.properties
   Configuration.xml
   Data.xml
   DatabaseChangelog.xml
   DeploymentSpecifics.properties
   Polling.xml
   example.xml
   org/wearefrank/mermaid/dashboard/AnalyzeMermaidTemplatePipe$Analysis.class
   org/wearefrank/mermaid/dashboard/AnalyzeMermaidTemplatePipe$MappingItem.class
   org/wearefrank/mermaid/dashboard/AnalyzeMermaidTemplatePipe.class
   webcontent/chunk-2D4RQQEM.js
   ...
   webcontent/favicon.ico
   webcontent/index.html
   webcontent/main-2JFPUTB3.js
   webcontent/polyfills-SC4UBBZS.js
   webcontent/styles-5INURTSO.css
   xsd/parsedTemplate.xsd
   ...
   xsl/prepareDbLineStatusForJsonUI.xsl
   ...

.. WARNING::

   It is tempting to create a test archive by hand using the command ``jar -cvf <some-name.jar> some-folder``. That would produce the unwanted top-level folder. Instead, go into ``some-folder`` and do ``jar -cvf <some-name.jar> *``. Also take care with zipping a folder using the Windows Explorer. If you use Maven, you can use the Maven resources plugin to copy the contents of your configuration's directory into the ``target/classes`` folder.

.. NOTE::

   The first entry of a .jar file should be ``META-INF/MANIFEST.MF``. Otherwise .jar and .zip files are the same. Take this as a hint to use standard tools to produce the .jar -- editing the files in the archive by hand is discouraged.

Putting custom code in ``/opt/frank/resources`` has as a drawback that mapping volumes for the customer's resources becomes a bit harder. The customer cannot use a common folder to be mapped to ``/opt/frank/resources`` anymore -- more granular volumes become necessary. See :ref:`advancedDevelopmentDockerDevelAppServer` or https://github.com/frankframework/frankframework/blob/master/Docker.md. Or the customer should be requested to install the custom code's library as an additional step of the installation procedure.

Finally, take care with the name of built archive file. Maven adds a version number by default, for example ``frank-mermaid-dashboard-0.0.1-SNAPSHOT.jar`` for configuration ``frank-mermaid-dashboard``. This is only possible if the configuration's name is defined in ``Configuration.xml``, for example: ``<Configuration name="frank-mermaid-dashboard" ... >``. If you omit this ``name`` attribute, the base name of your archive is used as the configurations'name -- in this example the archive's name should be ``frank-mermaid-dashboard.jar``.

Deployment
----------

In any case, the configuration's archive should be deployed in ``/opt/frank/configurations``. As said, there are two options regarding custom Java code:

**Custom code common for all configurations:** Make a dedicated archive for the custom code and put it in ``/opt/frank/resources``. In addition, set property ``configurations.allowCustomClasses`` to ``true``.

**Custom code only for one configuration:** Package the custom code in the archive of the configuration. In addition, set property ``configuration.<name of configuration>.allowCustomClasses`` to ``true``.

.. WARNING::

   In this section we advised you to package configurations. In that case DO NOT set ``configurations.directory.autoLoad``!. That would instruct the Frank!Framework to look for subdirectories of ``/opt/frank/configurations`` instead of archives. The other recommendations in :ref:`advancedDevelopmentDockerDevelBasicsDockerCompose` apply. It is wise to define ``instance.name`` and ``dtap.stage``.
