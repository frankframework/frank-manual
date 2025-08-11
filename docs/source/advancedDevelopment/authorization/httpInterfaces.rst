.. _advancedDevelopmentAuthorizationHttpInterfaces:

HTTP Interfaces
===============

In the previous subsections, authorization was configured to protect the Frank!Console including Ladybug. The second interface that can be protected was mentioned already in :ref:`advancedDevelopmentAuthorization`: HTTP interfaces. Actually, there are different HTTP interfaces that are protected separately. See the table below:

.. list-table:: Overview of HTTP interfaces
   :header-rows: 1

   * - URL
     - Listener
     - Servlet name
     - Role needed
   * - ``/api``
     - ``<ApiListener>``
     - ApiListenerServlet
     - no authorization required*
   * - ``/rest``
     - ``<RestListener>``
     - RestListenerServlet
     - any role
   * - ``/services``
     - ``<WebServiceListener>``
     - SoapProviderServlet
     - ``IbisTester`` or ``IbisWebService``
   * - ``/webcontent``
     - \*\*
     - WebContentServlet
     - any role
   * - ``/iaf/larva``
     - \*\*\*
     - LarvaServlet
     - ``IbisTester``


\* = ``ApiListenerServlet`` is open by default (no authentication required). To protect it, set property ``servlet.ApiListenerServlet.securityRoles`` and give it a list of roles as value. If a user has acquired one or more roles from the list, access is granted.

\*\* = No XML tag in Frank!Configurations; this is about authorizing frontend code embedded in configurations, see :ref:`gettingStartedWebcontent`.

\*\*\* This servlet allows users to access Larva, see :ref:`testingLarva`. Users are encouraged to disable access to Larva. Larva is meant for development testing which should happen with ``dtap.stage=LOC``. When ``dtap.stage=LOC``, authentication and authorization is by default not required and hence disabling Larva with these properties does not affect development.

A servlet is a Java class that handles incoming HTTP requests. Java programmers typically map different URLs to different servlets. For integration specialists, this means that the shown servlets within the source code of the Frank!Framework are used for the shown listeners. For example, the ApiListenerServlet services requests for URLs starting with ``/api``. And ``<ApiListener>`` elements within Frank configurations listen to URLs with this prefix. To protect access to ``<ApiListener>`` is to protect servlet ApiListenerServlet, and the same holds for the other lines of the table above.

Protecting HTTP interfaces is done by defining *authenticators* that are then assigned to the HTTP interfaces that they have to protect. Here is an example ``DeploymentSpecifics.properties`` that protects ``<ApiListener>`` elements:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v500/server/resources/DeploymentSpecifics.properties

This file defines an authenticator with the name ``inMem``, sets its properties like explained in subsection :ref:`advancedDevelopmentAuthorizationMethodsAndRoles` and then uses the authenticator to protect ``ApiListenerServlet``. In general, an authenticator is assigned to a servlet by setting property ``servlet.<servlet name>.authenticator=<name of the authenticator>``.

.. NOTE::

   To define multiple authenticators, assign a comma-separated list of their names to property ``application.security.http.authenticators``.

Please note that property ``servlet.ApiListenerServlet.securityRoles=IbisAdmin`` is set - a user must become ``IbisAdmin`` to gain access to ``ApiListenerServlet``. The ``ApiListenerServlet`` is an exception in requiring property ``servlet.ApiListenerServlet.securityRoles`` - the other HTTP interfaces do not have similar properties. See the above table for the roles that users have to acquire to gain access.
