.. _testingLarvaIgnores:

Ignores
========

Larva-tests verify whether values that are read from the tested Frank configuration are equal to the expected constant values. However, some tested systems produce different results each time that they are executed, even though the inputs are the same. Examples are systems that return a time stamp. In Larva, you can address this issue using ignores. With ignores, values returned from the tested system are transformed, before they are compared to the expected value. As a Frank developer, you have to choose these transformations wisely and retain meaningful aspects of your returned value. 

This section gives an overview of the transformations (ignores) that are available to you. Below is an overview table followed by explanation and examples for every transformation.

.. list-table:: Overview
   :widths: 30 70
   :header-rows: 1

   * - Options
     - Description
   * - ignoreRegularExpressionKey
     - Replaces all occurrences of regular expression with
      
       IGNORE
   * - ignoreKey 
     - Replaces all matching occurrences of provided key with
      
       IGNORE  
   * - ignoreContentBetweenKeys 
     - Replaces all characters found between key1 and key2,
      
       excluding key1 and key2, with IGNORE
   * - ignoreKeysAndContentBetweenKeys
     - Replaces all characters found between key1 and key2, 
       
       including key1 and key2, with IGNORE
   * - ignoreContentBeforeKey
     - Ignores everything before provided key has been found
   * - ignoreContentAfterKey
     - Ignores everything after provided key has been found
   * - ignoreCurrentTimeBetweenKeys       
     - Ignore current time between key1 and key2
   * - replaceRegularExpressionKeys
     - Replaces all matches of regular expression (key1) with
      
       the value of key2
   * - replaceKey
     - Replaces all matches occurrences of provided key with
      
       provided value
   * - replaceEverywhereKey     
     - Replaces all matches occurrences of provided key with
      
       provided value, same as replaceKey
   * - removeRegularExpressionKey
     - Replaces all matches of regular expression with “”
   * - removeKeysAndContentBetweenKeys
     - Removes all characters found between key1 and key2,
      
       including key1 and key2
   * - removeKey 
     - Removes all matching occurrences of provided key
   * - decodeUnzipContentBetweenKeys
     - Decode and unzip content between key1 and key2
   * - canonicaliseFilePathContentBetweenKeys
     - Canonicalise filepath content between key1 and key2
   * - formatDecimalContentBetweenKeys
     - Format decimal content between key1 and key2


The ignores use the following structure: ``<ignoreOption><numberOrName>.key=<text>``.

Some ignores require 2 keys to indicate start and end, which are denoted as key1 and key2. Both require the same identifier. The <numberOrName> is an increasing sequence of integers starting at 1 for each ignore or an string starting with a “.”. The <text> indicates what to look for.

Usually those ignores are written in the ``common.properties`` file where you define your services (see section :ref:`testingLarvaServices`), in this way they apply to all test scenarios which have included this ``common.properties`` file. If you want to use ignores in a particular test scenario, then you can put them in that related ``scenario.properties`` file.

In the subsections below, the ignores are explained by showing their effect on a target XML document. This target XML reads as follow:

.. code-block:: XML

    <Result>
      <RecordID>12</RecordID>
      <FilePath>C:\Users\..\myZipfile.zip</FilePath>
      <File>UEsDBBQAAAAAAABUqlKWlLkWCgAAAAoAAAASAAAAbXlaaXBmaWxlL3Rlc3QudHh0TGFydmEgVGVzdFBLAQIUABQAAAAAAABUqlKWlLkWCgAAAAoAAAASAAAAAAAAAAEAIAAAAAAAAABteVppcGZpbGUvdGVzdC50eHRQSwUGAAAAAAEAAQBAAAAAOgAAAAAA</File>
      <Decimal>12.34</Decimal>
      <Category>ABC</Category>
      <Timestamp>2019-10-02T10:12:43.788+0100</Timestamp>
      <Message>In this record, RecordID='12', RecordID and Timestamp change every time when you run the test</Message>
    </Result>

Using ignore
----------------------

**ignoreRegularExpressionKey**

This replaces all occurrences of regular expression with IGNORE. By writing  

.. code-block::

  ignoreRegularExpressionKey1.key=[A-Z] 
  OR 
  ignoreRegularExpressionKey.contentA.key=[A-Z]

all uppercase letters of the current result and the expected result will be replaced with IGNORE.

**ignoreKey**

This replaces all matching occurrences of provided key with IGNORE. By writing

.. code-block::

  ignoreKey1.key=RecordID
  OR
  ignoreKey.contentA.key=RecordID

all 4 “RecordID” which appeared in the above example will be replaced with IGNORE. In this case, comparing RecordID will still fail, because it won’t replace the content of RecordID.

**ignoreContentBetweenKeys**

This replace all characters found between key1 and key2 with IGNORE. By writing

.. code-block::

  ignoreContentBetweenKeys1.key1=<RecordID>
  ignoreContentBetweenKeys1.key2=</RecordID>
  OR
  ignoreContentBetweenKeys.contentA.key1=<RecordID>
  ignoreContentBetweenKeys.contentA.key2=</RecordID>

content between those two tags will be replaced with IGNORE, so comparing RecordID will always succeed no matter what the value is of it.

And by writing 

.. code-block::

  ignoreContentBetweenKeys1.key1=RecordID='
  ignoreContentBetweenKeys1.key2='
  OR
  ignoreContentBetweenKeys.contentA.key1=RecordID='
  ignoreContentBetweenKeys.contentA.key2='

this will replace the RecordID value in the element <Message> with IGNORE.

**ignoreKeysAndContentBetweenKeys**

This is similar to ignoreContentBetweenKeys, the only difference is that it replaces all characters found between key1 and key2, including key1 and key2, with IGNORE. Write as 

.. code-block::

  ignoreKeysAndContentBetweenKeys1.key1=<RecordID>
  ignoreKeysAndContentBetweenKeys1.key2=</RecordID>
  OR
  ignoreKeysAndContentBetweenKeys.contentA.key1=<RecordID>
  ignoreKeysAndContentBetweenKeys.contentA.key2=</RecordID>

**ignoreContentBeforeKey**

This replaces everything before provided key has been found with IGNORE. By writing

.. code-block::

  ignoreContentBeforeKey1.key=ABC
  OR
  ignoreContentBeforeKey.contentA.key=ABC

content before “ABC”, in this case is “<RecordID> 12</RecordID> <Category>”, will be replaced with IGNORE.

**ignoreContentAfterKey**

The opposite of ignoreContentBeforeKey is ignoreContentAfterKey, this replaces everything after  provided key has been found with IGNORE. By writing 

.. code-block::

  ignoreContentAfterKey1.key=ABC
  OR
  ignoreContentAfterKey.contentA.key=ABC

it will replace everything after “ABC” with IGNORE.

**ignoreCurrentTimeBetweenKeys**

This replaces time found between key1 and key2 with IGNORE_CURRENT_TIME, pattern can be null. Write as

.. code-block::

  ignoreCurrentTimeBetweenKeys1.key1=<Timestamp>
  ignoreCurrentTimeBetweenKeys1.key2=</Timestamp>
  ignoreCurrentTimeBetweenKeys1.pattern=yyyy-MM-dd'T'HH:mm:ss.SSSZ
  ignoreCurrentTimeBetweenKeys1.margin=12345
  ignoreCurrentTimeBetweenKeys1.errorMessageOnRemainingString=false
  OR
  ignoreCurrentTimeBetweenKeys.contentA.key1=<Timestamp>
  ignoreCurrentTimeBetweenKeys.contentA.key2=</Timestamp>
  ignoreCurrentTimeBetweenKeys.contentA.pattern=yyyy-MM-dd'T'HH:mm:ss.SSSZ
  ignoreCurrentTimeBetweenKeys.contentA.margin=12345
  ignoreCurrentTimeBetweenKeys.contentA.errorMessageOnRemainingString=false


**Other way of using ignore**

Since IAF 7.6 version, it allows ignoring the result of a specific test step by writing ``step.service.read=ignore``. For example, in the ``scenario.properties`` file, you write ``step7.database.Generic.read=ignore`` to ignore the result of this step.


Using replace
-----------------

**replaceRegularExpressionKeys**

This replaces all matches of regular expression (key1) with the value of key2. By writing

.. code-block::

  replaceRegularExpressionKeys1.key1=RecordID
  replaceRegularExpressionKeys1.key2=ID
  OR
  replaceRegularExpressionKeys.contentA.key1=RecordID
  replaceRegularExpressionKeys.contentA.key2=ID

all 4 “RecordID” will be replaced by “ID”.

**replaceKey / replaceEverywhereKey**

replaceKey and replaceEverywhereKey work the same, both replace all matching occurrences of provided key with provided value, write as:

.. code-block::

  replaceKey1.key1=RecordID
  replaceKey1.key2=ID
  OR
  replaceKey.contentA.key1=RecordID
  replaceKey.contentA.key2=ID

and

.. code-block::

  replaceEverywhereKey1.key1=RecordID
  replaceEverywhereKey1.key2=ID
  OR
  replaceEverywhereKey.contentA.key1=RecordID
  replaceEverywhereKey.contentA.key2=ID


Using remove
-----------------

**removeRegularExpressionKey**

This replaces all matches of regular expression with “”, write as

.. code-block::

  removeRegularExpressionKey1.key=\\d
  OR
  removeRegularExpressionKey.contentA.key=\\d

all digits will be removed from the result.

**removeKeysAndContentBetweenKeys**

This removes all characters found between key1 and key2, including key1 and key2. By writing

.. code-block::

  removeKeysAndContentBetweenKeys1.key1=<RecordID>
  removeKeysAndContentBetweenKeys1.key2=</RecordID>
  OR
  removeKeysAndContentBetweenKeys.contentA.key1=<RecordID>
  removeKeysAndContentBetweenKeys.contentA.key2=</RecordID>

“<RecordID> 12</RecordID>” will be removed from the result.

**removeKey**

This removes all matching occurrences of provided key, by writing

.. code-block::

  removeKey1.key=RecordID
  OR
  removeKey.contentA.key=RecordID

all 4 “RecordID” will be removed from the result.


Others
-----------------------

**decodeUnzipContentBetweenKeys**

This decodes and unzips file content between key1 and key2, if replaceNewlines is true, it will replace all “\\r” with "[CARRIAGE RETURN]" and all "\\n" with "[LINE FEED]". In the example, there is an element ``<File>UEsDB...</File>``, it is an encoded zip file named "myZipfile.zip", which contains a text file "test.txt" with content "Larva Test" written in it. By writing

.. code-block::

  decodeUnzipContentBetweenKeys1.key1=<File>
  decodeUnzipContentBetweenKeys1.key2=</File>
  decodeUnzipContentBetweenKeys1.replaceNewlines=false
  OR
  decodeUnzipContentBetweenKeys.contentA.key1=<File>
  decodeUnzipContentBetweenKeys.contentA.key2=</File>
  decodeUnzipContentBetweenKeys.contentA.replaceNewlines=false

it will first decode the content and then unzip this zip file to format “<tt:file xmlns:tt=\"testtool\"><tt:name>myZipfile/test.txt</tt:name><tt:content>Larva Test</tt:content></tt:file>”, and put it in between the 2 keys.

**canonicaliseFilePathContentBetweenKeys**

This canonicalizes file path content between key1 and key2. In the example, there is an element ``<FilePath>C:\Users\..\myZipfile.zip</FilePath>``, by writing

.. code-block::

  canonicaliseFilePathContentBetweenKeys1.key1=<FilePath>
  canonicaliseFilePathContentBetweenKeys1.key2=</FilePath>
  OR
  canonicaliseFilePathContentBetweenKeys.contentA.key1=<FilePath>
  canonicaliseFilePathContentBetweenKeys.contentA.key2=</FilePath>

it replaces “C:\\Users\\..\\myZipfile.zip” with the canonical pathname of the file object “C:\\myZipfile.zip”.

**formatDecimalContentBetweenKeys**

This formats decimal content between key1 and key2, the goal of using it is to be able to compare strings by formatting a decimal number to a canonical representation. For an integer, it will be presented as a string of digits, for example, “100” will still be “100”. And for a number which has a decimal fraction, it will be presented as a string, because the decimal precision is not known, for example, “003.0100” will become “3.01”. In the example, there is an element ``<Decimal>12.34</Decimal>``, by writing

.. code-block::

  formatDecimalContentBetweenKeys1.key1=<Decimal>
  formatDecimalContentBetweenKeys1.key2=</Decimal>
  OR
  formatDecimalContentBetweenKeys.contentA.key1=<Decimal>
  formatDecimalContentBetweenKeys.contentA.key2=</Decimal>

it will format this numeric value to ``<Decimal>12.34</Decimal>``, in this case nothing has changed.

Example solution
-----------------------

To make the target XML document at the beginning of this subsection pass the Larva test, you can write the following ignores in your test: 

.. code-block:: 

  ignoreContentBetweenKeys1.key1=<RecordID>
  ignoreContentBetweenKeys1.key2=</RecordID>
  ignoreContentBetweenKeys2.key1=<Timestamp>
  ignoreContentBetweenKeys2.key2=</Timestamp>
  ignoreContentBetweenKeys3.key1=RecordID='
  ignoreContentBetweenKeys3.key2='
  OR
  ignoreContentBetweenKeys.contentA.key1=<RecordID>
  ignoreContentBetweenKeys.contentA.key2=</RecordID>
  ignoreContentBetweenKeys.contentB.key1=<Timestamp>
  ignoreContentBetweenKeys.contentB.key2=</Timestamp>
  ignoreContentBetweenKeys.contentC.key1=RecordID='
  ignoreContentBetweenKeys.contentC.key2='
