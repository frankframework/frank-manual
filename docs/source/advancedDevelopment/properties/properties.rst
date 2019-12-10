Properties
==========

In chapter :ref:`gettingStarted`, you learned the basic concepts of Frank development. Simple Franks were presented that output a fixed message and inserted some records into a database. A H2 database was chosen because this type of database is easy to deploy. However in a production environment, a better-performing database like Oracle is often used.

A Frank often has to operate differently during different phases of its life cycle. During development a H2 database is often best, while during production some other database is needed. To take your work into production, you typically cooperate with system administrators of your customer to deploy your solution on their infrastructure. Your solution needs to be fine-tuned for the customer site. Your solution may also be relevant for multiple customers, requiring you to create a generalized Frank that is fine-tuned in a different way for each of your customers. If you are a system administrator yourself, please read chapter :ref:`deploying`. That chapter explains how to deploy Franks on different application servers and helps you ask the right questions to Frank developers.

This section explains to Frank developers that properties are the mechanism to satisfy all these requirements. Properties are just name/value pairs. You may know properties from other applications like Windows batch files or UNIX shell scripts. You encounter them in phrases like ``name=value``, ``set name=value``, ``export name=value`` or ``-Dname="value"`` when Java programs are being called.

This section first explains how characteristics of your deployment environment are expressed using properties (subsection :ref:`propertiesDeploymentEnvironment`). Then an overview is given about the ways that properties are set (subsection :ref:`propertiesInitialization`). After this, the impact of properties on your Frank is explained. First, it is explained how you can reference properties within your XML configuration files (subsection :ref:`propertiesReference`). Second, it is explained how properties influence the services offered by the Frank!Framework (subsection :ref:`propertiesFramework`).

Here is the table of contents for this section:

.. toctree::
   :maxdepth: 3

   deploymentEnvironment
   initialization
   referencing
   framework
