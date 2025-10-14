.. _advancedDevelopmentAuthorizationSecrets:

Credentials
===========

The previous subsections covered how to protect a server by restricting it to an internal network and by requiring authentication. But how should a client connect to a protected server? The client should know the credentials of the server to connect to. These credentials could be stored in properties, but then they could be read by anyone who has access to the Frank configuration. This section explains the credentials mechanism of the Frank!Framework, the way to keep credentials secret.

Keeping secrets
---------------

We continue the example started in subsection :ref:`advancedDevelopmentAuthorizationHttpInterfaces` and that was also treated in the previous subsection. We turn to the client container of ``docker-compose.yml``:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v500/docker-compose.yml
   :emphasize-lines: 19, 24, 25

Property ``credentialFactory.class`` defines what Java class should be used by the Frank!Framework to read credentials. Class ``org.frankframework.credentialprovider.PropertyFileCredentialFactory`` is the Java class that reads credentials from a properties file. The Frank!Framework also provides other ways to store credentials, for example in the application server.

Property ``credentialFactory.map.properties`` is only relevant when ``credentialFactory.class=org.frankframework.credentialprovider.PropertyFileCredentialFactory`` and specifies the file to read the properties from. Properties are read from ``/opt/frank/secrets/credentials.properties`` in this case. The shown ``docker-compose.yml`` is only used for development. It defines a volume so that some ``credentails.properties`` can be read during development. In production, these properties should be configured by the system administrator of the customer's site. See :ref:`deploymentCredentials`.

Here is the ``credentials.properties`` used in this example during development:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v500/client/secrets/credentials.properties

The user and the password configured for the server are repeated here so that the client should be able to authorize to the server. The words ``username`` and ``password`` are both prepended by ``myAlias/``. With ``PropertyFileCredentialFactory`` you can define multiple sets of credentials, aliases, that could give access to different servers requiring authentication. In this case there is one alias that is named  ``myAlias``.

.. NOTE::

   It is possible to store usernames and passwords in separate files; each username and each password in a dedicated file. This can be done by setting ``credentialFactory.class=org.frankframework.credentialprovider.FileSystemCredentialFactory``. Frank applications usually need multiple aliases, so this approach is more complicated than managing all aliases in a single filee using the ``org.frankframework.credentialprovider.PropertyFileCredentialFactory``.

.. WARNING::

   Take care with special characters and ``\`` in secrets files. The Frank!Framework has to convert the raw bytes of a secrets file to a character string, and then to a list of name/value pairs. It does this like it is done for properties files. See :ref:`propertiesSpecialChars`.

Using secrets to authenticate
-----------------------------

The client is to authenticate itself to the following server ``Configuration.xml``:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v500/server/configurations/Server/Configuration.xml
   :emphasize-lines: 7

The client's request has to reach the ``<ApiListener>`` that listens to ``uriPattern="/server"``. This relative URL is automatically prepended by ``/api`` because it is serviced by an ``<ApiListener>``. And the server's domain is ``http://frank-authorization-server:8080`` because of the service's name given to it in the Docker Compose file. The port number is ``8080``, the port where the Frank!Framework is serviced on the internal network. Here is the client configuration that accesses the server:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v500/client/configurations/Client/Configuration.xml
   :emphasize-lines: 11 - 14

The trick is the attribute added to the ``<HttpSender>``: ``authAlias="myAlias"``. This tells the Frank!Framework to authenticate itself using basic authentication, using the secrets from alias ``myAlias``.

This finishes the example started in subsection :ref:`advancedDevelopmentAuthorizationHttpInterfaces`. It :download:`is available for download <../../downloads/advancedDevelopmentAuthentication.zip>`.

How to authenticate when the server URL is protected by another mechanism than basic authentication? If the secrets are part of the URL or when they are needed as query parameters or within headers, the secrets can be kept by wrapping them in parameters. Here is an example:

.. literalinclude:: ../../../../srcSteps/Frank2Authentication/v520/client/configurations/Client/Configuration.xml
   :dedent:
   :lines: 11 - 16
   :prepend: ...
   :append: ...

The ``<HttpSender>`` does not have attribute ``url``, but attribute ``urlParam``. This way, the tricks available in the Frank!Framework's ``<Param>`` element to form patterns become available. The ``<Param>``'s ``authAlias`` is needed to get access to the username and the password, which are accessed as ``{username}`` and ``{password}``. The attribute ``hidden="true"`` is of key importance. Without it, the Frank!Framework would write the URL to logfiles and to Ladybug reports. With ``hidden="true"``, only stars are shown where the expanded URL would appear otherwise. See the Frank!Doc page of the ``<Param>`` element for details.

See https://github.com/wearefrank/frankframework-demo/blob/main/src/main/configurations/UpdateTemperature/Configuration.xml for an example where the password is given as a query parameter.

.. DANGER::

   It might be tempting to simply reference credentials as if they were properties, like ``${credential:username:myAlias}``. The FrankFramework allows this if the value of property ``authAliases.expansion.allowed``, a comma-separated list of aliases, contains the alias to expand: in this case ``myAlias``. This way, secrets are not kept secret! They can appear in logfiles, in Ladybug reports, and as results of Test a Pipeline. Use this only during development for testing purposes.