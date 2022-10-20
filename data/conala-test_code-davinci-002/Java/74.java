int[][] matrix = new int[list1.size()][list2.size()];
for (int i = 0; i < list1.size(); i++) {
    for (int j = 0; j < list2.size(); j++) {
        matrix[i][j] = list1.get(i) * list2.get(j);
    }
}