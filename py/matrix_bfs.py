from collections import deque

def bfs_matrix(matrix, start_row, start_col):
    # Define the queue and the visited set
    queue = deque([(start_row, start_col)])
    visited = set([(start_row, start_col)])
    
    # Define the directions to explore the neighboring cells
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Start the BFS
    while queue:
        row, col = queue.popleft()
        
        # Process the current cell
        print(matrix[row][col])
        
        # Explore the neighboring cells
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
                if (new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))