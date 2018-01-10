#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
int main(){
	srand(time(0));
	int *Tablica;
	double y = 10 + rand()%90;
	Tablica = (int*) malloc(y*sizeof(int));
	for(int i=0;i<y;i++){
		int x = 10 + rand()%90;
		*(Tablica+i)=x;
	}
	double suma=0;
	int m=0;
	int z=0;
	printf("y=%lf\n", y);
	for(int k=0; k<y; k++){
		
		suma = suma+Tablica[k];
		if (m<*(Tablica+k)){
			m=*(Tablica+k);
			z=k;
		}
	}
	double srednia;
	srednia=suma/y;
	printf("%lf\n%d\n", srednia, z);
	int *Tablica2;
	int b = rand()%100;
	Tablica2 = (int*) realloc(Tablica, b*sizeof(int));
	int c=y;
	for(c=y; c<b+y; c++){
		int v=rand()%100;
		*(Tablica2+c)=c;
	}
	for(int j=0;j<c;j++){
		printf("%d\n", *(Tablica2+j));
	}
	printf("c=%d\n", c);
	free(Tablica2);
	return 0;
}