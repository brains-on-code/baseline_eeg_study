public static int compute(int number) {
    if (number == 0) {
        return 0;
    }

    return (number % 10) + compute((int) number/10);
}

// What does the program output if you enter 3247?
// a) 16
// b) 3247
// c) 7423
// d) 24