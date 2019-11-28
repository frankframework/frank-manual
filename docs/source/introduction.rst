Introduction
============

Java has a long and rich history of enterprise grade application developement. Apart from Sun/Oracle a lot of Open Source Java libraries have been developed.
Getting all these libraries to work together can be difficult. Proving that
they do so is another challenge, especially when database transactions
or xa transactions are involved.

Second, adding a GUI to your application for service managers usually isn't you
first priority. But it is important for a production
environment. Once you've build your management console you also have to think about
authentication and autorisation (LDAP, DTAP, ..).

Building an enterprise grade Java application has a lot of challenges. Therefore, low-code
solutions from for example Oracle and Mendix have become popular. These solutions
often are not open. Debugging can be difficult because the inner workings of the
framework are hidden. Or expensive support appears to be required to maintain
your solution.

The frank!framework provides an open low-code way of developing an enterprise
application. There are multiple ways to install and run the frank!framework, but
the simplest way is to run it within a docker container. To set this up, please
visit https://github.com/ibissource/docker4ibis/ and follow the instructions.

An enterprise applications created with the frank!framework is called a Frank.
Franks are written in XML. Please read :ref:`gettingStarted` for an introduction to
programming Franks and for an introdution to the services the Frank!framework offers.
Detailed information can be found in the rest of this documentation.

