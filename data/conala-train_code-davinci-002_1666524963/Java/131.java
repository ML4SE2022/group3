String json = "{\"name\":\"John\",\"age\":30,\"car\":null}";

JSONObject obj = new JSONObject(json);

String name = obj.getString("name");
int age = obj.getInt("age");

System.out.println(name);
System.out.println(age);