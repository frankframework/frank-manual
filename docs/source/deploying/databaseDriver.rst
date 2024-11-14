   .. WARNING::

      Under construction.

.. _deployingDatabaseDriver:

The Database Driver
===================

To access a database, the Frank!Framework needs a database driver or a datasource. These are included in a Java library provided by the database vendor. Frank developers who provide a Docker image with a complete Frank application should include the database library of the chosen database. System administrators working with such Docker images do not have to worry about the library. System administrators who only receive a Frank configuration, not a complete Frank application, should install the database library in the deployment environment. This section is both for Frank developers and system administrators. It explains for each database brand which library is needed and how it can be obtained.

.. WARNING::

   Until release 8.3 of the Frank!Framework, the database libraries of many databases were included in the Docker image provided by the maintainers of the Frank!Framework. This is the Docker image that holds the Frank!Framework deployed on Apache Tomcat. From the 9.0 release onwards, the database libraries will be excluded from this standard image to make it smaller. Frank developers typically derive a Docker image from this standard image to provide the Frank configurations the customer needs. They should take care now to add the database library of the chosen database.

The following table shows for each database brand where the library can be found:

.. csv-table::
   :header: Brand, URL to download library, Note

   PostgreSQL, https://central.sonatype.com/artifact/org.postgresql/postgresql/versions
   MariaDB, https://mvnrepository.com/artifact/org.mariadb.jdbc/mariadb-java-client
   MySQL, https://mvnrepository.com/artifact/com.mysql/mysql-connector-j
   MS SQL, https://mvnrepository.com/artifact/com.microsoft.sqlserver/mssql-jdbc, JRE 11 versions work even though the FF! uses JRE 21.
   Oracle, https://mvnrepository.com/artifact/com.oracle.database.jdbc/ojdbc11
   "H2", https://mvnrepository.com/artifact/com.h2database/h2

Each of these URL provides an overview of all released versions. It depends on the FF! version you are using and on the application server which versions will work.
