import os
count = 0
i = 1
for dirpath, dirnames, filenames in os.walk("."): #./nombre
    input(i)
    print("Archivos ",i,filenames)
    print("Carpetas ",i,dirnames)
    i +=1
    for name in filenames:
        print('*',name)
        input()
        if ".txt" in name:
            count +=1
            print ("Archivo",count,":",os.path.join(dirpath,name))
            print ("El contenido del archivo es:")
            fo = open (os.path.join(dirpath,name),"r")
            for line in fo:
                print ('\t',line)
            fo.close()
print("Archivos encontrados",count)
