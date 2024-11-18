  .. WARNING::

     This page is still work in progress.

.. _deploymentMicrosoftEntraId:

Protecting the Frank!Console with OAuth provider Azure AD
=========================================================

This section explains how to protect the Frank!Console with OAuth 2.0 from OAuth provider Azure AD. There are two steps:

* Register the application with Microsoft Entra ID.
* Configure the properties in the Frank!Framework that govern authorization.

Registering with Microsoft Entra ID
-----------------------------------

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

The following properties have to be set in the Frank!Framework. They configure the Frank!Console so that its users should authenticate themselves at identity provider Azure AD. Use them on the class level (``src/main/resources`` or ``classes``) or as system properties.

.. code-block:: none

   application.security.console.authentication.type=OAUTH2
   application.security.console.authentication.provider=custom
   #Directory (tenant) ID
   application.security.console.authentication.clientId=<application id>
   #Secret value
   application.security.console.authentication.clientSecret=
   application.security.console.authentication.scopes=openid,profile,email
   application.security.console.authentication.authorizationUri=https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/authorize
   application.security.console.authentication.tokenUri=https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/token
   application.security.console.authentication.jwkSetUri=https://login.microsoftonline.com/common/discovery/v2.0/keys
   application.security.console.authentication.issuerUri=https://login.microsoftonline.com/<tenantID>/v2.0
   application.security.console.authentication.userInfoUri=https://graph.microsoft.com/oidc/userinfo
