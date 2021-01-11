package Complex;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner input=new Scanner(System.in);//����һ������ɨ�������
    	
    	//���븴����ʵ�����鲿
    	System.out.println("�������һ������x��ʵ�����鲿��");
    	double x_a=input.nextDouble();
    	double x_b=input.nextDouble();
    	System.out.println("������ڶ�������y��ʵ�����鲿��");
    	double y_a=input.nextDouble();
    	double y_b=input.nextDouble();
    	//���ɸ���
    	Complex x=new Complex(x_a,x_b);
    	Complex y=new Complex(y_a,y_b);
    	System.out.println("��һ������x��x="+x.toString());
    	System.out.println("�ڶ�������y��y="+y.toString());
    	Complex result=new Complex();
    	
    	//���x+y
    	result=result.add(x, y);
    	System.out.println("x��y�ĺ�Ϊ��x+y="+result.toString());
    	//���x-y
    	result=result.substract(x, y);
    	System.out.println("x��y�Ĳ�Ϊ��x-y="+result.toString());
    	//���x*y
    	result=result.multiply(x, y);
    	System.out.println("x��y�Ļ�Ϊ��x*y="+result.toString());
    	//����x/y
    	result=result.divide(x, y);
    	System.out.println("x��y����Ϊ��x/y="+result.toString());
        //��ģ|x|
    	System.out.println("x��ģΪ��|x|="+x.abs(x));
    	System.out.println("y��ģΪ��|y|="+y.abs(y));
    	
    	//��¡x
    	try {
	    	Complex z=x.clone();
	    	System.out.println("��¡�����"+z.toString());
    	}
    	catch(CloneNotSupportedException e) {
    	}
    }
}
