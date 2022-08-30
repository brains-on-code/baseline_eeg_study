public static int compute(String word) {
    char[] letters = {'a', 'e', 'i', 'o', 'u'};
    int result = 0;

    for (int i = 0; i < word.length(); i++) {
        for (int j = 0; j < letters.length; j++) {
            if (word.charAt(i) == letters[j]) {
                result++;
            }
        }
    }

    return result;
}

// What does the program output if you enter<b> "Magdeburg"</b>?
// a) 0
// b) 1
// c) 2
// d) 3
