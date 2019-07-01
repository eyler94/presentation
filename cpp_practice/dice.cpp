// dice.cpp
#include <iostream>

int roll(int sides) {
  if(std::cin.fail()) {
    std::cout << "Failed.";
    return "Please enter an integer.";
  }

  return sides;
}

int main() {
  std::cout << "Please enter the number of sides: ";
  int sides;
  std::cin >> sides;
  std::cout << roll(sides) << "\n";
}
