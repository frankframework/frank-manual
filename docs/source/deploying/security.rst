Security
========

Introduction
------------

The previous section was about fine-tuning the Frank!Framework. You learned about the DTAP stage and about setting properties. This section continues about fine-tuning the Frank!Framework. You will learn how to restrict access to the Frank!Console. On your production environment this is important, because you want to protect the integrity of your data and you do not want unauthorized users to read customer data.

In this section you will edit configuration files of Apache Tomcat. You do not need a manual deployment of the Frank!Framework. Instead you will use the Frank!Runner which installs Apache Tomcat automatically, and then you will change the Apache Tomcat files manually. This section is a tutorial: you can follow the instructions below to get hands-on experience. Alternatively, you can just read along. All information you need will be provided in the Frank!Manual.

Tutorial on setting up security
-------------------------------

.. highlight:: none

Please set up security as follows:

#. We recommend that you create a new directory for this directory. You are going to tweak files managed by the Frank!Runner. and you do not want your existing configurations to break. Let us call your directory ``security``.
#. On a command prompt, please change directory to ``security`` and clone the Frank!Framework as follows: ::

     security> git clone https://github.com/ibissource/frank-runner

#. You can work with the example configurations of the Frank!Framework, so you do not need ``build.properties``. Please change directory to your Frank!Runner checkout and start the Frank!Framework as follows: ::

     security\frank-runner> start.bat

#. The Frank!Runner will download Apache Tomcat and the Frank!Framework. If you are using Windows, it will create a new command window to start Apache Tomcat. When you see the message ``INFO: Server startup in <n> ms`` with ``<n>`` some number, then press ctrl-c to stop the Frank!Runner again. You need to do this in the new command window. Alternatively, you can run ``stop.bat`` in the original command window.
#. Please check that you have the following directory structure: ::

     security
     |- frank-runner
        |- build.xml
        |- start.bat
        |- stop.bat
        |- examples
        |- build
           |- apache-ant-1.10.7
           |- apache-tomcat-7.0.100
           |- h2
           |- openjdk-8u232-b09
           |- tmp
        ...

The file ``build.xml`` is an ANT script that is used by ``start.bat`` to start the Frank!Framewok. By changing ``build.xml``, you can control the version of the Frank!Framework you are using. By default, you always use the latest version. The ``examples`` directory contains Frank configs that you can use out-of-the-box. You are using them because you did not provide ``build.properties``. In the directory ``build``, you see a subdirectory ``apache-tomcat-7.0.100`` with your Apache Tomcat installation.

   .. WARNING::

      When you are reading this, you may be using later versions of Apache Ant, Apache Tomcat and the JDK. The directory names will be slightly different in this case. Please check the directory names you have. Use your directory names instead of the directory names you see in the reminder of this section.

6. Please open file ``security\frank-runner\build\apache-tomcat-7.0.100\webapps\ROOT\WEB-INF\web.xml`` in a text editor. Scroll down until you see the following:

   .. code-block:: XML

      <!--
	  When a security-constraint element is present Tomcat will autenticate the
	  user for all url's whereas WebSphere does this only for the url's mentioned
	  in the security constraint(s). The PublicAccess security constraint will
	  make Tomcat behave the same as WebSphere.
	  -->

	  <!-- security-constraint>
          <web-resource-collection>
              ...
      </security-constraint -->

#. Uncomment the ``security-constraint``, resulting in:

   .. code-block:: XML
      :emphasize-lines: 8

      <!--
	  When a security-constraint element is present Tomcat will autenticate the
	  user for all url's whereas WebSphere does this only for the url's mentioned
	  in the security constraint(s). The PublicAccess security constraint will
	  make Tomcat behave the same as WebSphere.
	  -->

      <security-constraint>
          <web-resource-collection>
              ...

#. At the bottom, uncomment the closing tag to arrive at:

   .. code-block:: XML
      :emphasize-lines: 2

              <role-name>IbisTester</role-name>
          </security-role>

      </web-app>

#. Close the file you edited, ``web.xml``
#. Open file ``security\frank-runner\build\apache-tomcat-7.0.100\conf\tomcat-users.xml``.
#. The file has a lot of comments. The only non-commentary tags are the opening ``<tomcat-users>`` and the closing ``</tomcat-users>``. Between them, add a new user. Please insert the following XML:

   .. code-block:: XML

      <user username="frank" password="frank" roles="IbisObserver"/>

   You create a user with username ``frank`` and password ``frank``. This user gets role ``IbisObserver``. The possibilities for the roles will be explained later in this page.

With security enabled, users should connect to your Apache Tomcat server through https. You need a dummy certificate for this and you need to enable https traffic in your ``server.xml`` file. Please do the following:

12. To create the dummy certificate, change directory to ``security\frank-runner\build\openjdk-8u232-b09\bin``. Execute the following command there: ::

       security\frank-runner\build\openjdk-8u232-b09\bin> keytool -genkey -alias tomcat -keyalg RSA

#. To enable https, edit ``security\frank-runner\build\apache-tomcat-7.0.100\conf\server.xml``. Uncomment the following piece:

   .. code-block:: XML

      <Connector port="8443" protocol="org.apache.coyote.http11.Http11Protocol"
          maxThreads="150" SSLEnabled="true" scheme="https" secure="true"
          clientAuth="false" sslProtocol="TLS" />

Now you can start the Frank!Runner.

14. Please change directory to ``security\frank-runner`` and execute ``start.bat``.
#. Browse to http://localhost.
#. Your browser shows a message that your site is not secure. This is true, because your certificate was not signed by a Certificate Authority. For your production environment, you need a real certificate from a Certificate Authority. Every browser hides an option to carry on nevertheless. Apply this option to continue.
#. A dialog appears asking you to login, see below:

   .. image:: login.jpg

#. Enter username ``frank`` and password ``frank``, the credentials you configured in ``tomcat-users.xml``. You should now see the Frank!Framework as shown below. You see an error that something is wrong with your security certificate, but you do enter the Frank!Console.

   .. image:: loggedInHttps.jpg

#. In the main menu, click "Testing" to expand it (number 1 in the figure below):

   .. image:: mainMenuTestPipeline.jpg

#. Click "Test Pipeline" (number 2). You see the page shown below:

   .. image:: testPipelineAccessDenied.jpg

#. Select adapter "Example1Adapter" (number 1). Enter some dummy text in the Message field (number 2). Press "Send" (number 3). You will see a red bar (number 4).

   .. WARNING::

      When this text was written, no proper error message resulted from unauthorized access of Test Pipeline. Therefore, an issues has been created on GitHub, see https://github.com/ibissource/iaf/issues/617. You may be doing this tutorial after this issue has been solved. In this case, you see a clear message indicating that access is denied.

   .. WARNING::

      Restricting access to the Frank!Console is not sufficient in itself to implement security. You also need to restrict access to your Apache Tomcat configuration and installation files, and you need to restrict access to your Apache Tomcat server. If you have an external database, you also have to implement security on that. All this is beyond the scope of the Frank!Manual.

Overview of security roles
--------------------------

With the above tutorial, you learned how security is configured. Now we explain what options you have to restrict access to the Frank!Console. Your options follow from the roles that are defined within the Frank!Framework. See the following list:

IbisWebService
  Can call Ibis WebServices.

IbisObserver
  Can look in configurations, statistics and log files.

IbisDataAdmin
  Can browse the error queue and resend or delete the messages in it, reload configurations, start and stop adapters, has all IbisObserver permissions too.

IbisAdmin
  Can do a full reload and test a pipeline, has all IbisDataAdmin permissions too.

IbisTester
  Can execute jdbc query, send jms message and test a service, has all IbisAdmin and IbisWebService permissions too.

.. NOTE::

   "What is 'Ibis'?", you might ask. WeAreFrank! used this brand before they acquired their name. Before, the company was called "Integration Partners". In that time, they used the brands "Ibis" and "Ibis Adapter Framework". These names have not all been replaced by their Frank! equivalents.

You can assign these roles to users, as you did when you edited ``tomcat-users.xml``. You assign a value to the ``roles`` attribute that is a comma-separated list of roles. Each role should be taken from the list.

.. NOTE::

   You may wonder why you would assign multiple roles to a user, because the IbisObserver, IbisDataAdmin, IbisAdmin and IbisTester are cumulative. For example, an IbisAdmin can do everything an IbisDataAdmin can do. Actually, there is no reason to do this. The possibility to assign multiple roles is a feature of Apache Tomcat.