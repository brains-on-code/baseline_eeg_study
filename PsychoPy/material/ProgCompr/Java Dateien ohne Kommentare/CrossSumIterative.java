public static int compute(int number) {
    int result = 0;

    while (number != 0) {
        result += number % 10;
        number /= 10;
    }

    return result;
}
