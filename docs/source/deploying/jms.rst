.. _deployingJms:

Configuring JMS
===============

JMS stands for Java Message Service. This is a standard that allows Java applications, including the Frank!Framework, to write and read queues. Writing and reading to queues is relevant to support asynchronous communication between different processes. In other words: it supports the fire and forget integration pattern. When a Frank configuration needs asynchronous communication, it probably accesses a queue that is managed using the JMS standard.

Frank configurations access the queue through its JNDI name (Java Naming and Directory Interface). This is a string that starts with ``jms/``, for example ``jms/qcf-artemis``. As a system administrator, you should receive the JNDI name that is given to the queue to be accessed. It is your job to set up this queue and to provide information on how to reach the queue.

You can use file ``resources.yml`` for this that is also used to configure databases. As a brother of the ``jdbc`` YAML object, there is a ``jms`` object. The ``jms`` object has a list of JMS resources. Here is an example:

.. code-block::

   jdbc:
     - name: "frank2transactions"
       ...
   jms:
     - name: "qcf-artemis"
       type: "org.apache.activemq.artemis.jms.client.ActiveMQXAConnectionFactory"
       url: "tcp://${jms.hostname:-localhost}:61615"

