import heapq

class mex():
    def __init__(self,s:set):
        self.queue=[0]
        heapq.heapify(self.queue)
        self.s=s
        self.m=heapq.heappop(self.queue)
        while self.m in self.s:
            heapq.heappush(self.queue,self.m+1)
            self.m=heapq.heappop(self.queue)
        heapq.heappush(self.queue,self.m)
    def add(self,n):
        self.s.add(n)
        while self.m in self.s:
            heapq.heappush(self.queue,self.m+1)
            self.m=heapq.heappop(self.queue)
        heapq.heappush(self.queue,self.m)
    def remove(self,n):
        self.s.remove(n)
        heapq.heappush(self.queue,n)
        self.m=heapq.heappop(self.queue)

        while self.m in self.s:
            heapq.heappush(self.queue,self.m+1)
            self.m=heapq.heappop(self.queue)
    def __str__(self):
        return str(self.m)
    def __int__(self):
        return self.m
    
s={1,2,3,4,5}
m=mex(s)
print(m)
m.add(0)
print(m)
m.remove(4)
print(m)
