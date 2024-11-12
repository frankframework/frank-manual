   .. WARNING::

      Under construction.

.. _deployingDatabaseDriver:

The Database Driver
===================

To access a database, the Frank!Framework needs a *database driver*. A database driver is a Java library provided by the database vendor. Frank developers who provide a Docker image with a complete Frank application should include the database driver of the chosen database. System administrators working with such Docker images do not have to worry about the database driver. System administrators who only receive a Frank configuration, not a complete Frank application, should install the database driver in the deployment environment. This section is both for Frank developers and system administrators. It explains for each database brand which database driver is needed and how it can be obtained.

.. WARNING::

   Until release 8.3 of the Frank!Framework, the database drivers of many databases were included in the Docker image provided by the maintainers of the Frank!Framework. This is the Docker image that holds the Frank!Framework deployed on Apache Tomcat. From the 9.0 release onwards, the database drivers will be excluded from this standard image to make it smaller. Frank developers typically derive a Docker image from this standard image to provide the Frank configurations the customer needs. They should take care now to add the database driver of the chosen database.

The database driver is related to the ``type`` field of ``resources.yml``, see the previous section :ref:`deployingDatabase`. The value of the ``type`` field is the name of a Java class that should be in the database driver. The Frank!Framework uses the class referenced by the ``type`` field as the entry point of the database driver.

Java applications use Maven as a tool to manage dependencies. In Maven, each library is referenced by three *Maven coordinates* which are the group id, the artifact id and the version. These coordinates are not only usable by Maven, but they can also be used to search for database drivers on the internet. The following table lists for each ``type`` the Maven coordinates of the related database driver.

+--------------------------------------------------+-----------------------------------------------------+
| ``type``                                         | Maven dependency                                    |
+==================================================+=====================================================+
| ``org.postgresql.Driver``                        | .. code-block::                                     |
| or                                               |                                                     |
| ``org.postgresql.xa.PGXADataSource``             |    <dependency>                                     |
|                                                  |        <groupId>org.postgresql</groupId>            |
|                                                  |        <artifactId>postgresql</artifactId>          |
|                                                  |        <version>42.7.4</version>                    |
|                                                  |    </dependency>                                    |
+--------------------------------------------------+-----------------------------------------------------+
| ``org.mariadb.jdbc.Driver``                      | .. code-block::                                     |
|                                                  |                                                     |
|                                                  |    <dependency>                                     |
|                                                  |        <groupId>org.mariadb.jdbc</groupId>          |
|                                                  |        <artifactId>mariadb-java-client</artifactId> |
|                                                  |        <version>3.5.0</version>                     |
|                                                  |    </dependency>                                    |
+--------------------------------------------------+-----------------------------------------------------+
| ``com.mysql.cj.jdbc.Driver``                     | .. code-block::                                     |
|                                                  |                                                     |
|                                                  |    <dependency>                                     |
|                                                  |        <groupId>com.mysql</groupId>                 |
|                                                  |        <artifactId>mysql-connector-j</artifactId>   |
|                                                  |        <version>9.1.0</version>                     |
|                                                  |    </dependency>                                    |
+--------------------------------------------------+-----------------------------------------------------+
| ``com.microsoft.sqlserver.jdbc.SQLServerDriver`` | .. code-block::                                     |
|                                                  |                                                     |
|                                                  |    <dependency>                                     |
|                                                  |        <groupId>com.microsoft.sqlserver</groupId>   |
|                                                  |        <artifactId>mssql-jdbc</artifactId>          |
|                                                  |        <version>12.8.1.jre11</version>              |
|                                                  |    </dependency>                                    |
+--------------------------------------------------+-----------------------------------------------------+
| ``oracle.jdbc.driver.OracleDriver``              | .. code-block::                                     |
|                                                  |                                                     |
|                                                  |    <dependency>                                     |
|                                                  |        <groupId>com.oracle.database.jdbc</groupId>  |
|                                                  |        <artifactId>ojdbc11</artifactId>             |
|                                                  |        <version>23.6.0.24.10</version>              |
|                                                  |    </dependency>                                    |
+--------------------------------------------------+-----------------------------------------------------+
| ``org.h2.jdbcx.JdbcDataSource``                  | .. code-block::                                     |
|                                                  |                                                     |
|                                                  |   <dependency>                                      |
|                                                  |       <groupId>com.h2database</groupId>             |
|                                                  |       <artifactId>h2</artifactId>                   |
|                                                  |       <version>2.3.232</version>                    |
|                                                  |   </dependency>                                     |
+--------------------------------------------------+-----------------------------------------------------+
