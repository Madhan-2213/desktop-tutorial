class demo{
    int length;
    int width;
    int height;
}


public class Main {
    public static void main(String[] args) {
        demo box = new demo();
        System.out.println(box.length = 20);
        System.out.println(box.width = 30);
        System.out.println(box.height = 40);
        int boxs = box.length * box.width * box.height;
        System.out.println(boxs);
    }
}

// output
// 20
// 30
// 40
// 24000
