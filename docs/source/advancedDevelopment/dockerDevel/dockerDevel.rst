.. _advancedDevelopmentDockerDevel:

On developing and deploying
===========================

In :ref:`gettingStarted`, you learned the basics of developing Frank configurations. You used the Frank!Runner (https://github.com/wearefrank/frank-runner) to run them. This way of developing got you started quickly, but it has a few drawbacks. First, the Frank!Runner hides a lot of details that you should know about when you develop Frank configurations for enterprises. Second, the Frank!Runner does not make it easy to have the Frank!Framework access external systems like databases or queueing servers. These issues are addressed when you use Docker (see https://hub.docker.com/) to set up your development environment.

Using Docker has two additional advantages. First, developers with knowledge of Docker then use a tool that is more common than the less-known Frank!Runner. Second, with Docker it becomes easy to use the Frank!Flow, a tool that allows Frank configurations to be edited graphically.

This section has the following sub-sections:

.. toctree::
   :maxdepth: 3

   basics
   frankflow
   packaging
   deployingAppServer
   jms