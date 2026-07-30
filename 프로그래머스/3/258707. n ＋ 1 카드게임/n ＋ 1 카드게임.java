import java.util.*;

class Solution {
    public int solution(int coin, int[] cards) {
        int answer = 0;
        int N = cards.length;
        
        Set<Integer> mine = new HashSet<>();
        int[] pair = {0, 0, 0};
        for (int i = 0;i<N/3;i++){
            int card = cards[i];
            if (mine.contains(N+1-card)){
                mine.remove(N+1-card);
                pair[0]++;
            } else {
                mine.add(card);
            }
        }
        
        Set<Integer> waits = new HashSet<>();  

        for (int i=N/3;i<N;i+= 2){
            for (int j=i;j<i+2;j++){
                int card = cards[j];
                if (mine.contains(N+1-card)){
                    mine.remove(N+1-card);
                    pair[1]++;
                } else if (waits.contains(N+1-card)){
                    waits.remove(N+1-card);
                    pair[2]++;
                } else {
                    waits.add(card);
                }
                
            }
            
            if (pair[0] > 0){
                pair[0]--;
            } else if (coin >= 1 && pair[1]>0){
                pair[1]--;
                coin--;
            } else if (coin >= 2 && pair[2]>0){
                pair[2]--;
                coin -= 2;
            } else {
                break;
            }
            answer++;
        }
        
        return answer+1;
    }
}



/*
2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]


1 2             1
1 2     9 4     1


dp[i][coin] : i번째 턴을 진행했을 때 동전 coin개를 남기고 얻는 최대 pair수

1) mine에서 발견 할 때
2) waits에서 발견 할 때
dp[turn][coin] = dp[turn-1][coin-2]

*/