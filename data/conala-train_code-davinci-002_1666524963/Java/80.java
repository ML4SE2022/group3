int index = Collections.binarySearch(list, value);
if (index < 0) {
    index = -index - 1;
}