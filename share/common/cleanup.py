#! /usr/bin/python

import glob, os

directory='../templates'
os.chdir(directory)
filelist = glob.glob("*/generator.pyc")
for f in filelist:
    print "-- Removing file : " + f
    os.remove(f)