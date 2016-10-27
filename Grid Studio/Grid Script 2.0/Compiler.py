import pickle
import os
import sys
import time

pickle_in = open('file_path.gsrf', 'r')
path = pickle.load(pickle_in)

try:
    t = open(path, 'r')
    print("________________________________________________________________________")
    print("running " +str(path))
    print("________________________________________________________________________")  
    print ''
except:
    print("Somthing went wrong!")
    print('''It may be this:
1. it has to be a .gs or .txt file!
2. There cant be quotes(") in the path
3. Its not a path''')


line = 1
lines = t.readlines()
lineRea = 0

while True:
	try:
		lineRea = lines[line]
		lineLen = len(lineRea)
	except:
		print '_____FINISH_____'
		time.sleep(100)

	if lineRea[0:5] == 'print':
		print lineRea[6:lineLen]

	if lineRea[0:4] == 'wait':
		sleepLen = lineRea[5:lineLen]
		time.sleep(+int(sleepLen))

	line = line + 1
