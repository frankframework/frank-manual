.. _propertiesFramework:

Frank!Framework Properties
==========================

In subsection :ref:`propertiesReference` it was explained how you can reference properties in your adapters. You can reference any property in your adapter. If it is defined, the value of the property is substituted. This subsection explains another effect of configuring properties. The Frank!Framework offers some services that are not defined in your adapters. An example is logging. In your adapters you usually do not direct the Frank!Framework to write messages to log files, but the Frank!Framework still does so. You can set Frank properties to define how the Frank!Framework should perform these services. The Frank property ``log.dir`` determines the directory in which the Frank!Framework writes log files.

Below, the most important Frank properties are listed.

application.server.type
  The application server used in your deployment. Set automatically by the Frank!Framework. This property determines what property files are read by the Frank!Framework to set other properties. See subsection :ref:`propertiesDeploymentEnvironment` for all possible values.

otap.side
  Use this to characterize your deployment environment as explained in subsection :ref:`propertiesDeploymentEnvironment`. The default value is ``xxx``. This default is sufficient if the deployment server and the DTAP stage fully characterize your deployment. This property determines what property files are read by the Frank!Framework to set other properties.

otap.stage
  Defines the DTAP stage of this deployment. Possible values are "LOC",
  "DEV", "TST", "ACC" and "PRD". This property determines what property files are read by the Frank!Framework to set other properties. See subsection :ref:`propertiesDeploymentEnvironment` for more details.

log.dir
  The directory to which the Frank!Framework writes its log files. Usually you do not have to set this property because the Frank!Framework can automatically choose a suitable directory.

log.level
  TODO: Await fixing the Java code.

jdbc.migrator.active
  Can be "true" or "false" (the default). When true, database initialization
  is switched on. The default behavior is to do this with LiquiBase, see 
  https://www.liquibase.org/. With LiquiBase, the file ``DatabaseChangelog.xml`` is executed.

.. NOTE::

   Some features of your Frank are configured through the application server on which the Frank!Framework is deployed. An example is the database used by your Frank. In the Frank!Console you will not find a property that specifies the database being accessed.
