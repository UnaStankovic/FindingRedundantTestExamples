#include "library.h"

int sabiranje(int a, int b) {
	return a + b;
}

int oduzimanje(int a, int b) {
	return a - b;
}

int mnozenje(int a, int b) {
	return a * b;
}

int deljenje(int a, int b) {
	if(b != 0)
		return a / b;
	return ERR;
}
