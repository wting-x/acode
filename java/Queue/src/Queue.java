
public class Queue {
    private int element[];
    private int size=0;		//元素个数
    
    public Queue() {
    	element = new int[8];
    }		//构造容量为8的Queue对象
    public void enqueue(int v) {
    	if(size<element.length) {
    		size++;
    		element[size-1] = v;
    	}		//队列未满时
    	else {
    		int temp[]=new int[size+1];
    		System.arraycopy(element, 0, temp, 0, size);
    		temp[size]=v;
    		size++;
    		element = temp;
    	}		//队列已满时扩充数组
    }
    public void dequeue() {
    	int temp[]=new int[size-1];
    	System.arraycopy(element, 1, temp, 0, size-1);
    	System.out.println(element[0]);
    	element = temp;
    	size--;
    }		//删除队列的第一个元素并输出
    public boolean empty() {
    	if(size==0)
    		return true;
    	else
    		return false;
    }		//队列为空则返回true，否则返回false
    public int getSize() {
    	return size;
    }		//返回队列中元素的个数
}
