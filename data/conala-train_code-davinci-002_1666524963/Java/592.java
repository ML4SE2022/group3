public static double magnitudeSquared(double[] vector) {
    double sum = 0;
    for (int i = 0; i < vector.length; i++) {
        sum += vector[i] * vector[i];
    }
    return sum;
}