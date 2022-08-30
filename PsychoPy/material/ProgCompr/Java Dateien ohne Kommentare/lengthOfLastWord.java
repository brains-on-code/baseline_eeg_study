public static int compute(String text) {
    int result = 0;
    for (int i = text.length() - 1; i >= 0; i--) {
        char c = text.charAt(i);
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
            result++;
        } else {
            break;
        }
    }
    return result;
}