Installation Linux
==================

Installing the IAF requires two steps:

#. Create a Docker image
#. Create your first project

Creating a Docker image
-----------------------

Please take the following steps: 

* Extract the directory "Docker4Linux" from your
  installation media and put it somewhere in
  your file system.
* In your local copy of "Docker4Linux", open the file
  "project_directory.sh". Choose some directory where
  you will store all your ibisses. Edit
  "project_directory.sh" to get:

    PROJECTDIR=/your/ibis/directory

  Do not add a slash in the end.
* Go to your local copy of "Docker4Linux". Build your docker
  image there with the command:

    docker build -t iaf:7.5 .

  Here, 7.5 is the version of the IAF you want.

Creating your first project
---------------------------

Please follow these steps:

* Start a new project, say "myProject", by creating
  a project directory named your/ibis/directory/myProject.
* From your local copy of "Docker4Linux", copy
  "properties.sh" to your new project directory.
  It reads:

    | DATABASE=h2
    | IBISNAME=ibis-manual
    |
    | IBISCLASSES=$PROJECTDIR/$IBISNAME/classes
    | IBISCONFIG=$PROJECTDIR/$IBISNAME/configurations
    | IBISTESTS=$PROJECTDIR/$IBISNAME/tests

* Now fill in "DATABASE" and "IBISNAME". For
  "DATABASE", "h2" is a valid value. "IBISNAME"
  should be equal to the last component of your
  project directory.
* In your project directory, create subdirectories
  "classes", "configurations" and "tests".
* The IAF cannot start if there is no Ibis. In your directory
  "classes", please add a file "Configuration.xml" with the
  following contents:

  .. code-block:: XML

     <?xml version="1.0" encoding="UTF-8" ?>
       <Configuration
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="./ibisdoc.xsd"
           name="ibis4manual">
         <jmsRealms>
           <jmsRealm realmName="jdbc" datasourceName="jdbc/${instance.name.lc}"/>
         </jmsRealms>
         <adapter name="Hello">
           <receiver name="dummyInput">
             <ApiListener
                 name="helloListener"
                 uriPattern="hello"
                 method="GET"/>
           </receiver>
           <pipeline firstPipe="hello">
             <exits>
               <exit path="Exit" state="success" code="201"/>
             </exits>
             <FixedResultPipe name="hello" returnString="Hello 16">
               <forward name="success" path="Exit"/>
             </FixedResultPipe>
           </pipeline>
         </adapter>
       </Configuration>

  We will examine this Ibis in :ref:`helloIbis`.
- Now you can start up the IAF. Go to your local
  copy of "Docker4Linux" and do:
 
    ./script.sh <project name>

  You see a lot of logging from docker.
- When docker has started, you can browse to http://localhost/docker/iaf/gui/.
  Here you see the management console for your Ibis. That environment
  also provides test tools. All is explained in :ref:`gettingStarted`.

