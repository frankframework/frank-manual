.. _frankConsoleNewHorizons:

New Horizons
============

This chapter about the Frank!Console is a tutorial. You will run the Frank!Framework with a Frank configuration deployed on it. This way, you will learn how to manage your site. You can also use this chapter for reference. If you do not do the exercises, you will still see all the information you need.

Before examining the Frank!Console, we present the Frank config that you will deploy within the Frank!Framework. It is about an imaginary company called New Horizons. New Horizons allows travelers to book travels online, which constitute visits to hotels, apartments, campings or any other place where travelers can sleep. New Horizons makes traveling easier, because the traveler with a complex travel does not have to negotiate with the individual hosts. New Horizons takes the responsibility of paying them.

Our example configuration provides a user interface to hosts, allowing them to upload their accommodations. This is done by batch processing. Hosts provide ``.csv`` files to New Horizons with field delimiter ``;``. This tutorial is not about developing Frank configurations, so it is not important to work with a realistic interface. We restrict ourselves to apartments. The information in the columns is the following:

* The product id.
* The address.
* A description.
* The price per night the host wants to receive.

Here is an example:

.. literalinclude:: ../../../srcSteps/forFrankConsole/v500/example.csv
   :language: none

The example configuration processes these ``.csv`` files and writes the records in a H2 database. The configuration uses database table ``product``. The configuration expects incoming ``.csv`` files in a specific directory that is configurable by setting a property named ``work``.
