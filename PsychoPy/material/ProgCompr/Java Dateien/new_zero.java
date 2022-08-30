public static int compute(int number) {
   if (number <= 2) {
       return 0;
   }
   return compute(number - 1) * compute(number - 2);
}

// What does the program output if you enter 15?
// a) 2
// b) 1
// c) 0
// d) 150