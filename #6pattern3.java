import java.util.Scanner;

public class Main{

public static void main(String[] args) {
    Scanner se = new Scanner(System.in);
    System.out.println("Enter the range:");
    int N = se.nextInt();
    for(int i=1; i<=N;i++){
        for(int j=1;j<=N;j++){
            if(i==1||i==N||j==1||j==N||j==N-(i+1)||i==j) {
                System.out.print("*");
            }
            else{
                System.out.print(" ");
            }
        }
        System.out.print("\n");
    }
}
    }
