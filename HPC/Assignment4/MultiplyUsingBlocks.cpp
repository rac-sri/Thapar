//  Write a CUDA program vector multiplication of numbers using multiple blocks and multiple threads

#include<iostream>
using namespace std;
__global__ void mul(int *a, int *b, int *c){
	int j = blockDim.x;
	// blockDim specifies no. of threads in each block
	int i = blockIdx.x*j + threadIdx.x;
	c[i] = b[i]*a[i];
	// c[i] = i;
}nv
int main(){
	int a[6],b[6],c[6];
	for(int i=0; i<6; i++){
		a[i] = 2*i+11;
		b[i] = 4*i+7;
	}
	int *da, *db, *dc;
	cudaMalloc(&da, 6*sizeof(int)); 
	cudaMalloc(&db, 6*sizeof(int));
	cudaMalloc(&dc, 6*sizeof(int));
	cudaMemcpy(da, &a, 6*sizeof(int), cudaMemcpyHostToDevice);
	cudaMemcpy(db, &b, 6*sizeof(int), cudaMemcpyHostToDevice);
	mul<<<2,3>>>(da,db,dc);
	cudaMemcpy(&c, dc, 6*sizeof(int), cudaMemcpyDeviceToHost);
	for (int j=0; j<6; j++){
		cout<<b[j]<<" * "<<a[j]<<" = "<<c[j]<<endl;
	}
	cudaFree(da);
	cudaFree(db);
	cudaFree(dc);
	return 0;
}
