// Program to print a text 5 times

class Main {
    public static void main(String[] args) {

        int n = 5;
        // for loop
        for (int i = 1; i <= n; ++i) {
            System.out.println("Java is fun");
        }
    }
}

// Program to print numbers from 1 to 5

class Main {
    public static void main(String[] args) {

        int n = 5;
        // for loop
        for (int i = 1; i <= n; ++i) {
            System.out.println(i);
        }
    }
}

// Program to find the sum of natural numbers from 1 to 1000.

class Main {
    public static void main(String[] args) {

        int sum = 0;
        int n = 1000;

        // for loop
        for (int i = 1; i <= n; ++i) {
            // body inside for loop
            sum += i; // sum = sum + i
        }

        System.out.println("Sum = " + sum);
    }
}

// Program to find the sum of natural numbers from 1 to 1000.

class Main {
    public static void main(String[] args) {

        int sum = 0;
        int n = 1000;

        // for loop
        for (int i = n; i >= 1; --i) {
            // body inside for loop
            sum += i; // sum = sum + i
        }

        System.out.println("Sum = " + sum);
    }
}

// print array elements

class Main {
    public static void main(String[] args) {

        // create an array
        int[] numbers = { 3, 7, 5, -5 };

        // iterating through the array
        for (int number : numbers) {
            System.out.println(number);
        }
    }
}