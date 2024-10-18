   .. WARNING::

      The information given here is not complete. Please check :ref:`deploymentSecurity` for additional information.

.. _advancedDevelopmentAuthorizationMethodsAndRoles:

Authorization methods and roles
===============================

In the previous subsection, the Frank!Console and Ladybug were secured with a very basic authorization mechanism named ``IN_MEMORY``. A username and a password were included in ``DeploymentSpecifics.properties`` and hence these were not kept secret. Another authorization mechanism is ``YAML``. With this mechanism, a separate file named ``localUsers.yml`` is supplied with usernames and passwords. This file can be excluded from a Docker image provided to the customer. The system administrator of the customer's site can thus save it in a secure way.

Here is an example in which only the Frank!Console is accessible. It has the following ``DeploymentSpecifics.properties``:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v480/server/configurations/DeploymentSpecifics.properties

And ``localUsers.yml`` looks as follows:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v480/server/resources/localUsers.yml

You see here that ``localUsers.yml`` adds an item ``roles`` for each user. Roles allow for differentiation between the features supported by an interface - the Frank!Console, Ladybug or HTTP. For example, relatively many users should have access to the Adapter Status page of the Frank!Framework. In contrast, few user should be allowed to access Test a Pipeline. Test a Pipeline allows users to start arbitrary adapters, disregarding the purpose of the Frank application.

When a user logs in to the Frank!Framework, he is assigned a set of roles - in the shown example the single role ``IbisObserver``. When the logged-in user tries to access a feature of the Frank!Framework, the Frank!Framework determines the role that is required to access the feature. Only when the user has that role, then access to the feature is granted. An ``IbisObserver`` for example is allowed to see the Adapter Status page, but he is not allowed to access ``Test a Pipeline``. Only an ``IbisTester`` is allowed to do the latter.

The overview of which roles exist is not only relevant for Frank developers, but also for system administrators. To have the information in one place, it is only given in section :ref:`deploymentOverviewSecurityRoles`.

.. NOTE::

   With the ``roles`` item in ``localUsers.yml`` you can assign multiple roles to the same user. Do so by providing a comma-separated list of roles.

.. NOTE::

   Page :ref:`deploymentOverviewSecurityRoles` does not explain yet about Ladybug. It will be added what Ladybug features are accessible by what roles.

.. NOTE::

   With the ``IN_MEMORY`` authentication mechanism, no role list can be supplied. When a user authenticates by this mechanism, he is give every role and he can therefore access every feature of the configured interface.