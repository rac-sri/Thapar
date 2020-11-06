#include<stdio.h>
#include<cuda.h>
_global_ void c_hello(int* a1_d,int* a2_d,int* a3_d)
{
	a3_d[blockIdx.x]=0;
	//printf("\n%d y",*(a1_d));
	for(int i=0;i<3;i++)
	{
		a3_d[blockIdx.x]+=int((a1_d+3(blockIdx.x)+i))int((a2_d +3*(blockIdx.x) +i));
	}
	printf("%d \n",a3_d[blockIdx.x]);
	return;
}

int main()
{
	unsigned int n;
	scanf("%d",&n);
	int *arr1,*arr2,*a1_d,*a2_d,*a3_d;
	arr1=(int*)malloc(sizeof(int)*n*3);
	arr2=(int*)malloc(sizeof(int)*n*3);
	for(int i=0;i<n;i++)
	{
		int x,y,z;
		scanf("%d%d%d",&x,&y,&z);
		*(arr1+3*i)=x;
		*(arr1+i*3+1)=y;
		*(arr1+i*3+2)=z;
		scanf("%d%d%d",&x,&y,&z);
		*(arr2+i*3)=x;
		*(arr2+i*3+1)=y;
		*(arr2+i*3+2)=z;
	}
	cudaMalloc((void**) &a1_d,sizeof(int)*n*3);
	cudaMalloc((void**) &a2_d,sizeof(int)*n*3);
	cudaMalloc((void**) &a3_d,sizeof(int)*n);
	cudaMemcpy(a1_d,arr1,sizeof(int)*n*3,cudaMemcpyHostToDevice);
	cudaMemcpy(a2_d,arr2,sizeof(int)*n*3,cudaMemcpyHostToDevice);
	//printf("cpu %d\n",*arr1);
	dim3 dd;
	dd={n};
	//cudaMalloc((void**)&d_a, sizeof(int) * 1024);
	c_hello<<<dd,1>>>(a1_d,a2_d,a3_d);
	cudaDeviceSynchronize();
	return 0;
}