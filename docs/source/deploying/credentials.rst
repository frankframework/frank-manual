.. _deploymentCredentials:

Credentials
-----------

Frank configurations can communicate with external systems. These external systems may require credentials like usernames and passwords. The Frank!Framework needs to know these credentials. It is your job to configure these credentials, because they should not be included in Frank configurations. This section explains how you can do this.

First, you have to know the *alias* of the external account. This is a name used in the Frank configuration to reference the credentials. The Frank config uses strings like ``${credential:username:alias1}`` and ``${credential:password:alias1}``. Here, ``alias1`` is the alias of the external account being accessed. Frank configs also reference aliases by setting XML attribute ``authAlias``. Then you have to provide the credentials of the alias. The Frank!Framework allows you to do this in many ways. We demonstrate credentials first by providing them in a properties file.

You can exercise providing credentials using our example configuration :download:`credentials.zip <../downloads/configurations/credentials.zip>`. Please install it like explained in section :ref:`frankConsolePreparations` of chapter :ref:`operator`. Then continue as follows:

1. Create some properties file, say ``credentials.properties`` and give it the following contents:

   .. include:: ../../../src/advancedDevelopmentCredentials/credentials.properties
      :literal:

2. Start the Frank!Runner with the following command: 
   
   .. code-block::
   
      .\start.bat -DauthAliases.expansion.allowed=alias1 
      -DcredentialFactory.class=nl.nn.credentialprovider.PropertyFileCredentialFactory
      -DcredentialFactory.map.properties=<full-path-to-your-properties-file>
      
   This text all has to appear on the same line. In this command, replace ``<full-path-to-your-properties-file>`` to the full path of the file you created in the previous step.
3. Browse to http://localhost. In the main menu, choose "Testing" and "Test a Pipeline".
4. Choose adapter "TestCredentials" (number 1 in the picture below). Enter some arbitrary input message for this adapter (number 2). Then press "Send" (number 3). Check that the adapter succeeded (number 4). And check that the username and the password you provided are shown (number 5).

   .. image:: testCredentials.jpg

5. Restart the Frank!Runner but omit the Java Virtual Machine options: just ``.\start.bat``.
6. Run the same adapter. Now it should look like shown below:

   .. image:: credentialsNotAllowed.jpg

   You did not allow the Frank!Framework to expand the credentials of alias ``alias1``. You see text that tells you so.

The properties ``authAliases.expansion.allowed``, ``credentialFactory.class`` and ``credentialFactory.map.properties`` are system properties. You can initialize them as Java Virtual Machine properties (with ``-D`` as shown). If you run the Frank!Framework on Apache Tomcat, you can configure them in ``catalina.properties``. For other application servers, there are other ways but these are beyond the scope of this section.

With property ``authAliases.expansion.allowed``, you define for which aliases you want to allow credentials expansion. It is a comma-separated list. With property ``credentialFactory.class`` you define the source from which the credentials have to be obtained. In the example the credentials were in a properties file, but there are many other possibilities you can choose. You give the Java class name of the class that should read the credentials.

Depending on the value of ``credentialFactory.class``, additional properties can be needed to define the source of the credentials. If ``credentialFactory.class`` is ``nl.nn.credentialprovider.PropertyFileCredentialFactory``, you are defining that the credentials are in a properties file. In this case you should provide property ``credentialFactory.map.properties``. The value of the property is the name of the properties file where the credentials can be found.

In the table below, all the options are listed for providing credentials:

+-------------------------------------------------------------+-----------------------------------------------------+
| Credentials factory and extra properties                    | Explanation                                         |
+=============================================================+=====================================================+
| ``nl.nn.credentialprovider.PropertyFileCredentialFactory``  | Credentials from properties file.                   |
| with ``credentialFactory.map.properties``                   | ``credentialFactory.map.properties`` holds the      |
|                                                             | name of the file with usernames and passwords.      |
|                                                             | See above example for file contents.                |
+-------------------------------------------------------------+-----------------------------------------------------+
| ``nl.nn.credentialprovider.FileSystemCredentialFactory``    | Username and password in separate text files.       |
| with ``credentialFactory.filesystem.usernamefile``,         | The properties are names of files holding the       |
| ``credentialFactory.filesystem.passwordfile`` and           | username and the password. The paths in             |
| ``credentialFactory.filesystem.root``. Default values       | ``credentialFactory.filesystem.usernamefile``       |
| ``username``, ``password`` and ``/etc/secrets``.            | and ``credentialFactory.filesystem.passwordfile``   |
|                                                             | are relative to the path in                         |
|                                                             | ``credentialFactory.filesystem.root``.              |
+-------------------------------------------------------------+-----------------------------------------------------+
| ``nl.nn.credentialprovider.AnsibleVaultCredentialFactory``  | Credentials in Ansible vault. The extra             |
| with ``credentialFactory.ansibleVault.vaultFile`` and       | properties hold the vault file and the key file.    |
| ``credentialFactory.keyFile``.                              |                                                     |
+-------------------------------------------------------------+-----------------------------------------------------+
| ``nl.nn.credentialprovider.WebSphereCredentialFactory``,    | Credentials configured in Websphere Application     |
| no additional properties.                                   | Server.                                             |
+-------------------------------------------------------------+-----------------------------------------------------+
