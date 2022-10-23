public static void main(String[] args) {
    int n = 3;
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
        arr[i] = 0;
    }
    print(arr);
    while (increment(arr)) {
        print(arr);
    }
}

private static boolean increment(int[] arr) {
    int i = arr.length - 1;
    while (i >= 0) {
        if (arr[i] == 0) {
            arr[i] = 1;
            return true;
        } else {
            arr[i] = 0;
            i--;
        }
    }
    return false;
}

private static void print(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        System.out.print(arr[i]);
    }
    System.out.println();
}