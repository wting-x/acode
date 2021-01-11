package Complex;
import java.lang.Math;

public class Complex implements Cloneable {
    private double a;		//实部
    private double b;		//虚部
    
    //构造函数
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
    
    //返回复数实部
    public double getRealPart() {
    	return a;
    }
    //返回复数虚部
    public double getImaginaryPart() {
    	return b;
    }
    
    //复数加运算
    public Complex add(Complex x, Complex y) {
    	double a=x.getRealPart()+y.getRealPart();
    	double b=x.getImaginaryPart()+y.getImaginaryPart();
    	Complex result=new Complex(a,b);
    	return result;
    }
    //复数减运算
    public Complex substract(Complex x, Complex y) {
    	double a=x.getRealPart()-y.getRealPart();
    	double b=x.getImaginaryPart()-y.getImaginaryPart();
    	Complex result=new Complex(a,b);
    	return result;
    }
    //复数乘运算
    public Complex multiply(Complex x, Complex y) {
    	double a=x.getRealPart()*y.getRealPart()-x.getImaginaryPart()*y.getImaginaryPart();
    	double b=x.getRealPart()*y.getImaginaryPart()+x.getImaginaryPart()*y.getRealPart();
    	Complex result=new Complex(a,b);
    	return result;
    }
    //复数除运算
    public Complex divide(Complex x, Complex y) {
    	double a=x.getRealPart()*y.getRealPart()+x.getImaginaryPart()*y.getImaginaryPart();
    	double b=x.getImaginaryPart()*y.getRealPart()-x.getRealPart()*y.getImaginaryPart();
    	double c=y.getRealPart()*y.getRealPart()+y.getImaginaryPart()*y.getImaginaryPart();
    	Complex result=new Complex(a/c,b/c);
    	return result;
    }
    //复数绝对值运算
    public double abs(Complex x) {
    	return Math.sqrt(x.getRealPart()*x.getRealPart()+x.getImaginaryPart()*x.getImaginaryPart());
    }
    
    //覆盖toString方法
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
    
    //实现Cloneable接口
    public Complex clone() throws CloneNotSupportedException {
    	Complex a=(Complex)super.clone();
    	return a;
    }
}
