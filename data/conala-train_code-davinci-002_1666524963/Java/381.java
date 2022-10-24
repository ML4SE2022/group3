List<Integer> list1 = Arrays.asList(1, 2, 3);
List<Integer> list2 = Arrays.asList(4, 5, 6);
List<Integer> list3 = new ArrayList<>();

for (int i = 0; i < list1.size(); i++) {
    list3.add(list1.get(i) + list2.get(i));
}

System.out.println(list3);