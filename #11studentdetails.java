class Students{
    String Name;
    int roll_no;
    int[] marks;

    public Students(String Name, int roll_no, int[] marks) {
        this.Name = Name;
        this.roll_no = roll_no;
        this.marks  = marks;
    }


    void marksTotal(){
        System.out.println("Name "+Name);
        System.out.println("roll no "+roll_no);
        for(int marks:marks){
            System.out.println("Marks "+marks);
        }
        System.out.println();
    }

}

public class Main{
    public static void main(String[] args) {
        int[] mark1 = {98,99,100};
        int[] mark2 = {97,96,94};
        Students s1 = new Students("Madhan",27,mark1);
        Students s2 = new Students("Alice",1,mark2);

        s1.marksTotal();
        s2.marksTotal();
    }
}

// output:
// Name Madhan
// roll no 27
// Marks 98
// Marks 99
// Marks 100

// Name Alice
// roll no 1
// Marks 97
// Marks 96
// Marks 94
