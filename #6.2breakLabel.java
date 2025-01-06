import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number:");
        int number = scanner.nextInt();
        outerlabel:
        for (int i = 1; i <= number; i++) {
            innerlabel:
            for (int j = 1; j <= number; j++) {
                    System.out.print("*");
                if (i == 3 && j == 3) {
                    break outerlabel;
                }
            }
                System.out.print("\n");
            }
        }
    }


// output
// Enter the number:
// 5
// *****
// *****
// ***
