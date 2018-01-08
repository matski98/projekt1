#!/usr/bin/env python3

from random import randint
import time



def insertionSort(tab):

  for i in range(1,len(tab)):
	  for j in range(1,i+1):
	    a = i-j
	    if tab[a+1] < tab[a]:
		    tab[a+1], tab[a] = tab[a], tab[a+1]


  return tab


def bubbleSort(tab):

	
	length = len(tab) - 1
	sorted = False
	while not sorted:
		sorted = True
		for i in range(length):
			if tab[i] > tab[i+1]:
				sorted = False
				tab[i], tab[i+1] = tab[i+1], tab[i]


	return tab


def selectionSort(tab):
	start_time = time.time()

	for i in range(len(tab)):
		inx = i
		for j in range(i+1,len(tab)):
			if tab[j] < tab[inx]:
				inx = j
			if inx != i:
				tab[inx],tab[i] = tab[i],tab[inx]              


	return tab


def quickSort(tab):



	if len(tab) < 2:
		return tab

	p=tab[0]                                     
	tab1=[]                                      
	tab2=[]                                     
	for i in range(1,len(tab)):
		if tab[i]< p:
			tab1.append(tab[i])         
			
		elif tab[i]>=p: 
			tab2.append(tab[i])                                

	tab=quickSort(tab1)+[p]+quickSort(tab2)                                        
	

	return tab


def merge(tab1, tab2):
	mrgd = []
	i, j = 0, 0

	while i < len(tab1) and j < len(tab2):
		if tab1[i] < tab2[j]:
			mrgd.append(tab1[i])
			i += 1
		else:
			mrgd.append(tab2[j])
			j += 1

	mrgd += tab1[i:]
	mrgd += tab2[j:]

	return mrgd


def mergeSort(tab):
	


	if len(tab) <= 1:
		return tab
	
	mid = len(tab)//2

	return merge( mergeSort(tab[:mid]), mergeSort(tab[mid:])) 



def heapSort():
	pass


def main():

	tab = []
	for i in range(0, 50):
			tab[proba].append(randint(0,100)
			
		
	print("INSERTION SORT \n", insertionSort(tab[:]))


	print("\n\nBUBBLE SORT \n", bubbleSort(tab[:])
	

	print("\n\nSELECTION SORT \n", selectionSort(tab[:])
	

	print("\n\nQUICK SORT \n", quickSort(tab[:])


	print("\n\nMERGE SORT \n", mergeSort(tab[:])




main()