import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int v:scoville){
            pq.offer(v);
        }
        
        while (pq.size() >= 2 && pq.peek() < K){
            int s1 = pq.poll();
            
            int s2 = pq.poll();
            int value = s1 + s2*2;
            
            pq.offer(value);
            answer++;
        }
        if (pq.peek() < K) return -1;
        
        
        return answer;
    }
}
/*
first , second*2
*/