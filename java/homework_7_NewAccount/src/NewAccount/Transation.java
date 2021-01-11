package NewAccount;
import java.util.Date;
import java.text.*;

public class Transation {
	private Date date;		//交易时间
	private char type;		//交易类型
	private double amount;		//交易金额
	private double balance;		//余额
	private String description;		//交易描述
	
	Transation(char type, double amount, double balance, String description){
		date=new Date();
		this.type = type;
		this.amount = amount;
		this.balance = balance;
		this.description = description;
	}		//初始化Transation类
	public String toString() {
		String a=(type=='w')?("取款"):("存款");
		SimpleDateFormat ft=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		return (ft.format(date)+"\t"+a+"\t"+amount+"元\t"+balance+"元\t\t"+description);
	}
}
