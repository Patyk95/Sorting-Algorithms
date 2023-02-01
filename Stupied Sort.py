import numpy as np
from random import randint
tablica = np.random.randint(0,100,50)
print(tablica)

def Stupied(array):
    i=0
    numer_porownan= 0
    while i < len(array)-1:
        if array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
            i=0
        else:
            i+=1
        numer_porownan +=1
    print(f"Posortowana tablica to :{array}, wykonano porównań :{numer_porownan}, przy liczbie elementów {(len(array))}")
Stupied(tablica)
    
