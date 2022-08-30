static String compute(String input) {
  String s0 = "";
  String s1 = "";
  for(int i = 0; i < input.length(); i++){
    if(i%2 == 0){
      s0 = s0 + input.charAt(i);
    }else{
      s1 = s1 + input.charAt(i);
    }
  }
  return s1;
}


// What does the program output if you enter powerful?
// a) pwru
// b) oefl
// c) lufrewop
// d) p o w e r f u l