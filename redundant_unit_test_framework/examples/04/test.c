#include "library.h"
#include "test.h"

TST(test_com1)
BEGIN
	COMPARE(select_command("command1") == "execute command1");
END

TST(test_com2)
BEGIN
	COMPARE(select_command("command2") == "execute command2");
END

TST(test_com3)
BEGIN
	COMPARE(select_command("command3") == "execute command3");
END

TST(test_unknown)
BEGIN
	COMPARE(select_command("unknown") == "unknown command");
END

TEST_CASE_BEGIN
	ADD_TEST(test_com1),
	ADD_TEST(test_com2),
	ADD_TEST(test_com3),
	ADD_TEST(test_unknown)
TEST_CASE_END
