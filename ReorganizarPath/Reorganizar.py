'''
Created on 28/03/2015

@author: nicolas
'''

import re
import os
from cambiadorTexto.ArbolDirectorio import ArbolDirectorio
from cambiadorTexto.ManejadorArchivos import ManejadorArchivos
from cambiadorTexto.FuncionesPath import FuncionesPath

class Reorganizar(object):
    '''
    Reorganiza paths contenidos en documentos latex
    '''

    _pathLatex = None
    _raizPath  = None
    _manejadorDirectorios = None

    def __init__(self, pathLatex):
        self._pathLatex = FuncionesPath.quitarSeparadorRaiz(pathLatex)
        self._manejadorDirectorios = ArbolDirectorio(self._pathLatex)
        self._raizPath = FuncionesPath.separarUltimaCarArch(self._pathLatex)
        
    def encontrado(self, encontrados, posibleEncontrado):
        for i in range(0,len(encontrados)):
            if encontrados[i][0] == posibleEncontrado:
                return i
        return -1
    
    def reorganizarImagenes(self):
        archivosTex = self._manejadorDirectorios.getArchivos('.*\.tex$', True)
        encontrados = []
        for path in archivosTex:
            archivo = ManejadorArchivos(path)
            if archivo.existeArchivo():
                for i in archivo.obtenerLineas('includegraphics'):
                    i = re.findall(r'\{.*\}', i)[0]
                    i = i[1:len(i) - 1]
                    indiceImagen = 0
                    if i[0] == '.':
                        indiceImagen = 1
                    if str(i[indiceImagen:])[0] == os.sep:
                        indiceImagen = indiceImagen + 1
                    pathImagen = self._pathLatex + os.sep + i[indiceImagen:]
                    iEncontrado = self.encontrado(encontrados, i)
                    if iEncontrado == -1:
                        archivoImagen = ManejadorArchivos(pathImagen)
                        if not archivoImagen.existeArchivo():
                            encontrada = self._manejadorDirectorios.encontrarArchivo(\
                                         archivoImagen.getNombreArchivo())
                            if len(encontrada) > 0:
                                match = re.search(str('(' + self._raizPath + os.sep + ')'), encontrada[0])
                                encontrados.append([i, \
                                                    \
                                                    '.' + os.sep + \
                                                    encontrada[0][(match.end()):], \
                                                    [path]])
                            else:
                                print('--** No encontrado: ' + archivoImagen.getNombreArchivo())
                    else:
                        if path not in encontrados[iEncontrado][2]:
                            encontrados[iEncontrado][2].append(path)

        for i in encontrados:
            for j in i[2]:
                archivoCambio = ManejadorArchivos(j)
                if archivoCambio.existeArchivo():
                    archivoCambio.cambiarLineas(i[0], \
                                                i[1], \
                                                '../archivos_copia/' + archivoCambio.getNombreArchivo() + '_copia')
        