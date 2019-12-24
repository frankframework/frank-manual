.. _propertiesReference:

Setting and Referencing Properties
==================================

As said in the introduction of this section, properties are name/value pairs. This subsection gives basic information about setting and referencing properties. This subsection is written as a tutorial to allow you to get hands-on experience. You can check your work against the :download:`solution <../../downloads/advancedDevelopmentProperties.zip>`.

Please perform the following steps:

.. highlight:: none

#. Please install Tomcat4Ibis from https://github.com/ibissource/tomcat4ibis if you have not done so already. You should have the following directory structure: ::

     projects
     |- tomcat4ibis
        |- build.properties
        |- tomcat4ibis.bat
        |- tomcat4ibis.sh
      |- ...

#. Please make a subdirectory ``advancedDevelopmentProperties`` within ``projects``. Then open ``build.properties`` and give it the following contents: ::

     project.dir=advancedDevelopmentProperties

#. Please add file ``classes/Configuration.xml`` with the following contents:

   .. literalinclude:: ../../../../src/advancedDevelopmentProperties/classes/Configuration.xml
      :language: xml
   
   This file is very similar to the ``Configuration.xml`` examples shown in section :ref:`horizonsMultipleFiles`. The only difference is that we fill the classpath configuration to keep our example small.


#. Within ``advancedDevelopmentProperties``, please make a file ``classes/DeploymentSpecifics.properties``. Give it the following contents:

   .. literalinclude:: ../../../../src/advancedDevelopmentProperties/classes/DeploymentSpecifics.properties
      :language: xml
   
The file ``DeploymentSpecifics.properties`` allows you to set properties. The key is to the left of the ``=`` sign, while the value is to the right. Property names are words separated by dots. Lines starting with ``#`` are comments, which are ignored by the Frank!Framework.

Both in property files and in XML Frank config files, you can reference properties. To do this, surround the property name with ``${`` and ``}``. In the property file above, property ``my.text`` is defined with value ``My text is ${my.hello}``, which means that the value of property ``my.hello`` should be substituted to get the value of property ``my.text``. Note that property ``my.hyello`` can be defined after a property that references it, in this case ``my.text``.

5. Please create file ``classes/ConfigurationReferenceProperties.xml`` with the following contents:

   .. literalinclude:: ../../../../src/advancedDevelopmentProperties/classes/ConfigurationReferenceProperties.xml
      :language: xml
      :emphasize-lines: 8

   The highlighted line shows that properties are referenced by surrounding the property name with ``${`` and ``}`` as said before.

#. Execute adapter ``AccessProperties`` using the Test Pipeline screen, see :ref:`helloTestPipeline`.
#. The Frank!Framework replaces property references by the values of the referenced properties. The default value for ``otap.stage`` is ``LOC``. Check that the output is: ::

     From stage LOC, I say My text is Hello

#. For some application servers, you can also set Java properties like ``-Dproperty="value"``. These properties are then defined within the Frank!Framework. This applies to Apache Tomcat and also for Tomcat4Ibis. Please stop Tomcat4Ibis. Restart Tomcat4Ibis with an argument to set a Java property. This is different for Windows and Linux:

   * Windows users start Tomcat4Ibis as follows: ::

       projects\tomcat4ibis> tomcat4ibis.bat -Dmy.hello="Hello there"
   
   * Linux users start Tomcat4Ibis as follows: ::

       projects/tomcat4ibis> tomcat4ibis.sh -Dmy.hello="Hello there"

#. When Tomcat4Ibis is running again, please return to the Test Pipeline screen. Run adapter ``AccessProperties``. The output should now be as follows: ::

    From stage LOC, I say My text is Hello there

Depending on your application server, there are different ways to set system properties. Details can be fond in chapter :ref:`deploying`.
