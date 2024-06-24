Syntax highlighting while editing configurations
================================================

In :ref:`advancedDevelopmentDockerDevel`, it was said that the Frank!Runner downloads ``FrankConfig.xsd``. You need this file to have syntax checking while editing Frank configurations. If you work with Docker, you have to download the file yourself. Please do the following:

1. Download the Frank!Doc XSD from the Frank!Framework, see pictures below. You can use your development environment or https://frank2example.frankframework.org/.

   .. image:: ./clickFrankDoc.jpg

   .. image:: ./downloadXsd.jpg

2. Put the downloaded file ``FrankConfig.xsd`` in your ``configurations`` directory.
3. Update your configuration XMLs to reference ``FrankConfig.xsd`` as shown:

   .. include:: ../../snippets/Frank2DockerDevel/v520/refFrankConfigXsd.txt
