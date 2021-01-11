package ComparableCircle;
import java.lang.Math;

@SuppressWarnings({ "unused", "rawtypes" })
public class ComparableCircle extends Circle implements Cloneable{		
	//子类构造半径为a的可比较圆
	ComparableCircle(double a){
		super(a);
	}
	
	//返回圆面积（默认PI为3.14）
	public double getArea() {
		return super.getRadius()*super.getRadius()*PI;
	}
	
	//实现Cloneable接口
    public ComparableCircle clone() throws CloneNotSupportedException {
    	ComparableCircle a=(ComparableCircle)super.clone();
    	return a;
    }
    
    //实现Comparable接口
    public boolean equals(Object o) {
    	if(getArea()==((ComparableCircle)o).getArea())
    		return true;
    	else
    		return false;
    }

	public int compareTo(Object o) {
		// TODO Auto-generated method stub
		if(getArea()>((ComparableCircle)o).getArea())
			return 1;
		else if(getArea()<((ComparableCircle)o).getArea())
			return -1;
		else
		    return 0;
	}

}
