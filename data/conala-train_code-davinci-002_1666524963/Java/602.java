List<Integer> list = new ArrayList<Integer>();
list.add(1);
list.add(2);
list.add(3);
list.add(4);
list.add(5);

list.removeIf(i -> i % 2 == 0);

System.out.println(list);