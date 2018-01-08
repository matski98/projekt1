def losowanie(x):
    import random
    tablica = []
    random.seed(x)
    for i in range(rozmiar):
        a = random.randrange(100)
        tablica.append(a)
    return tablica


def wybieranie(tablica):
    for x in range(rozmiar-1):
        mini = int(tablica[x])
        ind = x
        for y in range(x+1,rozmiar):
            new=int(tablica[y])
            if new < mini:
                mini = new
                ind = y
        tablica[x], tablica[ind] = tablica[ind], tablica[x]
    return tablica


def wstawianie():
    for i in range(1, rozmiar):
        for j in range(0, i):
            p = tableau[i]
            q = tableau[j]
            if p < q:
                k = i
                a = tableau[i]
                while k > j:
                    tableau[k] = tableau[k - 1]
                    k = k - 1
                tableau[j] = a
                break
    return tableau

def babel():
    a=1
    while a!=0:
        a=0
        for x in range(1,rozmiar):
            n = tablix[x-1]
            m = tablix[x]
            if n > m:
                tablix[x-1],tablix[x]=tablix[x],tablix[x-1]
                a=a+1
    return tablix

def szybkie(lista):
    dl=len(lista)
    if dl <= 1:
        return lista
    p = lista.pop()
    left = []
    right = []
    for a in lista:
        if a>=p:
            right.append(a)
        else:
            left.append(a)
    gotowa = szybkie(left) + [p] + szybkie(right)
    return gotowa

def scalanie(lista):
    dl=len(lista)
    if dl<=1:
        return lista
    sr=dl/2
    x=0
    left=[]
    right=[]
    for a in lista:
        if x<sr:
            left.append(a)
        else:
            right.append(a)
        x=x+1
    left=scalanie(left)
    right=scalanie(right)
    i=0
    j=0
    di=len(left)
    dj=len(right)
    gotowa=[]
    while (i<di and j<dj):
        if left[i]<=right[j]:
            gotowa.append(left[i])
            i=i+1
        else:
            gotowa.append(right[j])
            j=j+1
    if i==di:
        while(j<dj):
            gotowa.append(right[j])
            j=j+1
    if j==dj:
        while(i<di):
            gotowa.append(left[i])
            i=i+1
    return gotowa

import heapq
def kopiec(lista):
    temp=list(lista)
    heapq.heapify(temp)
    dl=len(lista)
    for i in range(dl):
        lista[i]=heapq.heappop(temp)
    return lista

nasiono = 2
rozmiar=50
tablica = losowanie(nasiono)
tableau = list(tablica)
tablix = list(tablica)
lista=list(tablica)
tabela=list(tablica)
nazwa=list(tablica)
print(tablix)
print(wybieranie(tablica))
print(wstawianie())
print(babel())
print(szybkie(lista))
print(scalanie(tabela))
print(kopiec(nazwa))