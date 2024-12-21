public class TestVSCode {
    public static void main(String[] args) {
        // Print a welcome message
        System.out.println("Hello, VS Code!");
        
        // Perform a simple calculation
        int a = 5;
        int b = 10;
        int sum = a + b;
        System.out.println("The sum of " + a + " and " + b + " is: " + sum);

        // Check if a number is even or odd
        int number = 7;
        if (number % 2 == 0) {
            System.out.println(number + " is even.");
        } else {
            System.out.println(number + " is odd.");
        }

        // Print the first 5 numbers in the Fibonacci sequence
        System.out.println("Fibonacci sequence:");
        int n1 = 0, n2 = 1, n3, count = 5;
        System.out.print(n1 + " " + n2);
        for (int i = 2; i < count; ++i) {
            n3 = n1 + n2;
            System.out.print(" " + n3);
            n1 = n2;
            n2 = n3;
        }
        System.out.println("\nTest complete!");
    }
}
