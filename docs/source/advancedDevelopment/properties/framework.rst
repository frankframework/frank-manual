.. _propertiesFramework:

Frank!Framework Properties
==========================

In subsection :ref:`propertiesReference` it was explained how you can reference properties in your adapters. You can reference any property in your adapter. If it is defined, the value of the property is substituted. This subsection explains another effect of configuring properties. The Frank!Framework offers some services that are not defined in your adapters. An example is logging. In your adapters you usually do not direct the Frank!Framework to write messages to log files, but the Frank!Framework still does so. Frank developers and system administrators can set Frank properties to define how the Frank!Framework should perform these services. The Frank property ``log.dir`` determines the directory in which the Frank!Framework writes log files.

Below, the most important Frank properties are listed.

instance.name
  The name of the instance of the Frank!Framework (the Frank).

application.server.type
  The type of application server used to host the Frank!Famework. Set automatically by the Frank!Framework. This property determines what property files are read by the Frank!Framework to set other properties. See subsection :ref:`propertiesDeploymentEnvironment` for all possible values.

dtap.side
  Used to characterize the deployment environment as explained in subsection :ref:`propertiesDeploymentEnvironment`. Only works as system property. The default value is ``xxx``. This default is sufficient if the deployment server and the DTAP stage fully characterize the deployment. This property determines what property files are read by the Frank!Framework to set other properties.

dtap.stage
  Defines the DTAP stage of the deployment. Only works as system property. Possible values are ``LOC``, ``DEV``, ``TST``, ``ACC`` and ``PRD``. If the Frank!Runner is used then there is a default value, namely ``LOC``. This property determines what property files are read by the Frank!Framework to set other properties. See subsection :ref:`propertiesDeploymentEnvironment` for more details.

otap.side
  Has the same meaning as ``dtap.side``, exists for backward compatibility.

otap.stage
  Has the same meaning as ``dtap.stage``, exists for backward compatibility.

configurations.names
  The value should be a comma-separated list of all configurations. For example, if a Frank contains the classpath configuration and a configuration ``MyConfig``, then the value of this property should be ``${instance.name},MyConfig``. Only works as system property or classpath property, unless nested configurations are used. Nested configurations are beyond the scope of this manual at the moment.

configurations.MyConfig.classLoaderType
  If there is a configuration ``MyConfig``, then this property defines how configuration ``MyConfig`` is read. For example, ``DirectoryClassLoader`` indicates that ``MyConfig`` is stored on the local file system of the server. Configurations can also be stored in the database; then this property has another value. This property should exist for every configuration. ``MyConfig`` should be replaced with the configuration name to get the property name. This property only works as a system property or a classpath property, unless nested configurations are used. Nested configurations are beyond the scope of this manual.

configurations.autoDatabaseClassLoader
  If this property is false (the default), only configurations mentioned in ``configurations.names`` can be uploaded to the database and only if their ``configurations.<config name>.classLoaderType`` property is ``DatabaseClassLoader``. This requires you to set a lot of properties. If you do not need this strict control for uploading configurations, then set this property to true. You can then upload any configuration to the database. The only exceptions are the configs mentioned in ``configurations.names`` in this case. 

  .. WARNING::

     Do not set this property right now because of issue https://github.com/frankframework/frankframework/issues/927.

configurations.directory
  The directory where the Frank!Framework expects to find configurations. This directory is applied when a property ``configurations.SomeConfig.classLoaderType`` is set to ``DirectoryClassLoader`` for some configuration ``SomeConfig``. In this case, configuration ``SomeConfig`` is expected in a subdirectory of the value of ``configurations.directory``. This property can be overruled for a configuration ``MyConfig`` by setting ``configurations.MyConfig.directory``. When you do that for all your configurations, you do not have to define ``configurations.directory``.

  .. NOTE::

     The Frank!Runner sets this property for you.

configurations.MyConfig.directory
  Use this property to overrule ``configurations.directory`` for a configuration ``MyConfig``. This property specifies the directory that contains ``Configuration.xml``.

configurations.directory.autoLoad
  If this property is ``true``, then you can load configurations without specifying them in property ``configurations.names`` and without specifying their classLoaderType. The value of property ``configurations.directory`` is used to find your configurations. Each subdirectory of this directory is expected to be a configuration, and the Frank!Framework tries to load it. The default value is ``false``.

  .. NOTE::

     When you use the Frank!Runner, this property is ``false``. Nevertheless you do not have to specify property ``configurations.names``, because the Frank!Runner sets this property for you.

jdbc.migrator.active
  Can be "true" or "false" (the default). When true, database initialization is switched on. The default behavior is to do this with Liquibase, see https://www.liquibase.org/. With Liquibase, the file ``DatabaseChangelog.xml`` is executed. This property behaves differently as a system property or classpath property on the one hand, or as a configuration property on the other hand. See section :ref:`advancedDevelopmentDatabase` for details.

log.dir
  The directory to which the Frank!Framework writes its log files. Only works as system property. Usually it is not necessary to set this property because the Frank!Framework can automatically choose a suitable directory.

log.level
  Determines the amount of log messages written by defining the minimum log level. Only works as system property. Possible values are ``ERROR``, ``WARN``, ``INFO`` and ``DEBUG``. The default value depends on ``dtap.stage``, as follows:

  * If ``dtap.stage`` = ``LOC``, then the default value of ``log.level`` is ``DEBUG``.
  * If ``dtap.stage`` = ``DEV``, then the default value of ``log.level`` is ``DEBUG``.
  * If ``dtap.stage`` = ``TST``, then the default value of ``log.level`` is ``DEBUG``.
  * If ``dtap.stage`` = ``ACC``, then the default value of ``log.level`` is ``WARN``.
  * If ``dtap.stage`` = ``PRD``, then the default value of ``log.level`` is ``WARN``.

  This setting can be adjusted at runtime, see :ref:`frankConsoleDiskUsage`.

instance.name.lc
  Derived automatically by the Frank!Framework from ``instance.name`` by replacing uppercase letters by lowercase letters. For example if ``instance.name`` is ``GettingStarted``, then ``instance.name.lc`` is ``gettingstarted``.

testtool.enabled
  Defines whether a Ladybug testreport is created when an adapter executes. The default value is ``true``. The value of this property is applied after the Frank!Framework has been restarted. This setting can be adjusted at runtime, see :ref:`frankConsoleDiskUsage`.

ibistesttool.directory
  Defines the directory used by Ladybug to store test reports. See the note at the end of subsection :ref:`capture`.

warnings.suppress.defaultvalue
  In a Frank config, you can assign values to properties. Some properties have a default value. When you assign to a property its default value, the Frank!Framework detects this redundant assignment. When this property is false (the default), the Frank!Framework issues a warning in the status page of the Frank!Console. When this property is true, the warning is suppressed.

loadDatabaseSchedules.active
  If true, the Frank!Console allows its users to upload Frank configs to the database. See section :ref:`frankConsoleConfigsUploading`. The default value is ``false``.

warnings.suppress.sqlInjections.ManageDatabase
  This property helps you when you are seeing a warning about SQL injections. You see it in the Adapter Status page. It reads:

  .. code-block:: none

     The class [nl.nn.adapterframework.jdbc.XmlQuerySender] is used one or more times. Please change to [nl.nn.adapterframework.jdbc.FixedQuerySender] to avoid potential SQL injections!
    
  This warning expresses the following. Some of your adapters are using the sender "XmlQuerySender". This sender can execute SQL queries that are generated based on user input. This causes a potential security risk. If an attacker can write SQL queries and have them executed by the Frank!Framework, she can corrupt the database.

  From section :ref:`databaseInitialization`, remember that the Frank!Console offers the JDBC | Execute Query page, a service to Frank developers to enter SQL queries and have them executed! In DTAP stage LOC, the option to inject SQL is not a security risk. In this case, you want to suppress the warning. You can do this by setting this property to true.

warnings.suppress.sqlInjections.<your adapter>
   Set this property to true if you want your adapter to execute dynamic SQL on your database. Dynamic SQL statements are SQL statements that are generated based on user input. Such queries may be a security risk, because they may allow attackers to corrupt the database. In some situations, executing dynamic SQL statement is a useful service, however. An example is the "ManageDatabase" adapter. This adapter is used to provide the JDBC | Execute Query page of the Frank!Console, see the description of the previous property ``warnings.suppress.sqlInjections.ManageDatabase``. If your adapter, say "myAdapter", was designed to process dynamic SQL, then suppress the warning by setting property ``warnings.suppress.sqlInjections.myAdapter`` to true.

.. NOTE::

   Some features of a Frank are configured through the application server on which the Frank!Framework is deployed. An example is the database used by the Frank. In the Frank!Console there is no property that specifies the database being accessed.

credential:username:alias1 and credential:password:alias1
  These properties refer to credentials of external systems. Here, ``alias1`` has to be replaced by the alias you want to use for the external account. As a developer, you should document the chosen alias for the operator who deploys your config. The operator has to provide the credentials (username and password) for the alias. Section :ref:`deploymentCredentials` explains to operators how these values should be provided.

scenariosroot<n>.description and scenariosroot<n>.directory
  Define scenarios roots, see subsection :ref:`testingLarvaConsole`.

larva.timeout
  Larva request timeout, see :ref:`testingLarvaConsole`.

**soap.bus.org.apache.cxf.stax.maxAttributeSize**

**soap.bus.org.apache.cxf.stax.maxChildElements**

**soap.bus.org.apache.cxf.stax.maxElementDepth**

**soap.bus.org.apache.cxf.stax.maxAttributeCount**

**soap.bus.org.apache.cxf.stax.maxTextLength**

**soap.bus.org.apache.cxf.stax.maxElementCount**
  These properties are closely related. The Frank!Framework uses a library CXF to listen to SOAP messages (To listen to SOAP messages in your Frank config, use a WebServiceListener). The CXF library offers protection against DDOS attacks by rejecting SOAP messages when their XML data is 'too large'. All these properties should have integer values. For example, ``soap.bus.org.apache.cxf.stax.maxTextLength`` is the maximum allowed length of a text inside an XML node. The other properties have similar meanings as their names suggest. See also https://cxf.apache.org/docs/security.html. To see information about one of the mentioned F!F properties, omit the ``soap.bus.`` prefix. So F!F property ``soap.bus.org.apache.cxf.stax.maxTextLength`` corresponds to CXF property ``org.apache.cxf.stax.maxTextLength``.

  .. NOTE::

    The prefix ``soap.bus.`` is in the property names because we use the CXF library for multiple purposes. In the future, we may need other Frank!Framework properties that map to the same CXF properties.