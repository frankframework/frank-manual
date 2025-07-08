.. _advancedDevelopmentAuthorizationConsoleLadybug:

Interfaces Frank!Console and Ladybug
====================================

Restricting access to the Frank!Framework is done by setting properties. A very important property is ``dtap.stage``. When ``dtap.stage=LOC``, access to the Frank!Framework is not restricted by default. Setting ``dtap.stage=LOC`` is meant for testing Frank configurations during their development. Developers need access to every interface to test their work. The Frank!Runner, which is meant to start the Frank!Framework for local development testing, sets ``dtap.stage=LOC`` automatically. In the other DTAP stages, access to most interfaces is blocked by default.

Setting ``dtap.stage`` to another value than ``LOC`` has another major consequence. When application server Tomcat is used, then Tomcat is by default configured to require access through HTTPS. Only when ``dtap.stage=LOC``, access through HTTP is allowed by default. This default can be overridden by setting property ``application.security.http.transportGuarantee``. Set ``application.security.http.transportGuarantee=none`` for HTTP or ``application.security.http.transportGuarantee=confidential`` for HTTPS.

.. NOTE::

   In enterprises it is common to restrict access to the Frank!Framework without requiring HTTPS! When multiple servers cooperate they usually do so in a dedicated network that is not accessible from the outside. Requests from outside this network are required to be HTTPS and they enter via a dedicated server. This server handles the details of HTTPS like checking against a certificate. Configuring Tomcat to handle HTTPS is outside the scope of this manual. See :ref:`advancedDevelopmentAuthorizationInternalNetwork`.

Properties ``dtap.stage`` and ``application.security.http.transportGuarantee`` should be provided as system properties. The other properties required for authorization can be provided as application properties, but not configuration properties. File ``DeploymentSpecifics.properties`` shown below demonstrate a very basic way to protect the Frank!Console and Ladybug:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v460/server/resources/DeploymentSpecifics.properties

The properties that restrict access to the console and Ladybug have a name starting with ``application.security.console.authentication``. The Frank!Framework supports many mechanisms by which users can authenticate themselves, the simplest being ``IN_MEMORY``. The mechanism is configured by setting a property of which the name ends with ``type``. The mechanism to authorize access to the console and Ladybug is thus controlled by property ``application.security.console.authentication.type``.

.. NOTE::

   It is possible to configura authorization for Ladybug differently from the way it is configured for the Frank!Console. Use properties that have a name starting with ``application.security.testtool.authentication`` for Ladybug specifically. Configure the authorization mechanism using ``application.security.testtool.authentication.type``. And for ``application.security.testtool.authentication.type=IN_MEMORY``, the username and the password for Ladybug specifically are configured with ``application.security.testtool.authentication.username`` and ``application.security.testtool.authentication.password``.

When ``*.type`` is ``IN_MEMORY``, then properties ``*.username`` and ``*.password`` should be configured for the username and the password the user should enter. These are the remaining properties of the shown ``DeploymentSpecifics.properties``.

Exercise
--------

Examine :download:`this example Frank application <../../downloads/advancedDevelopmentAuthenticationConsole.zip>`. In particular, look at ``docker-compose.yml`` and ``DeploymentSpecifics.properties``. Check that you can access the Frank!Console and Ladybug.