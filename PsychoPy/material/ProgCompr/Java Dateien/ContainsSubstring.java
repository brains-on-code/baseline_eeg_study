public static boolean compute(String word1, String word2) {
    boolean result = false;

    for (int i = 0; i < word1.length(); i++) {
        for (int j = 0; j < word2.length(); j++) {
            if (i + j >= word1.length())
                break;
            if (word1.charAt(i + j) != word2.charAt(j)) {
                break;
            } else {
                if (j == word2.length() - 1) {
                    result = true;
                    break;
                }
            }
        }
    }

    return result;
}

// What does the program output if you enter<b> "Hamburg"</b> and <b> "burg"</b>?
// a) false
// b) burgHamburg
// c) grubmaHburg
// d) true