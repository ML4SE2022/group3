public static int convert(List<Integer> numbers) {
    StringBuilder sb = new StringBuilder();
    for (int number : numbers) {
        sb.append(number);
    }
    return Integer.parseInt(sb.toString());
}