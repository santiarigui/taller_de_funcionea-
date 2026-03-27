# promedio , nota alta y bajas

def analizar_notas(lista_notas):
    promedio = sum(lista_notas) / len(lista_notas)
    nota_alta = max(lista_notas)
    nota_baja = min(lista_notas)
    return promedio, nota_alta, nota_baja

# Ejemplo
notas = [3.2, 4.0, 3,0, 5.0]
print(analizar_notas(notas))



# estudiantes aprobados(notas>3.0)

def aprobados(lista_estudiantes):
    return [nombre for nombre, nota in lista_estudiantes if nota >= 3.0]

# Ejemplo
datos = [("Ana", 4.0), ("Luis", 2.5), ("Pedro", 3.2)]
print(aprobados(datos))

#Agenda con diccionario
agenda = {}

def agregar(nombre, telefono):
    agenda[nombre] = telefono

def buscar(nombre):
    return agenda.get(nombre, "No encontrado")

def eliminar(nombre):
    agenda.pop(nombre, None)
    
#inventario(valor total)
def valor_total(inventario):
    total = 0
    for producto in inventario:
        total += producto["precio"] * producto["cantidad"]
    return total

# Ejemplo
inventario = [
    {"nombre": "Mouse", "precio": 20000, "cantidad": 2},
    {"nombre": "Teclado", "precio": 50000, "cantidad": 1}
]
print(valor_total(inventario))

#frecuencia de palabras
def frecuencia_palabras(lista):
    diccionario = {}
    for palabra in lista:
        diccionario[palabra] = diccionario.get(palabra, 0) + 1
    return diccionario

# temperaturas por ciudad
def temperaturas(datos):
    max_temp = ("", float("-inf"))
    min_temp = ("", float("inf"))

    for ciudad, temps in datos.items():
        for t in temps:
            if t > max_temp[1]:
                max_temp = (ciudad, t)
            if t < min_temp[1]:
                min_temp = (ciudad, t)

    return max_temp, min_temp

# notas a letras
def convertir_nota(nota):
    if nota >= 4.5:
        return "A"
    elif nota >= 4.0:
        return "B"
    elif nota >= 3.0:
        return "C"
    elif nota >= 2.0:
        return "D"
    else:
        return "F"

def reporte(estudiantes):
    return [(nombre, convertir_nota(nota)) for nombre, nota in estudiantes]

# carrito de compras
carrito = []

def agregar_producto(nombre, precio):
    carrito.append(precio)

def aplicar_descuento(porcentaje):
    return sum(carrito) * (1 - porcentaje / 100)

def total():
    return sum(carrito)

#agrupacion por categoria
def agrupar(lista):
    resultado = {}
    for producto, categoria in lista:
        if categoria not in resultado:
            resultado[categoria] = []
        resultado[categoria].append(producto)
    return resultado

#sistema de votos
def votos(lista_votos, candidatos):
    conteo = {c: 0 for c in candidatos}
    invalidos = 0

    for voto in lista_votos:
        if voto in candidatos:
            conteo[voto] += 1
        else:
            invalidos += 1

    total = sum(conteo.values())
    ganador = max(conteo, key=conteo.get)
    porcentaje = (conteo[ganador] / total) * 100 if total > 0 else 0

    return ganador, porcentaje, invalidos

