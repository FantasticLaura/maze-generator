import random
class Maze:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.visited = set()
        self.walls = set()
        self.visited = set()

    def generate_maze(self, current_cell):
        stack = []
        stack.append(current_cell)
        self.visited.add(current_cell)
        while stack != []:
            current_cell = stack[-1] #last one of the stack list 
            unvisited = []
            neighbourd_coordinates = ((2,0), (0,2), (-2,0), (0,-2))
            for dx, dy in neighbourd_coordinates:
                nx = current_cell[0]+dx
                ny = current_cell[1]+dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) not in self.visited:
                        unvisited.append((nx, ny, nx - dx // 2, ny - dy // 2)) #dx/2=1 or 0
                    elif (nx, ny) in self.visited and random.random() < 0.1:#random.random gives a number from 0 to 1
                        unvisited.append((nx, ny, nx - dx // 2, ny - dy // 2))                   
            if unvisited:
                next_cell = random.choice(unvisited)
                self.visited.add((next_cell[0], next_cell[1]))#from ((nx (0), ny (1), nx - dx // 2 (2), ny - dy // 2 (3)))
                self.visited.add((next_cell[2], next_cell[3])) #adds to the visited set also step in between, as it goes from 0 to 2, so cell 1. 
                stack.append((next_cell[0], next_cell[1]))
            else:
                stack.pop() #if visited, delete from the stack pile so it can revisit
        self.walls = {
            (x,y) for x in range(self.width)
                  for y in range(self.height)
        }.difference(self.visited)

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x,y) in self.walls:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()

def BFS(maze, start, end):
    # Get all the cells' parents
    queue = [start]
    visited = dict()
    while queue != []:
        v = queue.pop(0)
        if v == end:
            break
        for dx, dy in ((2,0), (0,2), (-2,0), (0,-2)):
            nx = v[0]+dx
            ny = v[1]+dy
            ix = v[0] + dx // 2
            iy = v[1] + dy // 2
            if (nx, ny) not in visited and (ix, iy) not in maze.walls and 0 <= nx < maze.width and 0 <= ny < maze.height:
                visited[(nx, ny)] = v
                queue.append((nx, ny))
                
    # Reconstruct the path from the end
    path = []
    current = end
    while current != start:
        path.append(current)
        current = visited[current]
    path.append(start)

    for y in range(maze.height):
        for x in range(maze.width):
            if (x,y) in path:
                print("@", end="")
            elif (x,y) in maze.walls:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    return path


                    
my_maze = Maze(10, 10)
playing_cell=my_maze.generate_maze((0, 0))
my_maze.print()
#BFS(my_maze, (0, 0), (my_maze.width - 1, my_maze.height - 1))
path = BFS(my_maze, (0, 0), (8,8)) #8,8 as the maze is 9,9 in steps of 2
print(path)

