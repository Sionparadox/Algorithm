import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int N = Integer.parseInt(br.readLine());
      int K = Integer.parseInt(br.readLine());

      int left = 1, right = K;
      long answer = 0;

      while(left <= right){
        int mid = (left+right)/2;

        long cnt = 0;
        for (int i=1; i<=N; i++){
          cnt += Math.min(N, mid/i);
        }

        if(cnt >= K){
          answer = mid;
          right = mid-1;
        } else {
          left = mid+1;
        }
      }
      
      System.out.println(answer);
    }
}

/*
 1  2  3  4  5
 2  4  6  8 10
 3  6  9 12 15
 4  8 12 16 20
 5 10 15 20 25

11 이하
5
5
3

*/