List<Integer> list1 = new ArrayList<>();
list1.add(1);
list1.add(2);
list1.add(3);

List<Integer> list2 = new ArrayList<>();
list2.add(4);
list2.add(5);
list2.add(6);

list2.addAll(0, list1);

System.out.println(list2);