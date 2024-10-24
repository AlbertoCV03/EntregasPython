'''
Created on 3 oct 2024

@author: Alberto CV
'''
from funciones import funciones
from typing import Callable


def test_productorio(n:int,k:int)->int:
    return funciones.productorio(n, k)

def test_secuencia_geo(a1:int,r:int,k:int)->int:
    return funciones.secuencia_geo(a1, r, k)

def test_combinatorio(n:int,k:int)->int:
    return funciones.combinatorio(n, k)

def test_numeroS(n:int,k:int)->float:
    return funciones.numeroS(n, k)

def test_funcion5(f:Callable[[float],float],fd:Callable[[float],float],a:float,e:float)->float:
    return funciones.funcion5(f, fd, a, e)

if __name__ == '__main__':
    
    '''Test 1'''
    n=4
    k=2
    print('___________________________________________')
    print('Test 1 \n')
    print(f'El resultado de {n} y {k} es : ' + str(test_productorio(n,k)))
    print('___________________________________________')
    
    '''Test 2'''
    a1=3
    r=5
    k=2
    print('Test 2 \n')
    print(f'El producto de la secuencia geométrica con a1 = {a1}, r = {r} y k = {k} es: ' + str(test_secuencia_geo(a1, r, k)))
    print('___________________________________________')
    
    '''Test 3'''
    n=5
    k=4
    print('Test 3 \n')
    print(f'El nuero combinatorio de {n} y {k} es: ' + str(test_combinatorio(n, k)))
    print('___________________________________________')
    
    '''Test 4'''
    n=4
    k=2
    print('Test 4 \n')
    print(f'El numero S({n},{k}) es: ' + str(test_numeroS(n, k)))
    print('___________________________________________')
    
    '''Test 5'''
    f= lambda x: 2*(x**2)
    fd=lambda x: 4*x
    a=3
    e=0.001
    
    print('Test 5 \n')
    print(f'Resultado de la función 5 con a= {a} y e = {e}, f(x) = 2x^2 y fd(x) = 4x: ' + str(test_funcion5(f, fd, a, e)))
    print('___________________________________________')