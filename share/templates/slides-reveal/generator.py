from platform import system
import sys
import os
from os import mkdir, path, access, R_OK  # W_OK for write permission.
from shutil import copy, copytree

from platform import system

version = "1.0"
description = "This templates allows you to create Reveal.js presentation with the SysFera template"

# pwd = .../templates/pdf-simple
local_path = path.dirname(path.realpath(__file__))
in_image_path = local_path + "/images"

def usage_message() :
	if system() is "Windows":
		print "To compile : make-slides-reveal.bat"
		print "To clean : make-clean.bat"
	else:
		print "To compile : make slides-reveal"
		print "To clean : make clean"

def generate(out_path) :
	#print "local path is : " + local_path
	out_common_path = out_path + "/common"
	out_bin_path = out_path + "/bin"
	out_images_path = out_path + "/images"
	mkdir(out_common_path)
	print "- Copying configuration and compilation files"
	copy(local_path + "/generate_files", out_bin_path)
	print "-- Copying generate_files script"
	copy(local_path + "/configuration.json", out_path)
	print "-- Example configuration.json copied"
	copy(local_path + "/Makefile",out_path)
	print "-- Makefile copied"
	copy(local_path + "/make-clean.bat",out_path)
	print "-- make-clean.bat copied"
	copy(local_path + "/make-slides-reveal.bat",out_path)
	print "-- make-slides-reveal.bat copied"
	copy(local_path + "/index.html",out_common_path+"/")
	print "-- template index.html file copied"
	copytree(local_path + "/src", out_path + "/src")
	print "-- example source files copied"
	print "- Copying Reveal.js template files"
	copy(local_path + "/Gruntfile.js", out_path)
	copy(local_path + "/LICENSE", out_path)
	copy(local_path + "/favicon.ico", out_path)
	copy(local_path + "/package.json", out_path)
	copytree(local_path + "/css", out_path + "/css")
	copytree(local_path + "/js", out_path + "/js")
	copytree(local_path + "/lib", out_path + "/lib")
	copytree(local_path + "/plugin", out_path + "/plugin")
	print "-- Reveal.js files copied"

	print "- Copying documentation"
	copy(local_path + "/doc/README_slides-reveal.md", out_path + "/doc/")
	print "-- Letter template documentation (README_slides-reveal.md) copied"
	copy(local_path + "/doc/README_slides-reveal.pdf", out_path + "/doc/")
	print "-- Letter template documentation (README_slides-reveal.pdf) copied"

	print "- Copying image files"
	copytree(local_path + "/images", out_images_path)
	print "-- Images directory copied"
