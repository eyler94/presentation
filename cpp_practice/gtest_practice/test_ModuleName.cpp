#include "ModuleName.cpp"
#include <gtest/gtest.h>

TEST(TestSuiteName0, TestName0) {
  ASSERT_STUFF();
  //....
}

//....

TEST(TestSuiteName0, TestNameN) {
  ASSERT_STUFF();
  //....
}

//....

TEST(TestSuiteNameN, TestName0) {
  ASSERT_STUFF();
  //....
}

//.....

TEST(TestSuiteNameN, TestNameN) {
  ASSERT_STUFF();
  //....
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
