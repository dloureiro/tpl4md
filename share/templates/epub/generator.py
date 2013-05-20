from platform import system
import sys
import os
from os import mkdir, path, access, R_OK  # W_OK for write permission.
from shutil import copy

from platform import system

version = "1.0"
description = "This templates allows you to create e-books in ePub format"

# pwd = .../templates/pdf-simple
local_path = path.dirname(path.realpath(__file__))
in_image_path = local_path + "/images"

def usage_message() :
	if system() is "Windows":
		print "To compile : make-epub.bat"
		print "To clean : make-clean.bat"
	else:
		print "To compile : make epub"
		print "To clean : make clean"

def generate(out_path) :
	#print "local path is : " + local_path
	out_common_path = out_path + "/common"
	out_bin_path = out_path + "/bin"
	out_image_path = out_path + "/images"
	out_doc_path = out_path + "/doc"
	mkdir(out_common_path)
	copy(local_path + "/document.md", out_path)
	print "-- Example document.md copied"
	copy(local_path + "/generate_files", out_bin_path)
	print "-- Copying generate_files script"
	copy(local_path + "/configuration.json", out_path)
	print "-- Example configuration.json copied"
	copy(local_path + "/Makefile",out_path)
	print "-- Makefile copied"
	copy(local_path + "/make-clean.bat",out_path)
	print "-- make-clean.bat copied"
	copy(local_path + "/make-epub.bat",out_path)
	print "-- make-epub.bat copied"
	copy(local_path + "/title.txt", out_common_path )
	print "-- Title file (title.txt) copied"
	copy(local_path + "/doc/README-fr_epub.pdf", out_doc_path + "/")
	print "-- Epub template documentation (README-fr_epub.pdf) copied"
	copy(local_path + "/doc/README_epub.pdf", out_doc_path + "/")
	print "-- Epub template documentation (README_epub.pdf) copied"
	copy(local_path + "/README-fr.md", out_doc_path + "/README-fr_epub.md")
	print "-- Epub template documentation (README-fr.md) copied"
	copy(local_path + "/README.md", out_doc_path + "/README_epub.md")
	print "-- Epub template documentation (README.md) copied"
	print "- Copying image files"

	mkdir(out_image_path)
	print "-- image directory created"
	copy(in_image_path + "/hw.jpg", out_image_path)
	print "-- hello world image copied"