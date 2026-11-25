import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    boolean[] down = new boolean[N];
    for (int i=0; i<N; i++) down[i] = Integer.parseInt(st.nextToken()) < 0;

    ArrayDeque<int[]> stack = new ArrayDeque<>();
    
    int maxLength = 0, start = -1;

    for(int i=0; i<N; i++){
      if(down[i]){
        if(start == -1) start = i;
      }
      else if (start != -1){
        int length = i-start;
        stack.push(new int[] {start, length});
        maxLength = Math.max(maxLength, length);
        start = -1;
      }
    }
    
    if(start != -1){
      int length = N-start;
      stack.push(new int[] {start, length});
      maxLength = Math.max(maxLength, length);
    }

    if(stack.isEmpty()){
      System.out.println(0);
      return;
    }

    int[] diff = new int[N];

    for (int[] curr:stack){
      int s = curr[0];
      int d = curr[1];

      int left = Math.max(0, s-2*d);
      int right = s-1;
      if(left<=right){
        diff[left]++;
        diff[right+1]--;
      }
    }

    int[] prefix = new int[N+1];
    int sum = 0;
    for(int i=0; i<N; i++){
      sum += diff[i];
      prefix[i+1] = prefix[i]+ (sum>0 ? 1 : 0);
    }

    int answer = prefix[N];
    int remain = 0;

    for (int[] curr:stack){
      int s = curr[0];
      int d = curr[1];

      if(d != maxLength) continue;

      int left = Math.max(0, s-3*d);
      int right = s-1-2*d;

      if(left > right) continue;

      int len = right-left+1;
      int k = len - (prefix[right+1]-prefix[left]);
      remain = Math.max(remain, k);
    }

    System.out.println(answer+remain);  
  }
}


/*
뒤에가 엄청 크면 앞에 상관없이 다 덮어버리면 됨
15
1 2 1 2 3 -4 5 6 1 -4 -8 -3 -1 -2 1
*/