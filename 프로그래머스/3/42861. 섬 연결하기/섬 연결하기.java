import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        ArrayList<int[]>[] graph = new ArrayList[n];
        for (int i=0; i<n; i++){
            graph[i] = new ArrayList<>();
        }
        
        for (int[] cost:costs){
            int u = cost[0];
            int v = cost[1];
            int d = cost[2];
            graph[u].add(new int[] {v, d});
            graph[v].add(new int[] {u, d});
        }
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1[1], o2[1]));
        boolean[] visited = new boolean[n];
        
        int answer = 0;
        int cnt = 0;
        pq.offer(new int[] {0, 0});
        while (!pq.isEmpty()){
            int[] curr = pq.poll();
            
            int node = curr[0];
            int cost = curr[1];
            if(visited[node]) continue;
            
            visited[node] = true;
            answer += cost;
            cnt++;
            
            for (int[] next:graph[node]){
                int nxtNode = next[0];
                int nxtCost = next[1];
                
                if (!visited[nxtNode]) pq.offer(next);
            }
            
        }
        
        
        return answer;
    }
    
}