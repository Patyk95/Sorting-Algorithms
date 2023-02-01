from random import randint
import numpy as np
tablica =[1,5,8,7,4,6,0,15,22,78,4,2,9,3,10]
print(tablica)
tablica1 = np.random.randint(0,100000,1000)
print(tablica1)



def Quick(array, left, right):
    i, j, piv = left, right, array[(left+right)//2]
    while i < j:
        while array[i] < piv: i += 1
        while array[j] > piv: j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i] 
            i += 1
            j -= 1
            if left < j: 
                Quick(array, left, j)
            if i < right:
                 Quick(array, i, right)
 



Quick(tablica, 0, len(tablica)-1)
print(tablica)
Quick(tablica1,0,len(tablica1)-1)
print(tablica1) 
