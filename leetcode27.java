import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int[] arr = {3, 2, 2, 3,2,1};
        int count = 0;
        Scanner se = new Scanner(System.in);
        System.out.println("Enter the value to be Removed: ");
        int val  = se.nextInt();
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == val){
                continue;
            }
            else{
                arr[count] = arr[i];
                count++;
            }
        }
        System.out.println(count);
    }
}

// output
// Enter the value to be Removed: 
// 3
// 4
