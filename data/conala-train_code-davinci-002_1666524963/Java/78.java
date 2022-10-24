StringBuilder sb = new StringBuilder();
for (byte b : bytes) {
    sb.append(String.format("%02X ", b));
}
System.out.println(sb.toString());