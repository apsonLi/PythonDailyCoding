import os
import codecs
filenames=os.listdir(os.getcwd())

out=open("name.txt",'w')

for name  in filenames:
    out.write(name+'\n')
out.close()

    
