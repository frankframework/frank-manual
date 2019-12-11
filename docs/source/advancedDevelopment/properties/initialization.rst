.. _propertiesInitialization:

How Properties Are Set
======================

In subsection :ref:`propertiesDeploymentEnvironment`, the characteristics of the deployment environment of a Frank were explained. Franks can be deployed on different types of application servers. The Frank!Framework detects the type of application server and automatically sets the property ``application.server.type``. System administrators can configure the properties ``otap.stage`` and ``otap.side``. We do not tell here how to set system properties because this information is specific to each deployment environment. See chapter :ref:`deploying`.

As a Frank developer, you can reference these three properties to let your Frank depend on its deployment environment. Referencing properties is the subject of subsections :ref:`propertiesReference`. In addition you can set properties in property files that you add to your Frank configuration, for example ``DeploymentSpecifics.properties``. The Frank!Framework chooses what property files to consider, and this is a very important point. The Frank!Framework bases this choice on the values of properties ``application.server.type``, ``otap.stage`` and ``otap.side``.

As an example, assume that you deploy on your local laptop (``otap.stage = LOC``), that you use the WeAreFrank! Quick Docker Installer (``application.server.type = TOMCAT``) and that you chose to set ``otap.side = xxx``. Then the Frank!Framework reads the following properties, sorted from high priority to low priority:

#. System properties: These are never overwritten by properties you define in your Frank configuration.
#. ``StageSpecifics_LOC_TOMCAT.properties``
#. ``StageSpecifics_LOC.properties``
#. ``SideSpecifics_xxx_TOMCAT.properties``
#. ``SideSpecifics_xxx.properties``
#. ``ServerSpecifics_TOMCAT.properties``
#. ``DeploymentSpecifics.properties``

The Frank!Framework does not require these property files to be present. If some of these files do not exist, the Frank!Framework initializes the properties based on the other files.

You can use these property files to configure your properties differently for different deployment environments. As an example, suppose that your Frank calls a REST service hosted on https://someservice.io. If this service manages sensitive data, you do not want to access it during testing. You want clones of the REST service that work with fake data, so-called stubs. Within your company (DTAP stages local, development and test), you may want testdata that differs from the test data the customer has (DTAP stage acceptance). These two different stubs could be hosted on https://dev.someservice.io and https://acc.someservice.io.

You can use properties to call the right service URL from your Frank. In your adapters, you can reference a property ``serviceURL`` to find the URL of your service. In ``DeploymentSpecifics.properties``, you include the line ``serviceURL=https://dev.someservice.io``. In ``StageSpecifics_ACC.properties``, you include the line ``serviceURL=https://acc.someservice.io``. Finally in ``StageSpecifics_PRD.properties`` you set the real service URL: ``serviceURL=https://someservice.io``. In DTAP stages local, development and test, the service URL defined in ``DeploymentSpecifics.properties`` is applied. In DTAP stage acceptance, this value is superseeded by the definition in ``StageSpecifics_ACC.properties``. In production, the service URL found in ``StageSpecifics_PRD.properties`` is taken. 

Please note that system properties always take precedence over properties set within your Frank config. System administrators can use this feature to tweak you Frank. Suppose you have a Hello World adapter that outputs the value of property ``my.hello``. Normally, you want the text "Hello World". Therefore you include property file ``DeploymentSpecifics.properties`` and include the line ``my.hello=Hello World``. If the system administrator configures ``my.hello = Something Else``, then the output of your adapter will be "Something Else".

In addition to the chain of system properties and property files, some properties have default values. These default values are listed in subsection :ref:`propertiesFramework`. If some property is not configured by the system administrator and if it is not defined in the property files read by the Frank!Framework, then the default value is applied.

Finally, a few properties can be changed at run time. On the left hand menu of the Frank!Console, go to "Environment Variables":

.. image:: viewProperties.jpg

Look below the heading "Dynamic Parameters". Changes done at runtime will be undone when you restart the frank!framework.

An example is the log level, which determines how much logging data is produced. On production you normally set it to ``ERROR`` or ``WARN``. If there is an incident, you can temporarily put it to ``INFO`` or ``DEBUG`` to collect data about the issue.

The next subsection explains how to reference properties within your Frank configs.

.. In AppConstants.properties the following sequence is defined:
   CompanySpecifics.properties,
   CompanySpecifics_${otap.side}.properties,
   CompanySpecifics_${otap.stage}.properties,
   DeploymentSpecifics.properties,
   BuildInfo.properties,
   ServerSpecifics_${application.server.type}${application.server.type.custom}.properties,
   SideSpecifics_${otap.side}.properties,
   SideSpecifics_${otap.side}_${application.server.type}${application.server.type.custom}.properties,
   StageSpecifics_${otap.stage}.properties,
   StageSpecifics_${otap.stage}_${application.server.type}${application.server.type.custom}.properties,
   Test.properties
