
tablica =[1,5,8,7,4,6,0,15,22,78,4,2,9,3,10]

n=len(tablica)-1


def Bubble(array):
    n=len(array)
    for i in range (n):
        for j in range(0,n-i-1):
            if tablica[j]>tablica[j+1]:
                tablica[j],tablica[j+1]= tablica[j+1],tablica[j]
                print(f"ZAMIENIONO MIEJSCAMI {tablica[j]} z {tablica[j+1]}, aktualnie tablica wygląda : {tablica}")


Bubble(tablica)

