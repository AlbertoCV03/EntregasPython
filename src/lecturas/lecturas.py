import string
from typing import Optional

def funcion6(fichero:str,sep:str,cad:str)->int:
    with open(fichero,encoding='UTF-8')as f:
        ls:list[str]=[]
        for linea in f:
            if len(linea)>0:
                for p in linea.split(sep):
                    p=p.strip()
                    if p.upper()==cad.upper():
                        ls.append(p)
    return len(ls)


def funcion7(fichero:str,cad:str)->list:
    with open(fichero,encoding='UTF-8') as f:
        ls:list[str]=[]
        for linea in f:   
            if cad.upper() in linea.upper() and linea.strip() not in ls:
                ls.append(linea.strip())
                    
    
    return ls

def funcion8(fichero:str)->list:
    with open(fichero,encoding='UTF-8') as f:
        ls:list[str]=[]
        for linea in f:
            palabras=linea.split()
            #ls.append(linea.strip())
            for p in palabras: #' [ ,;.\n():?!\"]'
                palabra_limpia=p.strip(string.punctuation)
                if palabra_limpia not in ls:
                    ls.append(palabra_limpia)
                #print(p.strip(string.punctuation))
                    
    
    return ls

def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    with open(file_path, encoding='UTF-8') as f:
        nl=0
        res=0
        resfinal=0
        for linea in f:
            nl+=1
            linea_separada=linea.strip().split(',')
            a=len(linea_separada)
            for i in range(0,len(linea_separada)):
                longitud=len(linea_separada[i])
                
                if i==0:
                    res=0
                else:
                    res=res+longitud
                
                if i==len(linea_separada)-1:
                    resfinal=(res/a)+resfinal

        if resfinal>0:
            return resfinal/nl
        else:
            return None
       