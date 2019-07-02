// dice.cpp
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <typeinfo>


int roll(double sides) {
  // std::cout << "Input data is: " << sides << std::endl;
  // std::cout << "Input type is: " << typeid(sides).name() << std::endl;

  if(std::cin.fail()) {
    std::cout << "Please enter an integer.\n";
    return -1;
  }
  else if(sides != int(sides)){
    std::cout << "Please enter an integer.\n";
    return -1;
  }
  else if(sides <= 0){
    std::cout << "Please enter an integer greater than 0.\n";
    return -1;
  }
  else {
    int result = rand()%int(sides) + 1;
    return result;
  }
}

// int main() {
//   srand(time(NULL));
//   std::cout << "Please enter the number of sides: ";
//   double sides;
//   std::cin >> sides;
//   std::cout << roll(sides) << "\n";
// }
