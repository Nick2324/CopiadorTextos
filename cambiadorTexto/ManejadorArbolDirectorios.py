'''
Created on 28/03/2015

@author: nicolas
'''

class ManejadorArbolDirectorios(object):
    '''
    Objeto contenedor de varios arboles de directorios
    '''

    _manejadoresDirectorios = None

    def __init__(self, directorios):
        self._manejadoresDirectorios = []
        for i in directorios:
            self._manejadoresDirectorios = \
                ManejadorArbolDirectorios(directorios[i])
                