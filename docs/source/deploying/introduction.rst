Introduction
============

This section documents how the frank!framework can be deployed. The instructions
depend on the application server on which the frank!framework is deployed. It
can be deployed on Apache Tomcat, JBoss Application Server (recently renamed
to WildFly) or WebSphere Application Server. Alternatively wearefrank!
provides a quick installer to run the frank!framework within a Docker container,
see https://github.com/ibissource/docker4ibis/.

It is wise to consider testing during the deployment of the frank!framework.
Enterprise applications are typically developed or tested for the first time
in a development environment (D). The development team typically shares a
test environment to test the application before delivery (T).
When testing succeeds, the application is shipped to the
customer. The customer has a test environment to do acceptance tests (A).
When the customer accepts the application, it can finally be installed
in the production environment (P). The frank!framework supports these
DTAP stages, adding the L of Local for the PC of an individual Frank developer.

A Frank is typically deployed in multiple environments during its lifetime and
has to behave slightly different for each deployment. For example a Frank may
talk to an Oracle database in the Production environment, but a H2 database
may be sufficient for developers working on the Frank (DTAP stage L).
These differences are configured using properties, which are just key/value pairs.

Section :ref:`deploymentProperties` introduces some specific properties, describing
the impact of setting them on the behavior of your Frank. Section :ref:`deploymentConfigureProperties` 
describes how the environment determines property values, allowing the environment to
control the behavior of your Frank. Finally, sections :ref:`deploymentDockerDeployment`,
:ref:`deploymentTomcatDeployment`, :ref:`deploymentJbossDeployment` and
:ref:`deploymentWebsphereDeployment` give detailed information about deploying on these environments.
