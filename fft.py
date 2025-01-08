###高速離散フーリエ変換
import cmath
import math
import sys
sys.setrecursionlimit(10**9)
class Fast_Fourier_Transform():  
    def FFT(self,A):
        if len(A)==1:
            return A
        t=1
        while t<len(A):
            t*=2
        A=A+[0]*(t-len(A))

        even= self.FFT([A[2*i] for i in range(t//2)])
        odd=self.FFT([A[2*i+1] for i in range(t//2)])
        for i in range(t//2):
            odd[i]*=cmath.rect(1,-2*math.pi*i/t)
            A[i]=even[i]+odd[i]
            A[t//2+i]=even[i]-odd[i]
        return A
    def FFT_I(self,A,k=0):
        if len(A)==1:
            return A
        t=1
        while t<len(A):
            t*=2
        A=A+[0]*(t-len(A))

        even= self.FFT_I([A[2*i] for i in range(t//2)],1)
        odd=self.FFT_I([A[2*i+1] for i in range(t//2)],1)
        for i in range(t//2):
            odd[i]*=cmath.rect(1,2*math.pi*i/t)
            A[i]=even[i]+odd[i]
            A[t//2+i]=even[i]-odd[i]
        if k==0:
            for i in range(t):
                A[i]/=t
        return A
    
    def FPS(self,A,B):
        lA=len(A)
        lB=len(B)
        A=A+[0]*lB
        B=B+[0]*lA
        AF=self.FFT(A)
        BF=self.FFT(B)
        CF=[AF[i]*BF[i] for i in range(len(AF))]
        C=self.FFT_I(CF)
        return C


