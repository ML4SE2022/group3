List<List<List<Integer>>> list = new ArrayList<>();

List<List<Integer>> list1 = new ArrayList<>();
List<Integer> list11 = new ArrayList<>();
list11.add(1);
list11.add(2);
list11.add(3);
list1.add(list11);

List<Integer> list12 = new ArrayList<>();
list12.add(4);
list12.add(5);
list12.add(6);
list1.add(list12);

list.add(list1);

List<List<Integer>> list2 = new ArrayList<>();
List<Integer> list21 = new ArrayList<>();
list21.add(7);
list21.add(8);
list21.add(9);
list2.add(list21);

List<Integer> list22 = new ArrayList<>();
list22.add(10);
list22.add(11);
list22.add(12);
list2.add(list22);

list.add(list2);

for (List<List<Integer>> l : list) {
    for (List<Integer> l1 : l) {
        for (Integer i : l1) {
            System.out.println(i);
        }
    }
}