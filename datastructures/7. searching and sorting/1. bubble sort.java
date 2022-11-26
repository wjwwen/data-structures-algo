public void bubbleSort(int[] a) {
    int n = a.length;
    boolean didSwap = true;
    
    // Keep going until we didn't do any swaps during a pass
    while (didSwap) {
        didSwap = false;
        // Make a pass, swapping pairs if needed.
        for (int i = 0; i < n - 1; i++) {
            if (a[i] < a[i + 1]) {
                didSwap = true;
                swap(a, i, i + 1);
            }
        }
        // The previous loop puts the largest value at the end,
        // so we don't need to check that one again.
        n--;
    }
}