

recorridos = [
    {}
]
venta = [
    {}
]

def validacion_int_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Valor debe ser postivo.")
            else:
                return valor
        except Exception:
            print("Valor debe ser un numero entero.")

def validacion_str(mensaje):
    while True:
        valor = (input(mensaje))
        if len(valor.replace(" ","")):
            print("Valor no puede ser solo espacios vacios.")
        else:
            return valor

def validacion_codigo(mensaje)->bool:
    codigo = input(mensaje)
    for i in recorridos:
        if i == codigo:
            return False
        else:
            return codigo
    if len(codigo.replace(" ","")) == 0:
        return False
    else:
        return codigo

def validacion_precio(mensaje):
    while True:
        try:
            precio = int(input(mensaje))
            if precio < 0:
                return False
            else:
                return precio
        except Exception:
            return False
        
def validacion_asientos(mensaje):
    while True:
        try:
            asientos = int(input(mensaje))
            if asientos < 0:
                return False
            else:
                return asientos
        except Exception:
            return False

def validacion_origen(mensaje)->bool:
    while True:
        origen = (input(mensaje))
        if len(origen.replace(" ","")) == 0:
            return False
        else:
            return origen
        
def validacion_destino(mensaje)->bool:
    while True:
        destino = (input(mensaje))
        if len(destino.replace(" ","")) == 0:
            return False
        else:
            return destino

def validacion_distancia(mensaje):
    while True:
        try:
            distancia = int(input(mensaje))
            if distancia < 0:
                return False
            else:
                return distancia
        except Exception:
            return False

def asientos_origen(origen:str,recorridos:list,venta:list):
    origen.capitalize
    for i in recorridos:
        if i == origen:
            for i in venta:
                print(f"El total de asientos disponibles es: {i[1]}")

def validacion_tipo_bus(mensaje):
    tipo_bus = input(mensaje)
    if tipo_bus == "normal" or "semi-cama" or "cama":
        return tipo_bus
    else:
        return False
    
def validacion_tiene_wifi(mensaje):
    tiene_wifi = input(mensaje)
    if tiene_wifi == "s" or "n":
        return tiene_wifi
    else:
        return False
    
def validacion_servicio(mensaje):
    servicio = input(mensaje)
    if servicio == "dia" or "noche":
        return servicio
    else:
        return False

def agregar_recorrido(codigo, origen, destino, distancia, tipo_bus, servicio,
tiene_wifi, precio, asientos,recorridos:list,venta:list):

    anadido = {
        codigo:[origen,destino,distancia,tipo_bus,servicio,tiene_wifi]
    }

    recorridos.append(anadido)

    anadido_ventas = {
        codigo:[precio,asientos]
    }

    venta.append(anadido_ventas)

    print("Recorrido agregado.")

def busqueda_precio(p_min:int,p_max:int,venta:list):
    print("Desafortunadamente, no logre que funcionara esta opcion. :(")
    #    for i in venta:
    #        if i >= p_min and i <= p_max:
    #            print("En el rango solicitado se encuentras los siguientes recorridos: ")
    #            print(f"{i}")

def actualizar_precio(codigo, nuevo_precio,venta:list):
    while True:
        for i in venta:
            if i == codigo:
                i[1] == nuevo_precio
            else:
                print("El codigo no existe.")
                nueva_opcion = input("¿Desea actualizar otro precio (s/n)?")
                if nueva_opcion == "n":
                    return

def eliminar_codigo(codigo,venta:list,recorridos:list):
    for i in venta:
        if i == codigo:
            recorridos.remove(codigo)
            venta.remove(codigo)
        else:
            print("El codigo no existe.")

def menu():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Asientos por ciudad de origen")
        print("2. Búsqueda de recorridos por rango de precio")
        print("3. Actualizar precio de recorrido")
        print("4. Agregar recorrido")
        print("5. Eliminar recorrido")
        print("6. Salir")
        print("=====================================")
        opcion = validacion_int_positivo("Ingrese una opcion: ")
        if opcion < 1 or opcion > 6:
            print("Debe seleccionar una opción válida.")

        elif opcion == 1:
            origen = validacion_origen("Ingrese ciudad a buscar: ")
            if origen == False:
                print("Ingreso fallido.")
                return
            else:
                asientos_origen(origen,recorridos,venta)

        elif opcion == 2:
            p_min = validacion_int_positivo("Ingrese el precio minimo: ")
            p_max = validacion_int_positivo("Ingrese precio maximo: ")
            while True:
                if p_min >= p_max:
                    print("Valor minimo es mayor o igual al valor maximo, ingrese otra vez.")
                else:
                    break
            busqueda_precio(p_min,p_max,venta)
        elif opcion == 3:
            codigo = validacion_codigo("Ingrese codigo a actualizar: ")
            nuevo_precio = validacion_int_positivo("Ingrese el nuevo precio: ")
            actualizar_precio(codigo,nuevo_precio,venta)

        elif opcion == 4:
            codigo = validacion_codigo("Ingrese codigo del nuevo recorrido: ")
            if codigo == False:
                print("Codigo invalido. Operacion fallida.")
                return
            origen = validacion_origen("Ingrese lugar de origen del recorrido: ")
            if origen == False:
                print("Origen invalido. Operacion fallida.")
                return
            destino = validacion_destino("Ingrese el lugar de destino del recorrido: ")
            if destino == False:
                print("Destino invalido. Operacion fallida.")
                return
            distancia = validacion_distancia("Ingrese la distancia del recorrido (km): ")
            if distancia == False:
                print("Distancia invalido. Operacion fallida.")
                return
            tipo_de_bus = validacion_tipo_bus("Ingrese el tipo de bus (normal/semi-cama/cama): ")
            if tipo_de_bus == False:
                print("Tipo de bus invalido. Operacion fallida.")
                return
            servicio = validacion_servicio("Ingrese el tipo de servicio (dia/noche): ")
            if servicio == False:
                print("Sevicio invalido. Operacion fallida.")
                return
            tiene_wifi = validacion_tiene_wifi("Ingrese la disponibilidad del WIFI (s/n): ")
            if tiene_wifi == False:
                print("invalido. Operacion fallida.")
                return
            precio = validacion_precio("Ingrese el precio del recorrido: ")
            if precio == False:
                print("Precio invalido. Operacion fallida.")
                return
            asientos = validacion_asientos("Ingrese el numero de asientos del recorrido: ")
            if asientos == False:
                print("Asientos invalido. Operacion fallida.")
                return
            agregar_recorrido(codigo,origen,destino,distancia,precio,tipo_de_bus,servicio,tiene_wifi,asientos,recorridos,venta)
            
        elif opcion == 5:
            codigo = validacion_codigo("Ingrese codigo a eliminar: ")
            eliminar_codigo(codigo,venta,recorridos)

        elif opcion == 6:
            print("Programa finalizado.")
            break


menu()
