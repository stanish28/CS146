import java.util.*;

public class WaterSupplySystem {
    public int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        // Graph representation using adjacency list
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }

        // Adding virtual node (node 0) edges with well costs
        for (int i = 1; i <= n; i++) {
            adj.get(0).add(new int[]{wells[i - 1], i});
            adj.get(i).add(new int[]{wells[i - 1], 0});
        }

        // Adding pipes to adjacency list
        for (int[] pipe : pipes) {
            int house1 = pipe[0];
            int house2 = pipe[1];
            int cost = pipe[2];
            adj.get(house1).add(new int[]{cost, house2});
            adj.get(house2).add(new int[]{cost, house1});
        }

        // Prim's algorithm using a PriorityQueue
        boolean[] visited = new boolean[n + 1]; // track visited houses and the virtual node
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, 0}); // start from the virtual node

        int mstCost = 0;
        int edgesUsed = 0;

        while (!pq.isEmpty() && edgesUsed <= n) {
            int[] edge = pq.poll();
            int cost = edge[0];
            int house = edge[1];

            if (visited[house]) {
                continue;
            }

            // Include this edge in MST
            mstCost += cost;
            visited[house] = true;
            edgesUsed++;

            // Add all adjacent edges from the current house
            for (int[] next : adj.get(house)) {
                if (!visited[next[1]]) {
                    pq.offer(next);
                }
            }
        }

        return mstCost;
    }

    public static void main(String[] args) {
        WaterSupplySystem solver = new WaterSupplySystem();
        int n = 2;
        int[] wells = {1, 1};
        int[][] pipes = {{1, 2, 1}, {1, 2, 2}};
        int result = solver.minCostToSupplyWater(n, wells, pipes);
        System.out.println("Minimum cost to supply water: " + result);
    }
}
