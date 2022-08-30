public static List<Integer> compute(int a, int b, int c, int d) {
    if (a > b) { int temp = b; b = a; a = temp; }
    if (c > d) { int temp = d; d = c; c = temp; }
    if (a > c) { int temp = c; c = a; a = temp; }
    if (b > d) { int temp = d; d = b; b = temp; }
    if (b > c) { int temp = c; c = b; b = temp; }

    return Arrays.asList(a, b, c, d);
}

// What does the program output if you enter 9, 12, 8, 11?
// a) 40
// b) 12,11,9,8
// c) 10
// d) 8,9,11,12