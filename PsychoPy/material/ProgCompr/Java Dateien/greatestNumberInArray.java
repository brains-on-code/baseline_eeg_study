public static int compute(int[] numbersArray) {
    int result = numbersArray[0];
    for (int i = 1; i < numbersArray.length; i++)
    if (numbersArray[i] > result) {
        result = numbersArray[i];
    }
    return result;
}
