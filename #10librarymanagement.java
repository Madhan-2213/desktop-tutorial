

class User{
    String UserName;
    int id;
    String email;
}
class Book{
    String Author;
    int bookId;
    String bookName;
}



public class Main{
    public static void main(String[] args) {
        User m = new User();
        System.out.println(m.UserName = "Madhan");
        System.out.println(m.id = 27);
        System.out.println(m.email = "madhan20m@gmail.com");


        Book b = new Book();
        System.out.println(b.Author = "Hardy");
        System.out.println(b.bookId  = 2132);
        System.out.println(b.bookName = "Wonderland");
    }
}

// output:
// Madhan
// 27
// madhan20m@gmail.com
// Hardy
// 2132
// Wonderland
