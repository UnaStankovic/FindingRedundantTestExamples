#include <stdio.h>

#define COMPARE(uslov)	if(uslov == 0)  {\
							printf("\tFAIL (%s, %s, line %d)\n", __FILE__, __FUNCTION__, __LINE__);\
							ok = 0;\
						}

#define TST(fja) int fja()

#define BEGIN { int ok = 1; printf("Starting (%s, %s)\n", __FILE__, __FUNCTION__);

#define END return ok; }

#define ADD_TEST(fja) {fja, #fja, __FILE__}

#define TEST_CASE_BEGIN struct test_case tests[] = {

#define TEST_CASE_END }; int test_size = sizeof(tests);

struct test_case {
	int (*function)(void);
	char *name;
	char *file;
};
