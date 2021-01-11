package ComparableCircle;
import java.util.Scanner;

public class Main {
	public static void main(String[] args)throws Exception{
		@SuppressWarnings("resource")
		Scanner input=new Scanner(System.in);		//创建一个键盘扫描类对象
		
		System.out.println("请输入circle1的半径：");
		double a=input.nextDouble();		//输入circle1半径
		System.out.println("请输入circle2的半径：");
		double b=input.nextDouble();		//输入circle2半径
		
		//初始化circle1、circle2半径分别为a,b
		ComparableCircle circle1=new ComparableCircle(a);
		ComparableCircle circle2=new ComparableCircle(b);
		
		//克隆circle1
    	ComparableCircle circle3=circle1.clone();
    	System.out.println("circle1克隆成功，克隆结果为circle3");
    	
		//比较circle1与circle2是否相等
		System.out.println("circle1与circle2相等。\t"+circle1.equals(circle2));
		
    	//分别比较circle1、circle2与circle3是否相等
    	System.out.println("circle1与circle3相等。\t"+circle1.equals(circle3));
    	System.out.println("circle2与circle3相等。\t"+circle2.equals(circle3));
	}
}
