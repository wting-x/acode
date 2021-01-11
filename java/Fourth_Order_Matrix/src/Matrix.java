
public class Matrix {
	public static void main(String[] args) {
		int len=4;		//矩阵长
		int matrix[][]=new int[len][len];		//定义矩阵
		int line=0, column=0;		//拥有1最多的行与列
		int lin_num=0,col_num=0;		//对应行和列中1的个数
		
		for(int i=0;i<len;i++) {
			for(int j=0;j<len;j++) {
				matrix[i][j]=(Math.random()>0.5)?0:1;
				System.out.print(matrix[i][j]+" ");
			}
			System.out.println("");
		}		//产生随机四阶矩阵并打印
		
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
		
		System.out.println("第"+line+"行为所求行，共有"+lin_num+"个1");
		System.out.println("第"+column+"列为所求列，共有"+col_num+"个1");
	}
}
