String str = "This is a test. This is, too.";
String word = "is";
int pos = str.indexOf(word);
int start = str.lastIndexOf(" ", pos);
int end = str.indexOf(" ", pos);
if (start == -1) {
    start = 0;
}
if (end == -1) {
    end = str.length();
}
String sentence = str.substring(start, end);
System.out.println(sentence);