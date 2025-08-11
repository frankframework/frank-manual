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

Packaging and deploying
-----------------------

You have two options:

* If the custom code is specific to a configuration, package it with the configuration as explained in section :ref:`advancedDevelopmentDockerDevelSingleConfig`. The custom Java code is not accessible by other configurations in this case. To make this work, set property ``configurations.<configuration name>.allowCustomClasses`` to ``true``. Configurations with custom Java code have to be packaged and do not work as plain directory trees in ``/opt/frank/configurations``, see :ref:`advancedDevelopmentDockerDevelAppServer`.
* Build the custom code in a dedicated .jar file and deploy it in ``/opt/frank/resources``. This makes the Java code available to all Frank configurations in the Docker container. Set property ``configurations.allowCustomClasses`` to ``true``.
