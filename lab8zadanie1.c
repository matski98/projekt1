#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main(){
	int *Tablica;
	int x;
	x=rand()%100;
	Tablica = (int*) malloc(100*sizeod(int));
	for(int i=0;i<100;i++){
		*(Tablica+i)=x;
	}
	for(int j=0;j<100;i++){
		printf("%d", *(Tablica+i));
	}
	return 0;
}