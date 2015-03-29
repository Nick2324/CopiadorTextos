'''
Created on 28/03/2015

@author: nicolas
'''

import re

class AdapterPatron(object):
    '''
    Clase que extiende funcionalidades de la librería 're'
    '''
    _patron = None
    _string = None
    
    def __init__(self, patron, string):
        self.setPatron(patron)
        self.setString(string)
        
    def setPatron(self, patron):
        self._patron = patron
        
    def getPatron(self):
        return self._patron
    
    def setString(self, string):
        self._string = string
        
    def getString(self):
        return self._string
    
    def match(self):
        return re.match(self._patron, self._string)
    
    def reemplazarMatch(self, reemplazo):
        re.sub(self._patron, reemplazo, self._string)
        