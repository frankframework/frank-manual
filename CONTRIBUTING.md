# CONTRIBUTING

This file explains how to contribute to this project.

## Building the Manual

Building the manual involves the following steps:

1. Build download zips using buildDownloadZips.py.
2. Build the documentation locally or let ReadTheDocs build it.

### Build download zips

As said in `README.md`, some Franks in directory `src` should be available as download
links. Therefore, these subdirectories should be zipped and the zips should appear
in directory `docs/source/downloads`. All download zips appear in the same directory
to distinguish generated files from files edited manually. Please use
`buildDownloadZips.py` to execute this step. Before pushing your changes,
please run `buildDownloadZips.py` and include `docs/source/downloads`
in your commit. These files are checked-in because ReadTheDocs cannot build them.

Script `buildDownloadZips.py` requires Python 2.7. It works both for Windows and Linux.
It replaces Windows line endings with Linux line endings for each file included in a
download zip. This way, the same zips are produced from Windows or Linux checkouts
of the `src` directory.

If you edit files in the `docs` directory that contain Frank config, please sync it with the Frank configs in the `src` directory and vice versa. If you work on section Getting Started | Configuration Management, also please sync directories `src/gettingStarted` and `src/gettingStartedAfterConfig` and the download zips produced from them. The former is the solution of doing section Configuration Management and the subsequent sections on New Horizons. The latter is the solution of only doing Configuration Management.

### Building the documentation.

You can build the documentation using http://readthedocs.io or locally on your laptop.
The former happens automatically when you push your changes to GitHub, because the
server has a git hook to ReadTheDocs. The formatted manual can
be found at http://frank-manual.readthedocs.io. This is the official version. If you
do not have permission to push directly to GitHub, then please make a pull request.

Please check modifications to the manual first by reviewing them on your laptop.
After building the download links as explained before, use `make html` (Linux) or the script `make.bat html` (Windows). Before these scripts work, please do the following:

* Make sure you have Python 2.7 and Pip. Information on how to install these is available on the internet.
* `pip install sphinx`
* `pip install sphinx_rtd_theme`

## Guidelines for the contents

Here are some guidelines for updating the manual.

### Back up your statements with example code

When you state things about the Frank!Framework, it is wise to provide Frank code that proves your statements. Every section of the manual should have its own Frank with backup code. Each Frank has its own subdirectory of the `src` directory as explained in `README.md`. Please keep your examples grouped by manual section. It would be confusing to have an example Frank that applies to multiple unrelated parts of the manual. The name of an example Frank should reveal to which manual text it applies.

### Mind your audience

The manual is read by Frank developers, testers and system administrators. These professionals have very different backgrounds and ways of thinking. Developers want to understand language structures and details. Please do not only tell them to do something to get some result. Explain them the concepts behind. Testers and system administrators are different. They want to see a lot of pictures and they just want to see how to get the job done. They need to ask the right questions to developers, but they do not want to study the details. 

### Support lazy readers

Beginning users of the Frank!framework probably read the manual from cover to cover, but more advanced readers probably won't. They have a question, enter a search term in ReadTheDocs and land somewhere in the middle of a story. Therefore, each screen of the HTML version should be self contained. It needs a short introduction, which includes references to other sections with details about the context. After this introduction, the material of the screen can be presented. It is good to know that each screen of the manual corresponds to one .rst file in the git repository.

### How to address the reader

Much material can be formatted as a tutorial. This is a story in which the reader is asked to do something. The expected results of the reader's actions are described and explained. The reader is addressed as "you" and instructions are written using the (polite) imperative: "Please do this. You see that ...".

When there is much material about the same topic, a long set of reader actions and expected results is involved. You need subsections, each having their own introduction. The introduction of a subsection should explain to the reader that she is in the middle of a larger story, and it should tell her at what point in the story she has arrived. Each subsection introduction should support the reader who wants to start the tutorial from that subsection instead of the beginning of the story. Of course, each tutorial should be independent. It should not be necessary to do a tutorial before another tutorial can be started.

The reader should have the choice not to follow the directives but just read along. When a reader is smart or advanced, she should understand the story when she just reads on her webbrowser or even from her telephone. The manual writer should be careful not to omit anything relevant.

There may be more detailed material that does not fit naturally in a tutorial. Such text still has an introduction about something the reader wants to achieve. Such an introduction should interest the reader in proceeding. For each detail mentioned, it should be clear why the reader would care to know.

The only exception is reference material about individual Java classes. This material is allowed to just state the facts.

### Consistent usage of words

The manual should everywhere use the same word for the same thing, with the same spelling.

#### WeAreFrank! and their Products

In January 2020, the company Integration Partners changes their name to WeAreFrank!. Please use the right words to reference the company and their products, as listed below:

* WeAreFrank!: The name of the company that produces the Frank!Framework. The exclamation sign is part of the company name, the dot isn't.
* Frank!Framework: The product being documented in this manual. Note that the exclamation mark is part of the name and that there are two capitals. The dot is not part of the name.
* Frank: A solution produced with the Frank!Framework that can be deployed to a customer. This is the combination of the Frank!Framework and Frank configs deployed on it.
* Franks: Plural of Frank.
* Frank config(uration): A set of XML files and property files that configures the Frank!Framework to provide a solution for a customer. A Frank config is typically created by a Frank developer. This word is also used for a set of adapters that is defined in or included from the same ``Configuration.xml`` file. When you have multiple ``Configuration.xml`` files within your Frank, you have multiple Frank configs within your Frank.
* ~Frank code~: For Java developers who edit this manual, it is tempting to use this phrase. We kindly ask them to write about "Frank config" instead. You do not have to be a programmer to use the Frank!Framework.
* ~Frank language~: Franks are written in XML, not in a propriatary programming language. You can say that Frank configurations are XML documents that satisfy the Frank configuration schema.
* Frank config(uration) schema: The XML schema document that defines what XML code is valid for configuring the Frank!Framework.
* Frank!Console: The graphical user interface of the Frank!Framework.
* Frank!Doc: A complement to this manual that is shorter but provides better search capability. It can be accessed through the Frank!Console.
* Frank developer: Engineer who writes Frank configs.
* integration specialist: Engineer who wants to integrate software systems at a customer site. She may be interested in using the Frank!Framework to do her job.

#### Cross references

Do we write "This section explains..." or "This subsection explains..." or even "This sub-subsection explains..."? This should be uniform throughout the manual. Here is our choice:

* Chapter: Top-level chapter, for example Getting Started.
* Section: Second-level header, for example Getting Started | Hello World Source Code. Another example is Testing Frank Configurations | Ladybug.
* Subsection: Third-level header, for example Getting Started | Hello World Source Code | Adapter. Another example is Testing Frank Configurations | Ladybug | Preparations.
* Sub-subsection: Everything deeper.
