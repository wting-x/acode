package NewAccount;
import java.util.Date;
import java.text.*;

public class Transation {
	private Date date;		//����ʱ��
	private char type;		//��������
	private double amount;		//���׽��
	private double balance;		//���
	private String description;		//��������
	
	Transation(char type, double amount, double balance, String description){
		date=new Date();
		this.type = type;
		this.amount = amount;
		this.balance = balance;
		this.description = description;
	}		//��ʼ��Transation��
	public String toString() {
		String a=(type=='w')?("ȡ��"):("���");
		SimpleDateFormat ft=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		return (ft.format(date)+"\t"+a+"\t"+amount+"Ԫ\t"+balance+"Ԫ\t\t"+description);
	}
}
