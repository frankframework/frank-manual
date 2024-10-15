*Under construction*

.. _advancedDevelopmentDockerDevelJms:

Queues and Java Message Service (JMS)
=====================================

Some Frank applications work with queues to implement the Fire and Forget integration pattern, see :ref:`advancedDevelopmentIntegrationPatterns` and :ref:`advancedDevelopmentIntegrationPatternsFireForget`. When the sender of some message should not await a response before proceeding, the message is put on a queue. The intended recipient later dequeues the message and processes it. The recipient is responsible for processing the message and for handling errors. This section explains how to add a queue to a development environment based on Docker.

The Frank!Framework is programmed in the programming language Java. A standard has been established about the interface between Java applications and queues, which is named Java Message Service (JMS). The Frank!Framework only supports queueing systems that implement JMS.

To explain how to add a queue, we start from the following :download:`example Frank application <../../downloads/advancedDevelopmentDockerDevelPreJms.zip>`. It receives HTTP requests via an ``<ApiListener>`` and writes something in the database. We explain here how to add a queue to the development environment. Using the queue is explained in :ref:`advancedDevelopmentIntegrationPatternsErrorStoreXa`.

First, the ``docker-compose.yml`` file has to be extended to add a container with a queueing system:

.. include:: ../../snippets/Frank2Transactions/v510/docker-compose.txt

The JMS container comes from an image hosted on a server owned by the maintainers of the Frank!Framework, the same server that holds image ``nexus.frankframework.org/frankframework``. System property ``jms.createDestination`` is set to ``true`` to tell the Frank!Framework that it should create the queues that are referenced in Frank configurations. This is useful during development because it makes it easier to get up and running. In the production environment, queues should be created and maintained by a system administrator and then the Frank!Framework should only reference existing queues. On production, property ``jms.createDestination`` should be ``false``.

System property ``jms.hostname`` is added to make ``resources.yml`` independent of the service name (here ``jms``) chosen for the queue container. Propert ``transactionmanager.type.default: NARAYANA`` is needed to supports XA transactions, transactions that span multiple data-processing systems.

Second, ``resources.yml`` should be updated so that the Frank!Framework can find the queue:

.. include:: ../../snippets/Frank2Transactions/v510/reference-queue.txt

The queue is given JNDI name ``qcf-artemis``, the name by which Frank configurations can reference it. The ``type`` field references the Java class that should be used to access the queue. And the ``url`` is needed by the Frank!Framework to reach the queue that is refenced as ``qcf-artemis`` in Frank configurations. Within the value of the ``url`` field, property ``jms.hostname`` is referenced. If the name of the Docker container holding the queue is changed, this property should be updated to hold the new name. Because of the property reference, the ``url`` within ``resources.yml`` does not have to be updated in this case.

Above the JMS resource, the JDBC resource is updated to use another database driver, a database driver that supports XA transactions.