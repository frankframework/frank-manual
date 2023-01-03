.. _advancedDevelopmentMongoDBSetup:

Set up MongoDB
==============

MongoDB comes in two flavors. You can install it locally or you can save your data in the cloud with MongoDB atlas. MongoDB atlas has sample datasets that you can use for experimenting. It is difficult to import this sample data to a local MongoDB server. Therefore we work with MongoDB atlas here. This subsection explains how to get a database in MongoDB atlas and how to populate it with the sample data. Please do the following:

1. Open a webbrowser and go to https://mongodb.com/atlas.
1. Press button **Try Free**.
1. Make an Atlas account.
1. You get a page to verify your email address. Press the button that requests a verification email.
1. Wait for the verification email and press its button. You get a new browser window within the Atlas website.
1. Press **Continue**.
1. Log in using the Atlas account you just created.
1. Choose **Java** as your preferred language.
1. You have a few options to create a database, see the picture below. Choose the highlighted option to have a free database that you can easily populate with the sample data.

   .. image:: chooseFreeDatabase.jpg

1. You see the page shown below. Enter a username and a password.

   .. image:: securityControls.jpg

1. In the same page, you can restrict access by supplying IP addresses. You can only access the database from a listed IP address. Use button **Add My Current IP Address** to add your current IP address to the list. See below:

   .. image:: connectFrom.jpg

1. Press **Create User** to finish the security controls. You should see the message shown below. Press **Go to Databases**.

   .. image:: databaseSetupDone.jpg

1. You are in the overview of your databases. To the right of label "Load sample datasets to Cluster0.", there is a button to populate your database with the sample data. Click it.

   .. image:: databasesScreen.jpg

1. Importing the sample data takes some time. Wait until you see a message saying the loading has been successful.
1. Press **Browse Collections**. Open **sample - geospatial** and select collection **shipwrecks**. See below. In section :ref:`advancedDevelopmentMongoDBQueries` you will try queries on this collection.

   .. image:: browseSampleCollections.jpg

1. Press **Data Services** to return to the previous screen.
1. Press **Connect**. You see the screen below.

   .. image:: connectWithCompass.jpg

1. Press **Connect using MongoDB Compass**.
1. The dialog changes to the below screen. If you do not have MongoDB Compass yet, you can install it at this point. You also see the query string with your password omitted. You have to enter the query string in MongoDB Compass to connect to your database. You also need it within a Frank configuration to access the database.

   .. image:: installCompassAndSeeQueryString.jpg

1. Before you can substitute your password in the query string, you need to url encode it. You can do this using this website: https://www.urlencoder.org/. For example, if your password was `pwd$`, you have to substitute `<password>` by `pwd%24`.
1. Open MongoDB Compass. You should see the screen shown below:

   .. image:: compassStartScreen.jpg

1. In the middle, you can enter the query string to connect to. Using the **Save** button you can store query strings and give them a name. You can access them later by choosing an entry from the left.
1. If you have a query string in the edit field, you can press **Connect** to connect to the database. You should get the below screen. You should have a collection group "sample_geospatial" that contains "shipwrecks" when you expand it.

   .. image:: compassDatabaseOpen.jpg
