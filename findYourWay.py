maze = [
    [0,0,0,0,1,0,0,0],
    [0,0,0,1,1,1,0,0],
    [0,0,1,1,0,0,1,0],
    [1,1,1,1,0,1,0,0],
    [1,0,0,1,0,1,1,0],
    [0,1,1,1,1,0,0,0],
    [0,0,1,0,1,1,1,0],
    [0,0,2,0,0,0,0,0]
]

def findways(moveX, moveY):
    ways = []
    if 0 <= moveX < len(maze) and 0 <= moveY < len(maze):
        if maze[moveX+1][moveY] == 1 or maze[moveX+1][moveY] == 2: ways.append((moveX+1, moveY))
        if maze[moveX-1][moveY] == 1 or maze[moveX-1][moveY] == 2: ways.append((moveX-1, moveY))
        if maze[moveX][moveY+1] == 1 or maze[moveX][moveY+1] == 2: ways.append((moveX, moveY+1))
        if maze[moveX][moveY-1] == 1 or maze[moveX][moveY-1] == 2: ways.append((moveX, moveY-1))
    return ways

def findExitWay(moveX, moveY, x, y):
    if maze[moveX][moveY] == 2:
        return moveX, moveY
    else:
        maze[moveX][moveY] = -1
        print moveX, moveY
        ways = findways(moveX, moveY)
        if len(ways) > 1:
            x = moveX
            y = moveY
            (moveX, moveY) = ways[0]
        elif len(ways) == 1:
            (moveX, moveY) = ways[0]
        elif len(ways) == 0:
            moveX = x
            moveY = y
        return findExitWay(moveX, moveY, x, y)
            
print findExitWay(0, 4, -1, -1)
print maze