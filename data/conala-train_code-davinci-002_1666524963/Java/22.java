String text = "aab";
String regexp = "a+";
Pattern pattern = Pattern.compile(regexp);
Matcher matcher = pattern.matcher(text);
while (matcher.find()) {
    System.out.println(matcher.group());
}