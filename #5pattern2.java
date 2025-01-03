import java.util.Scanner;

public class Main{

public static void main(String[] args) {
    Scanner se  =  new Scanner(System.in);
    int N = se.nextInt();
    for(int i=1;i<=N;i++){
        for(int j = 1;j<=N;j++){
            if(i==1 || i==N || j==1||j==N){
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



// output:
// 5
// *****
// *   *
// *   *
// *   *
// *****
