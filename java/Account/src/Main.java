import java.util.Scanner; //����ɨ����

public class Main {
    public static void main (String[] args) {
    	Scanner input=new Scanner(System.in);		//����һ������ɨ�������
    	final int num=10;
    	Account ac[]=new Account[num];
        
        for(int i=0;i<10;i++) {
        	ac[i]=new Account(100+i,100);
        }		//��ʼ���˻���Ϣ
        
        int i=0;
        while(true) {
        	System.out.print("Enter and id:");
        	int id=input.nextInt();		//����һ��id
        	
        	for(i=0;i<10;i++) {
        		if(id==ac[i].show_id())
        			break;
        	}		//Ѱ�Ҷ�Ӧ�˻�
        	if(i==10 && id!=ac[9].show_id()) {
        		System.out.println("It's false. Please input id again:");
        	}		//��������˻�id����������������
        	
        	else {
        		System.out.println("Main menu:");
        		System.out.println("1:check balance");
        		System.out.println("2:withdraw");
        		System.out.println("3:deposit");
        		System.out.println("4:exit");
        		System.out.print("Enter a choice:");
        		//����˵���Ϣ
        		
        		while(true) {
        			int temp=input.nextInt();
	        		switch(temp){
	        			case 1:{
	        				System.out.println("���Ϊ��"+ac[i].show_ba());
	        				break;
	        			}		//����1��ʾ���
	        			case 2:{
	        				double money=input.nextInt();
	        				ac[i].withDraw(money);
	        				break;
	        			}		//����2ȡǮ
	        			case 3:{
	        				double money=input.nextInt();
	        				ac[i].deposit(money);
	        				break;
	        			}		//����3��Ǯ
	        			case 4:{
	        				break;
	        			}		
	        		}
	        		if(temp==4)
	        			break;
	        		//����4���س�ʼ���棬��������id
        		}
        	}
        }
    }
}
