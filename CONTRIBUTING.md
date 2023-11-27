# CONTRIBUTING

This file explains how to contribute to the Frank!Manual. Before investing your time, you should know whether you have the right build environment. Therefore we start by listing the basic characteristics of the build environment you need. Then we give some guidelines for the contents of the manual. To write the manual, you also have to understand how the work on the manual is automated. First we explain what automation tools we have and what they do. Finally it is explained how to use these tools.

## Built Environment

The manual is developed with the following build environment:
* Windows
* Git (version control)
* MinGW (command prompt)
* Python 3.8.2 (programming language)
* Pip (package manager for Python libraries)

If you have no administrator permissions on your computer, you cannot use installers to get these software packages. Please see [INSTALLATION_NO_ADMINISTRATOR.md](INSTALLATION_NO_ADMINISTRATOR.md).

You can download Git from the following link: https://git-scm.com/download/win. The installer of Git also installs MinGW.

You can download Python and Pip from https://www.python.org/downloads/. You also need to install some Python packages usign pip:

* `pip install sphinx`
* `pip install sphinx_rtd_theme`
* `pip install pyyaml`

WARNING: By the beginning of March 2021, the latest official Sphinx release does not build the Frank!Manual successful. The shown Sphinx release is a bugfix. It is not known when this fix will be included in an official release.

You may be able to use Linux instead of Windows and you may be able to do without MinGW. When using other tools, please check carefully whether everything works well. Make sure that you check-in all text files with UNIX-style line endings (not \r\n but \n).

## Guidelines for the contents

### Mind your audience

The manual is read by Frank developers, testers and system administrators. These professionals have very different backgrounds and ways of thinking. Developers want to understand language structures and details. Please do not only tell them to do something to get some result. Explain them the concepts behind. Testers and system administrators are different. They want to see a lot of pictures and they just want to see how to get the job done. They need to ask the right questions to developers, but they do not want to study the details. 

### Support lazy readers

Beginning users of the Frank!Framework probably read the manual from cover to cover, but more advanced readers probably won't. They have a question, enter a search term in ReadTheDocs and land somewhere in the middle of a story. Therefore, each screen of the HTML version should be self contained. It needs a short introduction, which includes references to other sections with details about the context. After this introduction, the material of the screen can be presented. It is good to know that each screen of the manual corresponds to one .rst file in the git repository.

### How to address the reader

Much material can be formatted as a tutorial. This is a story in which the reader is asked to do something. The expected results of the reader's actions are described and explained. The reader is addressed as "you" and instructions are written using the (polite) imperative: "Please do this. You see that ...".

When there is much material about the same topic, a long set of reader actions and expected results is involved. You need subsections, each having their own introduction. The introduction of a subsection should explain to the reader that she is in the middle of a larger story, and it should tell her at what point in the story she has arrived. Each subsection introduction should support the reader who wants to start the tutorial from that subsection instead of the beginning of the story. Of course, each tutorial should be independent. It should not be necessary to do a tutorial before another tutorial can be started.

The reader should have the choice not to follow the directives but just read along. When a reader is smart or advanced, she should understand the story when she just reads on her webbrowser or even from her telephone. The manual writer should be careful not to omit anything relevant.

There may be more detailed material that does not fit naturally in a tutorial. Such text still has an introduction about something the reader wants to achieve. Such an introduction should interest the reader in proceeding. For each detail mentioned, it should be clear why the reader would care to know.

The only exception is reference material about individual Java classes. This material is allowed to just state the facts.

### Consistent usage of words

The manual should everywhere use the same word for the same thing, with the same spelling.

#### Terminology

Please use the right words to reference the company and their products, as listed below:

* Frank!Framework: The organisation and product being documented in this manual. Note that the exclamation mark is part of the name and that there are two capitals. When no special characters are allowed, we use ``frankframework``.
* Frank!: A solution produced with the Frank!Framework. This is the combination of the Frank!Framework and Frank configs deployed on it.
* Franks!: Plural of Frank.
* Frank!Config(uration): A set of XML files and property files that configures the Frank!Framework to provide a solution for a customer. A Frank config is typically created by a Frank developer. This word is also used for a set of adapters that is defined in or included from the same ``Configuration.xml`` file. When you have multiple ``Configuration.xml`` files within your Frank, you have multiple Frank configs.
* Frank!Config(uration) schema: The XML schema document that defines what XML code is valid for configuring the Frank!Framework.
* Frank!Console: The graphical user interface of the Frank!Framework.
* Frank!Doc: A complement to this manual that is shorter but provides better search capability. It can be accessed through the Frank!Console.
* Frank!Developer: Engineer who writes Frank configs.

#### Cross references

Do we write "This section explains..." or "This subsection explains..." or even "This sub-subsection explains..."? This should be uniform throughout the manual. Here is our choice:

* Chapter: Top-level chapter, for example Getting Started.
* Section: Second-level header, for example Getting Started | Hello World Source Code. Another example is Testing Frank Configurations | Ladybug.
* Subsection: Third-level header, for example Getting Started | Hello World Source Code | Adapter. Another example is Testing Frank Configurations | Ladybug | Preparations.
* Sub-subsection: Everything deeper.

## Automation tools

### Sphinx and ReadTheDocs

The manual text is written in the markup language reStructuredText. In the directory ``docs/source`` there are text files with extension ``.rst``. These files contain text and formatting directives. There are many sources with additional information on the internet. The Python tool Sphinx processes these text files. Sphinx interprets the formatting directives within the ``.rst`` files to make up section headings, to build cross references, to import pictures, etc. Sphinx can make up the document in HTML and PDF. There is an options to build a single HTML page from all reStructuredText files, and another option to create a separate page for each reStructuredText file. Until now we only tested multi-page HTML. With this option, Sphinx builds a file ``index.html`` to hold the table of contents, providing links to the chapter/section/subsection pages.

When you have set up your build environment, you can run Sphinx on your development PC to get a test version of the Frank!Manual. Building also happens automatically when you push your changes to GitHub. When a new commit is pushed, GitHub does a HTTP request to http://www.readthedocs.io, the website of ReadTheDocs. That site picks up the latest version of the manual files and runs Sphinx on them. The result is the manual you can see on http://frank-manual.readthedocs.io.

### TutorialSteps

Please remember the guideline to write text about the Frank!Framework as a tutorial. You invite the reader to do things with the Frank!Framework and to check the results of her action. This way of writing comes with an additional responsibility for you as a technical writer. The work that the reader does should have the effect you intend. As a technical writer, you should do the work you request from the reader and test the resulting Frank configs yourself.

These Frank configs are checked in into this Git repository, but before we can tell how an additional issue has to be addressed. The Frank configs for the manual that you tested once will change, for example because the Frank!Framework is improved. When this happens, you have to update the Frank config backed up in this Git repository and also all related manual text. Doing this manually would be time-consuming and error-prone. Therefore, additional Python scripts have been created to automate this synchronisation. They are implemented in directory "TutorialSteps".

TutorialSteps requires that you do not only check-in the final tested Frank config that a manual reader produces, but also all intermediate versions that the reader will produce while making the tutorial. TutorialSteps then compares subsequent intermediate versions and produces reStructuredText code snippets. These snippets can be included using reStructuredText directives. To summarize, you do not write out updates to Frank configs in the manual source code, which would be code duplication. You store a list of snapshots and from them you generate the reStructuredText that explains each update step the reader should execute.

TutorialSteps has an additional feature. It checks whether the differences between subsequent versions are as expected. With each version, you add a YAML file named "meta.yml" that specifies what files are different from the previous version and also the nature of these differences. If you accidently introduce other differences, TutorialSteps will warn you. You can use this feature to see whether your manual text is complete. Compare the updates you explain to the difference expressed in "meta.yml". TutorialSteps makes sure that the description in "meta.yml" is in agreement with the actual differences with the previous snapshot.

### Download zips

The reader wants to download Frank configurations that you as a technical writer create. The manual has download links that provide these Frank configs as zip files. These zips are created by the script "buildDownloadZips.py". In the file "buildDownloadZips.txt" you configure the directories to zip and the output files to produce. Please do not call "buildDownloadZips.py" directly, but use the "generateAll.py" script instead.

### Contributing to automation software

Before contributing to the automation software, please study the source code carefully. Here are some general statements about the software architecture:

* Many Python files have unit tests. Please run them all by invoking the script  ``runTests.bat``. This script expects that you run it from the ``frank-manual`` checkout directory.
* Each piece of code is as focussed as possible. We try to avoid intermixing code that performs multiple duties. For example, in buildDownloadZips.py, browsing a directory tree is done in method "walkFilesInDirectory". This method gets as a parameter a function object. For each file found, walkFilesInDirectory calls that other function. The Python code within walkFilesInDirectory is focussed to doing the browsing.
* The code is documented extensively. Documentation focusses on what has to be achieved. Documenting implementation details is avoided when possible. The code should speak for itself. The code can speak for itself if variable names are chosen well and if code is focussed to one duty as explained above.

## Building the Frank!Manual

Building the manual involves the following steps:

1. Run Python script "generateAll.py". This will run TutorialSteps and generate the download zips.
2. Build the documentation locally using "make.bat html".
3. If you are satisfied, check-in your work and push your changes. ReadTheDocs will build a new version of the Frank!Manual.

What files and directories do you have to check in into Git and how do you know whether a file is generated? To answer this question, you have to know that ReadTheDocs does not know "generateAll.py", the entry point to TutorialSteps and producing download zips. Therefore, the results of "generateAll.py" should be checked in. All generated files appear in "docs/source/downloads" (download zips) and "docs/source/snippets" (generated snippets of reStructuredText).

There is only one directory you do not check in, and it is "docs/build". This directory contains the output of Sphinx, which can also be generated by ReadTheDocs.
