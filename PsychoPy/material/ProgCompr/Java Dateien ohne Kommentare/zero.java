public static int compute(int number) {
   if (number <= 2) {
       return 0;
   }
   return compute(number - 1) * compute(number - 2);
}