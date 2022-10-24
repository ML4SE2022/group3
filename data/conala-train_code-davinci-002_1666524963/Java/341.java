String[] list = {"a", "b", "c"};
String[] newList = new String[list.length + 1];
System.arraycopy(list, 0, newList, 0, list.length);
newList[list.length] = "d";