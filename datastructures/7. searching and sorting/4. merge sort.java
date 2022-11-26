/*  The algorithm works as follows:
Divide the array in half.
Recursively sort both halves.
Merge the halves back together. */

public static void mergeSort(int[] a) {
    if (a.length > 1) {
        int mid = a.length / 2; // first index of right half
        int[] left = new int[mid];
        for (int i = 0; i < left.length; i++) // create left subarray
            left[i] = a[i];
        int[] right = new int[a.length - mid];
        for (int i = 0; i < right.length; i++) // create right subarray
            right[i] = a[mid + i];
        mergeSort(left); // recursively sort the left half
        mergeSort(right); // recursively sort the right half
        merge(left, right, a); // merge the left and right parts back into a whole
    }
}

public static void merge(int[] left, int[] right, int[] arr) {
    int leftIndex = 0;
    int rightIndex = 0;
    for (int i = 0; i < arr.length; i++) {
        if (rightIndex == right.length || (leftIndex < left.length && left[leftIndex] < right[rightIndex])) {
            arr[i] = left[leftIndex];
            leftIndex++;
        } else {
            arr[i] = right[rightIndex];
            rightIndex++;
        }
    }
}