
public class Cabinet {
	public static char exchange(char c) {
		if(c=='c')
			c='o';
		else
			c='c';
		return c;
	}		//�ı���ӵ�״̬
	
	
	public static void main (String[] args) {
		int num = 100;		//��������
		char cabinet[] = new char[num];
		
		for(int i=0;i<num;i++) {
			cabinet[i] = 'c';
		}		
		
		for(int i=0;i<num;i++) {
			for(int j=i;j<num;j=j+i+1) {
				cabinet[j] = exchange(cabinet[j]);
			}
		}
		
		for(int i=0;i<num;i++) {
			if(cabinet[i] == 'o')
				System.out.println("��"+(i+1)+"�������ǿ��ŵ�");
		}
	}
}
