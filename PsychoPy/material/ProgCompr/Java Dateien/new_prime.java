static boolean compute(int input) {
  Boolean flag = true;
  for(int i = 2; i <= input/2; i++){
    if(input%i== 0){
      flag = false;
    }
  }
  return flag;
}


// What does the program output if you enter 13?
// a) true
// b) 0
// c) false
// d) 1
