.. _deploymentConfigureProperties:

Configuring Properties
======================

The previous section :ref:`deploymentProperties` explains what happens
when you set properties. This section explains how properties get their
value. Properties can be set explicitly or they are given their
value automatically. At the end of this section, we elaborate on
deployment-specific configuration that happens without properties,
as was announced in the note of section :ref:`deploymentIntroduction`.

Configuring properties explicitly
---------------------------------

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
important property file determines the value. Seen this way the above list of property files should be read in reverse order, because the property file read last overwrites properties read in an earlier file. System pyou can give properties
their value.roperties have the highest priority, because they are never changed when reading
a property file.

Finally, a few properties can be changed at run time. An example is property "log.level".
You can change this property in the Frank console. On the left hand menu, go to "Environment Variables":

.. image:: viewProperties.jpg

Then you see a heading "Dynamic Parameters". These can be edited at run time. Changes done at runtime will be undone when you restart the frank!framework.

Automatic property values
-------------------------

Many properties get their value implicitly. These properties are not
configured as system properties and they do not appear in Frank property
files like "DeploymentSpecifics.properties", but they do have the same
impact (see the previous section :ref:`deploymentProperties`). We describe
here how these implicit properties come into existence.

First, some properties have a default value as documented in
section :ref:`deploymentProperties`. If a property is not defined
explicitly, the default value is applied within the frank!framework.

Second, some properties have a default value that depends on
another property. An example is property "log.level". The
default value of this property depends on property "otap.stage"
as shown in the following table:

================  =======================
   otap.stage     Default value log.level
----------------  -----------------------
   LOC            TERSE (TODO)
   DEV            DEBUG
   TST            DEBUG
   ACC            WARN
   PRD            WARN

This is a handy feature, because for "log.level" this
is probably what you want. You get this behavior without
writing "StageSpecifics_LOC.properties" ... "StageSpecifics_PRD.properties".

Finally, some properties are set automatically when you
deploy on your application server or using the 
Wearefrank! Quick Docker Installer. An example is
property "application.server.type", see :ref:`deploymentProperties`.

Configuration without properties
--------------------------------

The operation of frank!framework framework depends on the way it is
deployed. So far, this has been documented in the context of
properties that you can view within the frank!framework. The
specifics of your deployment sometimes have impact on the
frank!framework without the existence of a corresponding
system property within the frank!framework.

An example is the database with which your Frank communicates.
Suppose you want a H2 database. When you work with
the Wearefrank! Quick Docker Installer you
edit a file "properties.sh" and include for example with the following line: ::

   DATABASE=h2

You do not see a system property "DATABASE" within the frank!framework.
The Wearefrank! Quick Docker Installer uses this Linux environment
variable to spin up the frank!framework, but does not pass
pass a system property like "DATABASE" to it.

.. NOTE::

   This example about database does not contradict our earlier
   statement about the Wearefrank! Quick Docker Installer. It
   was said that system properties are configured through
   a file "properties.sh", but a line "DATABASE=..." does not
   introduce a system property. Indeed, some keys within
   "properties.sh" are only interpreted within the start-up
   scripting of the Wearefrank! Quick Docker Installer and
   are not passed to the started frank!framework as system
   properties. The other keys are passed to the running
   frank!framework and influence its operation that way.

TODO: Edit this text when the Wearefrank! Quick Docker Installer
is finished. "properties.sh" and "properties.txt" are meant
to be the same file.
