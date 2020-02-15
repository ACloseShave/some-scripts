#!/usr/bin/env python3

#this calls a webpage and dumps a screen scrape to a file
#usage webget(url, filename)

import os
import subprocess

#webget is created as a function where the usage is defined as "webget (site_address,output_file)"
def webget(site, output):
    #a linux shell command is called to dump the text to the file
    command = 'w3m -dump ' + site + ' > ' + output
    outfile = open(output, "w")
    filetext = subprocess.Popen(command, shell=True, stdout=file(output,"w"))
    filetextfix = filetext.communicate()

#now we call our function with the variables we want
webget ('http://www.yahoo.com','test.txt')