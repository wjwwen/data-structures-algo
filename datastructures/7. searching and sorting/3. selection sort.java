public static void selectionSort(int[] a) {
    int n = a.length;
    for (int i = 0; i < n - 1; i++) {
        int indexOfSmallest = i;
        for (int j = i + 1; j < n; j++)
            if (a[j] < a[indexOfSmallest])
                indexOfSmallest = j;
        swap(a, i, indexOfSmallest);
    }