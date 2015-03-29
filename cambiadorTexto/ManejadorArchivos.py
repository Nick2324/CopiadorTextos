'''
Created on 28/03/2015

@author: nicolas
'''

import os
import traceback
import re
from cambiadorTexto.FuncionesPath import FuncionesPath

class ManejadorArchivos(object):
    '''
    Clase que maneja la apertura, escritura y lectura de archivos
    '''
    
    _pathArchivo = None
    _nombreArchivo = None

    def __init__(self, pathArchivo, nombreArchivo = None):
        if nombreArchivo is None:
            self._pathArchivo, self._nombreArchivo = \
                FuncionesPath.separarArchivoCarpeta(pathArchivo)
            if self._nombreArchivo is None:
                self._pathArchivo, self._nombreArchivo = \
                FuncionesPath.separarUltimaCarArchTupla(pathArchivo)
        else:
            self._pathArchivo = FuncionesPath.quitarSeparadorRaiz(pathArchivo)
            self._nombreArchivo = nombreArchivo
    
    def getPathArchivo(self):
        return self._pathArchivo
    
    def getNombreArchivo(self):
        return self._nombreArchivo
    
    def copiarArchivo(self, nuevo):
        archivoReal = open(self._pathArchivo + os.sep + self._nombreArchivo)
        archivo = open(nuevo, 'w+')
           
        for linea in archivoReal:
            archivo.write(linea)
        
        archivo.flush()
        archivo.close()
    
    def cambiarLineas(self, lineaAntigua, lineaNueva, nombreCopia = None):
        try:
            if nombreCopia is not None:
                #print(nombreCopia)
                nombreFinal = nombreCopia
                self.copiarArchivo(nombreCopia)
                archivo = open(nombreCopia, 'r+')
            else:
                nombreFinal = self._pathArchivo + os.sep + self._nombreArchivo
                archivo = open(self._pathArchivo + os.sep + self._nombreArchivo, 'r+')
            
            archivoCopia = open(nombreFinal + '~','w+')
            
            patron = '(' + \
                     re.sub('\.', '\.', lineaAntigua) + \
                     ')'

            for linea in archivo:
                if re.search(patron,linea) is not None:
                    linea = re.sub(patron, lineaNueva, linea)
                archivoCopia.write(linea)
            
            archivoCopia.flush()
            archivoCopia.close()
            
        except:
            print('Error * ' + traceback.format_exc())
            
    def obtenerLineas(self, patron): 
        patron = '(' + patron + ')'
        try:
            archivo = open(self._pathArchivo + os.sep + self._nombreArchivo)
            lineas = []
            for linea in archivo:
                if re.search(patron, linea) is not None:
                    lineas.append(linea)
            #print('estas son las lineas',lineas)
        except:
            #print('Error * ' + traceback.format_exc())
            print('** No procesado: ' + self._pathArchivo + os.sep + self._nombreArchivo)
        
        return lineas
            
    def existeArchivo(self):
        return os.path.isfile(self._pathArchivo + os.sep + self._nombreArchivo)
            