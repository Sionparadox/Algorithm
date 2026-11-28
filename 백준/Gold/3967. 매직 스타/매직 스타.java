import java.util.*;
import java.io.*;

public class Main {
  static int[][] lines = new int[][] {{0, 2, 5, 7}, {0, 3, 6, 10}, {1, 2, 3, 4}, {1, 5, 8, 11}, {4, 6, 9, 11}, {7, 8, 9, 10}};
  static int[] star;
  static boolean flag;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int idx = 0;
    star = new int[12];
    int mask = 0;
    for (int i=0; i<5; i++){
      String line = br.readLine();
      for (char c:line.toCharArray()){
        if (c == '.') continue;
        if (c != 'x') {
          star[idx] = c-'A'+1;
          mask |= (1<<star[idx]);
        }
        idx++;
      }
    }
    
    backTrack(0, mask);
  }

  private static void backTrack(int pos, int mask){
    if(flag) return;
    if(pos == 12){
      if(check()){
        flag = true;
        print();
      }
      return;
    }
    if(star[pos] > 0) {
      backTrack(pos+1, mask);
      return;
    }

    for (int v=1; v<=12; v++){
      if((mask & (1<<v)) > 0) continue;
      star[pos] = v;
      backTrack(pos+1, mask|(1<<v));
      star[pos] = 0;
    }
  }

  private static boolean check(){
    for (int[] line:lines){
      int cnt = 0;
      for (int v:line) cnt += star[v];
      if(cnt != 26) return false;
    }
    return true;
  }

  private static void print(){
    StringBuilder sb = new StringBuilder();
    sb.append("....").append(toChar(star[0])).append("....").append("\n");
    sb.append(".").append(toChar(star[1])).append(".").append(toChar(star[2])).append(".").append(toChar(star[3])).append(".").append(toChar(star[4])).append(".").append("\n");
    sb.append("..").append(toChar(star[5])).append("...").append(toChar(star[6])).append("..").append("\n");
    sb.append(".").append(toChar(star[7])).append(".").append(toChar(star[8])).append(".").append(toChar(star[9])).append(".").append(toChar(star[10])).append(".").append("\n");
    sb.append("....").append(toChar(star[11])).append("....").append("\n");
    System.out.println(sb);
  }

  private static char toChar(int x){
    return (char) (x+'A'-1);
  }
}

/*
   0
1 2 3 4
 5   6
7 8 9 10
   11

mask ; 2^13

각 인덱스가 속하는 라인 인덱스를 구하고
해당 라인의 합을 구하며 가지치기하면 성능 향상 가능
*/