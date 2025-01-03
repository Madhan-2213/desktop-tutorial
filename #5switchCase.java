import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner se = new Scanner(System.in);
        System.out.println("Enter the Alphabet:");
        char days = se.next().charAt(0);

        switch(Character.toUpperCase(days)){
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                System.out.println("Vowels");
                break;
            default:
                System.out.println("Consonents");
        }
    }

}
