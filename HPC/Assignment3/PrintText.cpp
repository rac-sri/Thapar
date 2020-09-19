// Write a CUDA program to print “Hello World” using one thread and one block

	
	#include<iostream>
using namespace std;
__global__ void printHello(){
}
int main(){
	printHello<<<1,1>>>();
cout<<”Hello World”;
	return 0;
}
	
