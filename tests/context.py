import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir) + "/mancala/"
sys.path.insert(0,parentdir)

print (parentdir)

import Mancala
