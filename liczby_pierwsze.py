def Quicksort(tab):
    less = []
    equal = []
    greater = []

    if len(tab) > 1:
        pivot = tab[0]
        for i in tab:
            if i < pivot:
                less.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                greater.append(i)
        return Quicksort(less)+equal+Quicksort(greater)
    
    else:
        return tab