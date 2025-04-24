import random
import math
import re

# Entrenando la programación

# 1 - Crea un programa que tenga la siguiente lista con los gastos de una empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Con estos valores, crea un programa que calcule el promedio de gastos. Sugerencia: usa las funciones integradas sum() y len().

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08];
print(f"El promedio es {sum(gastos)/len(gastos)}");

# 2 - Con los mismos datos de la pregunta anterior, determina cuántas compras se realizaron por encima de 3000 reales y calcula el porcentaje con respecto al total de compras.
count = 0;

for gasto in gastos:
    if gasto > 3000:
        count += 1;

porcentaje = count * 10;

print(f"\nPorcentaje de compras mayores de 3000 {porcentaje}%")

# 3 - Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].

lista_random = [];

for item in range(1, 6):
    lista_random.append(gastos[int(random.random() * 10)])

print(f"\nLista random: {lista_random}");

# 4 - Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado.

lista_random_inversa_original = [];
lista_random_inversa = []

for item in range(1, 6):
    lista_random_inversa_original.append(gastos[int(random.random() * 10)]);

lista_random_inversa = lista_random_inversa_original[::-1];

print(f"\n{lista_random_inversa_original} \n{lista_random_inversa}");

# 5 - Crea un programa que, al ingresar un número cualquiera, genere una lista que contenga todos los números primos entre 1 y el número ingresado.

print("\nDigita un numero")
n = int(input());

def cribaEratostenes(n):
    lista_boleana = [True] * (n+1);
    lista_boleana[0] = lista_boleana[1] = False;

    for i in range(2, int(math.sqrt(n) + 1)):
        if lista_boleana[i]:
            for j in range(i * i, n + 1, i):
                lista_boleana[j] = False

    return [x for x in range(n + 1) if lista_boleana[x]]

print(f"Los numeros primos hasta ese digito son: {cribaEratostenes(n)}");

# 6 - Escribe un programa que pida una fecha, especificando el día, mes y año, y determine si es válida para su análisis.

print("\nEscribe una fecha por dia mes y ano")
fecha = input();

if re.match(r'\d{2}\s*\d{2}\s*\d{4}', fecha):
    print("Fecha valida")
else:
    print("Fecha no valida")

# Momento para los proyectos

# 7 - Para un estudio sobre la multiplicación de bacterias en una colonia, se recopiló el número de bacterias multiplicadas por día y se puede observar a continuación: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Con estos valores, crea un código que genere una lista que contenga el porcentaje de crecimiento de bacterias por día, comparando el número de bacterias en cada día con el número de bacterias del día anterior. Sugerencia: para calcular el porcentaje de crecimiento, utiliza la siguiente ecuación: 100 * (muestra_actual - muestra_anterior) / muestra_anterior.

lista_bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
porcentaje_incremento_por_dia = [0];

for x in range(1, len(lista_bacterias)):
    porcentaje = round(100 * ((lista_bacterias[x] - lista_bacterias[x-1]) / lista_bacterias[x-1]), 2)
    porcentaje_incremento_por_dia.append(porcentaje)

print(f"\nPorcentaje de crecimiento en bacterias por dia: {porcentaje_incremento_por_dia}");

# 8 - Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados por números enteros, sabiendo que los productos con ID par son dulces y los que tienen ID impar son amargos. Crea un código que recoja 10 IDs. Luego, calcula y muestra la cantidad de productos dulces y amargos.

IDs = [9878, 98347, 98749369, 876873, 2387, 928379874, 98798743, 9874397, 876876]
dulces = []
amargos = []

for x in IDs:
    if x % 2 == 0:
        dulces.append(x)
    else: 
        amargos.append(x)

print(f"\nLa cantidad de IDs dulces son: {len(dulces)}\n{dulces} \nLa cantidad de IDs amargos son: {len(amargos)}\n{amargos}")


# 9 - Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas. Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide con el resultado. Cada pregunta vale un punto y hay opciones A, B, C o D.

# Resultado del examen:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B

print("\n")
respuestas = ['D','A','C','B','A','D','C','C','A','B']
puntuacion = 0

for x in range(1, 11):
    print(f"Respuesta de la pregunta {x}: ")
    respuestas_estudiante = input().upper()

    if respuestas_estudiante == respuestas[x - 1]:
        puntuacion += 1;

print(f"\nLa puntucion del estudiante es: {puntuacion}")

# 10 - Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año. Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista. Luego, calcula el promedio anual de las temperaturas y muestra todas las temperaturas por encima del promedio anual y en qué mes ocurrieron, mostrando los meses por su nombre (Enero, Febrero, etc.).
print("\n")
temperturas = {'Enero': '', 'Febrero':'', 'Marzo':'', 'Abril':'', 'Mayo':'', 'Junio':'', 'Julio':'', 'Agosto':'', 'Septiembre':'', 'Octubre':'', 'Noviembre':'', 'Diciembre':''}
temperatura_fuera_del_promedio = []
media = 0

for x in temperturas:
    print(f"Temperatura en {x}")
    temperatura = int(input())
    media += temperatura
    temperturas[x] = temperatura

media = media / 12

for x in temperturas:
    if temperturas[x] > media:
        temperatura_fuera_del_promedio.append(x);

print(f"Meses fuera de la temperatura promedio : {temperatura_fuera_del_promedio}")

# 11 - Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos. Los datos de ventas se han almacenado en un diccionario:

# {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

# Escribe un código que calcule el total de ventas y el producto más vendido.

print("\n")
productos = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}
total_de_ventas = 0

for x in productos:
    total_de_ventas += int(productos[x])


mas_vendido = max(productos.values())
producto = [k for k, v in productos.items() if v == mas_vendido]

print(f"Las ventas totales son: {total_de_ventas} y el producto mas vendido fue: {producto}")

