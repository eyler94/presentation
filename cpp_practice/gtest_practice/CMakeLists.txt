cmake_minimum_required(VERSION 3.4)

# Locate GTest
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

# Link TestDice with what we want to test and the GTest and pthread library
add_executable(TestDice test_dice.cpp)
target_link_libraries(TestDice ${GTEST_LIBRARIES} pthread)
