#include<stdio.h>
#include<stdlib.h>
#include<time.h>

char* keygen(int size) {

	/* Parameter: The length of the key. */
	/* Return: The key as a char pointer. */
	/* Objective: Generates a key for symmetric or private-key cryptography. */
	/* Usage: The pointer returned must be freed in the caller method later on. */

	srand(time(0));	/* We enter a seed so that the random() is different everytime. */

	int iter=0;
	char* key = (char*)malloc(sizeof(char)*size);

	for(iter=0; iter<20; iter++) { /* We generate SIZE random alpha-numeric characters. */
		int character = 0 + (rand()%3);
		if(character == 0) key[iter] = 48 + (0 + (rand()%10)); /* We output a number. */
		else if(character == 1) key[iter] = 65 + (0 + (rand()%26)); /* We output a small letter. */
		else if(character == 2) key[iter] = 97 + (0 + (rand()%26)); /* We output a big letter. */
	}

	return key;

}
