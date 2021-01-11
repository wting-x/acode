package Game;

import java.awt.Rectangle;

public class Brick {
	Rectangle rect=null;
    //长方形对象，砖块按钮的位置和宽高
    int brick_x,brick_y;
    //按扭的左上角坐标
    int brick_width,brick_height;
    //按扭的宽和高
    Boolean visible;
    public Brick(int x,int y,int w,int h)
       {
        brick_x=x;
        brick_y=y;
        brick_width=w;
        brick_height=h;
        visible=true;
        rect=new Rectangle(x,y,w,h);
        //创建长方形对象---砖块按钮的位置和宽高。
    }
}
