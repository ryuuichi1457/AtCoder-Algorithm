class rational:
    class TYPE_ERROR(Exception):
        pass

    def __init__(self,mo:int,de:int):
        tmp=self.gcd(mo,de)
        self.mo=mo//tmp
        self.de=de//tmp
    
    def __repr__(self):

        return f"{self.mo}/{self.de}"
    
    def judgment(self,x):
        if type(x)==rational:
            return x
        else:
            if type(x)==int:
                return rational(x,1)
            else:
                raise self.TYPE_ERROR("その型では演算できません")


    def gcd(self,x,y):
        r=x%y
        while r!=0:
            x,y=y,r
            r=x%y
    
        return y
    
    def get_mo(self):
        return self.mo
    
    def get_de(self):
        return self.de
    
    def __add__(self,other):
        return rational(self.get_mo()*(self.judgment(other).get_de())+self.judgment(other).get_mo()*(self.get_de()),self.get_de()*self.judgment(other).get_de())
    
    def __sub__(self,other):
        return rational(self.get_mo()*(self.judgment(other).get_de())-self.judgment(other).get_mo()*(self.get_de()),self.get_de()*self.judgment(other).get_de())
    
    def __mul__(self,other):
        return rational(self.get_mo()*self.judgment(other).get_mo(),self.get_de()*self.judgment(other).get_de())
    
    def __truediv__(self,other):
        return rational(self.get_mo()*self.judgment(other).get_de(),self.get_de()*self.judgment(other).get_mo())
    
    def __mod__(self,other:int):
        return(self.get_mo()*pow(self.get_de(), -1, other) % other)
    
    def __pow__(self,other:int):
        return rational(self.get_mo()**other,self.get_de()**other)
    
    def __neg__(self):
        return rational(-self.get_mo(),self.get_de())
    
    def __abs__(self):
        return rational(abs(-self.get_mo()),abs(self.get_de()))
    
    def __radd__(self,other):
        return rational(self.get_mo()*(self.judgment(other).get_de())+self.judgment(other).get_mo()*(self.get_de()),self.get_de()*self.judgment(other).get_de())
    
    def __rsub__(self,other):   
        return rational(-self.get_mo()*(self.judgment(other).get_de())+self.judgment(other).get_mo()*(self.get_de()),self.get_de()*self.judgment(other).get_de())
    
    def __rmul__(self,other):  
        return rational(self.get_mo()*self.judgment(other).get_mo(),self.get_de()*self.judgment(other).get_de())
    
    def __rtruediv__(self,other):
        return rational(self.get_de()*self.judgment(other).get_mo(),self.get_mo()*self.judgment(other).get_de())
    
    def few(self):
        return self.get_mo()/self.get_de()
    
    def __eq__(self,other):
        return (self.judgment(other).get_de()==self.get_de())and(self.judgment(other).get_mo()==self.get_mo())
    
    def __ne__(self,other):
        return not (self.judgment(other).get_de()==self.get_de())and(self.judgment(other).get_mo()==self.get_mo())
    
    def __lt__(self,other):
        return (self.judgment(other)-self).get_mo()>0
    
    def __gt__(self,other):
        return (self.judgment(other)-self).get_mo()<0
    
    def __le__(self,other):
        return (self.judgment(other)-self).get_mo()>=0
    
    def __ge__(self,other):
        return (self.judgment(other)-self).get_mo()<=0
        