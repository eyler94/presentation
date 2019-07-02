// dice.cpp
#include <iostream>
#include <stdlib.h>
#include <time.h>


int roll(double sides) {
  if(std::cin.fail()) {
    std::cout << "Please enter an integer.\n";
  }
  else if(sides != int(sides)){
    std::cout << "Please enter an integer.\n";
  }
  else if(sides <= 0){
    std::cout << "Please enter an integer greater than 0.\n";
  }
  else {
    srand(time(NULL));
    std::cout << rand()%int(sides) + 1 << "\n";
  }
}

int main() {
  std::cout << "Please enter the number of sides: ";
  double sides;
  std::cin >> sides;
  roll(sides);
}
