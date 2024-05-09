# COMENTARIOS

# Los comentarios son anotaciones que el programa no tiene en cuenta.
# Podemos añadirlos de una sola línea con #.
"""O bien lo haremos 
utilizando triple doble comillas
si vamos a ocupar varias líneas."""



# VARIABLES

# Podemos asignar una variable a otra variable:
var1 = "Hola Python"
var2 = var1     # var2 almacena el mismo valor asignado a var1
print(var2)     # Muestra el valor: Hola Python

# Pueden contener A-Z, a-z, 0-9 y _. Cualquier otro carácter dará error:
var& = "Hola Python"    # Este carácter (&) dará error de sintaxis.

# El primer carácter de una variable no puede ser un dígito:
1var = "Hola Python"

# Es sensible a mayúsculas y minúsculas.
Var3 = "Hola Python"
print(var3)     # Error, var3 no está definido.


# Declaración de variable string:
nombre1 = "Juan Manuel"             # Comillas dobles.
nombre2 = 'Jose Ramón'              # Comillas simples.
frase1 = 'Pedro es "amigo" mío.'    # Comillas dobles forman parte de la frase.

# Declaración de variable string en varias líneas:
frase2 = """Esta es una frase
con tres saltos
de linea."""                        # Triple comillas dobles.
frase3 = '''Esta es una frase
con tres saltos
de linea.'''                        # Triple comillas simples.


# Declaración de variable numérica entera:
numero1 = 29        # int

# Declaración de variable numérica decimal:
numero2 = 12.85     # float

# Podemos sobreescribir el valor de una variable numérica y convertirla en string añadiendo "" o '':
numero1 = "29"      # string


# Para declarar constantes utilizaremos MAYÚSCULAS:
NUMEROPI = 3.14159


# Declaración de booleanos:
verdadero = True
falso = False

# Cuando se valida una condición devuelve True o False:
print(5 > 3)        # True
print(8 == 7)       # False
print(10 < 9)       # False


# Declaración múltiple en una sola instrucción:
a, b, c = "String", 32, True

# Es lo mismo que poner:
a = "String"
b = 32
c = True


# Para comprobar el tipo de cualquier objeto usamos la función type():
print(type(numero1))
print(type(frase1))
print(type(NUMEROPI))
print(type(verdadero))




# CASTING

# Forzado de tipo entero:
x = int(1)      # x = 1
y = int(2.8)    # y = 2
z = int("3")    # z = 3
w = int("4.2")  # Nos devuelve error.

# Forzado de tipo decimal:
x = float(1)      # x = 1.0
y = float(2.8)    # y = 2.8
z = float("3")    # z = 3.0
w = float("4.2")  # w = 4.2

# Forzado de tipo string:
x = str("s1")     # x = "s1"
y = str(2)        # y = "2"
z = str(3.0)      # z = "3.0"


# Reconversión de entero a flotante:
n_numero1 = 19
n_numero2 = float(n_numero1)

# Reconversión de flotante a entero:
n_numero3 = 28.429
n_numero4 = int(n_numero3)

# Reconversión de string a entero:
s_texto1 = "23"
n_numero5 = int(s_texto1)

# Reconversión de entero a string:
n_numero6 = 95
s_texto2 = str(n_numero6)




# STRING

# Podemos concatenar textos utilizando + o , con la siguiente diferencia:
print("Hola" + "mundo")     # = Holamundo + no deja espacio.
print("Hola" , "mundo")     # = Hola mundo , deja espacio.

# Concatenación y multiplicación de strings:
a = "uno"
b = "dos"
c = a + b   # c = unodos
d = a * 3   # d = unounouno


# .lower() convierte el string en minúsculas:
s_texto3 = "ESTE TEXTO ESTÁ EN MAYÚSCULAS."
print(s_texto3.lower())         # = este texto está en mayúsculas.

# .capitalize() pone la primera letra en mayúscula:
s_texto4 = "este texto no tenía mayúsculas."
print(s_texto4.capitalize())    # = Este texto no tenía mayúsculas.

# .count() cuenta cuantas veces aparece un carácter o string:
s_texto5 = "Vamos a comprobar cuántas veces aparece la letra c."
print(s_texto5.count("c"))      # = 5

# .find() representa la primera posición en la cual aparece un carácter o string:
s_texto6 = "Vamos a comprobar en qué posición aparece comprobar en el texto."
print(s_texto6.find("comprobar"))       # = 8

# .rfind() misma función que .find(), empezando a la inversa:
s_texto7 = "Vamos a comprobar en qué posición aparece comprobar en el texto."
print(s_texto7.rfind("comprobar"))      # = 42

# Devuelven un boolean, deben ir entre comillas "".
# .isdigit() comprueba que el valor sea sólo numérico:
s_texto8 = "29"
print(s_texto8.isdigit())       # True
s_texto9 = "29a"
print(s_texto9.isdigit())       # False

# .isalnum() comprueba que no hay caracteres especiales en el valor:
s_texto10 = "abc123"
print(s_texto10.isalnum())      # True
s_texto11 = "abc!123"
print(s_texto11.isalnum())      # False

# .isalpha() comprueba que sólo hay letras:
s_texto12 = "Holamundo"
print(s_texto12.isalpha())      # True
            # "Hola mundo" o "Holamundo." nos devolvería False

# .split() separa por palabras creando una lista:
s_texto13 = "Vamos a separar esta frase por los espacios."
print(s_texto13.split())
# ['Vamos', 'a', 'separar', 'esta', 'frase', 'por', 'los', 'espacios.']

# .strip() elimina los espacios sobrantes a principio y final:
s_texto14 = "    Este texto contenía espacios al principio y al final.    "
print(s_texto14.strip())    # Este texto contenía espacios al principio y al final.

# .replace() reemplaza un carácter o un string por otro:
s_texto15 = "Vamos a reemplazar la palabra casa."
print(s_texto15.replace("casa", "hogar"))   # Vamos a reemplazar la palabra hogar.




# ENTRADA DE DATOS input()

# Nos permite introducir datos en la terminal:
s_nombreIntroducido1 = input("Introduzca su nombre: ")
print("Bienvenido", s_nombreIntroducido1)

# Si necesitamos operar con números tendremos que hacer un casting:
s_edadIntroducida1 = int(input("Introduza su edad: "))
print("El año que viene tendrá", s_edadIntroducida1 + 1, "años.")


# SALIDA DE DATOS print()

# Salida directa de datos:
print("Imprimimos diréctamente por pantalla este texto.")

# Salida de datos calculados:
numero_1 = 9
numero_2 = 3
print("El resultado de sumar" , numero_1 , "+" , numero_2 , "=" , (numero_1 + numero_2))
        # El resultado de sumar 9 + 3 = 12



# OPERADORES

# % Módulo, nos devuelve el resto de una división:
n_numerador1 = 85
n_denominador1 = 9
n_resto1 = n_numerador1 % n_denominador1
print("El resto de dividir", n_numerador1, "entre", n_denominador1, "es", n_resto1)

# == Igual que..., comprueba si dos objetos son iguales:
n_numero7 = 19
s_texto16 = "19"
print(n_numero7 == s_texto16)       # False
n_numero8 = 19
n_numero9 = 19
print(n_numero8 == n_numero9)       # True

# != Diferente que..., comprueba si dos objetos son diferentes:
n_numero7 = 19
s_texto16 = "19"
print(n_numero7 != s_texto16)       # True
n_numero8 = 19
n_numero9 = 19
print(n_numero8 != n_numero9)       # False

# += Suma e incremento:
n_numero10 = 99
n_numero10 += 1     # Igual que poner: n_numero10 = n_numero10 + 1
print(n_numero10)   # 100



# OPERADORES LÓGICOS

a = True
b = False

# and si un valor es False el resultado será False:
resultado = a and b
print(resultado)        # False

# or si un valor es True el resultado será True:
resultado = a or b
print(resultado)        # True

# not si el valor es True el resultado será False, si el resultado es False será True:
resultado = not a
print(resultado)        # False
resultado = not b
print(resultado)        # True



# OBJETOS MUTABLES E INMUTABLES

# Obtener la dirección de memoria de una variable:
f = 95
print("La dirección de memoria es", id(f))

# Obtener la dirección de memoria de una variable que apunta a otra:
miNumero1 = 95
miNumero2 = miNumero1
print("La dirección de memoria es", id(miNumero1))
print("La dirección de memoria es", id(miNumero2))
        # En ambos casos el resultado es el mismo.



# IMPORTAR MÓDULOS EXTERNOS

# random, número aleatorio:
import random
numero_aleatorio1 = random.randint(0, 999)
print(numero_aleatorio1)        # Elige un número al azar entre 0 y 999.

lista1 = [1, 2, 3, 4, 5]
print(random.choice(lista1))   # Elige un número al azar de la lista.


# math, operaciones matemáticas:
import math
h = math.pi         # .pi operaciones con el número pi.
print(h)            # 3.141592653589793
h = math.pi * 4
print(h)            # 12.566370614359172

j = math.sqrt(4)    # .sqrt operaciones con raíz cuadrada.
print(j)            # 2.0
j = math.sqrt(15)
print(j)            # 3.872983346207417



# SENTENCIAS CONDICIONALES

# Sentencia if:
a = int(input("Introduzca un número: "))
b = int(input("Introduzca un número: "))
if a > b:
    print("Se ha cumplido la condición.")
print("Ya estamos fuera del if.")

# Sentencia else if:
a = int(input("Introduzca un número: "))
b = int(input("Introduzca un número: "))
if a > b:
    print("Se ha cumplido la condición.")
else:
    print("No se ha cumplido la condición.")
print("Ya estamos fuera del if.")

# Sentencia elif:
a = int(input("Introduzca un número: "))
b = int(input("Introduzca un número: "))
if a > b:
    print(a, "es mayor que", b)
elif a == b:
    print(a, "es igual que", b)
else:
    print(a, "es menor que", b)


# Bucle while:
a = int(input("Introduzca un número: "))
while a < 50:
    print(a, end="  ")
    a += 1
print(a)
print("Hemos salido fuera del while")


# Operador ternario:
num = int(input("Introduzca un número: "))
if num % 2 == 0:
    print(num, "es un número par.")
else: print(num, "es un número impar.")


# Bucle for:
for numero in range(int(input("Introduzca un número: "))):
  print(numero)     # Recorre la secuencia desde 0 hasta el número anterior al introducido.




# LISTAS

# La lista es una colección ordenada y modificable.
def miFunccion(listaFrutas):
    for x in listaFrutas:
        print(x)
frutas = ["manzana", "pera", "cereza", "plátano", "naranja"]
miFunccion(frutas)      # Así podemos recorrer una lista.