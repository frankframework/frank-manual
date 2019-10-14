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

* Do a HTTP GET request to localhost/docker/api/hello. Note that "hello" is the relative URL you configured in the ``<ApiListener>`` tag. You can do this with curl, as follows:

  curl -i -X GET http://localhost/docker/api/hello

.. NOTE ::

   The -i option of the curl command shows the status
   code and the headers of the response.

The output is something like this::

   martijn@martijn-N7x0WU:~/integrationPartners/iafProjects/ibis4manual$ curl -i -X GET http://localhost/docker/api/hello
   HTTP/1.1 201 Created
   Server: Apache-Coyote/1.1
   Last-Modified: Mon, 14 Oct 2019 09:28:37 GMT
   Cache-Control: no-store, no-cache, must-revalidate, max-age=0, post-check=0, pre-check=0
   Pragma: no-cache
   etag: 21634437627_5e918d2_-728088493
   Allow: OPTIONS, GET
   Content-Type: */*;charset=UTF-8
   Content-Length: 8
   Date: Mon, 14 Oct 2019 09:28:37 GMT
   
   Hello 16martijn@martijn-N7x0WU:~/integrationPartners/iafProjects/ibis4manual$

You see the output string you configured in the
``<FixedResultPipe>`` , attribute ``returnString`` .
You also see status code 201, which was configured
in the ``<exit>`` tag, attribute ``code`` .
