%%cu
#include<bits/stdc++.h>
#include<stdio.h>
#include<cuda.h>
#define N 20
#include <time.h>
#include <stdlib.h>
#include <fstream>
#include <string.h>
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
            if((!(threadIdx.x&1)) && (threadIdx.x<(*count-1)))  //even 
            {
                if(c[threadIdx.x]>c[threadIdx.x+1])
                  intswap(c[threadIdx.x], c[threadIdx.x+1]);
            }
            __syncthreads();
            if((threadIdx.x&1) && (threadIdx.x<(*count-1)))     //odd 
            {
                if(c[threadIdx.x]>c[threadIdx.x+1])
                  intswap(c[threadIdx.x], c[threadIdx.x+1]);
            }
            __syncthreads();
    }
}

void getData(char buff[],int *a,int &i) 
{ 
		
   char *token = strtok(buff,","); 
	//cout<<token<<endl;
   int counter=0; 
		
	
		  
   while( token != NULL&&i<N )  
   { 
 counter++; 
 //cout<<token<<" ";
			a[i]=atoi(token);
			 i++;
// fgets(buff, N, (FILE*)fp); 
	 count++; 
…printf( " %s\n",token); 
      token = strtok(NULL,","); 
			 

   }	 
	//cout<<endl;  
} 


void fill(int *a){
		
  FILE *fp = fopen("data2.csv", "r");
      int count=0; 
			int i=0;
	do 
	{ 
	 char buff[1000000]; 
	 fgets(buff, N, (FILE*)fp); 
	 count++; 
	 if(count != 1) 
	 { 
	  //printf(buff);
		 //cout<<endl; 
		 if(i<N){
	 
	  getData(buff,a,i);
		} 
	 } 
	}while((getc(fp))!=EOF&&i<N);
}



int main()
{
    clock_t tStart = clock();
    int b[N],n;
   n=10;
     int *a;
 a=new int[N];
 fill(a);

 srand(time(NULL)); 

for(int x=0;x<n;x++){
    
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

