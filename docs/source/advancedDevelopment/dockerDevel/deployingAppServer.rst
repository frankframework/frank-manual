.. _advancedDevelopmentDockerDevelAppServer:

Deploying the full application
==============================

The previous page :ref:`advancedDevelopmentDockerDevelSingleConfig` explained one way to deploy: only distributing one Frank configuration. This has the advantage that system administrators of the customer have complete freedom to optimize the deployment environment. There are two drawbacks. First, deployment is not fully automated - there is a manual step to upload the configuration somewhere. A second drawback can be that Frank configurations need some control over the application server.

These issues can be addressed by distributing a docker image. Developers can create it by writing a dockerfile. The dockerfile should derive from image ``frankframework/frankframework`` (if the desired application server is Apache Tomcat), which is available on Dockerhub. It should include the Frank configurations (can be plural in this case) being deployed in the ``/opt/frank/configurations`` directory. The production environment does not reference them in a volume anymore.

The maintainers of the Frank!Framework have done a lot of work to make image ``frankframework/frankframework`` reliable, and hence you are recommended not to interfere with the way it configures Apache Tomcat. For example, it is deprecated upon to provide some ``context.xml``.

There is a caveat here conserning external resources. If the image configures Apache Tomcat and if it should be immutable, how should external resources be configured? The application is usually deployed in multiple environments during its life cycle, for example Develop, Test, Acceptance and Production (= DTAP, see :ref:`propertiesDeploymentEnvironment`). These environments should not share resources - production data should not be available to systems being tested for example. This issue can be addressed by defining all resources for all environments in ``resources.yml``, which becomes part of the deliverable here.

The dockerfile to be written by developers should add ``resources.yml`` in ``/opt/frank/configurations``. It is explained now how to add all the resources in ``resources.yml``. If you are working with this page as a tutorial, please return to the situation of :ref:`advancedDevelopmentDockerDevelFrankFlow`; the ``BuildInfo.properties`` file is not needed for this type of deployment. Then do the following:

1. Update ``configurations/resources.yml`` to reference the database with a new name:

   .. include:: ../../snippets/Frank2DockerDevel/v520/resourceVariableDb.txt

#. Update ``docker-compose.yml`` to provide the database under the new name:

   .. include:: ../../snippets/Frank2DockerDevel/v520/ffVariableDb.txt

For each environment, another database with another name can be added in ``configurations/resources.yml``. Each deployment environment can choose the right name by setting system property ``jdbc.datasource.default``. This keeps the image provided by the developers unchanged - the property is set for the docker container resulting from running the image.

.. NOTE::

   If the external resources have very similar URLs, it may be possible to have only one entry in ``resource.yml`` for all environments, which is defined in terms of other properties. This single name can still match the reference ``jdbc/${instance.name.lc}``, the default name referenced by the Frank!Framework. Then it is not necessary anymore to set external property ``jdbc.datasource.default`` and ``configurations/resources.yml`` is shorter. Of course, the properties that are referenced to instantiate the resource name still have to be set.