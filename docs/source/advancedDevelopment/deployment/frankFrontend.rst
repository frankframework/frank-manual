.. _advancedDevelopmentDeploymentMavenFrankFrontend:

Adding front-end code
=====================

In the previous subsection, you wrote a Maven application that leverages the Frank!Framework. In this subsection you add front-end code to it.

#. Create ``work/src/main/webapp/index.html`` and fill it as follows:

   .. literalinclude:: ../../../../srcSteps/Frank2Webapp/v510/src/main/webapp/index.html

#. Browse to ``localhost:8080`` or refresh a browser that points to that URL already. You should see the text "Hello World!" in a large font. You have added your own front-end code. The added front-end code is merged with the front-end code of the Frank!Framework. If there are duplicate files between the project and the Frank!Framework, the file from the project is taken. This is why the newly added file ``index.html`` file is used.
#. Update ``work/src/main/resources/DeploymentSpecifics.properties`` as shown:

   .. include:: ../../snippets/Frank2Webapp/v510/deploymentSpecificsAddCustomView.txt

#. Restart Jetty and browse to `http://localhost:8080/iaf/gui/ <http://localhost:8080/iaf/gui/>`_. Check that the main menu has an extra entry "Custom Tab".
#. Click that entry. Your browser should open a new tab with the text "Hello world!" in a large font. The Frank!Framework has a link to the front-end added in the project.

Property ``customViews.names`` holds a comma-separated list of identifiers of custom tabs. For each item in the list, there should be properties ``customViews.<id>.name`` and ``customViews.<id>.url``. These define the name of the shown entry and the target URL.