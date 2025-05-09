from clase_moto import Moto
import csv

class GestorMotos:
    motos:list
    
    def __init__(self):
        self.motos=[]
    
    def leer_archivo_motos(self,archivo):
        with open("datosMotos.csv",'r',encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            for fila in lector:
                patente = str(fila[0].split()[0])
                marca = str(fila[1].split()[0])
                nombre = str(fila[2].split()[0])
                apellido = str(fila[3].split()[0])
                kilometraje = fila[4].split()[0] #ignore type
                datos_moto = Moto(patente,marca,nombre,apellido,kilometraje)
                self.motos.append(datos_moto)
                return self.motos
            

        