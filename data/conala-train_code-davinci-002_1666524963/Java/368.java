public static int sumOfProductOfCombinations(List<Integer> list) {
    int sum = 0;
    for (int i = 0; i < list.size(); i++) {
        for (int j = i + 1; j < list.size(); j++) {
            sum += list.get(i) * list.get(j);
        }
    }
    return sum;
}