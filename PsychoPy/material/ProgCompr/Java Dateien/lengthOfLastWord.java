public static int compute(String text) {
    int result = 0;

    boolean flag = false;
    for (int i = text.length() - 1; i >= 0; i--) {
        char c = text.charAt(i);
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
            flag = true;
            result++;
        } else {
            if (flag)
                break;
        }
    }

    return result;
}

// What does the program output if you enter "The quick brown fox jumps"?
// a) 5
// b) 10
// c) 15
// d) jumps