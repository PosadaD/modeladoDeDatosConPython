# 1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.

# ! pip install matplotlib==3.7.1

# 2 - Escribe un código para importar la biblioteca numpy con el alias np.

import numpy as np;

# 3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.

lista = np.array([8, 12, 54, 23, 43, 1, 90, 87, 105, 77]);
rng = np.random.default_rng()
numeroRandomArray = rng.choice(lista);

print(numeroRandomArray);

# 4 - Crea un programa que genere aleatoriamente un número entero menor que 100.

numeroMenor100 = rng.integers(100);

print(numeroMenor100);  

# 5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y calcule la potencia del primer número elevado al segundo.

numero1 = int(input())
numero2 = int(input())

exp = np.emath.power(numero1, numero2);

print(exp)

# Aplicando a proyectos

# 6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes. Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.
print("Elige el numero de participantes")
numeroParticipantes = int(input())

ganador = rng.integers(1, numeroParticipantes);

print(ganador);


# 7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. El token debe ser par y variar de 1000 a 9998. Escribe un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este token generado aleatoriamente.

print("Nombre:")
nombre_usuario = input();

token_generado = rng.integers(500, 4999) * 2;

print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")


# 8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado "ensalada de frutas sorpresa". En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente. Crea el código que realice esta selección aleatoria según la lista dada.

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

seleccionAleatoriaIngredientes = rng.choice(frutas, 3)

print(f"Tu ensalada tiene: {seleccionAleatoriaIngredientes}");


# 9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, identificando cuáles resultan en un número entero. La lista es la siguiente:

numeros = [2, 8, 15, 23, 91, 112, 256]

raizNumeros = np.emath.sqrt(numeros);
enteros = raizNumeros[raizNumeros == raizNumeros.astype(int)];

print(enteros);

# 10 - Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.

print("Radio del area circular")
radio = int(input())
precioMetroCUadrado = 25.00;

areaCIrcular = np.pi * radio ** 2;
total = areaCIrcular * precioMetroCUadrado;

print(f"Total de reales : {total}")