package Game;

public class BallThread extends Thread{
    private HitBrick m;
    BallThread(HitBrick a){
        m=a;
    }
    public void run(){
        m.move();
        m.repaint();
    }
}
