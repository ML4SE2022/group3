String regex = "\\d+";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher(string);
if (matcher.find()) {
    System.out.println(matcher.group(0));
}