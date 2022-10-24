String regex = "\\d+";
String text = "123 456 789";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher(text);
while (matcher.find()) {
    System.out.println(matcher.group());
}