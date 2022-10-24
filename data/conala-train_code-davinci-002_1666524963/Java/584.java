List<String> list1 = new ArrayList<String>();
List<String> list2 = new ArrayList<String>();
List<String> list3 = new ArrayList<String>();

List<Tuple3<String, String, String>> list = new ArrayList<Tuple3<String, String, String>>();
list.add(new Tuple3<String, String, String>("a", "b", "c"));
list.add(new Tuple3<String, String, String>("d", "e", "f"));
list.add(new Tuple3<String, String, String>("g", "h", "i"));

for (Tuple3<String, String, String> tuple : list) {
    list1.add(tuple.getItem1());
    list2.add(tuple.getItem2());
    list3.add(tuple.getItem3());
}