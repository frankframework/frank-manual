.. _deployingRequiringAuthorization:

Requiring authorization
=======================

If you work with a Docker image, authorization should have been cared for. Otherwise you may need the information in :ref:`advancedDevelopmentAuthorization`. That section explains authorization to Frank developers.

.. WARNING::

   Application servers provide mechanisms outside the Frank!Framework to require authorization. The Frank!Framework has been developed to run on multiple brands of application servers. Therefore the Frank!Framework has its own mechanisms. It is recommended to use these and it is deprecated to use the authorization options of the applciation server.

This section assumes that authorization has been set up for you. Frank developers can choose the used authorization mechanism. The subsections below explain for each mechanism how you should configure users, passwords and roles.

YAML authorization
------------------

This mechanism expects that users, passwords and roles are in a YAML file that you provide. If you use a Docker image derived from the Frank!Framework on Tomcat Docker image, then the file is expected at ``/opt/frank/resources/localUsers.yml``. Here is an example:

.. code-block:: none

   users:
     - username: joe
       password: myPassword
       roles: IbisWebService,IbisObserver

This file says that user ``joe`` has the roles ``IbisWebService`` and ``IbisObserver``. The roles known by the Frank!Framework are listed in the next section :ref:`deploymentOverviewSecurityRoles`. When there are multiple roles they have to be separated by a comma.

Active Directory
----------------

With this authorization mechanism, you are responsible for configuring users, password and Active Directory roles. The Frank!Framework needs a role mapping file, a file that translates Active Directory roles to Frank!Framework roles. Here is an example:

.. code-block:: none

    IbisTester=xxx
    IbisAdmin=yyy

This example assumes that ``xxx`` and ``yyy`` are Active Directory  roles. To the left of the ``=`` sign is the Frank!Framework role corresponding to the Active Directory role.

.. WARNING::

   The mapping is one to one in this case! You cannot link one Frank!Framework role to multiple Active Directory roles.

.. NOTE::

   Information about the other authorization mechanisms supported by the Frank!Framework is not in this manual yet.