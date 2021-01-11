package TriangleSpiralArray;
import java.util.Scanner;

public class Matrix {
	private int num;
	private int array[][];
	
	public Matrix()
	{
		Scanner input=new Scanner(System.in);
		num = input.nextInt();
		array=new int[num][num];
		this.Generation_Matrix();
	}
	
	public void Generation_Matrix()
	{
		int i=0;
		int j=0;
		int a=0;
		
		while(j<num) {
			a++;
			array[i][j]=a;
			if((j+1)<num && array[i][j+1]==0) 
			{
				j++;
			}
			else
				j++;
		}
	}
	
	public void Show_Matrix()
	{
		for(int i=0;i<num;i++) {
			for(int j=0;j<num;j++)
			{
				System.out.print(array[i][j]);
				System.out.print(' ');
			}
			System.out.println();
		}
	}
}
