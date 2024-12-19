'''
Created on 19 dic 2024

@author: Alberto CV
'''
from __future__ import annotations
from dataclasses import dataclass
from Entrega3.grafo import Grafo
from Entrega3.recorridos import *
from typing import Dict

@dataclass(frozen=True)
class Gen:
    nombre:str
    tipo:str
    num_mutaciones:int
    loc_cromosomas:str
    
    @staticmethod
    def of(nombre:str,tipo:str,num_mutaciones:int,loc_cromosomas:str):
        assert num_mutaciones >=0, f'El numero de mutaciones debe ser mayor o igual que 0'
        return Gen(nombre,tipo,num_mutaciones,loc_cromosomas)
    
    @staticmethod
    def parse(linea:str):
        nombre,tipo,num_mutaciones,loc_cromosomas=linea.split(',')
        return Gen.of(nombre,tipo,int(num_mutaciones),loc_cromosomas)
    
@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1:str
    nombre_gen2:str
    conexion:float
    
    @staticmethod
    def of(nombre_gen1,nombre_gen2,conexion):
        assert -1<= conexion <= 1, 'La conexión debe ser un numero real entre [-1,1]'
        return RelacionGenAGen(nombre_gen1,nombre_gen2,conexion)
    
    @staticmethod
    def parse(linea:str):
        nombre_gen1,nombre_gen2,conexion=linea.split(',')
        
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, float(conexion))
    
    def coexpresados(self)->bool:
        
        if self.conexion > 0.75:
            return True
        
        else:
            return False
        
    def antiexpresados(self)->bool:
        if self.conexion < 0.75:
            return True
        
        else:
            return False
        
    
    
class RedGenica(Grafo[Gen, RelacionGenAGen]):
    
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> RedGenica:
        
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> RedGenica:
        
        red_genica = RedGenica.of(es_dirigido=False)
        
        with open(f1,encoding='UTF-8') as f:
            for linea in f:
                gen=Gen.parse(linea.strip())
                red_genica.genes_por_nombre[gen.nombre] = gen
                red_genica.add_vertex(gen)
                
        with open(f2,encoding='utf-8') as f:
            for linea in f:
                nombre_gen1, nombre_gen2, conexion= linea.strip().split(',')
                if nombre_gen1 not in red_genica.genes_por_nombre or nombre_gen2 not in red_genica.genes_por_nombre:
                    raise ValueError(f"Uno de los genes en la relación ({nombre_gen1}, {nombre_gen2}) no existe.")
                nombre_gen1 = red_genica.genes_por_nombre[nombre_gen1]
                nombre_gen2 = red_genica.genes_por_nombre[nombre_gen2]
                relacion_gen = RelacionGenAGen.of(nombre_gen1,nombre_gen2,float(conexion))
                red_genica.add_edge(nombre_gen1, nombre_gen2, relacion_gen)
                

        return red_genica


if __name__ == '__main__':
    
    print('___________________________________________________________________________________________________________')
    
    print('Test Clase GEN:')
    
    print(Gen.parse('TP53,supresor tumoral,256,17p13.1'))
    
    print('___________________________________________________________________________________________________________')
    
    
    print('Test Clase RelacionGenAGen:')
    
    print(RelacionGenAGen.parse('TP53,EGFR,0.5'))
    
    print('___________________________________________________________________________________________________________')
    
    raiz = ''
    rg = RedGenica.parse(raiz+'genes.txt', raiz+'red_genes.txt', es_dirigido=False)
    
    
    print("El camino más corto desde KRAS hasta PIK3CA es:")
    camino = bfs(rg, rg.genes_por_nombre['KRAS'], rg.genes_por_nombre['PIK3CA'])
    print(camino)
    g_camino = rg.subgraph(camino)
    
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.nombre}", lambda_arista=lambda e: e.conexion)
    

    
