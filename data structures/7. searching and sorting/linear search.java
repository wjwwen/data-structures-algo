public static int linearSearch(int[] a, int value) {
    int n = a.length;
    for (int i = 0; i < n; i++) {
        if (a[i] == value)
            return i;
    }
    return -1;
}