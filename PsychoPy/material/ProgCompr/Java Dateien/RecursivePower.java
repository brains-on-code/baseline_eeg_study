static int compute(int a, int b) {
    if (b == 0) {
        return 1;
    }

    if (b == 1) {
        return a;
    }

    return a * compute(a, b - 1);
// original version:    return (a + 1) * compute(a, b - 1);
}

//modification to match the definition of recursive power calculation

// What does the program output if you enter a = 3 and b = 2?
// a) 1
// b) 6
// c) 8
// d) 9