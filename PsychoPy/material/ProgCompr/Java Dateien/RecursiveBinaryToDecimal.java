static int compute(String s) {
    if(s.equals("0")){
      return 0;
    }
    if(s.equals("1")){
      return 1;
    }
    if (s.charAt(s.length()-1) == '0'){
        return 2 * compute(s.substring(0,s.length()-1));
    }
    if (s.charAt(s.length()-1) == '1'){
        return 1 + 2 * compute(s.substring(0,s.length()-1));
    }
    return -1;
  }
}

// original version: 
/*
static int compute(String s, int number) {
    if (number < 0) {
        return 0;
    }

    if (s.charAt(number) == '0'){
        return 2 * compute(s, number - 1);
    }

    return 1 + 2 * compute(s, number - 1);
}
*/

// modified to eliminate variable "number"

// What does the program output if you enter 101?
// a) 5
// b) 7 
// c) 1
// d) 0