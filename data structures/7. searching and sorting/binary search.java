public static int binarySearch(int[] a, int value) {
    int lowIndex = 0;
    int highIndex = a.length - 1;
    while (lowIndex <= highIndex) {
        int midIndex = (lowIndex + highIndex) / 2;
        if (value < a[midIndex])
            highIndex = midIndex - 1;
        else if (value > a[midIndex])
            lowIndex = midIndex + 1;
        else // found it!
            return midIndex;
    }
    return -1; // The value doesn't exist
}

// Array must already be sorted.