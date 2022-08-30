public static void main() {
    int number = 4;
    System.out.print(compute(number));
}

public static int compute(int number) {
    if (number <= 2) {
// orginal version: if (number <= 1){
        return 1;
    }

    return compute(number - 1) + compute(number - 2);
// original version: return compute(number - 2) + compute(number - 4);
}

//modification to match the definition of fibonacci numbers

// What does the program output if you enter 4?
// a) 0
// b) 1
// c) 2
// d) 3