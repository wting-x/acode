import java.util.Date;

public class Account {
    private int id;    //�˻���
    private double balance;		//���
    private double annuallnterestRate;		//������
    private Date dateCreated=new Date();		//�˻��Ŀ������� 
    
    public Account(){
    	id = 0;
    	balance = 0;
    	annuallnterestRate = 0;
    }		//��ʼ���˻������������ʾ�Ϊ0�Ĺ��캯��
    public Account(int a, double b){
        id = a;
        balance = b;
    }        //��ʼ���˻���Ϊa�����Ϊb�Ĺ��캯��
    
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
    		balance = balance-a;
    }        //ȡaԪ��������,����ʾ�����㡱������ʾ���
    public void deposit(double a) {
    	balance = balance+a;
    } 		//����aԪ
}
