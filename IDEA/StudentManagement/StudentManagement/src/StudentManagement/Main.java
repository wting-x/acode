package StudentManagement;

import java.util.Scanner;
import java.util.ArrayList;

/*
* 解决学号不存在问题
* 解决学号重复问题
* */

public class Main {
    public static void show() {
        System.out.println("----------欢迎来到学生管理系统----------");
        System.out.println("1 添加学生");
        System.out.println("2 删除学生");
        System.out.println("3 修改学生");
        System.out.println("4 查看所有学生");
        System.out.println("5 退出");
        System.out.println("请输入您的选择：");
    }

    public static void add(ArrayList<Student> stus) {
        Scanner input = new Scanner(System.in);
        System.out.println("请输入姓名：");
        String name = input.nextLine();
        System.out.println("请输入年龄：");
        int age = input.nextInt();
        Student stu = new Student(name, age);
        stus.add(stu);
        System.out.println("操作成功！！！");
    }

    public static void delete(ArrayList<Student> stus) {
        System.out.println("请输入要删除的学生学号：");

        Scanner input = new Scanner(System.in);
        int num=input.nextInt();
        int index=0;
        for(index=0;index<stus.size();index++){
            if(num==stus.get(index).getAge())
                break;
        }
        stus.remove(index);

        System.out.println("操作成功！！！");
    }

    public static void change(ArrayList<Student> stus) {
        Scanner input = new Scanner(System.in);

        System.out.println("请输入要修改的学生学号：");
        int num=input.nextInt();

        int index=0;
        for(index=0;index<stus.size();index++){
            if(num==stus.get(index).getAge())
                break;
        }

        System.out.println("请输入修改后的姓名：");
        String name= input.next();

        Student s=new Student(name,num);
        stus.set(index,s);

        System.out.println("操作成功！！！");
    }

    public static void all(ArrayList<Student> stus) {
        if(stus.size()!=0){
            System.out.println("序号\t\t\t姓名\t学号");
            for(int i=0;i<stus.size();i++){
                System.out.println("第"+(i+1)+"位同学：\t"+stus.get(i).getName()+"\t"+stus.get(i).getAge());
            }
            System.out.println("全部学生信息显示完毕！！！");
        }
        else
            System.out.println("当前无学生信息！！！");
    }

    public static void main(String[] args) {
        ArrayList<Student> stus = new ArrayList<>();

        show();
        Scanner in = new Scanner(System.in);
        int option = in.nextInt();

        while (option != 5) {
            switch (option) {
                case 1:
                    add(stus);
                    break;
                case 2:
                    delete(stus);
                    break;
                case 3:
                    change(stus);
                    break;
                case 4:
                    all(stus);
                    break;
                default:
                    System.out.println("输入的选项错误！！！");
                    break;
            }
            System.out.println("请输入您下一步的选择：");
            option = in.nextInt();
        }
        System.out.println("已退出！！！");
    }
}
