List<Tuple<String, Integer>> list1 = new ArrayList<>();
list1.add(new Tuple<>("a", 1));
list1.add(new Tuple<>("b", 2));
list1.add(new Tuple<>("c", 3));

List<Tuple<String, Integer>> list2 = new ArrayList<>();
list2.add(new Tuple<>("a", 1));
list2.add(new Tuple<>("b", 2));
list2.add(new Tuple<>("c", 3));

boolean isEqual = list1.equals(list2);