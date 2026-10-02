import java.util.*;

class Solution {
    int[] parent;
    public int solution(int n, int[][] costs) {
        int answer = 0;
        parent = new int[n+1];
        for (int i=1; i<=n; i++){
            parent[i] = i;
        }
        Arrays.sort(costs, (o1, o2) -> Integer.compare(o1[2], o2[2]));
        
        for (int[] cost:costs){
            int u = cost[0];
            int v = cost[1];
            int d = cost[2];
            
            if (find(u) != find(v)){
                union(u, v);
                answer += d;
            }
        }
        
        return answer;
    }
    
    private int find(int node){
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }
    
    private void union(int u, int v){
        int ru = find(u), rv = find(v);
        if (ru != rv) parent[rv] = ru;
    }
}