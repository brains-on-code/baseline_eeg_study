public static int compute(int a, int b) {
  int result = a * b;
  for(int i = 1; i < a * b; i++){
    if(i%a == 0 && i%b == 0){
      result = i;
      break;
    }
  }
  return result;
}