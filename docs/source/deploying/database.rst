.. _deployingDatabase:

Configuring the Database
========================

This page contains general information on configuring databases with the Frank!Framework. If you understand this and if you are looking up specific information about database drivers or details for the chosen database, please go to :ref:`deployingDatabaseDriver`.

Frank developers write Frank configurations that may access a database. This database is referenced in Frank configurations by its name. The name of a database starts with ``jdbc/`` and after the ``/`` comes some unique name. As a system administrator it is your job to configure the database that belongs to the name referenced in the Frank configuration. This is done by file ``resources.yml``, see below. The Frank!Framework also needs a database-vendor-supplied Java class to access the database on the Java classpath. See below, :ref:`deployingDatabaseGeneralAboutDriver`.

Introduction to ``resources.yml``
---------------------------------

When a Frank application is applied in the application server Apache Tomcat, then Tomcat's ``context.xml`` may be provided to configure the database. This approach is discouraged, because the Frank!Framework supports multiple application servers. The Frank!Framework supports database configurations that are provided in a YAML file, ``resources.yml``. When you use the image provided by the maintainers of the Frank!Framework, the path is expected to be ``/opt/frank/resources/resources.yml`` (or ``/opt/frank/configurations/resources.yml`` but doing that is not recommended, see :ref:`advancedDevelopmentDockerDevelBasics`).

Here is an example that shows the syntax of ``resources.yml`` (do not use in production):

.. code-block:: none

   jdbc:
     - name: "ibis4test-mssql"
       type: "com.microsoft.sqlserver.jdbc.SQLServerXADataSource"
       url: "jdbc:sqlserver://${jdbc.hostname:-localhost}:1433;database=testiaf"
       authalias: "${db.authalias}"
       username: "testiaf_user"
       password: "testiaf_user00"
       properties:
         sendStringParametersAsUnicode: "false"
         sendTimeAsDatetime: "true"
         selectMethod: "direct"

.. NOTE::

   The shown line ``authalias: "${db.authalias}"`` demonstrates that system properties or application properties can be referenced in ``resources.yml``.

There is a top-level YAML object ``jdbc`` that contains a list of database resources. Each resource is an object that has at least the fields ``name``, ``type`` and ``url``. The ``name`` should be the part of the database name that comes after ``jdbc/``. If the database name is ``jdbc/myDatabase``, then the ``name`` field should be ``myDatabase``. The fields ``type`` and ``url`` define how to reach the database. Sometimes the ``properties`` field is added, see below. Credentials to access the database should be provided through the combination of fields ``username`` and ``password``, or through ``authalias`` if the username and the password are treated as secrets (see :ref:`deploymentCredentials`).

.. NOTE::

   The shown example has both ``authalias``, ``username`` and ``password``. In this situation, the ``authalias`` takes precedence over the ``username`` / ``password`` combination.

The ``type`` field
------------------

Database vendors provide Java libraries to access their databases from Java code. The library for the chosen database has to be available on the Java classpath, see :ref:`deployingDatabaseGeneralAboutDriver` and :ref:`deployingDatabaseDriver`. As a system administrator, you have to choose a Java class from the library; the Java class that the Frank!Framework should access. This is the value of the ``type`` field. In general, there are two options: choosing a *database driver* (not recommended) or choosing a *datasource*. A database driver attempts to initialise a DataSource for you. It may do this based on bias defaults. It is therefor recommended to always configure a DataSource directly. Drivers do not provider more functionality, and are purely a wrapper around (usually a NON-XA) DataSource.

.. NOTE::

   If you are a Java developer, you can read https://medium.com/@satyendra.jaiswal/demystifying-jdbc-drivers-and-data-sources-a-comprehensive-guide-e7a498ab9f0b for a better understanding about database drivers and data sources.

To choose a value for the ``type`` field, you need to know the brand of the database and you need to know whether you need XA transactions. XA transactions are transactions that have to commit or rollback manipulations of multiple systems; these systems can be databases or queues. If you need XA transactions, you have to configure a datasource and you have to choose one that supports XA transactions. For a concrete overview of your options, see :ref:`deployingDatabaseDriver`.

Fields ``url`` and ``properties``
---------------------------------

The field ``url`` contains the address of the database. The syntax is a bit different for different database brands. Some vendors allow property/value pairs within the URL to configure the connection to the database. The syntax for adding properties in the ``url`` is different for different database vendors. For this reason, the Frank!Framework supports the ``properties`` field in ``resources.yml``. All properties supported by each database vendor can be configured in the ``properties`` field of ``resources.yml``. For detailed information, see :ref:`deployingDatabaseDriver`.

.. _deployingDatabaseGeneralAboutDriver:

Database driver or datasource
-----------------------------

To access a database, the Frank!Framework needs a database driver or a datasource, see :ref:`deployingDatabaseDriver`. These drivers are included in a Java library provided by the database vendor. The driver needs to be placed or mounted in the ``/opt/frank/drivers`` directory. Depending on your needs you might want to do this as part of your project (and use a Containerfile to copy the file over), or let a system administrator install the database library in the deployment environment.

.. WARNING::

   This is possible sinds release 9.2 of the Frank!Framework, before this version the database libraries of many databases were included in the Docker image provided by the maintainers of the Frank!Framework. In order to give end users more granularity and control over which version they use, they can now easily overwrite driver types and versions.

Frank developers should carefully consider the location of the database library. If the standard image is used to derive a customer-specific image and if the database library should be in the image, then add the library in ``/opt/frank/drivers``. If the customer is to add the database driver, make ``/opt/frank/drivers`` a volume. The customer can then supply the database library.
