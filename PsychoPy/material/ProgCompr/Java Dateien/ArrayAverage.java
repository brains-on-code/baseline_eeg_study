public static float compute(int[] numbers) {
    int number1 = 0;
    int number2 = 0;

    while (number1 < numbers.length) {
        number2 = number2 + numbers[number1];
        number1 = number1 + 1;
    }

    float result = number2 / (float) number1;
    return result;
}

// What does the program output if you enter {2, 4, 1, 9}?
// a) 4
// b) 16
// c) 2
// d) 5