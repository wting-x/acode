import java.util.Scanner; //����ɨ����

public class Matrix {
	public static void main(String[] args) {
		  Scanner input=new Scanner(System.in);//����һ������ɨ�������
		  System.out.print("����������󳤣�");
		  int length=input.nextInt();   //�������
		  
		  int matrix[][]=new int[length][length];
		  int i=0,j=0;
		  for(i=0;i<length;i++) {
			  for(j=0;j<length;j++) {
				  matrix[i][j]=Math.random()>0.5?0:1;
				  System.out.print(matrix[i][j]);
				  System.out.print(" ");
			  }
			  System.out.println("");
		  }		//�����帳ֵ���
		  
		  for(i=0;i<length;i++) {
			  
			  for(j=0;j<length;j++) {
				  if(j!=0 && matrix[i][j]!=matrix[i][j-1])
					  break;
			  }
			  if(j==length && matrix[i][j-1]==matrix[i][j-2])
				  System.out.println("��"+(i+1)+"��ȫ������"+matrix[i][j-1]);	//���ж�
			  
			  for(j=0;j<length;j++) {
				  if(j!=0 && matrix[j][i]!=matrix[j-1][i])
					  break;
			  }
			  if(j==length && matrix[j-1][i]==matrix[j-2][i])
				  System.out.println("��"+(i+1)+"��ȫ������"+matrix[j-1][i]);	//���ж�
		  }
		  
		  for(i=0;i<length;i++) {
			  if(i!=0 && matrix[i][i]!=matrix[i-1][i-1])
				  break;
		  }
		  if(i==length && matrix[i-1][i-1]==matrix[i-2][i-2])
			  System.out.println("���Խ�����ȫ������"+matrix[i-1][i-1]);		//���Խ����ж�
		  
		  for(i=0;i<length;i++) {
			  if(i!=0 && matrix[i][length-i-1]!=matrix[i-1][length-i])
				  break;
		  }
		  if(i==length && matrix[i-1][length-i]==matrix[i-2][length-i+1])
			  System.out.println("���Խ�����ȫ������"+matrix[i-1][length-i]);	//���Խ����ж�
	}
}