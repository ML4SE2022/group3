String sentence = "This is a sentence";
String[] words = sentence.split(" ");
int[] lengths = new int[words.length];
for (int i = 0; i < words.length; i++) {
    lengths[i] = words[i].length();
}