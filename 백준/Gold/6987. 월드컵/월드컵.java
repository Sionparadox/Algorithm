import java.util.*;
import java.io.*;

public class Main {
  static int[][] games;
  static boolean answer;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    StringBuilder sb = new StringBuilder();

    for (int t=0; t<4; t++){
      games = new int[6][3];
      answer = false;
      st = new StringTokenizer(br.readLine());
      int sum = 0;
      for(int i=0; i<6; i++){
        for (int j=0; j<3; j++){
          games[i][j] = Integer.parseInt(st.nextToken());
          sum += games[i][j];
        }
      }
      if(sum == 30) backTrack(0);
      sb.append(answer? 1 : 0).append(" ");
    }
    System.out.println(sb);
  }

  private static void backTrack(int match){
    if(answer) return;
    if(match == 15){
      answer = true;
      return;
    }

    int[] team = matchToTeam(match);
    int x = team[0], y = team[1];
    // x승
    if(games[x][0]>0 && games[y][2]>0){
      games[x][0]--;
      games[y][2]--;
      backTrack(match+1);
      games[x][0]++;
      games[y][2]++;
    }
    // 무
    if(games[x][1]>0 && games[y][1]>0){
      games[x][1]--;
      games[y][1]--;
      backTrack(match+1);
      games[x][1]++;
      games[y][1]++;
    }

    // x패
    if(games[x][2]>0 && games[y][0]>0){
      games[x][2]--;
      games[y][0]--;
      backTrack(match+1);
      games[x][2]++;
      games[y][0]++;
    }
  }

  private static int[] matchToTeam(int match){
    int cnt = 0;
    for(int i=0; i<5; i++){
      for (int j=i+1; j<6; j++){
        if(cnt == match) return new int[] {i, j};
        cnt++;
      }
    }
    return new int[] {-1, -1};
  }
}

/*
15번 경기
승합 = 패합, 무/2 =0
전체 = 30

한팀이랑 한번만 경기해야함
c 무 2, d 무 2, 나머지 무 0이면 안되는 케이스
전체 수가 맞더라도 같은 매치가 나오면 안되는 케이스

3^15
2 9
4 81
6 729
7 2187
14 약 4_000_000
15 1200만 이상

15
0 1 2 3 4 5
1 2 3 4 5
2 3 4 5
3 4 5
4 5
*/