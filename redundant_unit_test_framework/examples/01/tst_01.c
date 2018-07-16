#include "library.h"
#include "test.h"

TST(test_sabiranje)
BEGIN
	COMPARE(sabiranje(10, 5) == 15);
END

TST(test_oduzimanje)
BEGIN
	COMPARE(oduzimanje(10, -5) == 15);
END

TST(test_deljenje_nulom)
BEGIN
	COMPARE(deljenje(5, 0) == ERR);
END

TEST_CASE_BEGIN
	ADD_TEST(test_sabiranje),
	ADD_TEST(test_oduzimanje),
	ADD_TEST(test_deljenje_nulom)
TEST_CASE_END
