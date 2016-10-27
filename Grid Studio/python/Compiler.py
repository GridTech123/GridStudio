import pickle
import os
import sys
import time

pickle_in = open('file_path.gsrf', 'r')
path = pickle.load(pickle_in)

try:
    t = open(path, 'r')
    print("________________________________________________________________________")
    print("Compiling " +str(path))
    print("________________________________________________________________________")  
    print ''
except:
    print("Somthing went wrong!")
    print('''It may be this:
1. it has to be a .gs or .txt file!
2. There cant be quotes(") in the path
3. Its not a path''')

try:
    if path[len(path) - 2:len(path)] == 'py':
        f = open(path, 'w')
    else:
        f = open(path +str('.py'), 'w')
except:
    print 'there was an error making ' +str(path+str('.py'))
    time.sleep(100)

lines = t.readlines
line = 0
lineReading = 0

while True:
    try:
        f.writelines(''+str(lines[line]))
        line = line + 1
    except:
        if path[len(path) - 2:len(path)] == 'py':
            os.startfile(path)   
        else:
            os.startfile(path+str('.py'))   
        sys.exit()
        

