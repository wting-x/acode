package Game;

import java.awt.Color;
import java.awt.Container;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.UIManager;

@SuppressWarnings({ "serial", "unused" })
public class HitBrick extends JFrame implements KeyListener{
	private BallThread greenBallThread;
    //控制小球的线程
    private Boolean xUp,yUp,bouncing;
    private int x,y,xDx,yDy;
    //小球坐标,增量
    private final int MAX_X=300,MAX_Y=500;
    private Boolean renew;
    private JLabel label;
    private int Rx,Ry;
    //横板坐标
    private Brick brick[]=new Brick[22];
    //砖块
    private Ball ball;
    //小球
    private long starttime,currenttime;
    
    private int count1,count2;
    public HitBrick(){
        super("敲砖块");
        Container pane=getContentPane();
        //设置空白面板容器
        
        label=new JLabel("按回车键开始");
        //标签
        label.setHorizontalAlignment(JLabel.CENTER);
        //水平
        label.setVerticalAlignment(JLabel.BOTTOM);
        //垂直
        
        pane.add(label);
        //向面板里添加标签
        pane.setBackground(Color.white);
        
        xUp=true;
        //横坐标可以移动
        yUp=false;
        //纵坐标不可以移动
        
        xDx=1;
        yDy=1;
        //小球坐标
        x=145;
        y=450;
        
        //横板坐标
        Rx=110;
        Ry=460;
        
        renew=true;
        bouncing=false;
        addKeyListener(this);
        //键盘监听器
        
        brick[0]=new Brick(0,60,50,20);
        //砖块坐标
        brick[1]=new Brick(50,60,50,20);
        brick[2]=new Brick(100,60,50,20);
        brick[3]=new Brick(150,60,50,20);
        brick[4]=new Brick(200,60,50,20);
        brick[5]=new Brick(250,60,50,20);
        brick[6]=new Brick(0,90,50,20);
        brick[7]=new Brick(50,110,50,20);
        brick[8]=new Brick(100,130,50,20);
        brick[9]=new Brick(150,130,50,20);
        brick[10]=new Brick(200,110,50,20);
        brick[11]=new Brick(250,90,50,20);
        brick[12]=new Brick(0,160,50,20);
        brick[13]=new Brick(50,160,50,20);
        brick[14]=new Brick(100,160,50,20);
        brick[15]=new Brick(150,160,50,20);
        brick[16]=new Brick(200,160,50,20);
        brick[17]=new Brick(250,160,50,20);
        brick[18]=new Brick(100,200,50,20);
        brick[19]=new Brick(150,200,50,20);
        brick[20]=new Brick(50,140,50,10);
        brick[21]=new Brick(200,140,50,10);
        ball=new Ball(x,y,xDx,yDy);
        //球的坐标
        setSize(MAX_X,MAX_Y);
        //窗口大小
        setResizable(false);
        setVisible( true );
        //可视化
    }
    @SuppressWarnings("static-access")
    
    //按键事件
	public void keyPressed(KeyEvent e) {
    	//按回车键
        if (e.getKeyCode() ==e.VK_ENTER) {
            if(renew){
            	count1=0;
            	count2=0;
                greenBallThread=new BallThread(this);
                bouncing = true;
                greenBallThread.start();
                starttime=System.currentTimeMillis();
            }
            renew=false;
        }
        
        //按左移键
        if(e.getKeyCode()==e.VK_LEFT){
            Rx=Rx-10;
            if(bouncing){
                if(Rx<0){
                    Rx=0;
                }
            } 
            else{
                if(Rx<0){
                    Rx=0;
                } 
                else{
                    x=x-10;
                    ball.ball_x=x;
                }
            }
            repaint();
        }
        
        //按右移键
        if(e.getKeyCode()==e.VK_RIGHT){
            Rx=Rx+10;
            if(bouncing){
                if(Rx+80>300){
                    Rx=220;
                }
            } else{
                if(Rx+80>300){
                    Rx=220;
                } else{
                    x=x+10;
                    ball.ball_x=x;
                }
            }
            repaint();
        }
    }
    public void keyReleased (KeyEvent e) {
    }
    public void keyTyped (KeyEvent e){
    }
    
    //显示
    public void paint(Graphics g){
        super.paint(g);
        ball.rect.setLocation(x,y);
        if(bouncing){
            for (int i=0;i<22;i++){
                if(brick[i].visible==true){
                    switch(i){
                        case 0 :g.setColor(Color.gray);
                        break;
                        case 1 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 2 :g.setColor(Color.gray);
                        break;
                        case 3 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 4 :g.setColor(Color.gray);
                        break;
                        case 5 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 6 :g.setColor(Color.gray);
                        break;
                        case 7 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 8 :g.setColor(Color.gray);
                        break;
                        case 9 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 10 :g.setColor(Color.gray);
                        break;
                        case 11 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 12 :g.setColor(Color.gray);
                        break;
                        case 13 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 14 :g.setColor(Color.gray);
                        break;
                        case 15 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 16 :g.setColor(Color.gray);
                        break;
                        case 17 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 18 :g.setColor(Color.gray);
                        break;
                        case 19 :g.setColor(Color.LIGHT_GRAY);
                        break;
                        case 20 :g.setColor(Color.BLACK);
                        break;
                        case 21 :g.setColor(Color.BLACK);
                        break;
                    }
                    g.fill3DRect(brick[i].brick_x,brick[i].brick_y,brick[i].brick_width,brick[i].brick_height,true);
                }
            }
            g.setColor(Color.BLUE);
            g.fillOval(x, y, 10, 10);
            g.setColor(Color.black);
            g.fillRect(Rx,Ry,80,10);
        } else{
            for (int i=0;i<22;i++){
                switch(i){
	                case 0 :g.setColor(Color.gray);
	                break;
	                case 1 :g.setColor(Color.LIGHT_GRAY);
	                break;
	                case 2 :g.setColor(Color.gray);
	                break;
	                case 3 :g.setColor(Color.LIGHT_GRAY);
	                break;
	                case 4 :g.setColor(Color.gray);
	                break;
	                case 5 :g.setColor(Color.LIGHT_GRAY);
	                break;
	                case 6 :g.setColor(Color.gray);
	                break;
	                case 7 :g.setColor(Color.LIGHT_GRAY);
	                break;
	                case 8 :g.setColor(Color.gray);
	                break;
	                case 9 :g.setColor(Color.LIGHT_GRAY);
	                break;
	                case 10 :g.setColor(Color.gray);
	                break;
	                case 11 :g.setColor(Color.LIGHT_GRAY);
	                break;
	                case 12 :g.setColor(Color.gray);
	                break;
	                case 13 :g.setColor(Color.LIGHT_GRAY);
	                break;
	                case 14 :g.setColor(Color.gray);
	                break;
	                case 15 :g.setColor(Color.LIGHT_GRAY);
	                break;
	                case 16 :g.setColor(Color.gray);
	                break;
	                case 17 :g.setColor(Color.LIGHT_GRAY);
	                break;
	                case 18 :g.setColor(Color.gray);
                    break;
                    case 19 :g.setColor(Color.LIGHT_GRAY);
                    break;
                    case 20 :g.setColor(Color.BLACK);
                    break;
                    case 21 :g.setColor(Color.BLACK);
                    break;
                }
                g.fill3DRect(brick[i].brick_x,brick[i].brick_y,brick[i].brick_width,brick[i].brick_height,true);
            }
            g.setColor(Color.BLUE);
            g.fillOval(x, y, 10, 10);
            g.setColor(Color.black);
            g.fillRect(Rx, Ry, 80, 10);
        }
    }
    
    //球的移动
    @SuppressWarnings("static-access")
	public void move(){
    	try {  
        	Thread.currentThread().sleep(10); 
        } catch (Exception e) {  
            e.printStackTrace();  
        }  
        while(true){
            try{
            	Thread.currentThread().sleep(25);
            }
            catch(InterruptedException exception){
                System.err.println(exception.toString());
            }
            
            currenttime=System.currentTimeMillis();
            label.setText("得分："+(count1*5+count2*10)+"    用时："+(currenttime-starttime)/1000+"s");
            label.setHorizontalAlignment(JLabel.CENTER);
            label.setVerticalAlignment(JLabel.TOP);
            
            
            for (int i=0;i<22;i++){
                if(ball.rect.intersects(brick[i].rect)&&brick[i].visible){
                    if(i<20) {
                    	brick[i].visible=false;
	                    if(i%2!=0)
	                    	count2++;
	                    else
	                    	count1++;
	                    //被球打到不可见
                    }
                    yUp=!yUp;
                }
            }
            if(x+5>Rx&&x+5<Rx+80&&y+10>=Ry){
                yUp=false;
                xDx=(int)(Math.random()*5+2);
                //小球坐标增量
                yDy=(int)(Math.random()*5+2);
            }
            if(xUp==true){
                x+=xDx;
                //小球左右移动坐标改变
            } else{
                x-=xDx;
            }
            if(yUp==true){
                y+=yDy;
            } else{
                y-=yDy;
            }
            if(y<=0){
                y=0;
                ball.ball_y=y;
                yUp=true;
                xDx=(int)(Math.random()*5+2);
                yDy=(int)(Math.random()*5+2);
            } else if(y>=Ry){
                yDy=(int)(Math.random()*5+2);
                label.setHorizontalAlignment(JLabel.CENTER);
                label.setVerticalAlignment(JLabel.CENTER);
                label.setText("游戏失败！！！"+"最终得分为"+(count1*5+count2*10));
                break;
            }
            if(x<=0){
                x=0;
                ball.ball_x=x;
                xUp=true;
                xDx=(int)(Math.random()*5+2);
                yDy=(int)(Math.random()*5+2);
            } else if(x>=MAX_X-10){
                x=MAX_X-10;
                ball.ball_x=x;
                xDx=(int)(Math.random()*5+2);
                yDy=(int)(Math.random()*5+2);
                xUp=false;
            }
            ball.rect.setLocation(ball.ball_x,ball.ball_y);
            repaint();
            
            int i;
            //如果所有砖块都不可见
            for (i=0;i<20&&brick[i].visible==false;i++){
                //则重新玩
            }
            if(i==20){
                label.setHorizontalAlignment(JLabel.CENTER);
                label.setVerticalAlignment(JLabel.CENTER);
            	label.setText("恭喜您，游戏成功！！！用时"+(currenttime-starttime)/1000+"s");
            	break;
            }
        }
        
        renew=true;
        //初始化
        bouncing=false;
        for (int i=0;i<20;i++){
            brick[i].visible=true;
        }
        xUp=true;
        yUp=false;
        xDx=1;
        yDy=1;
        x=150;
        y=450;
        Rx=120;
        Ry=460;
        
        repaint();
        repaint();
    }
}
