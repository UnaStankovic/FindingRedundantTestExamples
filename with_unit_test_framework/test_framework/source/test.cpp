#include <string.h>
#include "../include/test.h"

extern struct test_case tests[];
extern int test_size;

int main(int argc, char **argv) {
	if(argc == 2) {
		for(int i = 0; i < test_size/sizeof(struct test_case); i++)
			if(!strcmp(argv[1], tests[i].name)) {
				if(tests[i].function())
					printf("[O] PASS (%s, %s)\n", tests[i].file, tests[i].name);
				else
					printf("[X] FAIL (%s, %s)\n", tests[i].file, tests[i].name);
				break;
			}
	} else
		for(int i = 0; i < test_size/sizeof(struct test_case); i++) {
			if(tests[i].function())
				printf("[O] PASS (%s, %s)\n", tests[i].file, tests[i].name);
			else
				printf("[X] FAIL (%s, %s)\n", tests[i].file, tests[i].name);
			
			printf("\n\n");
		}

	return 0;
}
