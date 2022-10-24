String s = "a\nb";
Pattern p = Pattern.compile("(.*?)b", Pattern.DOTALL);
Matcher m = p.matcher(s);
m.find();
System.out.println(m.group(1));