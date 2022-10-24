List<List<Integer>> list = new ArrayList<>();

list.add(Arrays.asList(1, 2, 3));
list.add(Arrays.asList(1, 2, 4));
list.add(Arrays.asList(1, 2, 5));

Collections.sort(list, new Comparator<List<Integer>>() {
    @Override
    public int compare(List<Integer> o1, List<Integer> o2) {
        for (int i = 0; i < Math.min(o1.size(), o2.size()); i++) {
            int cmp = Integer.compare(o1.get(i), o2.get(i));
            if (cmp != 0) {
                return cmp;
            }
        }
        return Integer.compare(o1.size(), o2.size());
    }
});

System.out.println(list);