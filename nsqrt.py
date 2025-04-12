def nsqrt(n):
    if n==0 or n==1:
        return n
    ok=1
    ng=n
    while (ng-ok)>1:
        mid=(ok+ng)//2
        if mid**2 >n:
            ng=mid
        else:
            ok=mid
    return ok

print(nsqrt(4))
print(nsqrt(99))