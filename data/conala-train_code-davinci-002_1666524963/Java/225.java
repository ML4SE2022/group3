String hex = "0123456789ABCDEF";
List<Integer> values = new ArrayList<Integer>();
for (int i = 0; i < hex.length(); i++) {
    char c = hex.charAt(i);
    int d = Character.digit(c, 16);
    values.add(d);
}