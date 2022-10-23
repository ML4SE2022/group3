String regex = "[a-zA-Z0-9]";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("");
String matchableCharacters = matcher.group();