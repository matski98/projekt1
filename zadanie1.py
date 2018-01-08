import time
import os
import random
a=int(input("szerokosc=\n"))
b=int(input("wysokosc=\n"))
c=b
lista=[]

for i in range (1,b+1):
    r=random.randrange(1, a+1)
    lista.insert(i,r)
    for x in range (1,i+1):
        f=lista[-x]
        print(" "*(f-1)+"X"+" "*(a-f))
    c=c-1
    for z in range (1,c+1):
        print (" "*a)
    time.sleep(0.3)
    os.system("cls")