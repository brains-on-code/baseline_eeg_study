public static String compute(String input) {
  String s1 = "";
  for(int i = 0; i < input.length(); i++){
    if(i%2 == 1){
      s1 = s1 + input.charAt(i);
    }
  }
  return s1;
}