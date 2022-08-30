public static boolean compute(String word) {
    boolean result = true;

    for (int i = 0, j = word.length() - 1; i < word.length() / 2; i++, j--) {
        if (word.charAt(i) != word.charAt(j)) {
            result = false;
            break;
        }
    }

    return result;
}

// What does the program output if you enter "rentner"?
// a) 7
// b) false
// c) true
// d) rentner