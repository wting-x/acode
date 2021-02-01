#include <iostream> 
using namespace std;

void change(int arr[]) {
	cout << arr << endl;
	arr[0] = 100;
}
int main() {
	int arr[] = { 1,4,2,4 };
	cout << arr[0] << endl;
	change(arr);
	cout << arr[0] << endl;
	cout << arr << endl;

	return 0;
}