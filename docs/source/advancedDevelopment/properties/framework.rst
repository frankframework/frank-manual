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

     Do not set this property right now because of issue https://github.com/ibissource/iaf/issues/927.

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

  From section :ref:`databaseInitialization`, remember that the Frank!Console offers the JDBC | Execute Query page, a service to Frank develpers to enter SQL queries and have them executed! In DTAP stage LOC, the option to inject SQL is not a security risk. In this case, you want to suppress the warning. You can do this by setting this property to true.

warnings.suppress.sqlInjections.<your adapter>
   Set this property to true if you want your adapter to execute dynamic SQL on your database. Dynamic SQL statements are SQL statements that are generated based on user input. Such queries may be a security risk, because they may allow attackers to corrupt the database. In some situations, executing dynamic SQL statement is a useful service, however. An example is the "ManageDatabase" adapter provided by WeAreFrank!. This adapter is used to provide the JDBC | Execute Query page of the Frank!Console, see the description of the previous property ``warnings.suppress.sqlInjections.ManageDatabase``. If your adapter, say "myAdapter", was designed to process dynamic SQL, then suppress the warning by setting property ``warnings.suppress.sqlInjections.myAdapter`` to true.

.. NOTE::

   Some features of a Frank are configured through the application server on which the Frank!Framework is deployed. An example is the database used by the Frank. In the Frank!Console there is no property that specifies the database being accessed.
