.. _dbVendorSpecific:

Database vendor specific
========================

This section contains database vendor specific information to use the database with the Frank!Framework.

PostgreSQL
----------

If you want to use XA transactions, you have to set a property within the database: ``max_prepared_transactions``. You can do this by executing the following query:

.. code-block:: none

   ALTER SYSTEM SET max_prepared_transactions = 100;

If this propery is not set, XA transactions may be rolled back unexpectedly.
