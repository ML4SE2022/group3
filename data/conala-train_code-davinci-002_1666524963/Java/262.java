public static void main(String[] args) {
    String word = "hello";
    int count = 0;
    for (int i = 0; i < word.length() - 1; i++) {
        if (isConsonant(word.charAt(i)) && isConsonant(word.charAt(i + 1))) {
            count++;
        }
    }
    System.out.println(count);
}

public static boolean isConsonant(char c) {
    return !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}