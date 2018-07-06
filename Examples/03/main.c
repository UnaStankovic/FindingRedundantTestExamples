#include<stdio.h>

extern int f(int c);
extern int g(int c);

int main()
{
	int c;
	
	scanf("%d",&c);
	
	f(c);
	
	g(c);
	
	//f(c);

	return 0;
}