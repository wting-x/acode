
public class Matrix {
	public static void main(String[] args) {
		int len=4;		//����
		int matrix[][]=new int[len][len];		//�������
		int line=0, column=0;		//ӵ��1����������
		int lin_num=0,col_num=0;		//��Ӧ�к�����1�ĸ���
		
		for(int i=0;i<len;i++) {
			for(int j=0;j<len;j++) {
				matrix[i][j]=(Math.random()>0.5)?0:1;
				System.out.print(matrix[i][j]+" ");
			}
			System.out.println("");
		}		//��������Ľ׾��󲢴�ӡ
		
		for(int i=0;i<len;i++) {
			
			int numlin=0,numcol=0;
			for(int j=0;j<len;j++) {
				if(matrix[i][j]==1)
					numlin++;
				if(matrix[j][i]==1)
					numcol++;
			}
			
			if(numlin>lin_num) {
				lin_num=numlin;
				line=i+1;
			}
			if(numcol>col_num) {
				col_num=numcol;
				column=i+1;
			}
		}
		
		System.out.println("��"+line+"��Ϊ�����У�����"+lin_num+"��1");
		System.out.println("��"+column+"��Ϊ�����У�����"+col_num+"��1");
	}
}
