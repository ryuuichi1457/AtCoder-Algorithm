import random
def IsPrime(N,K=20):#Miller_Rabin_Testという確率的素数判定砲を使用#Kは試行回数、一般に誤判定する確率は1/4^K　(初期値20だと1/1.2E+24ぐらい)
    if N<2:
        return False
    if N%2==0:
        return N==2  
    if N==3:
        return True  
    tmp= N-1
    c=0
    while tmp%2==0:
        c+=1
        tmp//=2
    d=tmp

    for _ in range(K):
        a=random.randint(2, N-2)
        x=pow(a,d,N)
        if x==1 or x==N-1:
            continue
        
        #2^r*d
        for _ in range(c-1):
            x = pow(x,2,N)
            if x==N-1:
                break
        else:
            return False

    return True