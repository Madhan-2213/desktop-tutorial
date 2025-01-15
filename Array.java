import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int arr[] = new int[6];
        Scanner se = new Scanner(System.in);
        System.out.println("Enter the number: ");
        for(int i = 0 ; i< arr.length ; i++) {
            arr[i] = se.nextInt();
        }
        for(int i = 0 ; i<arr.length;i++){
            System.out.println(arr[i]);
        }

    }
}


// output
// Enter the number: 
// 5
// 2
// 3
// 4
// 5
// 6
  
// 5
// 2
// 3
// 4
// 5
// 6
