
int f(int c)
{
	int a = 4;
	int b = 5;
	return a+b+c;
}

int g(int c)
{
	int a = 3;
	if (c > 4)
		a = a + c;
	if (c > 14)
		a = a + 2 * c;
	
	if (c < 0)
		a--;
	else
		a++;
	
	return a;	
}