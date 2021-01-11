import java.util.Scanner;

public class Salary {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);//创建一个键盘扫描类对象
		System.out.print("请输入这10个人的工资：");
		int salary[]=new int[10];		//工资 
		int RMB[][]=new int[10][6];		//数量
		int money[]={100,50,10,5,2,1};		//面值
		
		for(int i=0;i<salary.length;i++) {
			salary[i]=input.nextInt();
			int sal=salary[i];
			for(int j=0;j<money.length;j++) {
				RMB[i][j]=sal/money[j];
				sal=sal%money[j];
			}
		}		//输入工资 并计算
		
		for(int i=0;i<salary.length;i++) {
			System.out.println("");
			System.out.println("第"+(i+1)+"人工资为"+salary[i]+"元，需要：");
			for(int j=0;j<money.length;j++) {
				if(RMB[i][j]!=0)
					System.out.print(RMB[i][j]+"张"+money[j]+"元  ");
			}
			System.out.println("");
		}		//输出
		
		System.out.println("\r共需要：");
		int sum[]=new int[6];
		for(int i=0;i<money.length;i++) {
			sum[i]=0;
			for(int j=0;j<salary.length;j++) {
				sum[i]=sum[i]+RMB[j][i];
			}
			if(sum[i]!=0)
				System.out.println(sum[i]+"张"+money[i]+"元");
		}
	}
}
