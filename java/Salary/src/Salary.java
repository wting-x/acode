import java.util.Scanner;

public class Salary {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);//����һ������ɨ�������
		System.out.print("��������10���˵Ĺ��ʣ�");
		int salary[]=new int[10];		//���� 
		int RMB[][]=new int[10][6];		//����
		int money[]={100,50,10,5,2,1};		//��ֵ
		
		for(int i=0;i<salary.length;i++) {
			salary[i]=input.nextInt();
			int sal=salary[i];
			for(int j=0;j<money.length;j++) {
				RMB[i][j]=sal/money[j];
				sal=sal%money[j];
			}
		}		//���빤�� ������
		
		for(int i=0;i<salary.length;i++) {
			System.out.println("");
			System.out.println("��"+(i+1)+"�˹���Ϊ"+salary[i]+"Ԫ����Ҫ��");
			for(int j=0;j<money.length;j++) {
				if(RMB[i][j]!=0)
					System.out.print(RMB[i][j]+"��"+money[j]+"Ԫ  ");
			}
			System.out.println("");
		}		//���
		
		System.out.println("\r����Ҫ��");
		int sum[]=new int[6];
		for(int i=0;i<money.length;i++) {
			sum[i]=0;
			for(int j=0;j<salary.length;j++) {
				sum[i]=sum[i]+RMB[j][i];
			}
			if(sum[i]!=0)
				System.out.println(sum[i]+"��"+money[i]+"Ԫ");
		}
	}
}
