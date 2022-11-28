public class ForLoopExample {

    public static void main(String[] args) {
        // Print out all the numbers from [0,10)

        /*
         * The loop below can be thought of as follows:
         * 1. Before the loop runs, a new integer i is created and set to 0.
         * 2. The code inside the loop (in this case the print statement) runs once.
         * 3. The conditional check (i < 10) runs. If the conditional returns false
         * (meaning that i >= 10), then the loop stops. Otherwise, it continues.
         * 4. The incrementor (i++) runs and changes the value of i.
         * 5. Go back to step 2.
         */
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }
    }

}