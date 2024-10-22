   .. WARNING::

      The information given here is not complete. Please check :ref:`deploymentSecurity` for additional information.

.. _advancedDevelopmentAuthorization:

Authorization
=============

Organizations that store data have to protect this data. Customers of an organization trust that their privacy is guarenteed, which means that the data is only used as intended. System administrators should take care of this by restricting access to the data. When the Frank!Framework is part of their IT landscape, they should also restrict access to the Frank!Framework. Frank developers should enable system administrators to take care of this. This section explains to Frank developers how access to the Frank!Framework can be restricted to authorized users.

Three interfaces of the Frank!Framework need protection:

* HTTP interfaces accessed by the systems being integrated by the Frank!Framework, typically REST or SOAP endpoints.
* The Frank!Console, the management console of the Frank!Framework. See :ref:`operator`.
* The debugger Ladybug, see :ref:`ladybug`. This is a separate interface to be protected because it can be used without the Frank!Framework.

These three interfaces are not the only ones. For example, it is possible to write Frank configurations that read data from the local file system. System administrators should then protect access to the local file system - this is outside the scope of the Frank!Framework. In general, system administrators should protect the sources from which the Frank!Framework reads data.

The Frank!Framework also acts as a client that accesses systems that require authorization. The Frank!Framework needs access to the relevant credentials. These credentials should not be configured as properties because properties can be viewed by everyone. This section explains how the Frank!Framework can be used to keep credentials secret.

To understand the material of this section, knowledge on earlier sections of the manual is needed. First, the examples provided rely heavily on using Docker. Please study :ref:`advancedDevelopmentDockerDevel` before continuing with this section. Second, properties are very important, see :ref:`properties`.

.. toctree::
   :maxdepth: 3

   consoleAndLadybug
   authorizationMethodsAndRoles
   httpInterfaces
   internalNetwork
   secrets

.. WARNING::

   The following topics, and more, will be added:

   * Keeping secrets using parameters.
