class SegmentTree:
    def __init__(self,A,identity_element,keisan):
        self.le= len(A)
        self.identity_element=identity_element
        self.keisan=keisan
        self.maketree(A)

    def maketree(self,A):
        t=0
        while True:
            if 2**t<self.le:t+=1
            else:break
        self.t=t+1
        self.tree=[self.identity_element]*((2**(t+1))-1)
        self.tree[(2**t)-1:(2**t)-1+len(A)]=A
        for i in reversed(range((2**t)-1)):
            self.tree[i]=self.keisan(self.tree[(i*2)+1],self.tree[(i*2)+2])

    def update(self,i,x):#0インデックスに注意
        
        tmp=(2**(self.t-1))+i-1
        self.tree[tmp]=x
        tmp=(tmp-1)//2
        while tmp>=0:
            self.tree[tmp]=self.keisan(self.tree[2*(tmp+1)-1],self.tree[2*(tmp+1)])
            tmp=(tmp-1)//2

    def query(self,l,r):#rも含むので注意 lsitで帰ってくるから問題に応じて調理して
        
        ans=[]
        l=((2**max(self.t-1,0))+l-1)
        r=((2**max(self.t-1,0))+r-1)
        if l ==r:
            return [self.tree[r]]
        while l<r:
            if l % 2 == 0:
                ans.append(self.tree[l])
                l += 1
            
            if r % 2 == 1:
                ans.append(self.tree[r])
                r -= 1
                
            # leftとrightを親のノードに移動
            

            l =(l-1)// 2
            r =(r-1)// 2
        if l == r:
            ans.append(self.tree[r])
        return ans

    def Ptree(self):#デバッグプリント用
        c=0
        for i in range(self.t):
            for j in range(2**i):
                print(self.tree[c+j],end=" ")
            print()    
            c+=2**i

A=[6,3,4,1,3,5,123]
identity_element=(2**31)-1 #単位元 

def keisan(x,y):#問題に応じて
    return min(x,y)


segtree=SegmentTree(A,identity_element,keisan)


print((segtree.tree))#[1, 1, 3, 3, 1, 3, 123, 6, 3, 4, 1, 3, 5, 123, 2147483647]
segtree.Ptree()
"""
1 
1 3
3 1 3 123
6 3 4 1 3 5 123 2147483647
"""

segtree.update(6,73)#第一引数の値を第二引数にする

segtree.Ptree()
"""
1 
1 3
3 1 3 73
6 3 4 1 3 5 73 2147483647
"""

print(segtree.query(1,5))#[3,1,3]