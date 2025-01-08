###数論変換
import sys
sys.setrecursionlimit(10**9)
class Number_Theoretic_Transform():  
    def __init__(self):
        self.MOD=998244353
        self.ROOT=3
        self.ROOTIN=pow(self.ROOT,-1,self.MOD)
        self.POWS=[self.ROOT]
        self.POWSIN=[self.ROOTIN]
        for _ in range(30):
            self.POWS.append((self.POWS[-1]**2)%self.MOD)
            self.POWSIN.append((self.POWSIN[-1]**2)%self.MOD)
        
    def my_pow(self,n):
        if n==0:
            return 1
        n%=self.MOD
        res=1
        now=len(self.POWS)-2
        while n>0:

            for i in reversed(range(now+1)):
                if (2**i)<=n:
                    now=i
                    res*=self.POWS[i]
                    res%=self.MOD
                    n-=2**i
                    break
        return res
    def my_powin(self,n):
        if n==0:
            return 1
        n%=self.MOD
        res=1
        now=len(self.POWSIN)-2
        while n>0:
            
            for i in reversed(range(now+1)):
                if (2**i)<=n:
                    now=i
                    res*=self.POWSIN[i]
                    res%=self.MOD
                    n-=2**i
                    break
        return res
    def NTT(self,A):
        if len(A)==1:
            return A
        t=1
        while t<len(A):
            t*=2
        A=A+[0]*(t-len(A))


        even= self.NTT([A[2*i] for i in range(t//2)])
        odd=self.NTT([A[2*i+1] for i in range(t//2)])
        for i in range(t//2):
            odd[i]*=self.my_pow((self.MOD-1)*i//t)
            odd[i]%=self.MOD
            A[i]=(even[i]+odd[i])%self.MOD
            A[t//2+i]=(even[i]-odd[i])%self.MOD
        return A
    def NTT_I(self,A,k=0):
        if len(A)==1:
            return A
        t=1
        while t<len(A):
            t*=2
        A=A+[0]*(t-len(A))


        even= self.NTT_I([A[2*i] for i in range(t//2)],1)
        odd=self.NTT_I([A[2*i+1] for i in range(t//2)],1)
        for i in range(t//2):
            odd[i]*=self.my_powin((self.MOD-1)*i//t)
            odd[i]%=self.MOD
            A[i]=(even[i]+odd[i])%self.MOD
            A[t//2+i]=(even[i]-odd[i])%self.MOD
        if k==0:
            tmp=pow(t,-1,self.MOD)
            for i in range(t):
                A[i]*=tmp
                A[i]%=self.MOD
        return A
    
    def FPS(self,A,B):
        lA=len(A)
        lB=len(B)
        A=A+[0]*lB
        B=B+[0]*lA
        AN=self.NTT(A)
        BN=self.NTT(B)
        CN=[(AN[i]*BN[i])%self.MOD for i in range(len(AN))]
        C=self.NTT_I(CN)
        return C

