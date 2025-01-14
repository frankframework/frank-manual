.. _advancedDevelopmentDatabase:

The Database
============

Introduction
------------

In chapter :ref:`gettingStarted`, you learned how to access a relational database. In section :ref:`insertDb`, you used a ``<FixedQuerySender>`` to apply a query to a database. This sender had the following attribute: ``datasourceName="jdbc/${instance.name.lc}"``. This is how you referenced the database. In this section you will learn what is happening behind the scenes. You need this knowledge when you want to set up your own database instead of relying on the Frank!Runner. You will also learn how to work with multiple databases.

How the database is accessed
----------------------------

To understand the attribute ``datasourceName="jdbc/${instance.name.lc}"``, you first have to understand property ``instance.name.lc``, see subsection :ref:`propertiesFramework`. Each instance of the Frank!Framework must define a property ``instance.name``. The Frank!Framework automatically calculates property ``instance.name.lc`` by taking the value of ``instance.name`` and replacing uppercase letters with lowercase letters. For example, if ``instance.name`` is ``MyApp``, then ``instance.name.lc`` becomes ``myapp``. In this case, the shown attribute is equivalent to ``datasourceName="jdbc/myapp"``.

Your deployed configuration thus uses a database that is referenced by the name ``jdbc/myapp`` (or ``jdbc/otherapp`` if ``instance.name`` would be ``OtherApp``). To link a database name to an actual database, the Frank!Framework has to know a few properties: the username and the password, the URL where the database can be reached and the Java class of the driver or datasource the Frank!Framework should use to connect to the database. These are not defined like Frank!Framework properties as described in :ref:`properties`. Instead, they are usually defined in a file ``resources.yml``, see :ref:`deployingDatabase`. For older versions of the Frank!Framework and when application server Apache Tomcat is used, these configurations are done in Tomcat's ``context.xml`` file. This way, Frank developers can write configurations that are independent of the database used by the customer. Furthermore, Frank developers do not have to add sensitive information to Frank configurations.

This knowledge allows you to use multiple databases. If you have a second database then give it another name, say ``jdbc/alternative``. The senders and listeners that access the database all have an attribute ``datasourceName``. Set this attribute within your Frank config, ``datasourceName="jdbc/alternative"``, every time you want to access your second database. It is up to the system administrator of the customer to link this name to his own database.

.. WARNING::

   The Frank!Runner does not support multiple databases. This tool automates deploying the Frank!Framework and it automatically creates a database for your Frank application. You cannot use this project to connect to an existing database or to use multiple databases.

The Frank!Framework uses a default database to store data that is not managed explicitly in Frank configurations. The name of this database is defined in Frank!Framework property ``jdbc.datasource.default`` that has default value ``jdbc/${instance.name.lc}``. If you are using an Apache Tomcat application server, then the Frank!Framework expects that this database exist. If you want to use another default database, you can give property ``jdbc.datasource.default`` another value.

Initial data
------------

The Frank!Framework uses Liquibase to populate your database with tables and with initial data. In your Frank config you include a file ``DatabaseChangelog.xml`` that defines what tables you want to create and what initial data you want. You can provide this information in SQL statements or in pure XML, the latter being database agnostic. See https://www.liquibase.org/ to learn how to write ``DatabaseChangelog.xml``. You saw an example in chapter :ref:`gettingStarted`, section :ref:`databaseInitialization`. Your initial data is split into change sets, each wrapped within XML element ``<changeSet>``.

Liquibase allows multiple deployments of your Frank application to share the same database. Liquibase maintains database tables to remember what change sets have been processed. If one instance applies a change set, the others will see that the change set has been applied. Each instance only applies change sets not yet processed, which causes each change set to be executed only once. This approach only works if change sets are never altered. When you update your Frank config, please do not change existing change sets but append new ones.

.. NOTE::

   If you want to undo initialization by Liquibase and if you have a H2 database, you can execute SQL query ``DROP ALL OBJECTS`` in the JDBC | Execute Query screen.

If you have multiple databases, what database is selected by Liquibase? By default, it is the default database. You can override the database selected by Liquibase by setting property ``jdbc.migrator.dataSource``.

The Frank!Framework only does database initialization when property ``jdbc.migrator.active`` is true. There is a subtle point with this property. It has a different effect as a system property or classpath property on the one hand, or as a configuration property on the other hand. The Frank!Framework needs database tables to perform some advanced services like the error store, see :ref:`managingProcessedMessagesError`. These tables are only created when the Frank!Framework starts with property ``jdbc.migrator.active`` set as a system property or classpath property. If ``jdbc.migrator.active`` is only set within a configuration, then these system tables are not created and the mentioned features will not work.

When ``jdbc.migrator.active`` is true for a configuration, then that configuration can always create and initialize its own database tables using a ``DatabaseChangelog.xml``. This is automatically the case when ``jdbc.migrator.active`` is set to ``true`` as a system property or classpath property and if the configuration does not override that.
