.. _deploymentConfigureProperties:

Configuring Properties
======================

The previous section :ref:`deploymentProperties` explains what happens
when you set properties. This section explains how you can give properties
their value.

First remember from section :ref:`deploymentIntroduction` that properties
are the means to configure your Frank for a specific deployment
environment: the DTAP stage you deploy for, the application server
you deploy on, and more. Therefore, a mechanism is needed to
define properties outside your Frank. Such properties are
called system properties.

The way to set system properties
depends on your operating system and your application server.
For example when you deploy using the Wearefrank! Quick
Docker Installer, you configure properties in a file
"properties.txt" in your project directory, next to your
"classes", "tests" and "configurations" folders. Within this
file, you add lines like: ::

  some_key=some value

The frank!framework will replace the "_" appearing in keys with the "." character.
For details, see sections :ref:`deploymentDockerDeployment`,
:ref:`deploymentTomcatDeployment`, :ref:`deploymentJbossDeployment` and
:ref:`deploymentWebsphereDeployment`.

The frank!framework provides a mechanism to choose property
values depending on the values of the system properties.
When the frank!framework starts, it does the following:

* It establishes the system properties and their values. These values are then fixed.
* Read properties from "DeploymentSpecifics.properties" without changing system properties.
* Depending on the value of property "application.server.type", read properties "ServerSpecifics_TOMCAT.properties", "ServerSpecifics_WAS.properties" or TODO: value for JBoss? See section :ref:`deploymentProperties`. Do not overwrite system properties, but do overwrite properties read from "DeploymentSpecifics.properties".
* Read properties from file "SideSpecifics_${otap.side}.properties", substituting the value of property "otap.side" to get the name of the file. If "otap.side" would be "xxx", then additional properties would be read from "SideSpecifics_xxx.properties". Do not modify system properties, but modify properties read from earlier property files.
* Read properties depending on the combination of ${otap.side} and the application server. These are in "SideSpecifics_${otap.side}_${application.server.type}.properties" with the ${...} variables substituted like explained above. Do not change system properties but overwrite other properties.
* Read properties depending on property "otap.stage". They are in "StageSpecifics_${otap.stage}.properties" in which ${otap.stage} is substituted. Do not change system properties but overwrite other properties.
* Read properties depending on the combination of "otap.stage" and the application server. They are in "StageSpecifics_${otap.stage}_${application.server.type}". Do not change system properties.

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

This chain of property files constitutes a hierarchy in which the most
important property file determines the value. Seen this way the above list of property files should be read in reverse order, because the property file read last overwrites properties read in an earlier file. System properties have the highest priority, because they are never changed when reading
a property file.

Finally, a few properties can be changed at run time. An example is property "log.level".
You can change this property in the Frank console. On the left hand menu, go to "Environment Variables":

.. image:: viewProperties.jpg

Then you see a heading "Dynamic Parameters". These can be edited at run time. Changes done at runtime will be undone when you restart the frank!framework.
