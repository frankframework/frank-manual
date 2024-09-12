.. _deploying:

Administrator Manual
====================

The Frank!Framework is a solution to quickly build enterprise applications, called Franks. A Frank consists of the Frank!Framework that is combined with Frank configurations. Frank configurations configure the Frank!Framework to provide the services you need. They are written as XML documents and property files. The chapters :ref:`gettingStarted` and :ref:`advancedDevelopment` explain how to write Frank configurations. This chapter can be studied independently from :ref:`gettingStarted`. It is not about writing Frank configurations, but focuses on deployment. How can a given Frank configuration be deployed on the IT infrastructure you want?

The Frank!Framework is a Java web application that has to be served by an application server. The Frank!Framework can be deployed on many types of application servers, for example Apache Tomcat, JBoss Application Server (recently renamed to WildFly) or WebSphere Application Server. These application server types require different procedures for deploying the Frank!Framework. The present version of this manual only covers deployment on Apache Tomcat. If you want to deploy on a different type of application server, please seek info from one of the Frank!Framework maintainers.

The beginning of this chapter focuses on the application server. How can you get the Frank!Framework working on your application server? When you use :ref:`the Frank!Runner <deploymentTomcat4Frank>` this is easy, but for your production environment you need to understand :ref:`how to install the Frank!Framework manually <deploymentTomcat>`. The end of this chapter turns to the Frank!Framework. You learn how to configure the Frank!Framework by setting the DTAP stage (Development, Test, Acceptance, Production) and you learn how to set properties in general. Then you learn how to restrict access to the Frank!Console to protect your data and the privacy of your customers. Finally, you learn how to provide credentials of external systems to your Frank.

Here is the table of contents of this chapter:

.. toctree::
   :maxdepth: 3

   tomcat4frank
   tomcat
   dtapAndProperties
   security
   credentials
   IdentityProviders/MicrosoftEntraId/microsoftEntraId
   customLogging
 