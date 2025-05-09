from clase_pedido import Pedido
import csv

class Gestor_pedidos:
    listado_pedidos:list
    def __init__(self):
        self.listado_pedidos = []
    def leer_archivo_pedidos(self):
        with open('datosPedidos.csv','r',encoding='utf-8') as archivo:
            lector = csv.reader(archivo,delimiter=',')
            for fila in lector:
                patente = fila[0].split()[0]
                ID_pedido = fila[1].split()[0]
                cant_comidas= fila[2].split()[0]
                tiempo_entrega= fila[3].split()[0]
                precio = fila[4].split()[0]
                datos_pedido = Pedido(patente,ID_pedido,cant_comidas,tiempo_entrega,precio)
                self.listado_pedidos.append(datos_pedido)
                return self.listado_pedidos