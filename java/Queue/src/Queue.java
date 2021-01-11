
public class Queue {
    private int element[];
    private int size=0;		//Ԫ�ظ���
    
    public Queue() {
    	element = new int[8];
    }		//��������Ϊ8��Queue����
    public void enqueue(int v) {
    	if(size<element.length) {
    		size++;
    		element[size-1] = v;
    	}		//����δ��ʱ
    	else {
    		int temp[]=new int[size+1];
    		System.arraycopy(element, 0, temp, 0, size);
    		temp[size]=v;
    		size++;
    		element = temp;
    	}		//��������ʱ��������
    }
    public void dequeue() {
    	int temp[]=new int[size-1];
    	System.arraycopy(element, 1, temp, 0, size-1);
    	System.out.println(element[0]);
    	element = temp;
    	size--;
    }		//ɾ�����еĵ�һ��Ԫ�ز����
    public boolean empty() {
    	if(size==0)
    		return true;
    	else
    		return false;
    }		//����Ϊ���򷵻�true�����򷵻�false
    public int getSize() {
    	return size;
    }		//���ض�����Ԫ�صĸ���
}
