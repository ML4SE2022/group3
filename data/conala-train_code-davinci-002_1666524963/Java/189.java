List<Integer> list = new ArrayList<>();
list.add(1);
list.add(2);
list.add(null);
list.add(0);
list.removeAll(Collections.singleton(null));
System.out.println(list);