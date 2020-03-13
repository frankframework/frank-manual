.. _properties:

Properties
==========

In chapter :ref:`gettingStarted`, you learned the basic concepts of Frank development. Simple Franks were presented that output a fixed message and inserted some records into a database. A H2 database was chosen because this type of database is easy to deploy. However in a production environment, a better-performing database like Oracle is often used.

A Frank config often has to operate differently during different phases of its life cycle. For example, during development a H2 database is often best while during production some other database is needed. A Frank config may also be fine-tuned differently for different production sites. This fine-tuning is typically done by system administrators who know the deployment environment and have permission to modify the systems involved. If you are a system administrator yourself, please read chapter :ref:`deploying`. That chapter explains how to deploy Franks on different application servers and helps you ask the right questions to Frank developers.

This section explains to Frank developers how properties allow a Frank to be fine-tuned. Properties are just name/value pairs. You may know properties from other applications like Windows batch files or UNIX shell scripts. You encounter them in phrases like ``name=value``, ``set name=value``, ``export name=value`` or ``-Dname="value"`` when Java programs are being called.

This section first clarifies what properties are with a short tutorial (subsection :ref:`propertiesReference`). Then, properties are linked to characteristics of your deployment environment (subsection :ref:`propertiesDeploymentEnvironment`). Then more details are given about setting properties (subsection :ref:`propertiesInitialization`). Finally, it is explained how properties influence the services offered by the Frank!Framework (subsection :ref:`propertiesFramework`).

Here is the table of contents for this section:

.. toctree::
   :maxdepth: 3

   referencing
   deploymentEnvironment
   initialization
   framework
