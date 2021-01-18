//约瑟夫生者死者游戏 
#include <stdio.h>
#define total 30
#define special 9

int main(){
	int array[total]={0};
	int count=0;
	int i=0,c=1;
	while(count<15){
		for(i=0;i<total;i++){
			if(array[i]!=1){
				//printf("%d %d\n",i+1,c);
				if(c==9){
					array[i]=1;
					count++;
					c=1;
					printf("第%d号下船，%d\n",i+1,array[i]);
				}
				else{
					c++;
				}
			}
		}
	}
	return 0;
}
