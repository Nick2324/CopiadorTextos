'''
Created on 28/03/2015

@author: nicolas
'''
from ReorganizarPath.Reorganizar import Reorganizar

if __name__ == '__main__':
    ro = Reorganizar('/media/Archivos/Documentos/IngenieriaDeSistemas/' + \
                     'Tesis/tesis_red_social/Proyecto')
    ro.reorganizarImagenes()
    print('Reorganizacion terminada con éxito')