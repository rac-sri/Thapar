//Write a CUDA program for vector subtraction of numbers using 1 block and multiple threads

#include<iostream>
using namespace std;
__global__ void sub(int *a, int *b, int *c){
	int i = threadIdx.x;
	c[i] = b[i]-a[i];
}
int main(){
	int a[6],b[6],c[6];
	for(int i=0; i<6; i++){
		a[i] = 3*i+28;
		b[i] = 5*i+69;
	}
	int *da, *db, *dc;
	cudaMalloc(&da, 6*sizeof(int));
	cudaMalloc(&db, 6*sizeof(int));
	cudaMalloc(&dc, 6*sizeof(int));
	cudaMemcpy(da, &a, 6*sizeof(int), cudaMemcpyHostToDevice);
	cudaMemcpy(db, &b, 6*sizeof(int), cudaMemcpyHostToDevice);
	sub<<<1,6>>>(da,db,dc);
	cudaMemcpy(&c, dc, 6*sizeof(int), cudaMemcpyDeviceToHost);
	for (int j=0; j<6; j++){
		cout<<b[j]<<" - "<<a[j]<<" = "<<c[j]<<endl;
	}
	cudaFree(da);
	cudaFree(db);
	cudaFree(dc);
	return 0;
}

