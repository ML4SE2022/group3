int max = Integer.MIN_VALUE;
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[0].length; j++) {
        max = Math.max(max, matrix[i][j]);
    }
}