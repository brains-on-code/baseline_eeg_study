public static List<Integer> compute(int a, int b, int c) {
    if (a > b) { int temp = b; b = a; a = temp; }
    if (a > c) { int temp = c; c = a; a = temp; }
    if (b > c) { int temp = c; c = b; b = temp; }

    return Arrays.asList(a, b, c);
}