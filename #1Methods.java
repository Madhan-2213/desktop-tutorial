class box{
    int length;
    int breadth;
    int height;
}

public class Main {
    public static void main(String[] args) {
        box blackbox = new box();
        blackbox.length = 21;
        blackbox.height = 31;
        blackbox.breadth = 22;
        System.out.println(blackbox.length);
        System.out.println(blackbox.breadth);

    }
}
