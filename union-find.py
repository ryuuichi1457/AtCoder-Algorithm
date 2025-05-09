class union_find:
    def __init__(self,N):
        self.N=N
        self.Root=[i for i in range(N)]
        self.Par=[1 for _ in range(N)]
    def find_root(self,u):

        tmp=[]
        while self.Root[u]!=u:
            tmp.append(u)
            u=self.Root[u]
        for i in tmp:
            self.Root[i]=u
        return u
    def union(self,u,v):
        self.Root[self.find_root(u)]=self.find_root(v)
        self.Par[self.find_root(v)]+=self.Par[self.find_root(u)]
    def same(self,u,v):
        return self.find_root(u)==self.find_root(v)
    def size(self,u):
        return self.Par[self.find_root(u)]
    
    
N,Q=map(int,input().split())
uf=union_find(N)
for i in range(Q):
    x,u,v,=map(int,input().split())
    if x==0:
        uf.union(u,v)
    else:
        print(1 if uf.same(u,v) else 0) 