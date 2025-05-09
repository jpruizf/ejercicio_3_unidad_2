import datetime
class Pedido:
    __patente_pedido:str
    __Id_pedido:str
    __tiempo_entrega: datetime.time
    __precio:float
    __cant_comidas:int
    def __init__(self,patente,id,tiempo,cant_comidas,precio):
        self.__patente_pedido = patente
        self.__Id_pedido = id
        self.__tiempo_entrega=tiempo
        self.__cant_comidas=cant_comidas
        self.__precio=precio
    def get_patente_pedido(self):
        return self.__patente_pedido
    def get_id_pedido(self):
        return self.__Id_pedido
    def get_tiempo_entrega(self):
        return self.__tiempo_entrega
    def get_precio(self):
        return self.__precio
    def get_cant_comidas(self):
        return self.__cant_comidas