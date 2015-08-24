maze = [
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,1,0,1,1,1,0,0,0,0],
    [1,1,1,0,1,0,1,0,0,1,0,0,0,0,0],
    [1,0,0,0,1,1,1,1,1,1,0,0,0,1,0],
    [1,1,1,1,0,0,1,0,0,1,0,0,0,1,0],
    [0,0,0,1,0,1,0,0,1,1,1,1,0,1,0],
    [0,1,1,1,1,1,1,0,1,0,0,1,0,1,0],
    [0,0,0,1,0,0,0,1,1,1,0,1,0,1,0],
    [0,0,0,1,0,0,0,0,1,0,0,1,1,1,0],
    [0,0,0,1,0,0,0,0,1,0,0,0,0,1,0],
    [0,0,0,1,0,0,0,1,1,1,1,0,1,1,0],
    [0,0,0,1,0,0,0,0,0,1,0,1,0,1,0],
    [0,0,0,1,0,0,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0]
]

def findWays(moveX, moveY):
    ways = []
    if 0 <= moveX < len(maze) and 0 <= moveY < len(maze):
        if maze[moveX+1][moveY] in [1,2]: ways.append((moveX+1, moveY))
        if maze[moveX-1][moveY] in [1,2]: ways.append((moveX-1, moveY))
        if maze[moveX][moveY+1] in [1,2]: ways.append((moveX, moveY+1))
        if maze[moveX][moveY-1] in [1,2]: ways.append((moveX, moveY-1))
    return ways

def findExitWay(moveX, moveY, junction):
    if maze[moveX][moveY] == 2:
        return moveX, moveY
    else:
        maze[moveX][moveY] = -1
        ways = findWays(moveX, moveY)
        if len(ways) > 1:
            for way in ways:
                junction.append(way)
            (moveX, moveY) = junction.pop()
        elif len(ways) == 1:
            (moveX, moveY) = ways[0]
        elif len(ways) == 0:
            (moveX, moveY) = junction.pop() 
        return findExitWay(moveX, moveY, junction)
            
print findExitWay(0, 4, [])