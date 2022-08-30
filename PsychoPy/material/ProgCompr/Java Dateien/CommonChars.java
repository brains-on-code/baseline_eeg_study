public static int compute(String string1, String string2) {
    int x;
    if (string1.length() < string2.length()) {
        x = string1.length();
    } else {
        x = string2.length();
    }
    int result = 0;
    for (int i = 0; i < x; i++) {
        if (string1.charAt(i) == string2.charAt(i)) {
            result++;
        }
    }
    return result;
}
