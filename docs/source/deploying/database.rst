   .. WARNING::

      Under construction.

.. _deployingDatabase:

Configuring the Database
========================

Frank developers write Frank configurations that may access a database. This database is referenced in Frank configurations by its so-called JNDI name (Java Naming and Directory Interface). The JNDI name of a database starts with ``jdbc/`` and after the ``/`` comes some unique name. As a system administrator it is your job to configure the database that belongs to the name referenced in the Frank configuration. You may also have to take care of the database driver, see the next section :ref:`deployingDatabaseDriver`.

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

There is a top-level YAML object ``jdbc`` that contains a list of database resources. Each resource is an object that has at least the fields ``name``, ``type`` and ``url``. The ``name`` should be the part of the JNDI name that comes after ``jdbc/``. If the JNDI name of the database is ``jdbc/myDatabase``, then the ``name`` field should be ``myDatabase``. The fields ``type`` and ``url`` define how to reach the database. Sometimes the ``properties`` field is added, see below. Credentials to access the database should be provided through the combination of fields ``username`` and ``password``, or through ``authalias`` if the username and the password are treated as secrets (see :ref:`deploymentCredentials`).

.. WARNING::

   The shown example has both ``authalias``, ``username`` and ``password``. Do not do that in production.

The ``type`` field
------------------

Database vendors provide Java libraries to access their databases from Java code. The library for the chosen database has to be available on the Java classpath, see the next section :ref:`deployingDatabaseDriver`. As a system administrator, you have to choose a Java class from the library; the Java class that the Frank!Framework should access. This is the value of the ``type`` field. In general, there are two options: choosing a *database driver* or choosing a *datasource*. A database driver handles low-level details like parsing SQL statements and exchanging data with the database server. A datasource uses a driver to provide a more functionality to Java applications, so to the Frank!Framework as well. Data sources can for example manage a pool of database connections (connection pooling).

.. NOTE::

   If you are a Java developer, you can read https://medium.com/@satyendra.jaiswal/demystifying-jdbc-drivers-and-data-sources-a-comprehensive-guide-e7a498ab9f0b for a better understanding about database drivers and data sources.

If the ``type`` field references a database driver, the Frank!Framework creates a database vendor independent datasource that uses the driver. If the ``type`` field references a vendor-specific datasource, the Frank!Framework uses that datasource directly. For system administrators of the Frank!Framework, configuring a database driver is the simplest choice. It provides access to the database server and leaves details related to the datasource to the Frank!Framework. If you want more control over the database, configure a vendor-specific datasource and optionally configure it by setting additional properties.

To choose a value for the ``type`` field, you need to know the brand of the database and you need to know whether you need XA transactions. XA transactions are transactions that have to commit or rollback manipulations of multiple systems; these systems can be databases or queues. If you need XA transactions, you have to configure a datasource and you have to choose one that supports XA transactions.

The following table shows your options to configure the ``type``:

.. csv-table::
   :header: Brand, Kind, ``type``

   PostgreSQL, driver, ``org.postgresql.Driver``
   PostgreSQL, XA datasource*, ``org.postgresql.xa.PGXADataSource``
   MariaDB, driver, ``org.mariadb.jdbc.Driver``
   MariaDB, non-XA datasource, ``org.mariadb.jdbc.MariaDbDataSource``
   MySQL, driver, ``com.mysql.cj.jdbc.Driver``
   MySQL, XA datasource, ``com.mysql.cj.jdbc.MysqlXADataSource``
   MS SQL, driver, ``com.microsoft.sqlserver.jdbc.SQLServerDriver``
   MS SQL, XA datasource, ``com.microsoft.sqlserver.jdbc.SQLServerXADataSource``
   Oracle, driver, ``oracle.jdbc.driver.OracleDriver``
   Oracle, non-XA datasource, ``oracle.jdbc.pool.OracleDataSource``
   Oracle, XA datasource, ``oracle.jdbc.xa.client.OracleXADataSource``
   H2, non-XA datasource, ``org.h2.jdbcx.JdbcDataSource``

* = Only works if you also enable a transaction manager, i.e. Narayana. A transaction manager coordinates XA transactions.

Fields ``url`` and ``properties``
---------------------------------

The field ``url`` contains the address of the database. The syntax is a bit different for different database brands. Some vendors allow property/value pairs within the URL to configure the database driver. The syntax for adding properties in the ``url`` is different for different database vendors. For this reason, the Frank!Framework supports the ``properties`` field in ``resources.yml``. All properties supported by a database vendor can be configured within ``properties``.

The following table shows a basic template for the ``url`` for each database brand.

.. csv-table::
   :header: Brand, ``url``

   PostgreSQL, ``jdbc:postgresql://<host>:5432/<name of database>``
   MariaDB, ``jdbc:mariadb://<host>:3306/<name of database>``
   MySQL, ``jdbc:mysql://<host>:3306/<name of database>``
   MS SQL, ``jdbc:sqlserver://<host>:1433;database=<name of database>``
   Oracle, ``jdbc:oracle:thin:@<host>:1521:<name of database>``
   "H2", ``jdbc:h2:mem:<name of database>`` for in-memory or ``jdbc:h2:<directory name>/<name of database>`` to store the data in file(s)

**host:** IP address or DNS name.

**name of database:** Database vendors have different terms: database, service, sid and more.

Every shown URL has a port number. It is possible to omit the port number; the shown port number is the default in that case. It is also possible to work with a different port, but then the database has to be configured to listen to that other port.

Some database vendors support more URL syntaxes than shown here. These possibilities are beyond the scope of this manual. See also https://www.netiq.com/documentation/identity-manager-49-drivers/jdbc/data/supported-third-party-jdbc-drivers.html#t47303hry5lw. and https://www.baeldung.com/java-jdbc-url-format. 

.. WARNING::

   For H2 databases, it is recommended to configure properties ``DB_CLOSE_DELAY=-1``, ``DB_CLOSE_ON_EXIT=FALSE``, ``AUTO_RECONNECT=TRUE`` and ``MODE=Post``.