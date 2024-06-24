Editing your configurations as flow charts
==========================================

In the previous section you learned to start the Frank!Framework with docker. With that set-up, you can already edit your configurations in a text editor. The files you edit on your device's ``configurations`` folder are seen by your Docker container as files in ``opt/frank/configurations``. After editing you can thus press the refresh button (see below, Adapter Status page screen capture from https://frank2example.frankframework.org) to load your edits.

.. image:: refreshButtonFromFrank2Example.jpg

This section explains how you can edit your Frank configurations as flow charts. You can do this using the Frank!Flow that runs in your webbrowser. It can show your configurations as flow charts in which you can drag-and-drop pipes, senders and receivers. The Frank!Flow also allows you to edit your configurations as XML files.

Please do the following to set this up:

1. Download the Frank!Flow war file from our Nexus repository https://nexus.frankframework.org/. Get it from Browse | public | org | wearefrank | frankframework | frank-flow. Rename the .war file you have there to ``frank-flow.war`` and put it in your project root.

   .. WARNING::

      On June 24 2024, Martijn only got this to work by downloading an older version of the Frank!Flow. When this will have been investigated, the text will be updated accordingly.

2. Update your ``docker-compose.yml`` as shown:

   .. include:: ../../snippets/Frank2DockerDevel/v510/dockerComposeAddFrankFlow.txt

   This adds a volume that maps your ``frank-flow.war`` file to the ``webapps`` folder of your container. It also sets a necessary Java property.

3. When you restart your work with ``docker-compose up``, you can visit the Frank!Flow at http://localhost:8080/frank-flow/.
