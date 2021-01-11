import java.util.Scanner; //键盘扫描类

public class Matrix {
	public static void main(String[] args) {
		  Scanner input=new Scanner(System.in);//创建一个键盘扫描类对象
		  System.out.print("请您输入矩阵长：");
		  int length=input.nextInt();   //输入矩阵长
		  
		  int matrix[][]=new int[length][length];
		  int i=0,j=0;
		  for(i=0;i<length;i++) {
			  for(j=0;j<length;j++) {
				  matrix[i][j]=Math.random()>0.5?0:1;
				  System.out.print(matrix[i][j]);
				  System.out.print(" ");
			  }
			  System.out.println("");
		  }		//矩阵定义赋值输出
		  
		  for(i=0;i<length;i++) {
			  
			  for(j=0;j<length;j++) {
				  if(j!=0 && matrix[i][j]!=matrix[i][j-1])
					  break;
			  }
			  if(j==length && matrix[i][j-1]==matrix[i][j-2])
				  System.out.println("第"+(i+1)+"行全部都是"+matrix[i][j-1]);	//行判断
			  
			  for(j=0;j<length;j++) {
				  if(j!=0 && matrix[j][i]!=matrix[j-1][i])
					  break;
			  }
			  if(j==length && matrix[j-1][i]==matrix[j-2][i])
				  System.out.println("第"+(i+1)+"列全部都是"+matrix[j-1][i]);	//列判断
		  }
		  
		  for(i=0;i<length;i++) {
			  if(i!=0 && matrix[i][i]!=matrix[i-1][i-1])
				  break;
		  }
		  if(i==length && matrix[i-1][i-1]==matrix[i-2][i-2])
			  System.out.println("主对角线上全部都是"+matrix[i-1][i-1]);		//主对角线判断
		  
		  for(i=0;i<length;i++) {
			  if(i!=0 && matrix[i][length-i-1]!=matrix[i-1][length-i])
				  break;
		  }
		  if(i==length && matrix[i-1][length-i]==matrix[i-2][length-i+1])
			  System.out.println("副对角线上全部都是"+matrix[i-1][length-i]);	//副对角线判断
	}
}