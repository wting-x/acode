package NewAccount;
import java.util.Date;
import java.util.ArrayList;

public class Account {
    private int id;    //�˻���
    private double balance;		//���
    private double annuallnterestRate;		//������
    private Date dateCreated=new Date();		//�˻��Ŀ������� 
    private String name;		//�ͻ�������
    public ArrayList transation=new ArrayList();		//�˻����׼�¼
    
    Account(){
    	id = 0;
    	balance = 0;
    	annuallnterestRate = 0;
    }		//��ʼ���˻������������ʾ�Ϊ0�Ĺ��캯��
    Account(int a, double b){
        id = a;
        balance = b;
    }        //��ʼ���˻���Ϊa�����Ϊb�Ĺ��캯��
    Account(String a, int b, double c) {
    	name = a;
    	id = b;
    	balance = c;
    }		//��ʼ���ͻ�����Ϊa���˻���Ϊb�����Ϊc�Ĺ��캯��
    
    public int show_id(){
    	return id;
    }		//�����˻�����ֵ
    public double show_ba(){
    	return balance;
    }        //��������ֵ
    public double show_an(){
    	return annuallnterestRate;
    }        //���������ʵ�ֵ
    public Date show_da(){
    	return dateCreated;
    }        //�����˻��Ŀ�������
    public String show_na() {
    	return name;
    }
    
    public void set_id(int a) {
    	id = a;
    }        //���˻�������Ϊa
    public void set_ba(double a) {
    	balance = a;
    }        //���������Ϊa
    public void set_an(double a) {
    	annuallnterestRate = a;
    }        //������������Ϊa
    
    public double getMonthlyInterestRate() {
    	return annuallnterestRate/12.0;
    }        //���������ʵ�ֵ
    public void withDraw(double a) {
    	if(a > balance)
    	{
    		System.out.println("���㣡����");
            System.out.println("���Ϊ��"+balance);
    	}
    	else
    	{
    		balance = balance-a;
    		transation.add(new Transation('w',a,this.show_ba(),"�������ˣ������ֱ���ˣ�"));
    		//�洢�û�ȡ���¼
    	}
    }        //ȡaԪ��������,����ʾ�����㡱������ʾ���
    public void deposit(double a) {
    	balance = balance+a;
    	transation.add(new Transation('d',a,this.show_ba(),"����Ҳ��ø���Ǯ���أ�"));
        //�洢�û�����¼
    } 		//����aԪ
}
