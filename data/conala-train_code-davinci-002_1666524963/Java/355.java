Arrays.sort(arr, (a, b) -> {
    if (a.equals(b)) {
        return 0;
    }
    if (a.length() == b.length()) {
        return a.compareTo(b);
    }
    return a.length() - b.length();
});