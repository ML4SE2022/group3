int sum = 0;
for (List<List<Integer>> listOfLists : listOfListsOfLists) {
    for (List<Integer> list : listOfLists) {
        sum += list.get(1);
    }
}