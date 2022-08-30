public static int compute(int value) {
    if (value == 1) {
        return 1;
    }

    return compute(value - 1) * value;
}

// What does the program output if you enter 4?
// a) 24
// b) 16
// c) 8
// d) 12