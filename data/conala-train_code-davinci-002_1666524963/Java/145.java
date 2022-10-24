int[] numbers = {1, 2, 3, 4, 5};
int[] differences = new int[numbers.length - 1];
for (int i = 0; i < numbers.length - 1; i++) {
    differences[i] = numbers[i + 1] - numbers[i];
}