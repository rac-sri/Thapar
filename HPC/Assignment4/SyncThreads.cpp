.Write a CUDA program pairwise sum of elements of vector to showcase concept of syncthreads.

#include<iostream>
using namespace std;
__global__ void fun(int *a, int *b){
	int t = threadIdx.x;
	int n = blockDim.x;
	while(n!=0){
		if (t<n){
	// eg. a[0] += a[0+n], similary for other indices, this would resuse the array again and again and keep on adding values.
		a[t] += a[t+n];
		}
		__syncthreads();
		n = n/2;
	}
	*b = a[0];
}
int main(){
	int N = 8;
	int a[N], b;
	for(int i=0; i<N; i++){
		a[i] = 2*i+11;
	}
	int *da, *db;
	cudaMalloc(&da, N*sizeof(int));
	cudaMalloc(&db, sizeof(int)); 
	cudaMemcpy(da, &a, N*sizeof(int), cudaMemcpyHostToDevice);
	cudaMemcpy(db, &b, sizeof(int), cudaMemcpyHostToDevice);
	fun<<<1,N/2>>>(da, db);
	cudaMemcpy(&b, db, sizeof(int), cudaMemcpyDeviceToHost);
	cout<<"Res: "<<b<<endl;
	cudaFree(da);
	cudaFree(db);
	return 0;
}