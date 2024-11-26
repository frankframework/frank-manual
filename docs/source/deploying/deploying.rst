.. _deploying:

Administrator Manual
====================

The Frank!Framework is a solution to quickly build enterprise applications, called Franks. A Frank consists of the Frank!Framework that is combined with Frank configurations. Frank configurations configure the Frank!Framework to provide the services you need. They are written as XML documents and property files. The chapters :ref:`gettingStarted` and :ref:`advancedDevelopment` explain how to write Frank configurations. This chapter can be studied independently from :ref:`gettingStarted`. It is not about writing Frank configurations, but focuses on deployment. How can a given Frank configuration or Frank application be deployed on the IT infrastructure you want?

The Frank!Framework is a Java web application that has to be served by an application server. The Frank!Framework can be deployed on many types of application servers, for example Apache Tomcat, WildFly or WebSphere Application Server. When you receive a Frank configuration or Frank application that has to be deployed, you usually have to do some additional configurations. The following should be considered:

* The DTAP stage (Development, Test, Acceptance, Production) and property ``instance.name``.
* Configuring databases and queues.
* Configuring users, passwords and roles.
* Providing credentials to the Frank!Framework that it needs to contact third-party applications.
* The way Frank configurations can be found (already handled in a Docker image provided by Frank developers).

.. WARNING::

   The information in this chapter is not complete yet. Not all subject listed here are covered.

This manual does not explain how to use an application server. Instead, it explains how to do the configurations listed above. The maintainers of the Frank!Framework have created a Docker image that holds the Frank!Framework deployed on Apache Tomcat, see https://github.com/frankframework/frankframework/blob/master/Docker.md. Frank developers can derive their image from this image to add Frank configurations.

When you get a Docker image from Frank developers, you can trust that Apache Tomcat has been properly configured. In addition, the Frank!Framework should be able to find the Frank configurations without any additional configurations. It remains your responsibility to take care of the other configurations explained in this chapter.

Here is the table of contents of this chapter:

.. toctree::
   :maxdepth: 3

   dtapAndInstanceName
   database
   databaseDriver
   jms
   requiringAuthorization
   overviewSecurityRoles
   credentials
   IdentityProviders/MicrosoftEntraId/microsoftEntraId
   customLogging
 