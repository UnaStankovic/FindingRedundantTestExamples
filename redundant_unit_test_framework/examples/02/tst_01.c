#include "library.h"
#include "test.h"

TST(test_1)
BEGIN
	COMPARE(isPrime(1) == 1);
END

TST(test_2)
BEGIN
	COMPARE(isPrime(2) == 1);
END

TST(test_3)
BEGIN
	COMPARE(isPrime(3) == 1);
END

TST(test_nije_prost)
BEGIN
	COMPARE(isPrime(9) == 0);
END

TST(test_prost)
BEGIN
	COMPARE(isPrime(71) == 1);
END

TEST_CASE_BEGIN
	ADD_TEST(test_1),
        ADD_TEST(test_2),
        ADD_TEST(test_3),
        ADD_TEST(test_nije_prost),
        ADD_TEST(test_prost)
TEST_CASE_END
