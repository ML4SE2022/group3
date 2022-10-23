String str = "This is a [test] string.";
Pattern p = Pattern.compile("\\[(.*?)\\]");
Matcher m = p.matcher(str);
while (m.find()) {
    System.out.println(m.group(1));
}