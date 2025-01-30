.. _dbVendorSpecific:

Database vendor specific
========================

This section contains database vendor specific information to use the database with the Frank!Framework.

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
