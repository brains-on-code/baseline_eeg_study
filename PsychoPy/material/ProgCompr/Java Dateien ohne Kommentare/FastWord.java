public static String compute(String input, int x) {
// initial values: x = 0
    if (input.length() > x){
      String result = "";
      for (int i = 0; i <= x; i++){
        result = result + input.charAt(x);
      }
      return result + compute(input, x+1);
    }
    return "";
}