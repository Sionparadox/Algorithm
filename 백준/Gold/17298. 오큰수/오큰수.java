import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int N = Integer.parseInt(br.readLine());
      StringTokenizer st = new StringTokenizer(br.readLine());
      int[] arr = new int[N];
      for (int i=0; i<N; i++) arr[i] = Integer.parseInt(st.nextToken());
      int[] answer = new int[N];
      Arrays.fill(answer, -1);
      ArrayDeque<int[]> stack = new ArrayDeque<>();
      for(int i=0; i<N; i++){
        while(!stack.isEmpty() && stack.peek()[0]<arr[i]){
          int[] left = stack.pop();
          answer[left[1]] = arr[i];
        }
        stack.push(new int[] {arr[i], i});
      }
      StringBuilder sb = new StringBuilder();
      for (int e:answer) sb.append(e).append(" ");
      System.out.println(sb);
    }
}