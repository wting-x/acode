import java.util.Scanner;

public class Matrix {
	private int num;
	
	public Matrix()
	{
		Scanner input=new Scanner(System.in);//����һ������ɨ�������
		num = input.nextInt();
	}
	
	public void Show_Matrix()
	{
		int a=1;
		for(int i=0;i<num;i++) {
			for(int j=0;j<=i;j++) {
				System.out.print(a);
				a++;
				System.out.print(' ');
			}
			System.out.println();
		}
	}
}
