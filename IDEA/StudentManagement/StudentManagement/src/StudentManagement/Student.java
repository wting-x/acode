package StudentManagement;

public class Student {
    private String name;//姓名
    private int school_number;//学号
    private int age;//年龄

    Student(String n, int num, int a){
        name = n;
        school_number=num;
        age= a;
    }
    public String getName(){
        return name;
    }
    public int getSchool_number(){
        return school_number;
    }
    public int getAge(){
        return age;
    }
    public void setName(String n){
        name = n;
    }
    public void setSchool_number(int num){
        school_number=num;
    }
    public void setAge(int a) {
        age = a;
    }
}
