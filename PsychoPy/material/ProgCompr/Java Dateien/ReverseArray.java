public static void compute(int[] numbersArray) {
    for (int i = 0; i <= numbersArray.length/2 - 1; i++) {
        int tmp = numbersArray[numbersArray.length - i - 1];
        numbersArray[numbersArray.length - i - 1] = numbersArray[i];
        numbersArray[i] = tmp;
    }
    return numbersArray;
}
