List<Tuple3<String, Integer, Integer>> list = new ArrayList<>();
list.add(new Tuple3<>("a", 1, 2));
list.add(new Tuple3<>("b", 2, 3));
list.add(new Tuple3<>("c", 3, 4));
list.add(new Tuple3<>("d", 4, 5));
list.add(new Tuple3<>("e", 5, 6));
list.add(new Tuple3<>("f", 6, 7));
list.add(new Tuple3<>("g", 7, 8));
list.add(new Tuple3<>("h", 8, 9));
list.add(new Tuple3<>("i", 9, 10));
list.add(new Tuple3<>("j", 10, 11));

list.sort(Comparator.comparingInt(t -> t._2() + t._3()));

list.forEach(System.out::println);