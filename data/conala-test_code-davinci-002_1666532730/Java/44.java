String str = "Hello <<name>>, We have your full name as <<full name>> in our system.";
String name = "Alex Kolenchiskey";
String fullName = "Alex Kolenchiskey";

String str1 = str.replace("<<name>>", name);
String str2 = str1.replace("<<full name>>", fullName);

System.out.println(str2);