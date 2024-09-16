.. _advancedDevelopmentIntegrationPatternsTransactions:

Transactions
============

Transactions ensure that manipulations of data are either done correctly or not at all. The typical example is money transfer. When some person A pays person B, then A's balance has to be reduced and B's balance has to be increased. Without transactions, it would be possible that A's balance were reduced while an error occurred increasing B's balance, causing a loss of money. With transactions in place, the transaction becomes atomic. Either A's balance is reduced *and* B's balance is increased, or both A's balance and B's balance are unmodified in case of an error.

Transactions are supported by databases. In Frank configurations, it is possible to manipulate the transactions applied by the underlying database. In addition, it is possible to work with XA transactions, transactions that run over multiple databases. That will be covered later. This section focuses on transactions that apply to a single database.

Transactions are configured in a ``<Receiver>`` or in a ``<Pipeline>``, in both of them using attribute ``transactionAttribute``. Possible values of this attribute are ``Required``, ``RequiresNew``, ``Mandatory``, ``NotSupported``, ``Supports`` and ``Never``. The exact meaning of these values can be found in the Frank!Doc. When the receiver of an ``<Adapter>`` has ``transactionAttribute="Required"``, then all data manipulations done by the receiver itself and by the pipeline are meant to happen in the same (database) transaction. When another adapter is called, the logic in that sub-adapter can happen in the same transaction depending on the ``transactionAttribute`` configured in the sub-adapter's ``<Receiver>`` or ``<Pipeline>``. When the ``transactionAttribute`` is set on the ``<Pipeline>``, the data manipulations done by the receiver are excluded from the transaction.

Tutorial
--------

The following exercise may help you to understand transactions:

1. Start with the same example as used in the previous section, the :download:`example Frank application <../../downloads/advancedDevelopmentIntegrationPatternsMessageId.zip>`. Undo possible modifications you may have done or extract the zip file again.
#. In the Frank!Console, stop adapter ``writeTableOtherMessage``.
#. Using your API client, send a HTTP request to the application - this time a plain-text body and header ``Message-Id`` for the message id.
#. Using JDBC | Execute query, check that table ``Message`` has been updated but not table ``otherMessage``. This is what we want to avoid with transactions.
#. Stop the application and modify it to set ``transactionAttribute`` as shown below:

   .. include:: ../../snippets/Frank2Transactions/v500/addTransactionAttribute.txt

#. In the Frank!Console, stop adapter ``writeTableOtherMessage``.
#. Using your API client, send a HTTP request to the application.
#. Check that there is a Ladybug report for handling this HTTP request. It should be red to indicate that an error occurred. It should also show that adapter ``writeTableMessage`` ran successfully.
#. Using JDBC | Execute Query, check that neither table ``Message`` nor table ``otherMessage`` has been updated, even though the adapter that initially updated table ``Message`` was successful. This demonstrates that the transaction was *rolled back*.
#. Stop the application and modify it as follows. Remove the attribute ``transactionAttribute="RequiresNew"`` from adapter ``writeDb``, but leave the ``transactionAttribute="Mandatory"`` of the two sub-adapters.
#. Start the application again and make sure that all adapters are up and running.
#. Using your API client, issue a HTTP request to the application.
#. It should fail. Check the messages in the Frank!Console. It has failed because adapters ``writeTableMessage`` and ``writeTableOtherMessage`` were called outside of a transaction. The attribute ``transactionAttribute="Mandatory"`` means that calling this receiver (or pipeline) outside of a transaction should be flagged as an error.

.. NOTE::

   Attribute ``transactionAttribute`` has a default value, which is ``Supports``. This means that the above example works without setting ``transactionAttribute`` on the sub-adapters. Setting ``transactionAttribute="RequiresNew"`` in the receiver of adapter ``writeDb`` is sufficient. This lets the sub-adapters support the transaction that was initiated by the calling adapter.