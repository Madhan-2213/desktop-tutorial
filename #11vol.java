public class Main{

    static int boxes(int length,int breadth,int height){
        int vol = length*breadth*height;
        return vol;
    }


    public static void main(String[] args) {
        int vol = boxes(20,30,40);
        System.out.println(vol);
    }
}

// output:
// 240000
