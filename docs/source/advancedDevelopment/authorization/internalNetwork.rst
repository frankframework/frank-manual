   .. WARNING::

      The information given here is not complete. Please check :ref:`deploymentSecurity` for additional information.

.. _advancedDevelopmentAuthorizationInternalNetwork:

Restricting server to internal network
======================================

In :ref:`advancedDevelopmentAuthorizationConsoleLadybug`, it was said that requiring authorization can be combined with allowing acces through HTTP instead of HTTPS. This makes sense when the server is only accessible from an internal network -- an internal network that only connects servers that are part of the same product.

We continue the example of the previous subsection :ref:`advancedDevelopmentAuthorizationHttpInterfaces` in which only access to ``<ApiListener>`` elements is possible. The example adds a client that connects to the server and authenticates using basic authentication. The client is treated in the next subsection. Below you see the ``docker-compose.yml`` file in which the server container is highlighted:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v500/docker-compose.yml
   :emphasize-lines: 2 - 11

The important part here is what is missing -- there is no ``ports`` entry. No port is made accessible on the host network. This is the way to restrict docker containers to the internal network. The network of containers that are part of the same Docker Compose file.
