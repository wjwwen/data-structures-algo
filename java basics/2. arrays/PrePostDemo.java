public class PrePostDemo {

    public static void main(String[] args) {
        int a = 10;
        int b = 10;

        int c = 7 + a++; // line 7
        int d = 7 + ++b; // line 8

        System.out.println("a is " + a);
        System.out.println("b is " + b);
        System.out.println("c is " + c);
        System.out.println("d is " + d);
    }
}