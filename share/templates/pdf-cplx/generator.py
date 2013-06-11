from platform import system
import sys
import os
from os import mkdir, path, access, R_OK  # W_OK for write permission.
from shutil import copy, copytree

from platform import system

version = "1.0"
description = "This templates allows you to create complexe documents in PDF format"

# pwd = .../templates/pdf-simple
local_path = path.dirname(path.realpath(__file__))
in_images_path = local_path + "/images"

def usage_message() :
	if system() is "Windows":
		print "To compile : make-pdf-cplx.bat"
		print "To clean : make-clean.bat"
	else:
		print "To compile : make pdf-cplx"
		print "To clean : make clean"

def generate(out_path) :
	#print "local path is : " + local_path
	in_common_path = local_path + "/common"
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
	copy(local_path + "/make-pdf-cplx.bat",out_path)
	print "-- make-pdf-cplx.bat copied"
	copy(local_path + "/pdf-template-cplx.tex", out_common_path )
	print "-- Complexe pdf template (pdf-template-cplx.tex) copied"
	copytree(local_path + "/dblatex", out_path + "/common/dblatex")
	print "-- Adding dblatex"
	copy(local_path + "/tplformd-cplx.sty", out_common_path )
	print "-- Complexe tpl4md stylesheet (tplformd-cplx.sty) copied"
	copy(local_path + "/doc/README-fr_pdf-cplx.md", out_path + "/doc/")
	print "-- Complex template documentation (README-fr_pdf-cplx.md) copied"
	copy(local_path + "/doc/README-fr_pdf-cplx.pdf", out_path + "/doc/")
	print "-- Complex template documentation (README-fr_pdf-cplx.pdf) copied"
	copy(local_path + "/doc/README_pdf-cplx.md", out_path + "/doc/")
	print "-- Complex template documentation (README_pdf-cplx.md) copied"
	copy(local_path + "/doc/README_pdf-cplx.pdf", out_path + "/doc/")
	print "-- Complex template documentation (README_pdf-cplx.pdf) copied"

	print "- Copying image files"

	mkdir(out_images_path)
	print "-- image directory created"
	copy(in_images_path + "/hw.jpg", out_images_path)
	print "-- hello world image copied"
	copy(in_images_path + "/quotes_opening.png", out_images_path)
	print "-- quotes_opening image copied"