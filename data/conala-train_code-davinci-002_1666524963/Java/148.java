List<String> list = new ArrayList<>();
list.add("abc");
list.add("def");
list.add("ghi");
list.add("jkl");

List<String> subList = new ArrayList<>();
subList.add("abc");
subList.add("jkl");

list.removeAll(subList);