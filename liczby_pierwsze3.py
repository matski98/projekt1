def Quicksort(tab): 
     if len(tab) <= 1:
          return tab
     else:
          return quicksort([x for x in tab[1:] if x<tab[0]]) + [tab[0]] + quicksort([x for x in tab[1:] if x>=tab[0]])
def Quick(li,first,last):
    if first < last:
        pivot = li[first]
        index = first+1
  
    for i in range(first+1,last+1):
        if pivot > li[i]:
            li[index], li[i] = li[i], li[index]
            index += 1
            li[first], li[index - 1] = li[index - 1], li[first]
  
        if first < index:
            Quick(li,first,index-2)
        if index < last:
            Quick(li,index,last)
    return li