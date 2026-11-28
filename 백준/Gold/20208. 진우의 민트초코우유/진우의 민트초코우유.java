import java.util.*;
import java.io.*;

public class Main {
  static int N, M, H, L, answer, home;
  static int[] milk;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    H = Integer.parseInt(st.nextToken());
    
    milk = new int[10];
    home = -1;
    for(int r=0; r<N; r++){
      st = new StringTokenizer(br.readLine());
      for (int c=0; c<N; c++){
        int v = Integer.parseInt(st.nextToken());
        if(v == 1){
          home = r*N+c;
        } else if (v == 2){
          milk[L++] = r*N+c;
        }
      }
    }

    backTrack(0, 0, M, home);
    System.out.println(answer);
  }

  private static void backTrack(int k, int mask, int health, int pos){
    int r = pos/N, c = pos%N, hr = home/N, hc = home%N;
    if(Math.abs(hr-r)+Math.abs(hc-c) <= health){
      answer = Math.max(answer, k);
    }
    if(k == L || answer == L) return;

    for (int nxt=0; nxt<L; nxt++){
      if((mask & (1<<nxt))>0) continue;
      int nr = milk[nxt]/N, nc = milk[nxt]%N;
      int d = Math.abs(r-nr)+Math.abs(c-nc);
      if(d > health) continue;
      backTrack(k+1, mask|(1<<nxt), health-d+H, milk[nxt]);
    }

  }
}


/*
최대 10개
백트래킹 10! = 360만

*/