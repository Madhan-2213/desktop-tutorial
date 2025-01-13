class pizza{
    int rating;
    int cs_rating;
    int food_taste;
    public pizza(int r,int cs,int ft) {
        this.rating = r;
        this.cs_rating = cs;
        this.food_taste = ft;
    }
     void display(){
            System.out.println("Rating: "+rating);
            System.out.println("Customer Service Rating: "+cs_rating);
            System.out.println("Food Taste Rating: "+food_taste);
        }
    }



public class Main{
    public static void main(String[] args) {
        pizza p = new pizza(4,5,3);

        p.display();
    }
}
