   .. WARNING::

      Under construction.

.. _deployingDatabase:

Configuring the Database
========================

Frank developers write Frank configurations that may access a database. This database is referenced in Frank configurations by its so-called JNDI name (Java Naming and Directory Interface). The JNDI name of a database starts with ``jdbc/`` and after the ``/`` comes some unique name. As a system administrator it is your job to configure the database that belongs to the name referenced in the Frank configuration. You may also have to take care of the database driver, see the next section :ref:`deployingDatabaseDriver`.

When a Frank application is applied in the application server Apache Tomcat, then Tomcat's ``context.xml`` may be provided to configure the database. This approach is discouraged, because the Frank!Framework supports multiple application servers. The Frank!Framework supports database configurations that are provided in a YAML file, ``resources.yml``. When you use the image provided by the maintainers of the Frank!Framework, the path is expected to be ``/opt/frank/resources/resources.yml``.

Here is an example of a ``resources.yml`` file:

.. literalinclude:: ../../../srcSteps/Frank2DockerDevel/v500/resources/resources.yml
   :language: none

.. NOTE::

   H2 is not meant for production, only for testing. This explains why this example does not have a username or a password.

There is a top-level YAML object ``jdbc`` that contains a list of database resources. Each resource is an object that has at least the fields ``name``, ``type`` and ``url``. The ``name`` should be the part of the JNDI name that comes after ``jdbc``. If the JNDI name of the database is ``jdbc/myDatabase``, then the ``name`` field should be ``myDatabase``. Credentials to access the database should be provided through the combination of fields ``username`` and ``password``, or through ``authalias`` if the username and the password are treated as secrets (see :ref:`deploymentCredentials`).

The fields ``type`` and ``url`` depend on the database brand. They also depend on whether XA transactions are needed (transactions over multiple databases or queues). The ``url`` also allows the system administrator to configure database brand specific options. See the table below:

.. csv-table::
   :header: "Kind", ``type``, ``url``

   "PostgreSQL", ``org.postgresql.Driver`` if no XA or ``org.postgresql.xa.PGXADataSource`` if XA should be supported, ``jdbc:postgresql://<host>:5432/<name of database>``
   "MariaDB", ``org.mariadb.jdbc.Driver``, ``jdbc:mysql://<host>:3306/<name of database>``
   "MySQL", ``com.mysql.cj.jdbc.Driver``, ``jdbc:mysql://<host>:3306/<name of database>``
   "MS SQL", ``com.microsoft.sqlserver.jdbc.SQLServerDriver``, ``jdbc:sqlserver://<host><optional-port><mssql-options>``
   Oracle thin client, ``oracle.jdbc.driver.OracleDriver``, ``jdbc:oracle:thin:<host>:1521:<sid>`` or ``jdbc:oracle:thin:<host>:1521/<service>``
   Oracle OCI driver, ``oracle.jdbc.driver.OracleDriver``, ``jdbc:oracle:oci8:<tns-name>``
   "H2", ``org.h2.jdbcx.JdbcDataSource``, ``jdbc:h2:mem:<name of database><h2-options>`` for in-memory or ``jdbc:h2:<directory name>/<database name>`` to store the data in file(s)

**host:** IP address or DNS name.

**mssql-options:** A list of name/value pairs in which a ``;`` is used as delimiter. Specify the database by taking ``;databaseName=<name of database>``. Another URL parameter is ``integratedSecurity``. This parameter can be ``false`` (the default) or ``true``. Value ``false`` means that JDBC authentication is used. Value ``true`` means that Windows process-level authentication is used.

**h2-options:** A list of name/value pairs in which a ``;`` is used as the delimeter. An example url is ``jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE;AUTO_RECONNECT=TRUE;MODE=Post``. See https://h2database.com/html/features.html#database_url for details.

**optional-port:** ``:<port number>`` or omitted.

See also https://www.netiq.com/documentation/identity-manager-49-drivers/jdbc/data/supported-third-party-jdbc-drivers.html#t47303hry5lw.

