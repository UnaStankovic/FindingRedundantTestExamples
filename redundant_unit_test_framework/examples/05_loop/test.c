#include "fibonaci.h"
#include "test.h"

TST(test_0)
BEGIN
	COMPARE(fibonaci(0) == 0);
END

TST(test_1)
BEGIN
	COMPARE(fibonaci(1) == 1);
END

TST(test_5)
BEGIN
	COMPARE(fibonaci(5) == 5);
END

TST(test_10)
BEGIN
	COMPARE(fibonaci(10) == 55);
END

TEST_CASE_BEGIN
	ADD_TEST(test_0),
	ADD_TEST(test_1),
	ADD_TEST(test_5),
	ADD_TEST(test_10)
TEST_CASE_END
