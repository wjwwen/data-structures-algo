public static void insertionSort(int[] a) {
    int n = a.length;
    for (int i = 0; i < n; i++) {
        int index = i;
        int valueToInsert = a[index];
        while (index > 0 && valueToInsert < a[index - 1]) {
            a[index] = a[index - 1];
            index--;
        }
        a[index] = valueToInsert;
    }
}