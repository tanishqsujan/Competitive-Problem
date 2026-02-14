def longest_path(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_length = 0
    
    def dfs(i, j):
        if dp[i][j] > 0:
            return dp[i][j]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_path = 1  #Minimum length is always 1
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                max_path = max(max_path, 1 + dfs(x, y))
                
        dp[i][j] = max_path
        return max_path
    
    for i in range(rows):
        for j in range(cols):
            max_length = max(max_length, dfs(i, j))
            
    return max_length


matrix = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 9]
]

print(longest_path(matrix))
#(Longest path: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9)