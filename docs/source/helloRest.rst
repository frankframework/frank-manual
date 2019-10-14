.. _helloRest:

Hello World Executable
======================

In section :ref:`installationLinux` , a simple Frank was presented,
which is the XML code of an enterprise application to be interpreted by
the frank!framework. In section :ref:`helloIbis` , the code of the
Frank was analyzed, demonstrating some basic structures you can
apply when you create your own Frank.

Let's see what the application does. Please run it as follows:

* As explained in :ref:`installationLinux` , go to your local copy of "Docker4Linux".
* Run the following command:

  ./script.sh <project name>

* Do a HTTP GET request to localhost/docker/api/hello. You can do this with curl, as follows:

  curl -i -X GET http://localhost/docker/api/hello

.. NOTE ::

   The -i option of the curl command shows the status
   code and the headers of the response.

You will see the output string you configured in the
``<FixedResultPipe>`` , attribute ``returnString`` .
You also see status code 201, which was configured
in the ``<exit>`` tag, attribute ``code`` .