static Boolean compute(String input) {
    input = input.toLowerCase();

    if (input.contentEquals("n")) {
        return false;
    } else if (input.contentEquals("no")) {
        return false;
    }

    if (input.contentEquals("y")) {
        return true;
    } else if (input.contentEquals("yes")) {
        return true;
    }

    return null;
}

// What does the program output if you enter "Yes"?
// a) yes
// b) null
// c) false
// d) true