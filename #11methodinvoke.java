class box{
    int length;
    int breadth;
    int height;


     int  volume(){
        return length*breadth*height;
    }

}

public class Main{
    public static void main(String[] args) {
        box blackbox = new box();
        box woodbox = new box();
        blackbox.length = 20;
        blackbox.breadth = 30;
        blackbox.height = 40;

        woodbox.length = 20;
        woodbox.breadth = 30;
        woodbox.height = 10;
        int v = blackbox.volume(); //invoke method
        System.out.println(v);
        int vr = woodbox.volume();
        System.out.println(vr);

    }
}

// output:
// 24000
// 6000
