.. _deployingJms:

Configuring JMS and its driver
==============================

JMS stands for Java Message Service. This is a standard that allows Java applications, including the Frank!Framework, to write and read from queues. Frank configurations access the queue system through its name. This is a string that starts with ``jms/``, for example ``jms/qcf-artemis``. As a system administrator, you should receive the name that is given to the queue system to be accessed. It is your job to set up this queue system and to configure how the Frank!Framework should reach the queue system.

.. NOTE::

   Frank developers should know that the name of the queue system to read or write is specified in attribute ``queueConnectionFactoryName`` of the ``<JmsSender>`` or ``<JmsListener>``. The actual queue is specified by attribute ``destinationName``.

``resources.yml``
-----------------

You can use file ``resources.yml`` to specify how the Frank!Framework can access the queue; this is the same file as used to configure databases. As a brother of the ``jdbc`` YAML object, there is a ``jms`` object. The ``jms`` object has a list of JMS resources. Here is an example:

.. code-block::

   jdbc:
     - name: "frank2transactions"
       ...
   jms:
     - name: "qcf-artemis"
       type: "org.apache.activemq.artemis.jms.client.ActiveMQXAConnectionFactory"
       url: "tcp://${jms.hostname:-localhost}:61615"

The fields that can appear under ``jms`` to configure queues are the same as the fields that can appear under ``jdbc`` to configure databases: they are ``name``, ``type``, ``url``, ``authalias``, ``username``, ``password`` and ``properties``.

The ``name`` field should be the part of the queue system name that comes after ``jms/``.

The ``type`` specifies the Java class that should be used as connection factory. The ``type`` field is more straightforward for queues than it is for databases - for queues there is no counterpart for the choice between a driver and a datasource. You still have to take care that your queue connection factory supports XA transactions when required -- you need XA transactions if you want transactions that span multiple systems, for example when reading a queue and writing a database has to happen within the same transaction.

The values to use for the ``type`` and the ``url`` depend on the brand of the queueing system; more information is given in the remainder of this page. Detailed information on the ``url`` to use is often given by the vendor of the queueing system. When the vendor documents that the URL can contain name/value pairs, you are adviced to put them in the ``properties`` field of ``resources.yml`` instead. Different vendors may require a different syntax for name/value pairs in the URL. Using ``properties`` is less error-prone and easier to read.

The following table shows for a few queueing system vendors what value to use for ``type`` and ``url``:

.. csv-table::
   :header: Brand, XA, ``type``, ``url``

   Active MQ Classic, yes, ``org.apache.activemq.ActiveMQXAConnectionFactory``, ``tcp://<host>:61616``
   Active MQ Artemis, yes, ``org.apache.activemq.artemis.jms.client.ActiveMQXAConnectionFactory``, ``tcp://<host>:61616``

**host:** IP address or DNS name.

Every shown URL has a port number. It is possible to omit the port number; the shown port number is the default in that case. It is also possible to work with a different port, but then the queueing system has to be configured to listen to that other port.

There are many other vendors of queueing systems. Please browse the internet to find them and to find the appropriate values for ``type``, ``url`` and ``properties``.

Fields ``authalias``, ``username`` and ``password`` are needed if the queueing system requires authentication. If you want to keep the username and the password secret, you can use ``authalias`` and use the Frank!Framework's credentials system to keep the username and the password secret, see :ref:`deploymentCredentials`. If ``authalias``, ``username`` and ``password`` are all given, then ``authalias`` takes precedence over ``username`` and ``password``.

Vendor specific library
-----------------------

The Java class referenced in the ``type`` field, the queue connection factory, is in a vendor-specific queueing library. From the 9.0 release of the Frank!Framework onwards, the queueing library is not in the standard Docker image of the Frank!Framework. Frank developers may or may not add this library to customer-specific Docker images. The location of the queueing library is the same as the location of the database library: ``/usr/local/tomcat/lib`` or ``/opt/frank/resources``, see :ref:`deployingDatabaseDriver` for more information.

The following table shows for a few vendors where to find the queueing library:

.. csv-table::
   :header: Brand, URL to download library

   Active MQ Classic, https://mvnrepository.com/artifact/org.apache.activemq/activemq-all
   Active MQ Artemis, https://mvnrepository.com/artifact/org.apache.activemq/artemis-jms-client-all

Please browse the internet for JMS library if you are using another brand.
