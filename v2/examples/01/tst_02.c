#include "library.h"
#include "test.h"

TST(test_mnozenje)
BEGIN
	COMPARE(mnozenje(10, 5) == 50)
END

TEST_CASE_BEGIN
	ADD_TEST(test_mnozenje)
TEST_CASE_END
