class union_find:
    def __init__(self,N):
        self.N=N
        self.Root=[i for i in range(N)]
        self.dict={i:i for i in range(N)}
        #dictはインデックスと実際のインデックスを適合させる
    def find_root(self,u):
        t=self.dict[u]
        tmp=[]
        while self.Root[self.dict[t]]!=t:
            tmp.append(self.dict[t])
            t=self.Root[self.dict[t]]
        for i in tmp:
            self.Root[i]=t
        return t
    def union(self,u,v):
        self.Root[self.dict[self.find_root(u)]]=self.find_root(v)
    def same(self,u,v):
        if self.find_root(u)==self.find_root(v):
            return 1
        else:
            return 0
    
    
N,Q=map(int,input().split())
uf=union_find(N)
for i in range(Q):
    x,u,v,=map(int,input().split())
    if x==0:
        uf.union(u,v)
    else:
        print(1 if uf.same(u,v) else 0)