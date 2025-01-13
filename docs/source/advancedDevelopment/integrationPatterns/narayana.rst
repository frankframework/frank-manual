.. _advancedDevelopmentIntegrationPatternsNarayana:

Narayana TransactionManager
===========================

This section shows how to configure the Narayana Transaction Manager. Its purpose was explained in :ref:`advancedDevelopmentIntegrationPatternsErrorStoreXa`. Narayana is the OpenSource implementation of a two phase commit transaction coordinate. It was developed for WildFly and JBoss EAP and it is backed by the company Red Hat.

**TX-Managers uniqueness**

When deploying an application, the transaction manager needs to have a unique identifier. We call this the uid. There are also a few default transaction settings that you can change to improve your workflow. More information can be found in the community documentation, a link has been added at the end of this document.

.. code-block:: none

   transactionmanager.uid=

   # Maximum timeout (in s) that can be allowed for transactions.
   transactionmanager.defaultTransactionTimeout=180

   # Amount of time (in ms) between runs of the TX maintenance thread.
   transactionmanager.narayana.reapTime=120000
   # Interval (in ms) allowed for a single active connection to be in use to the backend resource before it is considered to be *stuck*
   transactionmanager.narayana.stuckTime=180000
   # How often (in ms) the connection pool checks for stuck connections.
   transactionmanager.narayana.stuckTimerTime=30000

**Types of ObjectStores**

Narayana has multiple types of storing the transaction information. This can be done on the local filesystem (should not be a mount and requires low latency access), in memory (though should the application stop, all information will be lost), or stored in a database.

The JDBCStore is the preferred cloud solution due to the way filesystem mounts work. In a clustered environment filesystems may be shared over multiple nodes which may create extra latency. Databases are more robust and made for (local) transactional data transfer, they can operate independently of any availability zone or cluster.

**ShadowNoFileLockStore**

The default storage implementation is the ShadowNoFileLockStore which relies upon user-level locking. It uses pairs of files to represent objects. One file is the shadow version and the other is the committed version. Files are opened, locked, operated upon, unlocked, and closed on every interaction with the object store.

**JDBCStore**

Another implementation is the JDBCStore which uses a database to save persistent object states in BLOB format.

Changing between ObjectStores can be done by using the ``objectStoreType`` property. When using the JDBCStore, three additional properties may be configured.

The ``objectStoreDatasource`` property may refer to a DataSource available in the applicationservers JDNI context. And if the application has been given create / drop table access it can also control the table structure.

.. code-block:: none

   ## Narayana ObjectStore Settings
   # When using the database the FQDN must be used, eg; com.arjuna.ats.internal.arjuna.objectstore.jdbc.JDBCStore
   transactionmanager.narayana.objectStoreType=com.arjuna.ats.internal.arjuna.objectstore.ShadowNoFileLockStore
   # DataSource name, should not be XA-capable and will be managed + pooled by the framework.
   transactionmanager.narayana.objectStoreDatasource=
   transactionmanager.narayana.dropTable=false
   transactionmanager.narayana.createTable=true

Notes:

* The limitation on object state size imposed by using BLOBs is 64k.
* The JDBCStore’s DataSource should not be transactional itself.

More information regarding the JDBC ObjectStore can be found in the community documentation, section ‘A.1.1.5. The JDBC store’. Narayana website: https://www.narayana.io/ Product documentation: https://www.narayana.io/docs/project/index.html