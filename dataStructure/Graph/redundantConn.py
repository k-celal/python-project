class Solution:
    def findRedundantConn(self,edges):
        parents=[]
        for i in range(len(edges)+1):
            parents.append(i)
        ranks=[1]*(len(edges)+1)
        
        def find(n):
            parent=parents[n]
            while parent !=parents[parent]:
                #path compression
                parents[parent]=parents[parents[parent]]
                parent=parents[parent]
            return parent
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                #connected
                return False
            if ranks[p1]>ranks[p2]:
                parents[p2]=p1
                ranks[p1]+=ranks[p2]
            else:
                parents[p1]=p2
                ranks[p2]+=ranks[p1]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return[n1,n2]
            
sol=Solution()
edge=[[1,2],[1,3],[2,3]]
print(sol.findRedundantConn(edge))    