# Documentation du template pdf simple

## Introduction

Cette documentation est en lien avec le template pour la création de pdf simples pour le programme `marksf_gen`

## Structure du template

    root
	|- Makefile
	|- configuration.json
	|- doc
	|  |- README_pdf-simple.md
	|  |- README_pdf-simple.pdf
	|- document.md
	|- generator.py
	|- images
	|  |- hw.jpg
	|- enumitem.sty
	|- make-clean.bat
	|- make-pdf-simple.bat
	|- pdf-template-simple.tex
	|- sysfera-simple.sty

## Description de ce contenu

 **Fichier**                      **Description**
------------------------------   ----------------------------------------------------------------
  Makefile                        Makefile pour la génération/clean du pdf simple d'output
  doc/README_pdf-simple.(md/pdf)  Ce fichier de readme
  configuration.json              Fichier de configuration pour le fichier pdf final
  generator.py                    Fichier permettant la génération du projet basé sur le template
  document.md                     Le document de base d'exemple pour ce template
  images/*                        Un ensemble d'images de base
  make-clean.bat                  Fichier batch à utiliser sous windows pour le nettoyage d'un projet
  make-pdf-simple.bat             Fichier batch à utiliser sous windows pour la génération du pdf simple
  pdf-template-simple.tex         Fichier de template utilisé pour la création de l'enrobage du fichier pdf créé
  sysfera-simple.sty              Feuille de style définissant le style simple SysFera

Nous allons aborder les fichiers les plus importants.

## Makefile

Fichier de compilation permettant la gestion de la compilation d'un document simple en pdf :

 * pdf-simple : génération de la version simple en pdf
 * clean : pour le nettoyage

## pdf-template-simple.tex

Ce fichier LaTeX décrit l'ensemble des éléments qui forment le template qui permet la création des fichiers simples en pdf au style SysFera.

Ce fichier possède des balises de la forme :

    !title!
    
Qui sont automatiquement remplies par le script generate_files

Pour information, voici les variables qui sont utilisées :

 * Le titre avec la balise `\title`. Ex :
 
~~~latex
\title{Exemple de document SysFera}
~~~
 
 * L'auteur avec la balise `\author`. Ex :
       
~~~latex
\author{John Doe}
~~~

 * Le client avec la balise `\SFclient`. Ex :
 
~~~latex
\SFclient{Client 404}
~~~
 
D'autres options sont disponibles dans le template comme :

 * `\SFreleaseinfo` pour afficher une box en en-tête de page affichant un texte. Ex :

~~~latex
\SFreleaseinfo{Réalisé} 
~~~

 * `\showwatermark` pour avoir un filigrane utilisé sur les pages. Vous pouvez utiliser du texte ou mettre un image en utilisant l'environnement LaTeX adapté. Ex :
 
~~~latex
\showwatermark{DRAFT} 
~~~

*\underline{Note} : Sauf si vous souhaitez modifier le template lui-même, nous n'avez pas à modifier ce fichier lorsque vous souhaitez créer un document.*

## document.md

Ce fichier est le document maître dans lequel il faudra ajouter l'ensemble des informations qui vont constituer le corps du résultat produit.

À noter que la syntaxe markdown supportée est une extension de la version officielle et vous pouvez retrouver l'ensemble des éléments fournis par Pandoc dont on peut trouver la description sur [la page dédiée](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown).

*\underline{Note} : Vous pouvez donner le nom que vous voulez à ce fichier tant que vous donnez le nom du fichier source dans le fichier de configuration*

## configuration.json

Voici le contenu d'un fichier complet de configuration avec les variables correspondantes pour un pdf simple :

    {
		"source_file_name":"document.md", // nom du document
		"destination_file_name":"example", // nom de destination du document
		"client":"Client", // nom du client a qui est destine le document
		"title" : "Document entre SysFera et un client", // titre du document
		"author" : "John Doe", // auteur du document
		"project_name" : "Projet 999", // nom du projet
		"release_info":"Réalisé héhé", // information de release du document
		"water_mark":"DRAFT" // watermark s'affichant en fond du document
	}

## generator.py

Ce fichier est utilisé par le script `marksf_gen` pour la copie des fichiers d'un template lors de la création d'un projet basé sur ce template. Il déclare deux variables :

 * `version` : version du template
 * `description` : description du template

Elle serve notamment pour l'affichage de la liste des templates disponibles.

Il implémente aussi deux fonctions :

 * `usage_message`: fonction affichant l'usage du template
 * `generate` : fonction générant les fichiers spécifique d'une template lors de la création d'un nouveau projet
 
## Structure d'un projet généré

Voici, après génération, le contenu d'un projet pour un pdf simple :

    root
	|- Makefile
	|- bin
	|  |- config_parsing
	|  |- generate_files
	|- common
	|  |- bgsysfera.png
	|  |- logosysfera.pdf
	|  |- pdf-template-simple.tex
	|  |- sysfera-simple.sty
	|  |- enumitem.sty
	|- configuration.json
	|- doc
	|  |- README.md
	|  |- README_pdf-simple.md
	|  |- README_pdf-simple.pdf
	|  |- README.pdf
	|- images
	|  |- hw.jpg
	|- document.md
	|- make-clean.bat
	|- make-pdf-simple.bat
 
## README.pdf

Le readme en pdf est générée avec la commande suivante :

    pandoc -f markdown-raw_tex README_pdf-simple.md -o README_pdf-simple.pdf