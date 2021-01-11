package ComparableCircle;
import java.lang.Math;

@SuppressWarnings({ "unused", "rawtypes" })
public class ComparableCircle extends Circle implements Cloneable{		
	//���๹��뾶Ϊa�ĿɱȽ�Բ
	ComparableCircle(double a){
		super(a);
	}
	
	//����Բ�����Ĭ��PIΪ3.14��
	public double getArea() {
		return super.getRadius()*super.getRadius()*PI;
	}
	
	//ʵ��Cloneable�ӿ�
    public ComparableCircle clone() throws CloneNotSupportedException {
    	ComparableCircle a=(ComparableCircle)super.clone();
    	return a;
    }
    
    //ʵ��Comparable�ӿ�
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
