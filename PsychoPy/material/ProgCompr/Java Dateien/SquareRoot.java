public static String compute(int[] numbers) {
    double[] result = new double[numbers.length];

    for (int i = 0; i < numbers.length; i++) {
        if (numbers[i] == 0) {
            result[i] = 0;
            continue;
        }

        if (numbers[i] < 0) {
            result[i] = Math.sqrt(-1 * numbers[i]);
        } else {
            result[i] = Math.sqrt(numbers[i]);
        }
    }

    return Arrays.toString(result);
}

// What does the program output if you enter [9, 25, 16, 100]?
// a) [3,4,5,10]
// b) [3,5,4,10]
// c) 35410
// d) [-3,-5,-4,-10]