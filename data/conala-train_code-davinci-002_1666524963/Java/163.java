int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int[] arr2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

for (int i = 0; i < arr.length; i++) {
    for (int j = 0; j < arr2.length; j++) {
        if (arr[i] == arr2[j]) {
            System.out.println(i + " " + j);
        }
    }
}