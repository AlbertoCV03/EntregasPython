from __future__ import annotations

from dataclasses import dataclass
from typing import Dict
from datetime import date, datetime
#from grafo.recorridos import * --> Adáptalo a tu proyecto
from Entrega3.recorridos import *
#from grafo.grafo import * --> Adáptalo a tu proyecto
from Entrega3.grafo import Grafo

@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        assert fecha_nacimiento < datetime.now().date(), "La fecha de nacimiento tiene que ser anterior a la fecha actual"
        assert len(dni)==9, "El formato del DNI tiene que ser 8 digitos seguidos de una letra"
        try:
            dni_numeros=int(dni[0:8])
            
            #letra_indice=dni_numeros%23
            
        except:
            dni_numeros=None
            
        letras_abc:list[str]=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        if dni[8:9].upper() not in letras_abc:
            raise Exception("El último dígito del DNI debe ser una letra")
            
        if dni_numeros==None:
            raise Exception("Los primeros 8 dígitos deben ser números")
#        
#        letras_dni:list[str]= ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
#        
#    
#        if dni[8:9].upper() not in letras_dni:
#            raise Exception("El último dígito del DNI debe ser una letra de las siguientes: T, R, W, A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E")
#        elif not dni[8:9].upper()==letras_dni[letra_indice]:
#            raise Exception("Letra incorrecta")
        
        return Usuario(dni,nombre,apellidos,fecha_nacimiento)
    
    def __str__(self) -> str:
        return f'{self.dni}-{self.nombre}'
    
    @staticmethod
    def parse(linea:str)->Usuario:
        trozos=linea.split(',')
        fecha=datetime.strptime(trozos[3], "%Y-%m-%d").date()
        return Usuario.of(trozos[0],trozos[1],trozos[2],fecha)

@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0 # Contador de relaciones. Servirá para asignar identificadores únicos a las relaciones.
    
    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        Relacion.__n += 1
        return Relacion(Relacion.__n, interacciones, dias_activa)
    
    def __str__(self) -> str:
        return f'({self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones})'

class Red_social(Grafo[Usuario, Relacion]):
    """
    Representa una red social basada en el grafo genérico.
    """
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        '''
        usuarios_dni: Diccionario que asocia un DNI de usuario con un objeto Usuario.
        Va a ser útil en la lectura del fichero de relaciones para poder acceder a los usuarios
        '''
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> Red_social:
        """
        Método de factoría para crear una nueva Red Social.
        
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        return Red_social(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> Red_social:
        """
        Método de factoría para crear una Red Social desde archivos de usuarios y relaciones.
        
        :param f1: Archivo de usuarios.
        :param f2: Archivo de relaciones.
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        red_social = Red_social.of(es_dirigido=False)
        
        with open(f1,encoding='UTF-8') as f:
            for linea in f:
                usuario=Usuario.parse(linea.strip())
                red_social.usuarios_dni[usuario.dni] = usuario
                red_social.add_vertex(usuario)
                
        with open(f2,encoding='utf-8') as f:
            for linea in f:
                dni_origen, dni_destino, interacciones, dias_activa = linea.strip().split(',')
                if dni_origen not in red_social.usuarios_dni or dni_destino not in red_social.usuarios_dni:
                    raise ValueError(f"Uno de los usuarios en la relación ({dni_origen}, {dni_destino}) no existe.")
                usuario_origen = red_social.usuarios_dni[dni_origen]
                usuario_destino = red_social.usuarios_dni[dni_destino]
                relacion = Relacion.of(int(interacciones), int(dias_activa))
                red_social.add_edge(usuario_origen, usuario_destino, relacion)
                

        return red_social

        
    
if __name__ == '__main__':
    # print(Usuario.parse('45718832U,Carlos,Lopez,1984-01-14'))
    #print(Relacion.of(300, 6))
    #print(Relacion.of(309, 8))
    
    raiz = '' # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse(raiz+'resources/usuarios.txt', raiz+'resources/relaciones.txt', es_dirigido=False)
    
    
    print("El camino más corto desde 25143909I hasta 87345530M es:")
    camino = bfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'])
    print(camino)
    g_camino = rrss.subgraph(camino)
    
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: e.id)
    
    print("El camino más corto desde 25143909I hasta 76929765H es:")
    camino = bfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['76929765H'])
    print(camino)
    g_camino = rrss.subgraph(camino)
    
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: e.id)
    

