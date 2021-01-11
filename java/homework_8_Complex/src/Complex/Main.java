package Complex;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner input=new Scanner(System.in);//创建一个键盘扫描类对象
    	
    	//输入复数的实部与虚部
    	System.out.println("请输入第一个复数x的实部与虚部：");
    	double x_a=input.nextDouble();
    	double x_b=input.nextDouble();
    	System.out.println("请输入第二个复数y的实部与虚部：");
    	double y_a=input.nextDouble();
    	double y_b=input.nextDouble();
    	//生成复数
    	Complex x=new Complex(x_a,x_b);
    	Complex y=new Complex(y_a,y_b);
    	System.out.println("第一个复数x：x="+x.toString());
    	System.out.println("第二个复数y：y="+y.toString());
    	Complex result=new Complex();
    	
    	//求和x+y
    	result=result.add(x, y);
    	System.out.println("x和y的和为：x+y="+result.toString());
    	//求差x-y
    	result=result.substract(x, y);
    	System.out.println("x和y的差为：x-y="+result.toString());
    	//求积x*y
    	result=result.multiply(x, y);
    	System.out.println("x和y的积为：x*y="+result.toString());
    	//求商x/y
    	result=result.divide(x, y);
    	System.out.println("x和y的商为：x/y="+result.toString());
        //求模|x|
    	System.out.println("x的模为：|x|="+x.abs(x));
    	System.out.println("y的模为：|y|="+y.abs(y));
    	
    	//克隆x
    	try {
	    	Complex z=x.clone();
	    	System.out.println("克隆结果："+z.toString());
    	}
    	catch(CloneNotSupportedException e) {
    	}
    }
}
