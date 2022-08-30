static int compute(int a, int b) {
  int result = a * b;
  for(int i = 1; i < a * b; i++){
    if(i%a + i%b == 0){
      result = i;
      break;
    }
  }
  return result;
}

// What does the program output if you enter 6 and 10?
// a) 60
// b) 30
// c) 0,6
// d) 5
