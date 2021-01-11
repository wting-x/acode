package Complex;
import java.lang.Math;

public class Complex implements Cloneable {
    private double a;		//ʵ��
    private double b;		//�鲿
    
    //���캯��
    Complex(double a, double b){
    	this.a=a;
    	this.b=b;
    }
    Complex(double a){
    	this.a=a;
    	b=0;
    }
    Complex(){
    	a=0;
    	b=0;
    }
    
    //���ظ���ʵ��
    public double getRealPart() {
    	return a;
    }
    //���ظ����鲿
    public double getImaginaryPart() {
    	return b;
    }
    
    //����������
    public Complex add(Complex x, Complex y) {
    	double a=x.getRealPart()+y.getRealPart();
    	double b=x.getImaginaryPart()+y.getImaginaryPart();
    	Complex result=new Complex(a,b);
    	return result;
    }
    //����������
    public Complex substract(Complex x, Complex y) {
    	double a=x.getRealPart()-y.getRealPart();
    	double b=x.getImaginaryPart()-y.getImaginaryPart();
    	Complex result=new Complex(a,b);
    	return result;
    }
    //����������
    public Complex multiply(Complex x, Complex y) {
    	double a=x.getRealPart()*y.getRealPart()-x.getImaginaryPart()*y.getImaginaryPart();
    	double b=x.getRealPart()*y.getImaginaryPart()+x.getImaginaryPart()*y.getRealPart();
    	Complex result=new Complex(a,b);
    	return result;
    }
    //����������
    public Complex divide(Complex x, Complex y) {
    	double a=x.getRealPart()*y.getRealPart()+x.getImaginaryPart()*y.getImaginaryPart();
    	double b=x.getImaginaryPart()*y.getRealPart()-x.getRealPart()*y.getImaginaryPart();
    	double c=y.getRealPart()*y.getRealPart()+y.getImaginaryPart()*y.getImaginaryPart();
    	Complex result=new Complex(a/c,b/c);
    	return result;
    }
    //��������ֵ����
    public double abs(Complex x) {
    	return Math.sqrt(x.getRealPart()*x.getRealPart()+x.getImaginaryPart()*x.getImaginaryPart());
    }
    
    //����toString����
    public String toString() {
    	if(a!=0&&b!=0)
    		return (a+"+"+b+"i");
    	else if(a!=0&&b==0)
    		return (""+a);
    	else if(a==0&&b!=0)
    		return (b+"i");
    	else
    		return "0";
    }
    
    //ʵ��Cloneable�ӿ�
    public Complex clone() throws CloneNotSupportedException {
    	Complex a=(Complex)super.clone();
    	return a;
    }
}
