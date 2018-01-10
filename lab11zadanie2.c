#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]){
	
	int suma = 0;
	
	for(int i=0;i<argc;i++){
		suma = atoi(argv[i])+suma;
	}
	printf("%i\n", suma);
	return 0;
}