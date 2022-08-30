public static int compute(String s) {
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