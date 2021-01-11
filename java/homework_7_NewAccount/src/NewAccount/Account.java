package NewAccount;
import java.util.Date;
import java.util.ArrayList;

public class Account {
    private int id;    //账户名
    private double balance;		//余额
    private double annuallnterestRate;		//年利率
    private Date dateCreated=new Date();		//账户的开户日期 
    private String name;		//客户的名字
    public ArrayList transation=new ArrayList();		//账户交易记录
    
    Account(){
    	id = 0;
    	balance = 0;
    	annuallnterestRate = 0;
    }		//初始化账户名，余额，年利率均为0的构造函数
    Account(int a, double b){
        id = a;
        balance = b;
    }        //初始化账户名为a，余额为b的构造函数
    Account(String a, int b, double c) {
    	name = a;
    	id = b;
    	balance = c;
    }		//初始化客户名字为a，账户名为b，余额为c的构造函数
    
    public int show_id(){
    	return id;
    }		//返回账户名的值
    public double show_ba(){
    	return balance;
    }        //返回余额的值
    public double show_an(){
    	return annuallnterestRate;
    }        //返回年利率的值
    public Date show_da(){
    	return dateCreated;
    }        //返回账户的开户日期
    public String show_na() {
    	return name;
    }
    
    public void set_id(int a) {
    	id = a;
    }        //将账户名设置为a
    public void set_ba(double a) {
    	balance = a;
    }        //将余额设置为a
    public void set_an(double a) {
    	annuallnterestRate = a;
    }        //将年利率设置为a
    
    public double getMonthlyInterestRate() {
    	return annuallnterestRate/12.0;
    }        //返回月利率的值
    public void withDraw(double a) {
    	if(a > balance)
    	{
    		System.out.println("余额不足！！！");
            System.out.println("余额为："+balance);
    	}
    	else
    	{
    		balance = balance-a;
    		transation.add(new Transation('w',a,this.show_ba(),"存款变少了，但快乐变多了！"));
    		//存储用户取款记录
    	}
    }        //取a元，若余额不足,则显示“余额不足”，并显示余额
    public void deposit(double a) {
    	balance = balance+a;
    	transation.add(new Transation('d',a,this.show_ba(),"今天也变得更有钱了呢！"));
        //存储用户存款记录
    } 		//存入a元
}
