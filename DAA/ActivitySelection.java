// You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

import java.util.*;
import java.lang.*;
import java.io.*;

class ActivitySelection {
    public static void printMaxActivities(int s[], int f[], int n){
        int i,j;

        System.out.print("Following activitues are selected : \n");

        i = 0;
        System.out.print(i+" ");

        for(j=1;j<n;j++){
            if(s[j] >= f[i]){
                System.out.print(j+ " ");
                i=j;
            }
        }
    }

    public static void main(String[] args){
        int s[] =  {1, 3, 0, 5, 8, 5}; 
        int f[] =  {2, 4, 6, 7, 9, 9}; 
        int n = s.length; 
             
        printMaxActivities(s, f, n); 
    }
}