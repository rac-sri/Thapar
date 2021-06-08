#include <iostream>
#include <fstream>
using namespace std;


void matrix_mul(float *restrict r, float *a, float *b, int N, int accelerate){

#pragma acc data copyin (a[0: N * N ], b[0: N * N]) copyout (r [0: N * N ]) if(accelerate)
{
# pragma acc region if(accelerate)
{
# pragma acc loop independent vector(32) 
for (int j = 0; j < N; j ++)
{    
   # pragma acc loop independent vector(32) 
   for (int i = 0; i < N ; i ++ )
   {
      float sum = 0;
      for (int k = 0; k < N ; k ++ ) {
         sum += a [ i + k*N ] * b [ k + j * N ];
      }
      r[i + j * N ] = sum ;
   }
}
}
}
}


int main() {
    ifstream fin("fname.txt"); 
    int word=1; 
    char ch;
    fin.seekg(0,ios::beg); 
    
    while(fin)
    {
    fin.get(ch);
    if(ch==' '||ch=='\n')
    word++;
    } 
    
    float r[word];
    float a[word/2];
    float b[word/2];
    int t=0;
    int q=0;

    std::string line;

    while(getline(fin, line))
    {
        
    for(int i = 0; i < line.length()/2; ++i)
    {       
    char ch = line[i]; 
    if(ch==' '||ch=='\n'){
        continue;
    }
    else {
        a[t] = ch;
        t++;
    }
    }

    for(int i = line.length()/2; i < line.length(); ++i)
    {       
    char ch = line[i]; 
    if(ch==' '||ch=='\n'){
        continue;
    }
    else {
        b[t] = ch;
        t++;
    }
    }

    }

    matrix_mul(r,a,b,word/2,5);

}