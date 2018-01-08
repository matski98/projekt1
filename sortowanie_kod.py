import random
def main():
    tab=[]
    size=50
    for i in range(size):
        tab.append(random.randint(0,100))
    print("nieposortowana", tab)
    print("bąbelkowe", bubble_sort(tab[:]))
    print("wstawianie" ,insertion_sort(tab[:]))
    print("wybieranie", selection_sort(tab[:]))
    print("szybkie", quicksort(tab[:]))
    print("scalanie", mergesort(tab[:]))
    print("kopcowanie", heap_sort(tab[:]))   
    
def minimum(n,tab):
    tindex=n
    minimal = tab[n]
    for i in range(n+1,len(tab)):
        if tab[i] < minimal:
            minimal=tab[i]
            tindex=i
    return tindex  

def selection_sort(tab):
    for n in range(len(tab)):
        tab[minimum(n,tab)], tab[n] = tab[n], tab[minimum(n,tab)]
    return(tab)

def insertion_sort(tab):
    for i in range(1,len(tab)):
        for j in range(1,i+1):
            a = i-j
            if tab[a+1] < tab[a]:
                tab[a+1], tab[a] = tab[a], tab[a+1]
    return(tab)

def bubble_sort(tab):
    j=len(tab)-1
    while j>0:
        for i in range(j):
            if tab[i+1] < tab[i]:
                tab[i], tab[i+1] = tab[i+1], tab[i] 
        j-=1
    return(tab)

def quicksort(tab):
    if len(tab) <= 1:
        return tab
    p = tab.pop()
    left = []
    right = []
    for a in tab:
        if a>=p:
            right.append(a)
        else:
            left.append(a)
    tab = quicksort(left) + [p] + quicksort(right)
    return tab    

def mergesort(tab):
    if len(tab)>1:
        mid = len(tab)//2
        lefthalf = tab[:mid]
        righthalf = tab[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                tab[k]=lefthalf[i]
                i=i+1
            else:
                tab[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            tab[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            tab[k]=righthalf[j]
            j=j+1
            k=k+1
    return tab

def heapify(end,i,tab):   
    l=2*i + 1  
    r=2*(i + 1)   
    max=i   
    if l < end and tab[i] < tab[l]:   
        max = l   
    if r < end and tab[max] < tab[r]:   
        max = r   
    if max != i:   
        tab[i], tab[max] = tab[max], tab[i]
        heapify(end, max, tab)   

def heap_sort(tab):     
    end = len(tab)   
    start = end//2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i, tab)   
    for i in range(end-1, 0, -1):   
        tab[i], tab[0] = tab[0], tab[i]   
        heapify(i, 0, tab)   
    return tab

main()