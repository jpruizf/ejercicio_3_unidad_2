from gestor_moto import GestorMotos
def menu():
    gestor_motos = GestorMotos()
    print("1.Registrar datos de las motos en un archivo:")
    print("2.Registrar datos de los pedidos en un archivo:")
    print("3.Registrar un nuevo pedido:")
    print("4.Ingresar numero de patente e identificador de pedido y tiempo de entrega:")
    print("5.Mostrar el nombre del conductor y tiempo promedio de un pedido ingresando la patente de la moto:")
    print("6.Listado de pago de comisiones para cada conductor de cada moto:")
    print("0.finalizar")
    opcion = input("Ingrese una de las opciones dadas:")
    while(opcion != '0'):
        if opcion == '1':
            if(gestor_motos.leer_archivo_motos('datosMotos.csv')):
                print("Carga exitosa!")
        elif opcion == '2':
            pass
        print("1.Registrar datos de las motos en un archivo:")
        print("2.Registrar datos de los pedidos en un archivo:")
        print("3.Registrar un nuevo pedido:")
        print("4.Ingresar numero de patente e identificador de pedido y tiempo de entrega:")
        print("5.Mostrar el nombre del conductor y tiempo promedio de un pedido ingresando la patente de la moto:")
        print("6.Listado de pago de comisiones para cada conductor de cada moto:")
        print("0.finalizar")
        opcion = input("Ingrese una de las opciones dadas:")
if __name__ == '__main__':
    menu()