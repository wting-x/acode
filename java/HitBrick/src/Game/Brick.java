package Game;

import java.awt.Rectangle;

public class Brick {
	Rectangle rect=null;
    //�����ζ���ש�鰴ť��λ�úͿ��
    int brick_x,brick_y;
    //��Ť�����Ͻ�����
    int brick_width,brick_height;
    //��Ť�Ŀ�͸�
    Boolean visible;
    public Brick(int x,int y,int w,int h)
       {
        brick_x=x;
        brick_y=y;
        brick_width=w;
        brick_height=h;
        visible=true;
        rect=new Rectangle(x,y,w,h);
        //���������ζ���---ש�鰴ť��λ�úͿ�ߡ�
    }
}
