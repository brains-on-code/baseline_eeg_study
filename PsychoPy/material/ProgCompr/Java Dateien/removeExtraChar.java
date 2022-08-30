public static String compute(String text) {
    String result = "";

    for (int i = 0; i < text.length(); i++) {
        char c = text.charAt(i);
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
            result = result + c;
        }
    }

    return result;
}