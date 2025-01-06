import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int number = scanner.nextInt();

        for (int i = number; i >= 0; i--) {
            if (i % 10 == 0) {
                System.out.println(i);
                break;
            }
        }
    }
}


// output
// Enter the number: 68
// 60
