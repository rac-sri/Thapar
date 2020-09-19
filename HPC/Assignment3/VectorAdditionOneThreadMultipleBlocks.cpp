// Write a CUDA program vector addition of numbers using 1 thread and multiple blocks

#include<iostream>
using namespace std;
__global__ void add(int *a, int *b, int *c){
	int i = blockIdx.x;
	c[i] = a[i]+b[i];
}
int main(){
	int c[6];
	int a[6] = {1,2,3,4,5,6};
	int b[6] = {11,12,13,14,15,16};
	int *da, *db, *dc;
	cudaMalloc(&da, 6*sizeof(int));
	cudaMalloc(&db, 6*sizeof(int));
	cudaMalloc(&dc, 6*sizeof(int));
	cudaMemcpy(da, &a, 6*sizeof(int), cudaMemcpyHostToDevice);
	cudaMemcpy(db, &b, 6*sizeof(int), cudaMemcpyHostToDevice);
	add<<<6,1>>>(da,db,dc);
	cudaMemcpy(&c, dc, 6*sizeof(int), cudaMemcpyDeviceToHost);
	for (int j=0; j<6; j++){
		cout<<a[j]<<" + "<<b[j]<<" = "<<c[j]<<endl;
	}
	cudaFree(da);
	cudaFree(db);
	cudaFree(dc);
	return 0;
}