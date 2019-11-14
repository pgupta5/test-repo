def findAllPaths(node, childrenFn, depth, _depth=0, _parents={}):
    if _depth == depth - 1:
        # path found with desired length, create path and stop traversing
        path = []
        parent = node
        for i in range(0,depth):
            path.insert(0, parent)
            if not parent in _parents:
                continue
            parent = _parents[parent]
            if parent in path:
                return # this path is cyclic, forget
        yield path
        return

    for nb in childrenFn(node):
        _parents[nb] = node # keep track of where we came from
        for p in findAllPaths(nb, childrenFn, depth, _depth + 1, _parents):
            yield p
            
graph = {
    0: [1,2,3,4],       
    1: [2,3,4, 5,0],
    2: [1,3, 4,5],
    3: [0,1,2,4,6],
    4: [0,1,2,3,5,6,7,8],
    5: [1,2,4,7,8],
    6: [3,4,5,7,8],
    7: [3,4,5,6,8],
    8: [4,5,7]
}

for p in findAllPaths(1, lambda n: graph[n], depth=3):
    print(p)

#Creating a D dimensional Grid
import numpy as np
d = 4
subdivision = 10
step = 1.0/subdivision
grid = np.mgrid[tuple(slice(step-1,1.0-step,complex(0,subdivision)) for i in range (d))]

#Converting into an Adjacency Matrix
import numpy as np
import numpy.matlib #for matrices

def cutblocks(xv,yv,allBlocks):
    x_new,y_new = np.copy(xv), np.copy(yv)
    ori_x,ori_y = xv[0][0], yv[0][0]
    for block in allBlocks:
        block = sorted(block)
        block_xmin = np.min((block[0][0], block[2][0]))
        block_xmax = np.max((block[0][0], block[2][0]))
        block_ymin = np.min((block[0][1], block[1][1]))
        block_ymax = np.max((block[0][1], block[1][1]))

        rx_min, rx_max = int((block_xmin-ori_x)/stepSize)+1, int((block_xmax-ori_x)/stepSize)+1
        ry_min, ry_max = int((block_ymin-ori_y)/stepSize)+1, int((block_ymax-ori_y)/stepSize)+1

        for i in range(rx_min,rx_max):
            for j in range(ry_min,ry_max):
                x_new[j][i] = np.nan
        for i in range(ry_min,ry_max):
            for j in range(rx_min,rx_max):
                y_new[i][j] = np.nan
    return x_new, y_new

stepSize = 0.2
##Blocks that should be disabled
allBlocks = [[(139.6, 93.6), (143.6, 93.6), (143.6, 97.6), (139.6, 97.6)],
 [(154.2, 93.4), (158.2, 93.4), (158.2, 97.4), (154.2, 97.4)],
 [(139.2, 77.8), (143.2, 77.8), (143.2, 81.8), (139.2, 81.8)],
 [(154.2, 77.8), (158.2, 77.8), (158.2, 81.8), (154.2, 81.8)],
 [(139.79999999999998, 86.4),
  (142.6, 86.4),
  (142.6, 88.0),
  (139.79999999999998, 88.0)],
 [(154.79999999999998, 87.2),
  (157.6, 87.2),
  (157.6, 88.8),
  (154.79999999999998, 88.8)]]

x = np.arange(136.0, 161.0, stepSize)
y = np.arange(75.0, 101.0, stepSize)

xv, yv = np.meshgrid(x, y)
xv, yv = cutblocks(xv,yv,allBlocks)

MazeSize = xv.shape[0]*xv.shape[1]
adj = np.matlib.zeros((MazeSize,MazeSize)) #initialize AdjacencyMatrix

#make 1 whenever there is a connection between neighboring coordinates
mazeR, mazeC = 0,0
for row in range(xv.shape[0]):

    for col in range(xv.shape[1]):
        if xv[row][col]>0 and col+1<xv.shape[1] and round(np.abs(xv[row][col] - xv[row][col+1]),2) == stepSize:
            adj[mazeR,mazeC+1] = 1
            break
        mazeC = mazeC+1
    mazeR = mazeR+1
    
    
    
    
    
    
    
    
    
def numberOfPaths(m, n): 
    if(m == 1 or n == 1): 
        return 1
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1) 
d = 8  
m = d+1 
n = 12
print(numberOfPaths(m, n)) 

20!
10!10!

2,432,902,008,176,640,000

3,628,800