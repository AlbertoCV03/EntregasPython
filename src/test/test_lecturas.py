'''
Created on 3 oct 2024

@author: Alberto CV
'''
from lecturas import lecturas
from typing import Optional

def test_funcion6(fichero:str,sep:str,cad:str)->int:
    return lecturas.funcion6(fichero, sep, cad)

def test_funcion7(fichero:str,cad:str)->list:
    return lecturas.funcion7(fichero, cad)

def test_funcion8(fichero:str)->list:
    return lecturas.funcion8(fichero)

def test_longitud_promedio_lineas(file_path: str) -> Optional[float]:
    return lecturas.longitud_promedio_lineas(file_path)

if __name__ == '__main__':
    
    '''Test 6'''
    fichero='../../resources/lin_quijote.txt'
    sep=' '
    cad='quijote'
    print('___________________________________________')
    print('Test 6 \n')
    print(f'El número de veces que aparece la palabra {cad} en el fichero resources/lin_quijote.txt es: ' + str(test_funcion6(fichero, sep, cad)))
    print('___________________________________________')
    
    '''Test 7'''
    fichero='../../resources/lin_quijote.txt'
    cad='quijote'
    print('___________________________________________')
    print('Test 7 \n')
    print(f'Las líneas en las que aparece la palabra {cad} son: ' + str(test_funcion7(fichero,cad)))
    print('___________________________________________')
    
    '''Test 8'''
    fichero='../../resources/archivo_palabras.txt'
    print('___________________________________________')
    print('Test 8 \n')
    print(f'Las palabras únicas en el fichero resources/archivo_palabras.txt son: ' + str(test_funcion8(fichero)))
    print('___________________________________________')
    
    '''Test 9'''
    file_path='../../resources/palabras_random.csv'
    print('___________________________________________')
    print('Test 9 \n')
    print(f'La longitud promedio de las líneas del fichero resources/palabras_random.csv es: ' + str(round(test_longitud_promedio_lineas(file_path),1)))
    file_path='../../resources/vacio.csv'
    print(f'La longitud promedio de las líneas del fichero resources/vacio.csv es: ' + str(test_longitud_promedio_lineas(file_path)))
    print('___________________________________________')