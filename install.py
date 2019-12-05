#!/usr/bin/python

import sys, os, shutil

if (os.path.exists('/usr/local/Git-Switch')):
    pass
else:
    os.mkdir('/usr/local/Git-Switch')

if (os.path.exists('/usr/local/Git-Switch/switch.py')):
    print("Git-Switch already installed")
    pass
else:
    shutil.copy('switch.py', '/usr/local/Git-Switch/switch.py') 

with open(os.path.expanduser("~/.bashrc"), "r") as bashrc:
  for line in bashrc:
      if "Git-Switch" in line.rstrip():
          print("Git-Switch already added to bashrc")
          sys.exit()

with open(os.path.expanduser("~/.bashrc"), "at") as bashrc:
  bashrc.write(
    "\n"
    "# Added by Git-Switch\n"
    "function git () {\n"
    "  if [[ $@ == 'push' ]]; then\n"
    "    shift\n"
    "    command /usr/local/Git-Switch/switch.py\n"
    "  elif [[ $1 == 'real' && $2 == 'push' ]]; then\n"
    "    shift\n"
    "    shift\n"
    "    command git push $@\n"
    "  else\n"
    "    command git $@\n"
    "  fi\n"
    "}\n"
  )

