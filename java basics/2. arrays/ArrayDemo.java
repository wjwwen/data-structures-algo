public class ArrayDemo {

    public static void main(String[] args) {

        // Declare an array and initialize it inline
        int[] arr = { 1, 5, 10, 60, 32, 3, 2, -78 };

        // Print out the number of elements in arr
        System.out.println("There are " + arr.length + " items in arr.");

        // Print out the contents of arr
        System.out.println("The [2]'d item in arr is " + arr[2]);
        System.out.print("All the items in arr are: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("");

        // Declare an array and initialize it using new
        int[] arr2 = new int[5];

        // Print out the number of elements in arr2
        System.out.println("\nThere are " + arr2.length + " items in arr2.");

        // Print out the contents of arr2
        System.out.print("All the items in arr2 are: ");
        for (int i = 0; i < arr2.length; i++) {
            System.out.print(arr2[i] + " ");
        }
        System.out.println("");

        // Modify some elements of arr2
        arr2[0] = 105;
        arr2[3] = 56;

        // Print out the contents of arr2 again
        System.out.print("All the items in arr2 are: ");
        for (int i = 0; i < arr2.length; i++) {
            System.out.print(arr2[i] + " ");
        }
        System.out.println("");
    }

}