package ComparableCircle;

public abstract class Circle {
	private double radius;		//����Բ�뾶radius
	public final double PI=3.14; 		//���峣��PI=3.14
	
	Circle(){
		radius = 0;
	}		//����Բ�뾶Ϊ0
	Circle(double a){
		radius = a;
	}		//����Բ�뾶Ϊa
	
	public double getRadius() {
		return radius;
	}		//����Բ�뾶
}
