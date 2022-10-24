String s = "aabfooaabfooabfoob";
String[] tokens = s.split("a*b");
for (String token: tokens) {
    System.out.println(token);
}