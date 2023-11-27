.. _advancedDevelopmentDeploymentMavenBasicFrankWebapp:

Basic webapplication with Frank!Framework
=========================================

The previous subsections presented the basics of Java and Maven. The Frank!Framework is a Java webapplication that is available as a Maven artifact. This subsection shows how to write Frank configurations within a Maven project. The Frank!Framework appears as a dependency. Maven can package the configuration and the Frank!Framework together in a ``.war`` file. This ``.war`` file can be deployed in an application server to execute it. All code is packaged in a single file, allowing it to be tested and deployed easily.

A basic Hello World application that leverages the Frank!Framework can be created as follows:

#. Take a new work directory. This example is not related to the example of the previous subsections.
#. Create ``work/src/main/resources/Configuration.xml`` and fill it as shown:

   .. literalinclude:: ../../../../srcSteps/Frank2Webapp/v500/src/main/resources/Configuration.xml
      :language: xml

   The configuration has a single ``<Adapter>``. The ``<Receiver>`` has an ``<ApiListener>``, making it process HTTP requests. ``<ApiListener>``-s are meant to proces RESTful HTTP requests. All ``<ApiListener>``-s listen to URLs that start with ``api``. The ``uriPattern`` attribute thus configures the URL to be ``/api/hello`` like in the previous subsections. The ``<FixedResultPipe>`` provides the output: ``Hello World!``.

#. Create ``work/pom.xml`` and fill it as shown:

   .. literalinclude:: ../../../../srcSteps/Frank2Webapp/v500/pom.xml
      :language: xml

Some points of this file may need some explanation:

* There is a property ``ff.version``. Its value is referenced as ``${ff.version}`` later in the file. The value signifies a range of Frank!Framework versions: ``7.8-20220509.173348`` or the latest version published after that. Earlier versions of the Frank!Framework may not understand the ``Configuration.xml`` in this example.

  .. NOTE::

     You may want to work with a stable release, for example ``7.7``. Release ``7.7`` will work if you apply some minor changes to ``Configuration.xml``. To see what changes are needed, you need file the ``FrankConfig.xsd`` that belongs to that version of our framework. You can download the file from `GitHub <https://github.com/frankframework/frankframework/blob/master/core/src/main/resources/xml/xsd/FrankConfig.xsd>`_

  .. NOTE::

     In projects with the Frank!Runner, the Frank!Runner downloads ``FrankConfig.xsd`` automatically. If you do without, it has to be downloaded manually. To do this, visit `https://frank2example.frankframework.org/ <https://frank2example.frankframework.org/>`_ and choose option "Frank!Doc" on the main menu. There will be a button for the download.

* Dependency ``ibis-adapterframework-webapp`` is a ``.war`` archive. Therefore the reference to it needs an extra line ``<type>war</type>``.
* Dependency ``ibis-adapterframework-core`` has files that are also in the ``.war`` file of ``ibis-adapterframework-webapp``. It is wise to add ``ibis-adapterframework-core`` nevertheless, because Maven does not check for duplicate JAR files with type ``war`` dependencies. By adding ``ibis-adapterframework-core`` it is checked that dependencies of the Frank!Framework do not conflict with dependencies added in your project.
* The Frank!Framework will not start without a database driver. Artifact ``h2`` is the driver for a simple database called H2. If you want another database, you can include a driver for that database. Not every database runs within the same JVM as the webapplication however. Using another database may be more complicated during development.
* Jetty and Apache Tomcat do not fully satisfy the Jakarta EE specification. The Frank!Framework expects some classes that are part of the Jakarte EE specification, but that are not included in your application server. This has been fixed by including the ``geronimo-jms_1.1_spec`` dependency.
* The Frank!Framework depends on some system properties that are explained in section :ref:`properties`. These are set in the ``<configuration>`` tag of the Jetty plugin. These settings only apply when Maven is used to start the project in application server Jetty. These values are not packaged.
* Jetty scans JAR files included in the webapplication for web app configuration data. The number of JAR files searched is limited by the ``<webInfIncludeJarPattern>`` tag.
* An application server can host multiple webapplication. It supports users to login to these webapplications. Some webapplications share users, while others keep track of their own users without sharing them. Application servers support this using login services. Each webapp can declare a login service. When multiple webapplications declare the same login service, they share their users. Jetty expects an implementation for every declared login service. This is the purpose of the ``<loginServices>`` tags: each inner ``<loginServices>`` tag fixes how the named login service is implemented. Recently the name of the login service declared by the framework was changed. The name changed from ``Ibis`` to ``Frank``. This is why two login services are listed.

  .. NOTE::

     If application server Apache Tomcat is used, then implementations of login services can be omitted if the related webapplications do not require users to login.

* The ``<repository>`` tag is needed to download Frank!Framework version 7.8-20220509.173348 or any other non-stable version. Only stable releases like 7.7 are published to Maven Central, the repository of all public artifacts. The ``<repository>`` tag allows access to a repository of Maven artifacts hosted by Frank!Framework.

4. Create ``work/src/main/resources/DeploymentSpecifics.properties`` with the following contents:

   .. literalinclude:: ../../../../srcSteps/Frank2Webapp/v500/src/main/resources/DeploymentSpecifics.properties
      :language: none

   This gives the instance of the Frank!Framework a name. Without this file, the name defaults to "Ibis" and a warning is shown in the Adapter Status page.

Please note the role of the classpath in this webapplication. Maven takes care that all files in ``src/main/resources`` appear on the classpath when the application server boots. Relate this to the figure in subsection :ref:`propertiesDeploymentEnvironment` that presents layers "Frank!Framework + classes" and above that "Configurations". This project puts the configuration in the "Frank!Framework + classes" layer and omits the "Configurations" layer. As a consequence, there is only one set of property files ``DeplocmentSpecifics.properties``, ``StageSpecifics_LOC``, etc. and they all appear in ``src/main/resources``.

.. WARNING::

   Jetty cannot update the classpath dynamically. If you change a file in ``src/main/resources``, you have to restart Jetty before this change will have effect. The refresh button in the Adapter Status page will not work, because the changes of the configuration will not appear on the classpath. This may be a reason to organize your project differently. A consequence will be that the configuration will not be packaged inside the ``.war`` file. See subsection :ref:`advancedDevelopmentDeploymentMavenUsingFrankRunner`.

.. NOTE::

   You may organize your project differently in different phases of the life cycle of the configuration (``LOC``, ``DEV``, ``TST``, ``ACC`` or ``PRD``). This can be done with Maven build profiles, see https://maven.apache.org/guides/introduction/introduction-to-profiles.html. You probably need some Maven experience to do this successfully.

5. Using a command prompt, start the webapplication with ``mvn clean install jetty:run``.
#. Open a browser and go to `http://localhost:8080/iaf/gui <http://localhost:8080/iaf/gui>`_. You will see the Frank!Framework here. You have it because of dependency ``ibis-adapterframework-webapp``.
#. In the address bar, type ``localhost:8080/api/hello``. This should produce ``Hello World!``, the output from your Frank configuration.
#. Browse to `http://localhost:8080 <http://localhost:8080>`_. This should show the Frank!Framework again. It shows up if the project has no other front-end code.

In the next subsection, front-end code will be added.