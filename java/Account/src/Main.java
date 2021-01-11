import java.util.Scanner; //键盘扫描类

public class Main {
    public static void main (String[] args) {
    	Scanner input=new Scanner(System.in);		//创建一个键盘扫描类对象
    	final int num=10;
    	Account ac[]=new Account[num];
        
        for(int i=0;i<10;i++) {
        	ac[i]=new Account(100+i,100);
        }		//初始化账户信息
        
        int i=0;
        while(true) {
        	System.out.print("Enter and id:");
        	int id=input.nextInt();		//输入一个id
        	
        	for(i=0;i<10;i++) {
        		if(id==ac[i].show_id())
        			break;
        	}		//寻找对应账户
        	if(i==10 && id!=ac[9].show_id()) {
        		System.out.println("It's false. Please input id again:");
        	}		//若输入的账户id不存在则重新输入
        	
        	else {
        		System.out.println("Main menu:");
        		System.out.println("1:check balance");
        		System.out.println("2:withdraw");
        		System.out.println("3:deposit");
        		System.out.println("4:exit");
        		System.out.print("Enter a choice:");
        		//输出菜单信息
        		
        		while(true) {
        			int temp=input.nextInt();
	        		switch(temp){
	        			case 1:{
	        				System.out.println("余额为："+ac[i].show_ba());
	        				break;
	        			}		//输入1显示余额
	        			case 2:{
	        				double money=input.nextInt();
	        				ac[i].withDraw(money);
	        				break;
	        			}		//输入2取钱
	        			case 3:{
	        				double money=input.nextInt();
	        				ac[i].deposit(money);
	        				break;
	        			}		//输入3存钱
	        			case 4:{
	        				break;
	        			}		
	        		}
	        		if(temp==4)
	        			break;
	        		//输入4返回初始界面，重新输入id
        		}
        	}
        }
    }
}
