import numpy as np
from random import random


def sortuj_wybor_min(tab, n):
    for x in range(n-1): #iterujemy poprzez wszsytkei elementy tablicy, poza ostatnim
        minimum = x #usatwiamy aktualny element jako ten najmniejszy
        for j in range(x+1, n):  #a nastepnie szukamy elementow od niego mniejszych
            if tab[j] < tab[minimum]:
                minimum = j
        if x != minimum: #jezeli znajdziemy element jakkolwiek mniejszy
            print ("\nKrok ", (x+1), ": wstawianie elementu minimalnego ", tab[minimum], " na pozycje ", x)
            pom = tab[x] #dokonujemy jego zamiany
            tab[x] = tab[minimum]
            tab[minimum] = pom
            print (tab)
def sortuj_wybor_max(tab, n):
    for x in range(n-1): #iterujemy poprzez wszsytkei elementy tablicy, poza ostatnim
        maximum= x #usatwiamy aktualny element jako ten najwiekszy
        for j in range(x+1, n):  #a nastepnie szukamy elementow od niego mniejszych
            if tab[j] > tab[maximum]:
                maximum = j
        if x != maximum: #jezeli znajdziemy element jakkolwiek większy
            print ("\nKrok ", (x+1), ": wstawianie elementu maxymalnego ", tab[maximum], " na pozycje ", x)
            pom = tab[x] #dokonujemy jego zamiany
            tab[x] = tab[maximum]
            tab[maximum] = pom
            print(tab)
def sortowanie_glupie(tab):
    i=0
    while i < len(tab)-1:
        if tab[i] > tab[i+1]:
            tab[i+1],tab[i] = tab[i], tab[i+1]
            i=0
        if tab[i] <= tab[i+1]:
            i+=1
    print (tab)
def sortowanie_bombelkowe(tab):
    n=len(tab)-1
    for i in range (n):
        for j in range(n-1):
            if tab[j]>tab[j+1]:
                tab[j], tab[j + 1] = tab[j + 1]
            else:
                break
    print(tab)
def bubbleSort(tab):
    n = len(tab)
    for i in range(n - 1):
        flag = 0
        for j in range(n - 1):
            if tab[j] > tab[j + 1]:
                tab[j],tab[j + 1] = tab[j + 1],tab[j]
                flag = 1
        if flag == 0:
            pass
    return tab
def sort_shella(tab):
    n=len(tab)
    h=n//2
    while h>0:
        for i in range(h,n):
            x=tab[i]
            j=i
            while (j>=h) and (tab[j-h]>x):
                tab[j]=tab[j-h]
                j-=h

            tab[j]=x
        h//=2
    print(tab)
def sortoweanie_przez_scalanie(tab):
    n=len(tab)
    if n>1:
        mid=n//2
        L=tab[:mid]
        R=tab[mid:]
        sortoweanie_przez_scalanie(L)
        sortoweanie_przez_scalanie(R)
        i=0
        j=0
        k=0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1

            # Checking if any element was left
        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1
def partition(input_list,low,high):
    i = (low - 1)
    pivot = input_list[high]
    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] =  input_list[j], input_list[i]
    input_list[i+1],input_list[high] = input_list[high],input_list[i+1]
    return (i+1)
def quickSort(input_list, low, high):
    if low < high:
        partition_index = partition(input_list,low,high)
        quickSort(input_list, low, partition_index - 1)
        quickSort(input_list, partition_index + 1, high)



tab= [9, -3, 5, 2, 6, 8, -6, 1, 3]
print(tab)
tab1=np.random.randint(-10,60,40)
print(tab1)
n = len(tab)-1
n1=len(tab1)-1
quickSort(tab, 0,n)
quickSort(tab1, 0,n1)
print(tab)
print(tab1)





#x=[4,8,7,4,1,0,30,24,9]
#sortoweanie_przez_scalanie(x)
#print(x)
#sort_shella(x)
#sortowanie_bombelkowe(d)
#sortowanie_glupie(x1)
#sortuj_wybor_min(d,len(d))
#sortuj_wybor_max(d,len(d))

