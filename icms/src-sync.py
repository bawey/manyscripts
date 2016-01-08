#!/bin/python
"""
    This script work best with kerberos authentication enabled, as passwords don't need to be inserted
    sample usage:
    ./src-sync.py ~/Forge/cmsicms_git-svn/iCMS/src/jsp/ icmsbox:/opt/Packages/tomcat-portal/webapps/iCMS/jsp/
"""
import pyinotify
import sys
import os
import commands

def check_args(args):
    if len(args) != 2:
        usage()
        sys.exit(1)

def usage():
    print "Please pass two arguments: local directory path and a remote one, in an scp-like format."

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        relpath = event.pathname[len(args[0]):]
        command = "scp %s%s %s%s" % (args[0], relpath, args[1], relpath)
        print "command: " + command
        commands.getstatusoutput(command)


args = sys.argv[1:]
check_args(args)
args[0] = os.path.abspath(args[0])

wm = pyinotify.WatchManager()
wdd = wm.add_watch(args[0], pyinotify.IN_MODIFY, rec=True)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)       
notifier.loop()




