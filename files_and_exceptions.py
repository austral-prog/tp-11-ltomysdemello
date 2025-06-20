def read_file_to_dict(nombre_archivo):
    ventas = {}
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        producto = ""
        valor = ""
        destino = "producto"
        for caracter in contenido:
            if caracter == ":":
                destino = "valor"
            elif caracter == ";":
                monto = float(valor)
                if producto in ventas:
                    ventas[producto].append(monto)
                else:
                    ventas[producto] = [monto]  
                producto = ""
                valor = ""
                destino = "producto"
            else:
                if destino == "producto":
                    producto += caracter
                else:
                    valor += caracter
    return ventas


def process_dict(diccionario):
    for producto, ventas in diccionario.items():
        total = 0
        for monto in ventas:
            total += monto
        promedio = total / len(ventas)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
