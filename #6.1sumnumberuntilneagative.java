import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int sum = 0;
        Scanner scanner = new Scanner(System.in);
        while (true) {
            int n = scanner.nextInt();
            if(n<0){
                break;
            }
            sum += n;

        }
        System.out.println(sum);
    }
    }

// output:
// 22
// 23
// 23
// 24
// 2334
// -2
// 2426
