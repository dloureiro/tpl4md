from platform import system
import sys
import os
from os import mkdir, path, access, R_OK  # W_OK for write permission.
from shutil import copy

from platform import system

version = "1.0"
description = "This templates allows you to create simple documents in PDF format"

# pwd = .../templates/pdf-simple
local_path = path.dirname(path.realpath(__file__))
in_images_path = local_path + "/images"

def usage_message() :
	if system() is "Windows":
		print "To compile : make-pdf-simple.bat"
		print "To clean : make-clean.bat"
	else:
		print "To compile : make pdf-simple"
		print "To clean : make clean"

def generate(out_path) :
	#print "local path is : " + local_path
	out_common_path = out_path + "/common"
	out_bin_path = out_path + "/bin"
	out_images_path = out_path + "/images"
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
	copy(local_path + "/make-pdf-simple.bat",out_path)
	print "-- make-pdf-simple.bat copied"
	copy(local_path + "/enumitem.sty", out_path + "/common")
	print "-- Adding last v 3.5.2 of enumitem.sty"
	copy(local_path + "/pdf-template-simple.tex", out_common_path )
	print "-- Simple pdf template (pdf-template-simple.tex) copied"
	copy(local_path + "/tplformd-simple.sty", out_common_path )
	print "-- Simple tpl4md stylesheet (tplformd-simple.sty) copied"
	copy(local_path + "/doc/README_pdf-simple.md", out_path + "/doc/")
	print "-- Letter template documentation (README_pdf-simple.md) copied"
	copy(local_path + "/doc/README_pdf-simple.pdf", out_path + "/doc/")
	print "-- Letter template documentation (README_pdf-simple.pdf) copied"
	print "- Copying image files"

	mkdir(out_images_path)
	print "-- image directory created"
	copy(in_images_path + "/hw.jpg", out_images_path)
	print "-- hello world image copied"