String str = "{\"name\":\"John\",\"age\":30,\"car\":null}";

JSONObject json = new JSONObject(str);

String name = json.getString("name");
int age = json.getInt("age");

System.out.println(name);
System.out.println(age);