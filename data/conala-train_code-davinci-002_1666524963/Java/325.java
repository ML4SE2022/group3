String regex = "(\\d+)";
String string = "12345";
String subst = "$1a";

Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher(string);
String result = matcher.replaceAll(subst);
System.out.println(result);