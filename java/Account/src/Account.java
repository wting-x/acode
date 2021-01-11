import java.util.Date;

public class Account {
    private int id;    //账户名
    private double balance;		//余额
    private double annuallnterestRate;		//年利率
    private Date dateCreated=new Date();		//账户的开户日期 
    
    public Account(){
    	id = 0;
    	balance = 0;
    	annuallnterestRate = 0;
    }		//初始化账户名，余额，年利率均为0的构造函数
    public Account(int a, double b){
        id = a;
        balance = b;
    }        //初始化账户名为a，余额为b的构造函数
    
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
    		balance = balance-a;
    }        //取a元，若余额不足,则显示“余额不足”，并显示余额
    public void deposit(double a) {
    	balance = balance+a;
    } 		//存入a元
}
