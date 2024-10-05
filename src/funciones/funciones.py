#import sympy
from typing import Callable

def productorio (n:int,k:int)->int:
    assert n>k , 'n debe ser mayor que k'
    res:int=1
    if n>k:
        for i in range(0,k+1):
            res= res* (n-i+1)
    return res

def secuencia_geo(a1:int,r:int,k:int)->int:

    for n in range(2,k+1):
        
        if n==2:
            an=a1*(r**(n-1))
            res=an*a1
        else:
            an=a1*(r**(n-1))
        
            res=an*res
        
        
        
    return res
def factorial(n:int)->int:
    assert n>0 , 'n debe ser un numero entero positivo'
    res:int=1
    for i in range(1,n+1):
        res=res*i
        
    return res
def combinatorio(n:int,k:int)->int:
    
    assert n>=k , 'n debe ser mayor o igual que k'
    
    res=factorial(n)//(factorial(k)*factorial(n-k))
    
    return res

def numeroS(n:int,k:int)->int:
    assert n>=k , 'n debe ser mayor o igual que k'
    res=0
    for i in range (0,k):
        res=(((-1)**i)*(combinatorio(k+1, i+1))*(k-i)**n)+res
    
    return (1/factorial(k))*res

def funcion5(f:Callable[[int],int],fd:Callable[[int],int],a:float,e:float)->float:
    
    while abs(f(a))>e:
    
        x2=a-(f(a)/fd(a))
    
        a=x2
        
    
    return x2