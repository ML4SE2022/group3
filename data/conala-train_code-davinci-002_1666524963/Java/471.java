public static double average(List<Integer> list) {
    double sum = 0;
    for (int i = 0; i < list.size(); i++) {
        sum += list.get(i);
    }
    return sum / list.size();
}