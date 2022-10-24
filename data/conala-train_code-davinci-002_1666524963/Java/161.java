Random rand = new Random();
int[][] matrix = new int[10][10];
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        matrix[i][j] = rand.nextInt(100);
    }
}