# Epub template documentation

## Introduction

This documentation is linked to the epub template for `tpl4md`

The compilation is based on the usage of `pandoc`.

## Template structure

    root
	|- Makefile
	|- configuration.json
	|- doc
    |  |- README.pdf
    |  |- README-fr.pdf
	|- document.md
	|- generator.py
	|- images
    |  |- hw.jpg
	|- make-clean.bat
	|- make-epub.bat
	|- README.md
	|- README-fr.md
	|- title.txt

## Content description

 * **Makefile** : Makefile for the generation of the output epub
 * **doc/README(-fr).pdf** : This readme in the pdf format
 * **README(-fr).md** : This readme file
 * **configuration.json** : configuration file for the ebook generation
 * **generator.py** : Main file use during the generation of the project based on the template
 * **document.md** : Example document for this template
 * ** images/* ** : Example images
 * **make-clean.bat** : Batch file to use on Windows Operating Systems for the clean up
 * **make-epub.bat** : Batch file to use on Windows Operating Systems for the epub generation
 * **title.txt** : File used for the definition of the title and the author of the e-book

We will explore the different import files of this template.

## Makefile

The Makefile used for the compilation of the epub file provides two targets:

 * epub : for the e-book generation
 * clean : for the clean up
 
## title.txt

This file contains two lines, the first one is the title, the second one the author(s).

** These variables are automatically filled by the adaptation script **

## document.md

This file will contain the content of your epub document.

It should be noted that the markdown syntax available is the one supported by the Pandoc software. You can find the description of the corresponding elements on the [dedicated page](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown).

** \underline{Note} : Vous pouvez donner le nom que vous voulez à ce fichier tant que vous donnez le nom du fichier source dans le fichier de configuration **

## configuration.json

Here is an example of the configuration file that could be used for the generation of an epub:

    {
	"source_file_name":"document.md", // source file name
	"destination_file_name":"example", // destination file name
	"title" : "Example document", // document title
	"author" : "John Doe" // author
	}

## generator.py

This file is used by the `tpl4md` script for the generation of the project base on this template. Two variables are declared:

 * `version` : template version
 * `description` : template description

These variables are mainly used to display the available templates.

This file also implements to functions:

 * `usage_message`: to display how to use this template
 * `generate` : the main function of the script used to generate the skeleton of a project for the creation of an epub file
 
## Generated project structure

After generation, the content of a projet dedicated to the creation of a ebook is as follows:

    root
	|- Makefile
	|- bin
	|  |- config_parsing
	|  |- generate_files
	|- common
	|  |- title.txt
	|- configuration.json
	|- doc
	|  |- README.md
	|  |- README_epub.md
	|  |- README_epub.pdf
	|  |- README-fr_epub.md
	|  |- README-fr_epub.pdf
	|  |- README.pdf
	|- images
	|  |- hw.jpg
	|- document.md
	|- make-clean.bat
	|- make-epub.bat

 
## README.pdf

The pdf version of the README is generated using the following command:

    pandoc -f markdown-raw_tex README.md -o doc/README_epub.pdf