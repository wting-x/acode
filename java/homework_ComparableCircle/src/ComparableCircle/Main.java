package ComparableCircle;
import java.util.Scanner;

public class Main {
	public static void main(String[] args)throws Exception{
		@SuppressWarnings("resource")
		Scanner input=new Scanner(System.in);		//����һ������ɨ�������
		
		System.out.println("������circle1�İ뾶��");
		double a=input.nextDouble();		//����circle1�뾶
		System.out.println("������circle2�İ뾶��");
		double b=input.nextDouble();		//����circle2�뾶
		
		//��ʼ��circle1��circle2�뾶�ֱ�Ϊa,b
		ComparableCircle circle1=new ComparableCircle(a);
		ComparableCircle circle2=new ComparableCircle(b);
		
		//��¡circle1
    	ComparableCircle circle3=circle1.clone();
    	System.out.println("circle1��¡�ɹ�����¡���Ϊcircle3");
    	
		//�Ƚ�circle1��circle2�Ƿ����
		System.out.println("circle1��circle2��ȡ�\t"+circle1.equals(circle2));
		
    	//�ֱ�Ƚ�circle1��circle2��circle3�Ƿ����
    	System.out.println("circle1��circle3��ȡ�\t"+circle1.equals(circle3));
    	System.out.println("circle2��circle3��ȡ�\t"+circle2.equals(circle3));
	}
}
