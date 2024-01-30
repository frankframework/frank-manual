.. _advancedDevelopmentDeploymentMavenMavenWebapp:

Maven webapp
============

Maven webapplications are usually not executed by starting the JVM directly. Instead, an application server like Apache Tomcat is started in which webapplications are deployed. An application server provides services to operators who want to configure webapplications without rebuilding them.

Webapplications do network communication using the Hypertext Transfer Protocol (HTTP). First, update the ``Main`` class of subsection :ref:`advancedDevelopmentDeploymentMavenMavenBasics` to talk HTTP:

#. Undo the changes of subsection :ref:`advancedDevelopmentDeploymentMavenExecuteJar` by restoring the copy you made at the beginning of that subsection.
#. Change file ``work/src/main/java/org/frankframework/maven/webapp/example/Main.java`` to become as follows:

   .. literalinclude:: ../../../../srcSteps/mavenWebapp/v520/src/main/java/org/wearefrank/maven/webapp/example/Main.java

#. Link this servlet to the URL that should trigger it. Do so by creating file ``work/src/main/webapp/WEB-INF/web.xml`` and give it the following contents:

   .. literalinclude:: ../../../../srcSteps/mavenWebapp/v520/src/main/webapp/WEB-INF/web.xml
      :language: XML

Next, the ``pom.xml`` is updated:

4. Update ``work/pom.xml`` to tell Maven that a ``.war`` file should be produced. Unlike the ``.jar`` produced in the previous subsection, the ``.war`` file includes all dependencies. Update the file as shown:

   .. include:: ../../snippets/mavenWebapp/v520/pomPackaging.txt

5. Add an additional dependency:

   .. include:: ../../snippets/mavenWebapp/v520/pomDepBuild.txt

The Java compiler has to resolve the import of class ``javax.servlet.http.HttpServlet`` and some other classes. These are found in artifact ``javax.servlet``. Therefore, this artifact is added as a dependency. The artifat does not have to be packaged in the ``.war`` however, because every application server should provide the classes of this artifact. This common feature of application servers is required by the `Jakarta EE Servlet specification <https://jakarta.ee/specifications/servlet/>`_. It explains why there is an additional line ``<scope>provided</scope>`` in the ``pom.xml``.

The webapplication is done. It can be executed as follows:

6. On a command prompt in directory ``work``, run ``mvn clean install``. A file ``target/mavenWebappExample-1.0-SNAPSHOT.war`` should be generated.
#. Download and unzip Apache Tomcat from https://tomcat.apache.org/download-90.cgi. These instructions were tested on January 30 2024 for Tomcat version 9.0.85. In that test, the source code was built with Java 11.
#. Go to the root directory of the unzipped Tomcat download, for example ``C:\Users\martijn\temp\apache-tomcat-9.0.85``.
#. That directory has subdirectory ``webapps``. Put your ``.war`` file inside subdirectory ``webapps`` and name it ``mavenWebappExample.war``.
#. The Tomcat installation directory also has a subdirectory ``bin``. Enter that directory.
#. Start Tomcat by running ``startup.bat`` (under Windows).
#. Open a webbrowser with URL http://localhost:8080/mavenWebappExample/api/hello. This should produce a webpage with the text ``HELLO WORLD!``, the output from the servlet in class ``Main.java``. The number ``8080`` is the port number. The URL ``/api/hello`` has been configured in ``web.xml`` by tag ``<url-pattern>``.

The Frank!Framework is a Maven webapplication. You have a basic understanding now of what that means. Please study Frank2Example4 at https://github.com/wearefrank/frank-runner now to see how to package Frank configurations inside ``.war`` files for deployment. That code can be executed using the Frank!Runner, but it also shows how to organize your files for execution in production without the Frank!Runner.
