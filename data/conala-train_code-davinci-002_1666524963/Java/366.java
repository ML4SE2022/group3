String[] suffixes = {"a", "b", "c"};
String str = "abc";

for (String suffix : suffixes) {
    if (str.endsWith(suffix)) {
        System.out.println("String ends with " + suffix);
    }
}