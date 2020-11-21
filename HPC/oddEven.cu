#include<stdio.h>
#include<cuda.h>
#define N 20
#include <time.h>
#include <stdlib.h>
#include<iostream>
#define intswap(A,B) {int temp=A;A=B;B=temp;}
using namespace std;
__global__ void sort(int *c,int *count)
{
    int l;
    if(*count%2==0)
          l=*count/2;
    else
         l=(*count/2)+1;
    for(int i=0;i<l;i++)
    {
            if((!(threadIdx.x&1)) && (threadIdx.x<(*count-1)))  //even phase
            {
                if(c[threadIdx.x]>c[threadIdx.x+1])
                  intswap(c[threadIdx.x], c[threadIdx.x+1]);
            }
            __syncthreads();
            if((threadIdx.x&1) && (threadIdx.x<(*count-1)))     //odd phase
            {
                if(c[threadIdx.x]>c[threadIdx.x+1])
                  intswap(c[threadIdx.x], c[threadIdx.x+1]);
            }
            __syncthreads();
    }
}
int main()
{
 clock_t tStart = clock();
 int a[N],b[N],n;
 n=10;
 srand(time(NULL)); 
 for(int i=0;i<n;i++) {
     int r= rand()%10;
     a[i]=r;
 }
  printf("Array Before Sorting: \n");
  for(int i=0;i<n;i++)
          {
          printf("%d ",a[i]);
          }
  int *c,*count;
  cudaMalloc((void**)&c,sizeof(int)*N);
  cudaMalloc((void**)&count,sizeof(int));
  cudaMemcpy(c,&a,sizeof(int)*N,cudaMemcpyHostToDevice);
  cudaMemcpy(count,&n,sizeof(int),cudaMemcpyHostToDevice);
  sort<<< 1,n >>>(c,count);
  cudaMemcpy(&b,c,sizeof(int)*N,cudaMemcpyDeviceToHost);
  printf("\nSorted Array using Cuda C : \n");
  for(int i=0;i<n;i++)
      {
         printf("%d ",b[i]);
      }
  printf("\n");
 cout<<"Execution Time:"<<(double)(clock() - tStart)/CLOCKS_PER_SEC;
}

