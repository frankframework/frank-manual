.. _propertiesInitialization:

How Properties Are Set
======================

In subsection :ref:`propertiesDeploymentEnvironment`, the characteristics of the deployment environment of a Frank were explained. Franks can be deployed on different types of application servers. The Frank!Framework detects the type of application server and automatically sets the property ``application.server.type``. System administrators can configure the properties ``otap.stage`` and ``otap.side``. We do not tell here how to set system properties because this information is specific for each deployment environment. See chapter :ref:`deploying`.

As a Frank developer, you can reference these three properties to let your Frank depend on its deployment environment. Referencing properties is the subject of subsections :ref:`propertiesReference`. In addition you can set properties in property files that you add to your Frank configuration, for example ``DeploymentSpecifics.properties``. The Frank!Framework chooses what property files to consider, and this is a very important point. The Frank!Framework bases this choice on the values of properties ``application.server.type``, ``otap.stage`` and ``otap.side``.

As an example, assume that you deploy on your local laptop (``otap.stage = LOC``), that you use the WeAreFrank! Quick Docker Installer (``application.server.type = TOMCAT``) and that you chose to set ``otap.side = xxx``. Then the Frank!Framework reads the following properties, sorted from high priority to low priority:

#. System properties: These are never overwritten by properties you define in your Frank configuration.
#. ``StageSpecifics_LOC_TOMCAT.properties``
#. ``StageSpecifics_LOC.properties``
#. ``SideSpecifics_xxx_TOMCAT.properties``
#. ``SideSpecifics_xxx.properties``
#. ``ServerSpecifics_TOMCAT.properties``
#. ``DeploymentSpecifics.properties``

The Frank!Framework does not require these property files to be present. If some of these files do not exist, the Frank!Framework uses the others.

As a second example, assume that you deploy on production (``otap.stage = PRD``) and that you are deploying on JBoss Application Server (``application.server.type = JBOSS``). Finally suppose that you are deploying at the site of your customer "New Horizons". You can ask their system administrator to set ``otap.side = NewHorizons``. This deployment of the Frank!Framework reads the following properties, sorted from high priority to low priority:

#. System properties: These are never overwritten by properties you define in your Frank configuration. But they are certainly different from the system properties on your local laptop.
#. ``StageSpecifics_PRD_JBOSS.properties``
#. ``StageSpecifics_PRD.properties``
#. ``SideSpecifics_NewHorizons_JBOSS.properties``
#. ``SideSpecifics_NewHorizons.properties``
#. ``ServerSpecifics_JBOSS.properties``
#. ``DeploymentSpecifics.properties``

These example demonstrate that you can add many property files to your Frank configuration, each defining property values for specific deployments. You can implement special behavior for New Horizons by adding ``SideSpecifics_NewHorizons.properties``. This file will not be read on other sites, because their system administrators will not set ``otap.side = NewHorizons``.

This hierarchy of property files also allows more granular property configurations. If you want special behavior for the acceptance test environment if it happens to be a Websphere Application Server, then add property file ``StageSpecifics_ACC_WAS.properties``. The settings in this property file take precedence over settings in ``StageSpecifics_ACC.properties`` or ``StageSpecifics_WAS.properties``.

Please note that system properties always take precedence over properties set within your Frank config. System administrators can use this feature to tweak you Frank. Suppose you have a Hello World adapter that outputs the value of property ``my.hello``. Normally, you want the text "Hello World". Therefore you include property file ``DeploymentSpecifics.properties`` and include the line ``my.hello=Hello World``. If the system administrator configures ``my.hello = Something Else``, then the output of your adapter will be "Something Else".

In addition to this chain, some properties have default values. These default values are listed in subsection :ref:`propertiesFramework`. If some property is not configured by the system administrator and if it is not defined in the property files read by the Frank!Framework, then the default value is applied.

Finally, a few properties can be changed at run time. An example is property ``log.level``.
You can change this property in the Frank!Console. On the left hand menu, go to "Environment Variables":

.. image:: viewProperties.jpg

Then you see a heading "Dynamic Parameters". These can be edited at run time. Changes done at runtime will be undone when you restart the frank!framework.

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
