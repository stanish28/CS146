public class solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int m = image.length, n = image[0].length;
        int originalColor = image[sr][sc];
        
        dfs(image, sr, sc, color, originalColor, m, n);
        return image;
    }
    
    private void dfs(int[][] image, int x, int y, int color, int originalColor, int m, int n) {
        if (x < 0 || x >= m || y < 0 || y >= n || image[x][y] != originalColor || image[x][y] == color) {
            return;
        }
        
        image[x][y] = color;
        dfs(image, x+1, y, color, originalColor, m, n);
        dfs(image, x-1, y, color, originalColor, m, n);
        dfs(image, x, y+1, color, originalColor, m, n);
        dfs(image, x, y-1, color, originalColor, m, n);
    }
}
