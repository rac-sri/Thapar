#include "stdio.h"

__global__ void cuda_hello(){
    printf("Hellp world from GPU");
}

int main(){
    cuda_hello<<<1,1>>>();
    return 0;
}