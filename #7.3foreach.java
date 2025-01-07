import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int arr[] = {5, 6, 7, 4, 3, 2};
        int sum  = 0 ;
        for (int x : arr) {
            sum+=x;
        }
        System.out.println(sum);
    }
}


// output
// 27
