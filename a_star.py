import heapq

came_from = {}

def astar(grid, start, goal):
    # Define the heuristic function
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    # Define the cost function
    def cost(current, next):
        return 1
    
    # Initialize the open and closed lists
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))
    
    # Initialize the g and f scores for the starting position
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    # Loop until the open list is empty
    while open_list:
        # Pop the item with the lowest f score from the open list
        current_f, current = heapq.heappop(open_list)
        
        # Check if we've reached the goal
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        # Add the current position to the closed list
        closed_list.add(current)
        
        # Loop over the neighbors of the current position
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = current[0] + i, current[1] + j
            
            # Check if the neighbor is a valid position
            if not 0 <= neighbor[0] < len(grid) or not 0 <= neighbor[1] < len(grid[0]):
                continue
            
            # Check if the neighbor is an obstacle or is already in the closed list
            if grid[neighbor[0]][neighbor[1]] == 1 or neighbor in closed_list:
                continue
            
            # Calculate the tentative g score for the neighbor
            tentative_g_score = g_score[current] + cost(current, neighbor)
            
            # If the neighbor is not in the open list, add it
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    # If we get here, there is no path to the goal
    return None

def a_star_algo(grid,start,goal):
    path = astar(grid, start, goal)
    return path
