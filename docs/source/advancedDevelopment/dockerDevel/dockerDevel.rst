.. _advancedDevelopmentDockerDevel:

On developing and deploying
===========================

In :ref:`gettingStarted`, you learned the basics of developing Frank configurations. You used the Frank!Runner (https://github.com/wearefrank/frank-runner) to run them. This way of developing got you started quickly, but it has a few drawbacks. First, the Frank!Runner hides a lot of details that you should know about when you develop Frank configurations for enterprises. Second, the Frank!Runner does not make it easy to have the Frank!Framework access external systems like databases or queueing servers. These issues are addressed when you use docker (see https://hub.docker.com/) to set up your development environment.

Using docker has two additional advantages. First, developers with knowledge of docker then use a tool that is more common than the less-known Frank!Runner. Second, with docker it becomes easy to use the Frank!Flow, a tool that allows Frank configurations to be edited graphically.

The development environment that is introduced here is not suitable for production. During development, it is easy to run the external database in a docker container. This is not recommended in production because a database does not run efficiently in a docker container.

This section has the following sub-sections:

.. toctree::
   :maxdepth: 3

   basics
   frankflow
   deploySingleConfig
   deployingAppServer