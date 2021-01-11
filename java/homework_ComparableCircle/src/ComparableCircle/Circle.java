package ComparableCircle;

public abstract class Circle {
	private double radius;		//定义圆半径radius
	public final double PI=3.14; 		//定义常量PI=3.14
	
	Circle(){
		radius = 0;
	}		//构造圆半径为0
	Circle(double a){
		radius = a;
	}		//构造圆半径为a
	
	public double getRadius() {
		return radius;
	}		//返回圆半径
}
