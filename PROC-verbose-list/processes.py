from subprocess import call
import sys

system = sys.argv[1].upper()

if (system == "WINDOWS"):
    call("tasklist")

if (system == "LINUX"):
    call("ps aux")