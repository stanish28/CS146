class Solution:
    def floodFill(self, image, sr, sc, color):
        m, n = len(image), len(image[0])
        originalColor = image[sr][sc]
        
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != originalColor or image[x][y] == color:
                return
            image[x][y] = color
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            
        dfs(sr, sc)
        return image
