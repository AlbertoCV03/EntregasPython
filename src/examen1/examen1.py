'''
Created on 24 oct 2024

@author: Alberto CV
'''
from typing import Optional
from funciones import funciones
import math
from collections import Counter

def P2(n:int,k:int,i:int=1)->int:
    
    assert n>=k, 'n debe ser mayor o igual que k'
    assert n>0 and k>0 and i>0, 'n,k e i deben ser mayores que 0'
    assert i<k+1, 'i debe ser menor que k+1'
    res:int=1
    for e in range(i,k-1):
        res= (n-e+1) * res
    return res

def test_P2 (n:int,k:int,i:int=1)->Optional[int]:
    try:
        return P2(n,k,i)
        
    except Exception as e:
        print(f'Error: {e}')
        return None
        
def C2(n:int,k:int)->int:
    k=k+1
    assert n>k,'n debe ser mayor que k'
    assert n>0 and k>0, 'n y k deben ser mayores que 0'
    
    res=funciones.factorial(n)//(funciones.factorial(k)*funciones.factorial(n-k))
    
    return res

def test_C2(n:int,k:int)->Optional[int]:
    try:
        return C2(n,k)
        
    except Exception as e:
        print(f'Error: {e}')
        return None
    
    
def S2(n:int,k:int)->float:
    assert n>=k,'n debe ser mayor o igual que k'
    assert n>0 and k>0, 'n y k deben ser mayores que 0'
    
    resSumatorio:int=0
    
    for i in range(0,k+1):
        
        resSumatorio= (((-1)**i) * math.comb(k, i) * ((k-i)**(n+1))) + resSumatorio
        
    return (math.factorial(k)/(n* math.factorial(k+2))) * resSumatorio

def test_S2(n:int,k:int):
    try:
        return S2(n,k)
        
    except Exception as e:
        print(f'Error: {e}')
        return None


def palabrasMasComunes(fichero:str,n:int=5)->list[tuple[str, int]]:
    assert n>1, 'n debe ser mayor que 1'
    
    with open(fichero,encoding='UTF-8') as f:
        
        lt=[]
        for linea in f:
            
            palabras=linea.split()
            for p in palabras:
                palabra_limpia=p.strip()
                
                lt.append(palabra_limpia.upper())
                
                num_palabras=Counter(lt)
                palabras_comunes= num_palabras.most_common(n)
            
        
        return palabras_comunes

def test_palabrasMasComunes(fichero:str,n:int=5)->Optional[list[tuple[str, int]]]:
    try:
        return palabrasMasComunes(fichero, n)
        
    except Exception as e:
        print(f'Error: {e}')
        return None

if __name__ == '__main__':
    
    #Test P2
    print('Test P2')
    print('__________________________________________')
    print(test_P2(4, 3, 1))
    print('__________________________________________')
    print(test_P2(4, 3))
    print('__________________________________________')
    print(test_P2(2, 3, 1))
    print('__________________________________________')
    print(test_P2(5, -3, 1))
    print('__________________________________________')
    print(test_P2(7, 3, 4))
    print('__________________________________________')
    
    #Test C2
    print('Test C2')
    print('__________________________________________')
    print(test_C2(5, 3))
    print('__________________________________________')
    print(test_C2(2, 3))
    print('__________________________________________')
    print(test_C2(6, -3))
    print('__________________________________________')
    
    #Test S2
    print('Test S2')
    print('__________________________________________')
    print(test_S2(4, 3))
    print('__________________________________________')
    print(test_S2(2, 3))
    print('__________________________________________')
    print(test_S2(4, -3))
    print('__________________________________________')
    
    #Test PalabrasMasComunes
    
    print('Test PalabrasMasComunes')
    fichero='../../resources/archivo_palabras.txt'
    print('___________________________________________')
    print(test_palabrasMasComunes(fichero, 3))
    print('___________________________________________')
    print(test_palabrasMasComunes(fichero))
    print('___________________________________________')
    print(test_palabrasMasComunes(fichero,1))
    print('___________________________________________')
    
    