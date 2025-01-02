import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner se  = new Scanner(System.in);
        System.out.println("Enter your Name: ");
        String name = se.nextLine();
        System.out.println("Enter your password: ");
        int password = se.nextInt();
        se.nextLine();
        System.out.println("Enter the email: ");
        String email = se.nextLine();

        System.out.println(name);
        System.out.println(password);
        System.out.println(email);



    }
}
