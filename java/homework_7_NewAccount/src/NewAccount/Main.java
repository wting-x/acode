package NewAccount;

public class Main {
	public static void main(String[] args) {
		Account ac=new Account("George", 1122, 1000);
		ac.set_an(0.015);
		
		ac.deposit(30);
		ac.deposit(40);
		ac.deposit(50);
		ac.withDraw(5);
		ac.withDraw(4);
		ac.withDraw(2);		//���ж�Ӧ��ȡ�����
		//��ʾ�˻���Ϣ
		System.out.println("�˻��嵥��");
		System.out.println("�˻����������֣�"+ac.show_na());
		System.out.println("�����ʣ�"+ac.getMonthlyInterestRate());
		System.out.println("��"+ac.show_ba());
		//��ʾ���׼�¼
		System.out.println("���˻���ȫ�����ף�");
		System.out.println("\t����ʱ��"+"\t\t"+"��������"+"\t"+"���׽��"+"\t"+"���"+"\t\t"+"��ע");
		for(int i=0;i<ac.transation.size();i++) {
			System.out.println(ac.transation.get(i));
		}
	}
}
