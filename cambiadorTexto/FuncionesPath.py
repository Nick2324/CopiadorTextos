'''
Created on 28/03/2015

@author: nicolas
'''

import os

class FuncionesPath(object):
    '''
    Clase que brinda funcionalidades sobre paths
    '''


    def __init__(self, params):
        pass
    
    @staticmethod
    def separarUltimaCarArch(path):
        for i in range(1,len(path)):
            if path[-1 * i] == os.sep:
                return path[(-1 * i + 1):]
                
    @staticmethod
    def separarUltimaCarArchTupla(path):
        for i in range(1,len(path)):
            if path[-1 * i] == os.sep:
                return (path[-len(path):(-1 * i)], \
                        path[(-1 * i + 1):])
    
    @staticmethod          
    def separarArchivoCarpeta(path):
        if os.path.isfile(path):
            return FuncionesPath.separarUltimaCarArchTupla(path)
        else:
            return (FuncionesPath.quitarSeparadorRaiz(path),None)
        
    @staticmethod
    def quitarSeparadorRaiz(path):
        if path[len(path) - 1] == os.sep:
            return path[0:(len(path) - 1)]
        else:
            return path