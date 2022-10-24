String value = "00001";
int intValue = Integer.parseInt(value);
intValue++;
String newValue = String.format("%05d", intValue);