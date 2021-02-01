package StudentManagement;

public class Student {
    private String name;//姓名
    private int age;//学号

    Student(String n, int a){
        name = n;
        age= a;
    }
    public String getName(){
        return name;
    }
    public int getAge(){
        return age;
    }
    public void setName(String n){
        name = n;
    }

    public void setAge(int a) {
        age = a;
    }
}
