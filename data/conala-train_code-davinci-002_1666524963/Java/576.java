String str = "1,,3,4,5";
String[] strArr = str.split(",");
StringBuilder sb = new StringBuilder();
for (String s : strArr) {
    if (s.isEmpty()) {
        sb.append("0,");
    } else {
        sb.append(s).append(",");
    }
}
System.out.println(sb.toString());