# Documentation du template epub

## Introduction

Cette documentation est en lien avec le template pour la création d'e-book pour le programme `marksf_gen`

## Structure du template

    root
	|- Makefile
	|- configuration.json
	|- README.md
	|- README-fr.md
	|- doc
	|  |- README-fr_epub.pdf
    |  |- README_epub.pdf
	|- document.md
	|- generator.py
	|- images
    |  |- hw.jpg
	|- make-clean.bat
	|- make-epub.bat
	|- title.txt

## Description de ce contenu

 * **Makefile** : Makefile pour la génération/clean de l'e-book d'output
 * **README(-fr).md** : Ce fichier de readme
 * **doc/README(-fr)_epub.pdf** : Ce fichier de readme en pdf
 * **configuration.json** : Fichier de configuration pour l'e-book final
 * **generator.py** : Fichier permettant la génération du projet basé sur le template
 * **document.md** : Le document de base d'exemple pour ce template
 * ** images/* ** : Un ensemble d'images de base
 * **make-clean.bat** : Fichier batch à utiliser sous windows pour le nettoyage d'un projet
 * **make-epub.bat** Fichier batch à utiliser pour la génération de l'epub
 * **title.txt** : Fichier utiliser pour la définition du titre et de l'auteur de l'epub

Nous allons aborder les fichiers les plus importants.

## Makefile

Fichier de compilation permettant la gestion de la compilation de l'epub:

 * epub : génération de la version e-book
 * clean : pour le nettoyage
 
## title.txt

Ce fichier contient deux lignes, la première correspond au titre du document, la seconde à/aux auteurs.
** Ces variables sont automatiquement remplies par le script d'adaptation de fichier **

## document.md

Ce fichier est le document maître dans lequel il faudra ajouter l'ensemble des informations qui vont constituer le corps du résultat produit.

À noter que la syntaxe markdown supportée est une extension de la version officielle et vous pouvez retrouver l'ensemble des éléments fournis par Pandoc dont on peut trouver la description sur [la page dédiée](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown).

** \underline{Note} : Vous pouvez donner le nom que vous voulez à ce fichier tant que vous donnez le nom du fichier source dans le fichier de configuration **

## configuration.json

Voici le contenu d'un fichier complet de configuration avec les variables correspondantes pour un epub :

    {
	"source_file_name":"document.md", // nom du fichier source
	"destination_file_name":"example", // nom du fichier de destination
	"title" : "Document entre SysFera et un client", // titre du document
	"author" : "John Doe" // auteur du document
	}

## generator.py

Ce fichier est utilisé par le script `tpl4md` pour la copie des fichiers d'un template lors de la création d'un projet basé sur ce template. Il déclare deux variables :

 * `version` : version du template
 * `description` : description du template

Elle serve notamment pour l'affichage de la liste des templates disponibles.

Il implémente aussi deux fonctions :

 * `usage_message`: fonction affichant l'usage du template
 * `generate` : fonction générant les fichiers spécifique d'une template lors de la création d'un nouveau projet
 
## Structure d'un projet généré

Voici, après génération, le contenu d'un projet pour un e-book au format ePub :

    root
	|- Makefile
	|- bin
	|  |- config_parsing
	|  |- generate_files
	|- common
	|  |- title.txt
	|- configuration.json
    |- README.md
    |- README-fr.md
    |- README_epub.md
    |- README_epub-fr.md
	|- doc
	|  |- README_epub.pdf
	|  |- README_epub-fr.pdf
	|  |- README.pdf
	|  |- README-fr.pdf
	|- images
	|  |- hw.jpg
	|- document.md
	|- make-clean.bat
	|- make-epub.bat

 
## README.pdf

Le readme en pdf est générée avec la commande suivante :

    pandoc -f markdown-raw_tex README-fr.md -o doc/README-fr_epub.pdf