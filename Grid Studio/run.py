import os
import sys
import pickle
import time
import time

pickle_in = open('path.gsrf', 'r')
path = pickle.load(pickle_in)

pathLen = len(path)

if path[pathLen - 2:pathLen] == 'gs':
	os.chdir('Grid Script')
	pickle_out = open('file_path.gsrf', 'w')
	pickle.dump(path, pickle_out)
	pickle_out.close()
	os.startfile('Grid_Script_Compiler.py')

elif path[pathLen - 3:pathLen] == 'gsw':
	os.chdir('Grid Script Web')
	pickle_out = open('file_path.gsrf', 'w')
	pickle.dump(path, pickle_out)
	pickle_out.close()
	os.startfile('Compiler.py')

elif path[pathLen - 3:pathLen] == 'gs2':
	os.chdir('Grid Script 2.0')
	pickle_out = open('file_path.gsrf', 'w')
	pickle.dump(path, pickle_out)
	pickle_out.close()
	os.startfile('Compiler.py')

elif path[pathLen - 2:pathLen] == 'py' or path[pathLen - 3:pathLen] == 'pyc' or path[pathLen - 3:pathLen] == 'pyw':
	os.startfile(path)

elif path[pathLen - 4:pathLen] == 'html' or path[pathLen - 3:pathLen] == 'htm':
	os.startfile(path)

else:
    print 'unknown file could not run'
    time.sleep(100)

os.chdir('..')
sys.exit()
