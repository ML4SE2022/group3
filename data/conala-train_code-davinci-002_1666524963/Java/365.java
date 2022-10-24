int[][] array = new int[][] {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

int[] column = new int[array.length];
for (int i = 0; i < array.length; i++) {
    column[i] = array[i][1];
}