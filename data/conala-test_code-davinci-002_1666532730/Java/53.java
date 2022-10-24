List<String> list = new ArrayList<String>();
list.add("a");
list.add("b");
list.add("c");
list.add("a");
list.add("b");
list.add("c");
list.add("a");
list.add("b");
list.add("c");

Set<String> set = new HashSet<String>(list);
list.clear();
list.addAll(set);