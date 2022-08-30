static String compute(String input, int a, int b) {
// initial values: a = 1, b = 0
    if (input.length() > b){
      String result = "";
      for (int i = 0; i < a; i++){
        result = result + input.charAt(b);
      }
      return result + compute(input, a+1, b+1);
    }
    return "";
  }

// What does the program output if you enter "fast" with the initial values: a = 1 and b = 0? 
// a) tsaf
// b) faassstttt
// c) fast
// d) fastfastfast