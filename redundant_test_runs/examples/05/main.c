#include<stdio.h>

extern int leap_year(int year);

int main()
{
	int y;
	
	scanf("%d",&y);
	
	if (leap_year(y))
		printf("Year %d is a leap year",y);
	else
		printf("Year %d is not a leap year",y);

	return 0;
}