String s = "aabbccddeeff";
StringBuilder sb = new StringBuilder();
char last = '\0';
for (char c : s.toCharArray()) {
    if (c != last) {
        sb.append(c);
        last = c;
    }
}
System.out.println(sb.toString());