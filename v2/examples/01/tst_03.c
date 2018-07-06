#include "library.h"
#include "test.h"

TST(test_deljenje1)
BEGIN
	COMPARE(deljenje(10, 5) == 2);
END

TST(test_deljenje2)
BEGIN
	COMPARE(deljenje(10, 0) == ERR);
END

TEST_CASE_BEGIN
	ADD_TEST(test_deljenje1),
	ADD_TEST(test_deljenje2)
TEST_CASE_END
