'''
Created on 28/03/2015

@author: nicolas
'''

import re
import os
from cambiadorTexto.FuncionesPath import FuncionesPath

class ArbolDirectorio(object):
    '''
    Clase manejadora de arboles de directorios
    '''
    
    _directorio = None
    
    def __init__(self, directorio):
        self._directorio = FuncionesPath.quitarSeparadorRaiz(directorio)
        
    def getArchivos(self, regExp, subdirectorios = False):
        archivosRecuperados = []
        archivosCarpetas = os.walk(self._directorio)
        
        if subdirectorios:
            for i in archivosCarpetas:
                for j in i[2]:
                    if re.search(regExp,j) is not None:
                        archivosRecuperados.extend([i[0] + os.sep + j])
        else:
            first = next(archivosCarpetas)
            for i in first[2]:
                if re.search(regExp,i) is not None:
                    archivosRecuperados.extend(first[0] + os.sep + i)
                                             
        return archivosRecuperados
    
    def encontrarArchivo(self, nombreArchivo):
        return self.getArchivos(re.sub('\.','\.',nombreArchivo), True)
        