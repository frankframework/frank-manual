.. _deployingDatabaseDriver:

Database vendor specific information
====================================

The following table shows your options to configure the ``type`` field of ``resources.yml``:

.. csv-table::
   :header: Brand, Kind, ``type``

   PostgreSQL, driver, ``org.postgresql.Driver``
   PostgreSQL, non-XA datasource, ``org.postgresql.ds.PGSimpleDataSource``
   PostgreSQL, XA datasource*, ``org.postgresql.xa.PGXADataSource``
   MariaDB, driver, ``org.mariadb.jdbc.Driver``
   MariaDB, datasource with or without XA, ``org.mariadb.jdbc.MariaDbDataSource``
   MySQL, driver, ``com.mysql.cj.jdbc.Driver``
   MySQL, XA datasource, ``com.mysql.cj.jdbc.MysqlXADataSource``
   MS SQL, driver, ``com.microsoft.sqlserver.jdbc.SQLServerDriver``
   MS SQL, XA datasource, ``com.microsoft.sqlserver.jdbc.SQLServerXADataSource``
   Oracle, driver, ``oracle.jdbc.driver.OracleDriver``
   Oracle, non-XA datasource, ``oracle.jdbc.pool.OracleDataSource``
   Oracle, XA datasource, ``oracle.jdbc.xa.client.OracleXADataSource``
   H2, non-XA datasource, ``org.h2.jdbcx.JdbcDataSource``

\* = Only works if you also enable a transaction manager, i.e. Narayana. A transaction manager coordinates XA transactions. You also have to set PostgreSQL property ``max_prepared_transactions``, see :ref:`dbVendorSpecificPostgreSQL`.

The following table shows a basic template for the ``url`` field of ``resources.yml`` for each database brand.

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

The following table shows for each database brand where the vendor-specific library can be downloaded:

.. csv-table::
   :header: Brand, URL to download library, Note

   PostgreSQL, https://central.sonatype.com/artifact/org.postgresql/postgresql/versions
   MariaDB, https://mvnrepository.com/artifact/org.mariadb.jdbc/mariadb-java-client
   MySQL, https://mvnrepository.com/artifact/com.mysql/mysql-connector-j
   MS SQL, https://mvnrepository.com/artifact/com.microsoft.sqlserver/mssql-jdbc, JRE 11 versions work even though the FF! uses JRE 21.
   Oracle, https://mvnrepository.com/artifact/com.oracle.database.jdbc/ojdbc11
   "H2", https://mvnrepository.com/artifact/com.h2database/h2

Each of these URLs provides an overview of all released versions. It depends on the FF! version you are using and on the application server which versions will work. See :ref:`deployingDatabaseGeneralAboutDriver` for the purpose of this library.

.. _dbVendorSpecific:

Additional details
------------------

This page continues with vendor-specific details that does not fit within the above tables.

.. _dbVendorSpecificPostgreSQL:

PostgreSQL
----------

If you want to use XA transactions, you have to set a property within the database: ``max_prepared_transactions``. You can do this by executing the following query:

.. code-block:: none

   ALTER SYSTEM SET max_prepared_transactions = 100;

If this propery is not set, XA transactions may be rolled back unexpectedly. This problem may manifest itself with the following Java stacktrace in the log:

.. code-block:: none

   ...
   Caused by: org.postgresql.util.PSQLException: ERROR: prepared transactions are disabled
     Hint: Set "max_prepared_transactions" to a nonzero value.
       at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2733) ~[postgresql.jar:42.7.4]
       at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2420) ~[postgresql.jar:42.7.4]
       at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:372) ~[postgresql.jar:42.7.4]
       at org.postgresql.jdbc.PgStatement.executeInternal(PgStatement.java:517) ~[postgresql.jar:42.7.4]
       at org.postgresql.jdbc.PgStatement.execute(PgStatement.java:434) ~[postgresql.jar:42.7.4]
       at org.postgresql.jdbc.PgStatement.executeWithFlags(PgStatement.java:356) ~[postgresql.jar:42.7.4]
       at org.postgresql.jdbc.PgStatement.executeCachedSql(PgStatement.java:341) ~[postgresql.jar:42.7.4]
       at org.postgresql.jdbc.PgStatement.executeWithFlags(PgStatement.java:317) ~[postgresql.jar:42.7.4]
       at org.postgresql.jdbc.PgStatement.executeUpdate(PgStatement.java:290) ~[postgresql.jar:42.7.4]
       at org.postgresql.xa.PGXAConnection.prepare(PGXAConnection.java:357) ~[postgresql.jar:42.7.4]
       ... 20 more
   ...

H2
---

For H2 databases, it is recommended to configure properties ``DB_CLOSE_DELAY=-1``, ``DB_CLOSE_ON_EXIT=FALSE``, ``AUTO_RECONNECT=TRUE`` and ``MODE=Post``. These are properties for the ``properties`` field of ``resources.yml``.
