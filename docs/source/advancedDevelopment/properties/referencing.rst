.. _propertiesReference:

Setting and Referencing Properties
==================================

As said in the introduction of this section, properties are name/value pairs. This subsection gives basic information about setting and referencing properties. This subsection is written as a tutorial to allow you to get hands-on experience. You can check your work against the :download:`solution <../../downloads/advancedDevelopmentProperties.zip>`.

Please perform the following steps:

.. highlight:: none

#. Please install Frank!Runner and set up your instance as explained in :ref:`gettingStarted` if you did not do so already.
#. Within ``Frank2Manual/configurations``, create a subdirectory ``properties`` to start a new configuration with that name.
#. Please add file ``Configuration.xml`` with the following contents:

   .. literalinclude:: ../../../../src/advancedDevelopmentProperties/configurations/properties/Configuration.xml
      :language: xml
   
#. Please make a file ``DeploymentSpecifics.properties``. Give it the following contents:

   .. literalinclude:: ../../../../src/advancedDevelopmentProperties/configurations/properties/DeploymentSpecifics.properties
      :language: xml
   
The file ``DeploymentSpecifics.properties`` allows you to set properties. The key is to the left of the ``=`` sign, while the value is to the right. Property names are words separated by dots. Lines starting with ``#`` are comments, which are ignored by the Frank!Framework.

Both in property files and in XML Frank config files, you can reference properties. To do this, surround the property name with ``${`` and ``}``. In the property file above, property ``my.text`` is defined with value ``My text is ${my.hello}``, which means that the value of property ``my.hello`` should be substituted to get the value of property ``my.text``. Note that property ``my.hello`` can be defined after a property that references it, in this case ``my.text``.

5. Please create file ``ConfigurationReferenceProperties.xml`` with the following contents:

   .. literalinclude:: ../../../../src/advancedDevelopmentProperties/configurations/properties/ConfigurationReferenceProperties.xml
      :language: xml
      :emphasize-lines: 8

   The highlighted line shows that properties are referenced by surrounding the property name with ``${`` and ``}`` as said before.

#. Execute adapter ``AccessProperties`` using the Test Pipeline screen.
#. The Frank!Framework replaces property references by the values of the referenced properties. The default value for ``dtap.stage`` is ``LOC`` (only if you are using Frank!Runner, otherwise there is no default). Check that the output is: ::

     From stage LOC, I say My text is Hello

#. For some application servers, you can also set Java properties like ``-Dproperty="value"``. These properties are then defined within the Frank!Framework. This applies to Apache Tomcat and also for Frank!Runner. Please stop Frank!Runner. Restart Frank!Runner with an argument to set a Java property: ::

     frank-runner> start.bat -Dmy.hello="Hello there"
   
#. When Frank!Runner is running again, please return to the Test Pipeline screen. Run adapter ``AccessProperties``. The output should now be as follows: ::

    From stage LOC, I say My text is Hello there

Depending on your application server, there are different ways to set system properties. Details can be fond in chapter :ref:`deploying`.
