public String compute(String word1, String word2) {
    String result = "";

    if (word1.length() == word2.length()) {
        for (int i = 0; i < word1.length(); i++) {
            result = result + word1.charAt(i) + word2.charAt(i);
        }
    }

    return result;
}
