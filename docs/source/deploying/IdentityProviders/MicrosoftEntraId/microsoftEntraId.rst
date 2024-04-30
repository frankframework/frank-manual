.. _deploymentMicrosoftEntraId:

THIS PAGE IS STILL WORK IN PROGRESS

Register application with identity provider Microsoft Entra ID
==============================================================

This section explains how to register a Frank application with identity provider Microsoft Entra ID. First, screenshots are shown about what should be done in the Microsoft cloud. At the end of this section you find a list of Frank!Framework properties that should be set (on the class level).

The first screen you enter is shown below:

.. image:: registerApplication.jpg

Click "Register". Go to "Enterprise Applications" | "All applications". Find your newly created application. Configure group to claim mappings (this section will be extended to describe this). Continue by configuring the claims (API permissions):

* Click on "App registrations".
* Find your newly created application.
* Click "API Permissions".
* Go to "Add a permission" | "Microsoft Graph".
* Select "Delegated permissions". See the screenshot below:

.. image:: requestApiPermissions.jpg

After committing your edits, it should look like this:

.. image:: configuredPermissions.jpg

Continue as follows:

* Go to "Certificates & Secrets".
* Go to "New client secret" and enter a client secret.
* Save the value and secret ID.

You should see the following:

.. image:: endpoints.jpg

Frank!Framework properties
--------------------------

The following properties can be used to configure authentication with Microsoft Entra ID. Use them on the class level (`src/main/resources` or `classes`) or as system properties.

.. code-block:: none

   application.security.http.authenticators.myOauth.type=OAUTH2
   application.security.http.authenticators.myOauth.provider=custom
   #Directory (tenant) ID
   application.security.http.authenticators.myOauth.clientId=<application id>
   #Secret value
   application.security.http.authenticators.myOauth.clientSecret=
   application.security.http.authenticators.myOauth.scopes=openid,profile,email
   application.security.http.authenticators.myOauth.authorizationUri=https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/authorize
   application.security.http.authenticators.myOauth.tokenUri=https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/token
   application.security.http.authenticators.myOauth.jwkSetUri=https://login.microsoftonline.com/common/discovery/v2.0/keys
   application.security.http.authenticators.myOauth.issuerUri=https://login.microsoftonline.com/<tenantID>/v2.0
   application.security.http.authenticators.myOauth.userInfoUri=https://graph.microsoft.com/oidc/userinfo
