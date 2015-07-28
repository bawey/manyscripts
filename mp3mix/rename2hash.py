#!/bin/python

import hashlib
import sys
import commands

def rename2hash(files):
    command_template = "mv \"%s\" %s"
    for f in files:
        command = command_template % (f, hashlib.md5(f).hexdigest()+f[f.rfind('.'):])
        (status, output) = commands.getstatusoutput(command)
        print command
        

if __name__ == "__main__":
    rename2hash(sys.argv[1:])