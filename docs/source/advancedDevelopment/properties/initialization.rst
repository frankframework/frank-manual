.. _propertiesInitialization:

How Properties Are Set
======================

In subsection :ref:`propertiesDeploymentEnvironment`, the characteristics of the deployment environment of a Frank were explained. Franks can be deployed on different types of application servers. The Frank!Framework detects the type of application server and automatically sets the property ``application.server.type``. System administrators can configure the properties ``dtap.stage`` and ``dtap.side`` as system properties, for example by setting Java properties as explained in subsection :ref:`propertiesReference`. A consequence of the boot process of the Frank!Framework was explained, namely the difference between system properties, classpath properties and configuration properties. It was said that some properties can only be supplied as system properties, while some others can only be supplied as system properties or classpath properties.

Precedence Order
----------------

Each configuration in your ``configurations`` folder has its own set of properties, which you typically put in the subdirectory of that configuration. There is exactly one configuration within the deployment on your application server, which typically appears in your ``classes`` folder. This configuration is referenced as the classpath configuration. You best leave it empty (see section :ref:`horizonsMultipleFiles`). It does not have its own property definitions but uses the system properties and classpath properties. The system properties and classpath properties are common to all configurations.

There is a precedence order between the three property sources. For each configuration, the order or precedence is as follows:

#. System properties.
#. Configuration properties specific for the configuration.
#. Classpath properties.

As a consequence, the system administrator can tweak a Frank by changing properties that were defined in the Frank as classpath property or configuration property. You tried this at the end of subsection :ref:`propertiesReference`. Furthermore, you can set default values for properties in your ``classes`` folder and override them for some of your configurations.

Property files
--------------

You can set properties specific to a configuration by adding property files to the subdirectory of that configuration. For example if you have a configuration Xyz, then you can define properties in a file ``configurations/Xyz/DeploymentSpecifics.properties``. You can also define properties in other property files in directory ``configurations/Xyz/``. The Frank!Framework then chooses what property files to consider. The Frank!Framework bases this choice on the values of ``application.server.type``, ``dtap.stage`` and ``dtap.side``, the properties that reflect your deployment environment.

As an example, assume that you deploy on your local laptop (``dtap.stage = LOC``), that you use Tomcat4Frank (``application.server.type = TOMCAT``) and that you chose to set ``dtap.side = xxx``. Then the Frank!Framework reads the following property files, sorted from high priority to low priority:

#. ``StageSpecifics_LOC_TOMCAT.properties``.
#. ``StageSpecifics_LOC.properties``.
#. ``SideSpecifics_xxx_TOMCAT.properties``.
#. ``SideSpecifics_xxx.properties``.
#. ``ServerSpecifics_TOMCAT.properties``.
#. ``DeploymentSpecifics.properties``.

The Frank!Framework does not require these property files to be present. If some of these files do not exist, the Frank!Framework initializes the properties based on the other sources.

.. NOTE::

   For backward compatibility, the Frank!Framework uses both property ``dtap.stage`` and ``otap.stage`` to select property files. If both of these properties are set by the system administrator, then ``dtap.stage`` takes precedence. The same applies to properties ``dtap.side`` and ``otap.side``, ``dtap.side`` taking precedence.

You can use these property files to configure your properties differently for different deployment environments. As an example, suppose that your Frank calls a REST service hosted on https://someservice.io. If this service manages sensitive data, you do not want to access it during testing. You want clones of the REST service that work with fake data, so-called stubs. Within your company (DTAP stages local, development and test), you may want testdata that differs from the test data the customer has (DTAP stage acceptance). These two different stubs could be hosted on https://dev.someservice.io and https://acc.someservice.io.

You can use properties to call the right service URL from your Frank. In your adapters, you can reference a property ``serviceURL`` to find the URL of your service. In ``DeploymentSpecifics.properties``, you include the line ``serviceURL=https://dev.someservice.io``. In ``StageSpecifics_ACC.properties``, you include the line ``serviceURL=https://acc.someservice.io``. Finally in ``StageSpecifics_PRD.properties`` you set the real service URL: ``serviceURL=https://someservice.io``. In DTAP stages local, development or test, the service URL defined in ``DeploymentSpecifics.properties`` is applied. In DTAP stage acceptance, this value is superseeded by the definition in ``StageSpecifics_ACC.properties``. In production, the service URL found in ``StageSpecifics_PRD.properties`` is taken. 

The mentioned files ``StageSpecifics_LOC_TOMCAT.properties`` ... ``DeploymentSpecifics.properties`` can also exist within the deployment on your application server (your ``classes`` folder). Then they have the same order of precedence, but they have a lower precedence than the configuration specific property files. Please remember that system properties always take precedence over properties configured in your Frank config.

In addition to the chain of system properties and property files, some properties have default values. These default values are listed in subsection :ref:`propertiesFramework`. If some property is not configured by the system administrator and if it is not defined in the property files read by the Frank!Framework, then the default value is applied.

Finally, a few properties can be changed at run time. On the left hand menu of the Frank!Console, go to "Environment Variables":

.. image:: viewProperties.jpg

Look below the heading "Dynamic Parameters". Changes done at runtime will be undone when you restart the Frank!Framework.

An example is the log level, which determines how much logging data is produced. On production you normally set it to ``ERROR`` or ``WARN``. If there is an incident, you can temporarily put it to ``INFO`` or ``DEBUG`` to collect data about the issue.
