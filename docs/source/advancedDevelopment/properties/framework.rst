.. _propertiesFramework:

Frank!Framework Properties
==========================

In subsection :ref:`propertiesReference` it was explained how you can reference properties in your adapters. You can reference any property in your adapter. If it is defined, the value of the property is substituted. This subsection explains another effect of configuring properties. The Frank!Framework offers some services that are not defined in your adapters. An example is logging. In your adapters you usually do not direct the Frank!Framework to write messages to log files, but the Frank!Framework still does so. You can set Frank properties to define how the Frank!Framework should perform these services. The Frank property ``log.dir`` determines the directory in which the Frank!Framework writes log files.

Below, the most important Frank properties are listed.

instance.name
  The name of your Frank. You always have to set this property. Prefarably ``instance.name`` should equal the name of the parent directory of your ``classes`` folder. The Frank!Framework issues a warning if ``instance.name`` has another value. Only works as a system property or classpath property.

application.server.type
  The application server used in your deployment. Set automatically by the Frank!Framework. This property determines what property files are read by the Frank!Framework to set other properties. See subsection :ref:`propertiesDeploymentEnvironment` for all possible values.

otap.side
  Use this to characterize your deployment environment as explained in subsection :ref:`propertiesDeploymentEnvironment`. Only works as system property. The default value is ``xxx``. This default is sufficient if the deployment server and the DTAP stage fully characterize your deployment. This property determines what property files are read by the Frank!Framework to set other properties.

otap.stage
  Defines the DTAP stage of this deployment. Only works as system property. Possible values are "LOC", "DEV", "TST", "ACC" and "PRD". The default value is ``LOC``. This property determines what property files are read by the Frank!Framework to set other properties. See subsection :ref:`propertiesDeploymentEnvironment` for more details.

configurations.names
  The value should be a comma-separated list of all configurations. For example, if your Frank contains the classpath configuration and a configuration ``MyConfig``, then the value of this property should be ``${instance.name},MyConfig``. Only works as system property or classpath property, unless you work with nested configurations. Nested configurations are beyond the scope of this manual at the moment. If you only have the classpath configuration, this property can be omitted.

configurations.MyConfig.classLoaderType
  If you have a configuration ``MyConfig``, then this property defines how configuration ``MyConfig`` is read. When you use Tomcat4Ibis and when you have the configuration in your ``configurations`` directory, you should set the value to ``DirectoryClassLoader``, indicating that ``MyConfig`` is stored on the local file system of the server. This property should exist for every configuration. Replace ``MyConfig`` with the configuration name to get the property name. This property only works as a system property or a classpath property, unless you are working with nested configurations. Nested configurations are beyond the scope of this manual.

jdbc.migrator.active
  Can be "true" or "false" (the default). Works only as system property or classpath property. When true, database initialization is switched on. The default behavior is to do this with LiquiBase, see https://www.liquibase.org/. With LiquiBase, the file ``DatabaseChangelog.xml`` is executed.

log.dir
  The directory to which the Frank!Framework writes its log files. Only works as system property. Usually you do not have to set this property because the Frank!Framework can automatically choose a suitable directory.

log.level
  Determines the amount of log messages written. Only works as system property. Possible values are ``ERROR``, ``WARN``, ``INFO`` and ``DEBUG``.

.. NOTE::

   Some features of your Frank are configured through the application server on which the Frank!Framework is deployed. An example is the database used by your Frank. In the Frank!Console you will not find a property that specifies the database being accessed.
