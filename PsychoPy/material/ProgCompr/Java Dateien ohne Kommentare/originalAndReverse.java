public static String compute(String input) {
    String a = "";
    String b = "";
    for(int i = input.length()-1; i >= 0; i--){
      a = input.charAt(i) + a; 
      b = b + input.charAt(i);
    }
    return a + b;
  }