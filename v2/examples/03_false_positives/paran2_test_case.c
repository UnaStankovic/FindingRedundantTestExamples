#include "library.h"
#include "test.h"

TST(test_neparan)
BEGIN
	COMPARE(paran2(11) == 0);
END

TST(test_paran)
BEGIN
	COMPARE(paran2(16) == 1);
END

TEST_CASE_BEGIN
	ADD_TEST(test_neparan),
        ADD_TEST(test_paran)
TEST_CASE_END
