public static double[] mean(double[][] x) {
    double[] mean = new double[x[0].length];
    for (int i = 0; i < x.length; i++) {
        for (int j = 0; j < x[0].length; j++) {
            mean[j] += x[i][j];
        }
    }
    for (int i = 0; i < mean.length; i++) {
        mean[i] /= x.length;
    }
    return mean;
}