#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]){
if(argc>1){
	FILE *fp;
	FILE *fo;
	
	fp=fopen(argv[2],"r");
	fo=fopen(argv[3],"w");
	if (strncmp(argv[1],"-u", 3) == 0){
		
		
	}
	else if (strncmp(argv[1],"-l", 3) == 0){
		
		
	}
	else if (strncmp(argv[1],"-r", 3) == 0){
		
		
	}
}
	return 0;
}