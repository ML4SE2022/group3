String str = "Hello World";
int count = 0;
for (int i = 0; i < str.length(); i++) {
    if (str.charAt(i) == 'l') {
        count++;
    }
}
System.out.println(count);