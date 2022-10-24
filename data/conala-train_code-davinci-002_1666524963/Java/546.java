public static double[] removeNan(double[] array) {
    List<Double> list = new ArrayList<>();
    for (double d : array) {
        if (!Double.isNaN(d)) {
            list.add(d);
        }
    }
    double[] result = new double[list.size()];
    for (int i = 0; i < list.size(); i++) {
        result[i] = list.get(i);
    }
    return result;
}