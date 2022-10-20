String regex = "\\b(\\w+)(\\s+\\1)+\\b";
Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
Matcher m = p.matcher(input);
while (m.find()) {
    input = input.replaceAll(m.group(), m.group(1));
}