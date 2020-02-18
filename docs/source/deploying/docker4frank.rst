.. _deploymentDocker4Frank:

Docker4Frank
============

Docker4Frank also allows you to run a Frank right from the command line. It makes a Docker container with Apache Tomcat and the Frank!Framework. The container links some directories on its local file system to the ``classes``, ``configurations`` and ``tests`` directories of the Frank config you have on the host computer. This way, the container executes your Frank. Using Docker4Frank allows you to automatically spin up your database. Docker4Frank supports databases H2, Oracle, MsSQL, MySQL, MariaDB and PostgreSQL. For downloading Docker4Frank and for further instructions, see https://github.com/ibissource/docker4ibis.