#include<bits/stdc++.h>
using namespace std;
fstream fin;

__global__ void matMul(float *A,float *B,float *C,int n) {

    int ROW = blockIdx.y*blockDim.y+threadIdx.y;
    int COL = blockIdx.x*blockDim.x+threadIdx.x;
    int idx=ROW*n+COL;

    if (ROW < n && COL < n) {
        C[idx]= A[idx ] * B[idx ];
    }
}

void matrixMultiplication(float *A, float *B, float *C, int N){
    
     dim3 threadsPerBlock(N, N);
     dim3 blocksPerGrid(1, 1);
      if (N*N > 512){
          threadsPerBlock.x = 512;
          threadsPerBlock.y = 512;
          blocksPerGrid.x = ceil(double(N)/double(threadsPerBlock.x));
          blocksPerGrid.y = ceil(double(N)/double(threadsPerBlock.y));
      }
      matMul<<<blocksPerGrid,threadsPerBlock>>>(A, B, C, N);
}
int main(){
     fin.open("./dataFile.csv", ios::in);
     clock_t st1,e1,st,end;
     int N=8;
     cout<<N<<endl;
     int size= N*N;
     float *h_A,*h_B,*h_C; //host
     float *d_A,*d_B,*d_C; //device copy GPU

     h_A=(float *)malloc(size);
     h_B=(float *)malloc(size);
     h_C=(float *)malloc(size);
     cudaMalloc((void **)&d_A, size);
     cudaMalloc((void **)&d_B, size);
     cudaMalloc((void **)&d_C, size);
     string s;
     fin>>s;
     stringstream str(s);
     for(int i=0; i<size; i++){
        getline(str,s,',');
        h_A[i] = stoi(s);
        cout<<h_A[i]<<" ";
     }
     cout<<endl;
     for(int i=0; i<size; i++){
        getline(str,s,',');
        h_B[i] = stoi(s);
        cout<<h_B[i]<<" ";
     }
    cout<<endl;
    st1=clock();
    for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                 cout<< h_A[i*N+j]*h_B[i*N+j]<<" ";
            }
            cout<<endl;
        }
        
     e1=clock();
    
    
     double time_taken =((double)(e1-st1))/CLOCKS_PER_SEC;
     cout<<"\ncomputational time using sequential is "<<time_taken<<" secs\n";
     cudaMemcpy(d_A,h_A,size,cudaMemcpyHostToDevice);
     cudaMemcpy(d_B,h_B,size,cudaMemcpyHostToDevice);
    
     st=clock();
     matrixMultiplication(d_A, d_B, d_C, N);

     cudaMemcpy(h_C,d_C,size,cudaMemcpyDeviceToHost);
     end=clock();
     cout<<endl;
     for(int i=0; i<N; i++){
         for(int j=0;j<N;j++)
         cout<<h_C[i*N+j]<<" ";
         cout<<endl;
     }
     
     double time_taken1 =((double)(end-st))/CLOCKS_PER_SEC;
     cout<<"\ncomputational time using cuda is "<<time_taken1<<" secs\n";
     fin.close();
     return 0; 
}