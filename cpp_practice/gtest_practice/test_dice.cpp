#include "dice.cpp"
#include <gtest/gtest.h>
#include <iostream>
#include <string>
#include <stdlib.h>

TEST(DiceTest, Range) {
  srand(time(NULL));
  for(int i=0;i<100;i++){
    int result=0;
    result = roll(20);
    ASSERT_LE(result,20);
    ASSERT_GT(result,0);
  }
}

TEST(DiceTest, Input) {
  ASSERT_EQ(-1,roll(0));
  ASSERT_EQ(-1,roll(-1));
}

TEST(DiceTest, Types) {
  ASSERT_EQ(-1,roll(5.4));
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
