.. _deploymentOverviewSecurityRoles:

Overview of security roles
==========================

Here are the security roles known by the Frank!Framework:

IbisWebService
  Can call an Ibis WebserviceListener.

IbisObserver
  Can look in configurations, statistics and log files.

IbisDataAdmin
  Can browse message logs, message stores and error stores, see section :ref:`operatorManagingProcessedMessages`. Can resend or delete the messages in them. Can reload configurations and start and stop adapters. Has all IbisObserver permissions too.

IbisAdmin
  Can do a full reload and has all IbisDataAdmin permissions.

IbisTester
  Can execute jdbc query, send jms message, test a service and test a pipeline, has all IbisAdmin and IbisWebService permissions too.

.. NOTE::

   "What is 'Ibis'?", you might ask. This comes from the time before the frankemwork was renamed to Frank!Framework. In that time, the brands "Ibis" and "Ibis Adapter Framework" were used. These names have not all been replaced by their Frank! equivalents.
