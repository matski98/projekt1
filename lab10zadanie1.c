#include <stdio.h>
#include <stdlib.h>

typedef struct elem {
	struct elem *nastepny;
	int wartosc;
} el;

el *pierwszy;

void dodaj (el *lista, int liczba){
	el *wskaznik, *nowy;
	wskaznik = lista;
	while (wskaznik->nastepny != NULL)
	{
		wskaznik = wskaznik->nastepny;
	}
	nowy =(el*) malloc (sizeof(el));
	nowy->wartosc = liczba;
	nowy->nastepny = NULL;
	wskaznik->nastepny = nowy;
}
void wypisz(el *lista){
	el *wskaznik=lista;
	while(wskaznik != NULL){
		printf ("%d\n", wskaznik->wartosc);
		wskaznik = wskaznik->nastepny;
	}
}
int main(){
	pierwszy =(el*) malloc (sizeof(el));
	pierwszy->wartosc = 2;
	pierwszy->nastepny = NULL;
	int x=0;
	dodaj(pierwszy, 3);
	wypisz(pierwszy);
	return 0;
}