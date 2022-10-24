List<List<Integer>> subLists = new ArrayList<>();
for (int i = 0; i < list.size(); i += 2) {
    subLists.add(list.subList(i, Math.min(i + 2, list.size())));
}