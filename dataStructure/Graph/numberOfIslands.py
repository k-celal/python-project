class Solution:
    def numIsland(self,grid):
        rowN=len(grid)
        colN=len(grid[0])
        visited=set()
        islandCount=0
        def bfs(row,col):
            myQueue=[]
            visited.add((row,col))
            myQueue.append((row,col))
            while len(myQueue) !=0:
                row,col=myQueue.pop(0)
                myDriections=[[1,0],[-1,0],[0,1],[0,-1]]
                for rowDirection,columnDirection in myDriections:
                    newRow=row+rowDirection
                    newCol=col+columnDirection
                    if (newRow in range(rowN))and (newCol in range(colN))and (grid[newRow][newCol]=="1")and ((newRow,newCol) not in visited):
                        myQueue.append((newRow,newCol))
                        visited.add((newRow,newCol)) 
        for row in range(rowN):
            for col in range(colN): 
                if grid[row][col]=="1"and(row,col)not in visited:
                    bfs(row,col)
                    islandCount+=1
        return islandCount
sol=Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
   
            
            