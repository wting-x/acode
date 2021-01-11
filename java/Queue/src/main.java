
public class main {
    public static void main(String[] args) {
    	Queue q=new Queue();
    	for(int i=0;i<20;i++) {
    		q.enqueue(i+1);
    	}
    	for(int i=0;i<20;i++) {
    		q.dequeue();
    	}
    	if(q.empty())
    		System.out.println("队列为空");		//如果队列为空，输出“队列为空”
    }
}
