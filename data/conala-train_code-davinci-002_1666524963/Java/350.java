List<List<Integer>> list = new ArrayList<>();
list.add(Arrays.asList(1, 2, 3));
list.add(Arrays.asList(4, 5));
list.add(Arrays.asList(6, 7, 8));

List<List<Integer>> result = new ArrayList<>();
for (List<Integer> l1 : list) {
    for (List<Integer> l2 : list) {
        for (List<Integer> l3 : list) {
            result.add(Arrays.asList(l1.get(0), l2.get(0), l3.get(0)));
            result.add(Arrays.asList(l1.get(0), l2.get(0), l3.get(1)));
            result.add(Arrays.asList(l1.get(0), l2.get(0), l3.get(2)));
            result.add(Arrays.asList(l1.get(0), l2.get(1), l3.get(0)));
            result.add(Arrays.asList(l1.get(0), l2.get(1), l3.get(1)));
            result.add(Arrays.asList(l1.get(0), l2.get(1), l3.get(2)));
            result.add(Arrays.asList(l1.get(1), l2.get(0), l3.get(0)));
            result.add(Arrays.asList(l1.get(1), l2.get(0), l3.get(1)));
            result.add(Arrays.asList(l1.get(1), l2.get(0), l3.get(2)));
            result.add(Arrays.asList(l1.get(1), l2.get(1), l3.get(0)));
            result.add(Arrays.asList(l1.get(1), l2.get(1), l3.get(1)));