.. _gettingStartedWebcontent:

Web content
===========

Java applications may consist of front-end and backend code.
The backend code executes on the server. When a user
visits the application, the browser downloads the front-end code and
executes it. Front-end code typically has HTML files, stylesheets (CSS files)
and JavaScript code. 

Frank configurations can have front-end code like ordinary Java
applications. To add front-end code to a Frank configuration,
add a folder named ``webcontent`` and put the HTML files, CSS
files and JavaScript files there. These files will be available
at URL ``webcontent/name-of-configuration``.

This can be illustrated by adding a welcome page to the NewHorizons
configuration developed in this chapter. Please do the following:

1. In the ``NewHorizons`` folder, add a subfolder ``webcontent``.
#. In folder ``webcontent``, add a file ``index.html`` with the following contents:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v510/configurations/NewHorizons/webcontent/index.html
      :language: html

#. Start the configuration using the Frank!Runner. Then browse to http://localhost/webcontent/NewHorizons. The browser should show the text "Welcome to New Horizons!".

.. NOTE::

   The requested URL did not contain the text ``index.html``, but the Frank!Framework nevertheless served that file. When the Frank!Framework gets a HTTP request
   ``webcontent/name-of-a-configuration``, it is automatically interpreted as a request for the welcome file: the ``index.html`` file in folder ``webcontent`` of the referenced configuration.

.. NOTE::

   Each configuration in a Frank application can have a ``webcontent`` folder with front-end code. Each configuration has a different name and has its front-end code served at a different URL ``webcontent/name-of-configuration``.

.. NOTE::

   Each configuration can have a ``webcontent`` folder no matter the class loader type (property ``configurations.MyConfig.classLoaderType``), see subsection :ref:`propertiesFramework`.

.. WARNING::

   If your front-end conde consists of multiple files, you have to add a ``<base>`` tag within ``<head>``, for example ``<base href="/<application-context>/webcontent/my-configuration/">``. This way, relative URLs like ``my-file.html`` are queried from the server as ``webcontent/my-configuration/my-file.html`` which is what the Frank!Framework expects. If your frontend is built with Angular, do not configure this in ``index.html`` directly. Instead edit ``angular.json``. Add ``"baseHref": "/<application-context>/webcontent/my-configuration/"`` under ``"architect"`` \| ``"build"`` (of ``"@angular-devkit/build-angular:application"``) \| ``"options"``.

Angular
-------

Frontend code to be served with a Frank configuration can also be built with Angular. In this case, add the following to your ``angular.json``: ``"baseHref": "/<application-context>/webcontent/my-configuration/"``. This ensures that the browser interprets URLs relative to ``"/webcontent/my-configuration/"``, which produces the URLs the Frank!Framework expects. This looks like the following:

.. code-block:: none

   {
     ...
     "projects": {
       "my-configuration": {
         "projectType": "application",
         ...
         "architect": {
           "build": {
             "builder": "@angular-devkit/build-angular:application",
             "options": {
               ...
               "baseHref": "/<application-context>/webcontent/my-configuration/"
               ...
             },
             ...
           },
           ...
         }
       }
     }
   }

When you use the Angular router use the ``HashLocationStrategy``, not the ``PathLocationStrategy``. This way the Angular router assigns URLs like ``<application-context>/webcontent/my-configuration/#/my-route`` to the configured routes. The frontend can handle these URLs by requesting ``<application-context>/webcontent/my-configuration`` from the sever. The ``PathLocationStrategy`` would produce URLs without a hash sign which would make the application server responsible for serving longer URLs. Serving those longer URLs has not been implemented in the Frank!Framework.

Using the ``HashLocationStrategy`` can be configured in ``app.config.ts`` in the ``providers`` array. That array has a function call ``provideRouter``. Give that function the argument ``withHashLocation()``. This looks like the following:

.. code-block:: none

   import { ApplicationConfig } from '@angular/core';
   import { provideRouter, withHashLocation } from '@angular/router';
   import { routes } from './app.routes';
   ...
   export const appConfig: ApplicationConfig = {
     providers: [
       ...
       provideRouter(routes, withHashLocation(), ... other options... )
       ...
     ]
   };

Building and packaging with Angular involved
--------------------------------------------

When your configuration has frontend code that is built with Angular, it is wise to have a subfolder for the Angular project, say ``frontend``. The Angular build then typically produces ``frontend/dist/browser``. The contents of that folder should appear in the ``webcontent`` folder of the configuration's .jar file, see :ref:`advancedDevelopmentCustomCodeBackendPackaging`.

A configuration's .jar file is typically produced with Maven, while Angular builds are done using ``npm``, ``yarn``, ``pnpm`` or similar. This can be solved by wrapping the Angular build inside a Maven project. Maven's ``exec-maven-plugin`` can be used to wrap commands that would normally be executed from command prompts. It handles commands and arguments such that it works both for Windows and Linux. Here is a ``pom.xml`` snippet that illustrates this:

.. code-block:: xml

   <project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
       <modelVersion>4.0.0</modelVersion>
       ...
       <build>
           ...
           <plugins>
               ...
               <plugin>
                   <groupId>org.codehaus.mojo</groupId>
                   <artifactId>exec-maven-plugin</artifactId>
                   <version>3.5.0</version>
                   <executions>
                       <execution>
                           <id>pnpm install --frozen-lockfile</id>
                           <goals>
                               <goal>exec</goal>
                           </goals>
                           <phase>generate-resources</phase>
                           <configuration>
                               <workingDirectory>./frontend/</workingDirectory>
                               <executable>pnpm</executable>
                               <arguments>
                                   <argument>install</argument>
                                   <argument>--frozen-lockfile</argument>
                               </arguments>
                           </configuration>
                       </execution>
                       ... other executions that let this plugin do other tasks ...
                   </executions>
               <plugin>
               ... other plugins ...
           <plugins>
           ...
       <build>
       ...
   </project>
