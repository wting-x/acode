package Game;

import java.awt.Rectangle;

public class Ball {
	Rectangle rect=null;
    int ball_x,ball_y;
    int ball_width,ball_height;
    public Ball(int x,int y,int w,int h){
        ball_x=x;
        ball_y=y;
        ball_width=w;
        ball_height=h;
        rect=new Rectangle(x,y,w,h);
    }
}
