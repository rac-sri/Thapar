// Write a CUDA program for dot product using 1 block to showcase concept of shared memory.

#include<iostream>
using namespace std;
__global__ void dot_product(int *a, int *b, int *c){
	int i = threadIdx.x;
	// this allows accessing shared memory of all the threads of a block
	__shared__ int temp[6];
	temp[i] = b[i] * a[i];
	// this will ensure completion of all threads
	__syncthreads();
	if (threadIdx.x == 0){
		int res = 0;
		for (int i=0; i<6; i++){
			res += temp[i];
		}
		*c = res;
	}
}

int main(){
	int size = 6;
	int a[size],b[size],c;
	cout<<"Enter elements of a: ";
	for(int i=0; i<size; i++){
		cin>>a[i];
	}
	cout<<"Enter elements of b: ";
	for(int i=0; i<size; i++){
		cin>>b[i];
	}
	
	int *da, *db, *dc;
	cudaMalloc(&da, size*sizeof(int)); 
	cudaMalloc(&db, size*sizeof(int));
	cudaMalloc(&dc, sizeof(int)
            cudaMemcpy(da, &a, size*sizeof(int), cudaMemcpyHostToDevice);
	cudaMemcpy(db, &b, size*sizeof(int), cudaMemcpyHostToDevice);
	dot_product<<<1,6>>>(da,db,dc);
	cudaMemcpy(&c, dc, sizeof(int), cudaMemcpyDeviceToHost);
	cout<<c<<endl;
	cudaFree(da);
	cudaFree(db);
	cudaFree(dc);
	return 0;
}

