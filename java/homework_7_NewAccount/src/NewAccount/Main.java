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
		ac.withDraw(2);		//进行对应存取款操作
		//显示账户信息
		System.out.println("账户清单：");
		System.out.println("账户持有人名字："+ac.show_na());
		System.out.println("月利率："+ac.getMonthlyInterestRate());
		System.out.println("余额："+ac.show_ba());
		//显示交易记录
		System.out.println("该账户的全部交易：");
		System.out.println("\t交易时间"+"\t\t"+"交易类型"+"\t"+"交易金额"+"\t"+"余额"+"\t\t"+"备注");
		for(int i=0;i<ac.transation.size();i++) {
			System.out.println(ac.transation.get(i));
		}
	}
}
