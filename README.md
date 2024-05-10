# Hola-Python-by-Rafel




## 0. Introducción:


  ¡Domina los conceptos básicos de Python desde cero!


  En esta guía de aprendizaje encontrarás los fundamentos de Python, uno de los lenguajes de programación más populares y versátiles de la actualidad, para que puedas empezar a programar hoy mismo.


<details>
  <summary>¿Qué aprenderás?</summary>
  
  > 1. Funciones: Crea funciones reutilizables para un código más eficiente.
  >
  > 2. Estructuras de datos: Almacena y organiza información con listas, tuplas y diccionarios.
  >  
  > 3. Estructuras de control: Controla el flujo de tu programa con condicionales y bucles.
  >   
  > 4. Entrada/salida: Interactúa con el usuario y con archivos.
  >   
  > 5. Módulos y paquetes: Aprovecha el código de otros para potenciar tus programas.
  >   
  > 6. Programación orientada a objetos: Diseña programas robustos y escalables con clases y objetos.
</details>




## 1. Comentarios:


> Los comentarios son líneas de texto que se agregan al código para explicar su funcionamiento o propósito. No se ejecutan como parte del programa, sino que sirven como notas para el programador o para otras personas que lean el código.



### 1.1. Comentarios de una línea:


  > [!CAUTION]
  > Comienzan con el símbolo `#` seguido del texto del comentario. 


<details>

  > Se utilizan para explicar una línea específica de código o un bloque pequeño de código.
</details>


````Python
nombre = "Juan"   # Almacena la cadena de texto "Juan"
edad = 30         # Almacena el número entero 30
print(nombre)     # Muestra el valor de la variable "nombre" en la pantalla: "Juan"
print(edad)       # Muestra el valor de la variable "edad" en la pantalla: 30
````



### 1.2. Comentarios multilínea:


  > [!CAUTION]
  > Se escriben entre comillas triples, ya sean simples `'''` o dobles `"""`.


<details>

  > Se utilizan para explicar bloques de código más extensos o para agregar información adicional que no encaja en un comentario de una sola línea.
</details>


````Python
def calcular_area_cuadrado(lado):
  """
  Función que calcula el área de un cuadrado.

  Parámetro:
    lado: La longitud del lado del cuadrado.

  Retorno:
    El área del cuadrado.
  """
  area = lado * lado
  return area
````


> [!TIP]
> <details>
  > <summary>Beneficios de usar comentarios.</summary>
  >
  > 1. Mejoran la legibilidad del código: Los comentarios hacen que el código sea más fácil de entender para el programador que lo escribió y para  otras personas que lo lean.
  > 2. Documentan el código: Los comentarios explican el propósito del código y cómo funciona, lo que facilita su mantenimiento y actualización en el futuro.
  > 3. Aumentan la colaboración: Los comentarios ayudan a que otros programadores comprendan mejor el código, lo que facilita la colaboración en proyectos.
</details>




## 2. Variables:


<details>
  
  > Imagina que estás organizando una fiesta y necesitas llevar un registro de la cantidad de invitados. Para ello, utilizas una lista de nombres en un papel. Las variables funcionan de manera similar, son como etiquetas que nos permiten almacenar y manipular información.
</details>


  Para declarar una variable, utilizamos el siguiente formato:

  `nombre_variable = valor`


> [!IMPORTANT]
  > nombre_variable: Es el nombre que le damos a la variable, como si fuera una etiqueta que la identifica.
  > 
  > valor: Es la información que queremos almacenar en la variable. Puede ser un número, una cadena de texto, un valor booleano, etc.


````Python
var1 = "Hola Python"

# Podemos asignar una variable a otra variable:
var2 = var1     # var2 almacena el mismo valor asignado a var1
print(var2)     # Muestra el valor: Hola Python

# Pueden contener A-Z, a-z, 0-9 y _. Cualquier otro carácter dará error:
var& = "Hola Python"    # Este carácter (&) dará error de sintaxis.

# El primer carácter de una variable no puede ser un dígito:
1var = "Hola Python"

# Es sensible a mayúsculas y minúsculas.
Var3 = "Hola Python"
print(var3)     # Error, var3 no está definido.
````




## 3. Tipos de datos:


  > No todas las variables almacenan el mismo tipo de información. Cada tipo de dato tiene características y usos específicos.



### 3.1. Cadenas de texto:


  > [!CAUTION]
  > Se escriben entre comillas simples `'` o dobles `"`.


<details>
  
  > Representan secuencias de caracteres, como nombres, frases o descripciones.
  >
  > Pueden contener letras, números, símbolos y espacios en blanco.
  >
  > Se utilizan para almacenar y mostrar información textual.
</details>


````Python
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
````



### 3.2. Números:


  > [!CAUTION]
  > Pueden ser enteros `int` 1, 50, -100 o decimales `float` 1.5, 3.14, -75.28.


<details>
  
  > Se escriben sin comillas.
  >
  > Representan valores numéricos, como cantidades o edades. 
</details>


````Python
# Declaración de variable numérica entera:
numero1 = 29        # int

# Declaración de variable numérica decimal:
numero2 = 12.85     # float

# Podemos sobreescribir el valor de una variable numérica y convertirla en string añadiendo "" o '':
numero1 = "29"      # string

# Para declarar constantes utilizaremos MAYÚSCULAS:
NUMEROPI = 3.14159
````



### 3.3. Booleanos:


  > [!CAUTION]
  > Representan valores lógicos, que pueden ser `True` o `False`. 


<details>
  
  > Se utilizan para indicar si algo es verdadero o falso.
  >
  > Son útiles para controlar el flujo de ejecución de un programa en base a condiciones.
</details>


````Python
# Declaración de booleanos:
verdadero = True
falso = False

# Cuando se valida una condición devuelve True o False:
print(5 > 3)        # True
print(8 == 7)       # False
print(10 < 9)       # False
````



### 3.4. Listas:


  > [!CAUTION]
  > Se escriben entre corchetes `[]` y cada elemento se separa por comas `,`.


<details>
  
  > Representan colecciones ordenadas de elementos, como listas de compras, alumnos en una clase o canciones en una playlist.
  >
  > Los elementos pueden ser de diferentes tipos de datos.
</details>


````Python
colores = ["rojo", "azul", "verde"]              # Lista de string
numeros_primos = [2, 3, 5, 7, 11]                # Lista de int
estudiantes = ["Ana", "Juan", "Pedro", "María"]  # Lista de string
````



### 3.5. Tuplas:


  > [!CAUTION]
  > Se escriben entre paréntesis `()` y cada elemento se separa por comas `,`.


<details>

  > Ordenadas: Los elementos de una tupla mantienen el orden en el que se agregaron. Se puede acceder a ellos por índice, similar a las listas.
  > 
  > Inmutables: Una vez creada, no puedes modificar los elementos de una tupla. Si necesitas cambiar el contenido, deberás crear una nueva tupla.
</details>


````Python
# Ejemplo 1: Tupla simple
frutas = ("manzana", "pera", "naranja")

# Ejemplo 2: Tupla con elementos de diferentes tipos
datos_personales = ("Juan", 30, True)

# Ejemplo 3: Tupla vacía
tupla_vacia = ()
````


<details>
  <summary>Algunas diferencias con las listas:</summary>

  > Inmutabilidad: Las listas son mutables, lo que significa que puedes modificar sus elementos después de crearlas. Las tuplas son inmutables, una vez creada no puedes cambiar su contenido.
  >
  > Uso: Las tuplas se suelen utilizar cuando se necesita una colección ordenada de elementos que no se modificará. Por ejemplo, para representar coordenadas (x, y), almacenar información fija de un producto, etc. Las listas se utilizan para colecciones que pueden cambiar o crecer con el tiempo.
</details>


> [!TIP]
> <details>
  > <summary>Ventajas de las tuplas:</summary>
  >
  > Rapidez: Las tuplas son más eficientes en memoria y acceden a sus elementos más rápido que las listas debido a su inmutabilidad.
  >
  > Seguridad: La inmutabilidad de las tuplas previene modificaciones accidentales del contenido.
  >
  > Uso como claves de diccionarios: Las tuplas se pueden utilizar como claves de diccionarios debido a su inmutabilidad, lo que garantiza que la clave no cambie de hash (un valor único que identifica a la clave).
</details>



### 3.6. Diccionarios:


  > [!CAUTION]
  > Se escriben entre llaves `{}` y cada par se separa por comas `,`.


<details>
  
  > Representan colecciones no ordenadas de pares clave-valor, como información de contacto, datos de un usuario o configuraciones de un programa.
  >
  > Las claves deben ser únicas e identificables, mientras que los valores pueden ser de cualquier tipo de dato.
</details>


````Python
persona = {"nombre": "Carlos", "edad": 28, "ciudad": "Sevilla"}  # Diccionario
contactos = {
    "amigo1": "555-1234",
    "compañero": "555-5678",
    "familiar": "555-9012"
}  # Diccionario
configuracion = {
    "modo_pantalla": "claro",
    "idioma": "español",
    "notificaciones": True
}  # Diccionario
````




## 4. Operadores:


  > Permiten realizar operaciones sobre los datos almacenados en nuestras variables.



### 4.1. Operadores aritméticos:


  > Permiten realizar operaciones matemáticas básicas.



#### 4.1.1 Operador de suma:


  > [!NOTE]
  > El operador `+` combina dos valores numéricos para obtener su suma.


````Python
numero1 = 10
numero2 = 5
suma = numero1 + numero2
print("La suma de", numero1, "y", numero2, "es =", suma)  # 15
````



#### 4.1.2. Operador de resta:


  > [!NOTE]
  > El operador `-` obtiene la diferencia entre dos valores numéricos.


````Python
numero1 = 20
numero2 = 7
resta = numero1 - numero2
print("La resta de", numero1, "y", numero2, "es =", resta)  # 13
````



#### 4.1.3. Operador de multiplicación:


  > [!NOTE]
  > El operador `*` multiplica dos valores numéricos.


````Python
numero1 = 3
numero2 = 4
multiplicacion = numero1 * numero2
print("La multiplicación de", numero1, "y", numero2, "es =", multiplicacion)  # 12
````



#### 4.1.4. Operador de división:


  > [!NOTE]
  > El operador `/` divide un valor numérico por otro.


````Python
numero1 = 16
numero2 = 4
division = numero1 / numero2
print("La división de", numero1, "entre", numero2, "es =", division)  # 4.0
````



#### 4.1.5. Operador de residuo:


  > [!NOTE]
  > El operador `%` obtiene el residuo de la división entre dos valores numéricos.


````Python
numero1 = 17
numero2 = 3
residuo = numero1 % numero2
print("El residuo de la división de", numero1, "entre", numero2, "es =", residuo)  # 2
````



#### 4.1.6. Operador de exponenciación:


  > [!NOTE]
  > El operador `**` eleva un valor numérico a una potencia.


````Python
base = 2
exponente = 3
potencia = base ** exponente
print(base, "elevado a la potencia de", exponente, "es =", potencia)  # 8
````



> [!WARNING]
> <details>
  > <summary>La prioridad se realiza de izquierda a derecha.</summary>
  > 
  > El orden de las operaciones es importante: paréntesis `()`, exponentes `**`, multiplicación `*`, división `/`, suma `+` y resta `-`.
  >
  > Se puede utilizar paréntesis para forzar un orden de ejecución diferente.
  >
  > Python también ofrece funciones matemáticas más avanzadas que puedes encontrar en la biblioteca estándar de matemáticas `math`.
</details>



### 4.2. Operadores de comparación:


  > Permiten comparar valores en los programas, obteniendo resultados booleanos `True` o `False` que indican si la comparación se cumple o no. Son esenciales para controlar el flujo de ejecución de un programa en base a condiciones específicas.



#### 4.2.1. Operador de igualdad:


  > [!NOTE]
  > Comprueba si dos valores son iguales `==`.


````Python
numero1 = 10
numero2 = 10
son_iguales = numero1 == numero2
print("¿", numero1, "es igual a", numero2, "?", son_iguales)  # True
````



#### 4.2.2. Operador de desigualdad:


  > [!NOTE]
  > Comprueba si dos valores son diferentes `!=`.


````Python
texto1 = "Hola"
texto2 = "Python"
son_diferentes = texto1 != texto2
print("¿", texto1, "es diferente a", texto2, "?", son_diferentes)  # True
````



#### 4.2.3. Operadores de mayor que y menor que:


  > [!NOTE]
  > Comparan si un valor es mayor `>` o menor `<` que otro.


````Python
edad_persona1 = 25
edad_persona2 = 20
es_mayor = edad_persona1 > edad_persona2
es_menor = edad_persona1 < edad_persona2
print("¿", edad_persona1, "es mayor que", edad_persona2, "?", es_mayor)  # True
print("¿", edad_persona1, "es menor que", edad_persona2, "?", es_menor)  # False
````



#### 4.2.4. Operadores de mayor o igual que y menor o igual que:


  > [!NOTE]
  > Comparan si un valor es mayor o igual `>=`, o menor o igual `<=`.


````Python
altura1 = 1.75
altura2 = 1.70
es_mayor_igual = altura1 >= altura2
es_menor_igual = altura1 <= altura2
print("¿", altura1, "es mayor o igual que", altura2, "?", es_mayor_igual)  # True
print("¿", altura1, "es menor o igual que", altura2, "?", es_menor_igual)  # False
````



### 4.3. Operadores lógicos:


  > Permiten combinar y evaluar condiciones en los programas, permitiendo controlar el flujo de ejecución de manera más precisa. Trabajan con valores booleanos `True` o `False` y permiten crear expresiones lógicas más complejas.



#### 4.3.1. Operador Y:


  > [!NOTE]
  > Combina dos condiciones (x) `and` (y) para verificar si ambas son ciertas. Si una de las condiciones es falsa, el resultado de la expresión completa será `False`.


````Python
esta_soleado = True
esta_caluroso = False
ir_a_la_playa = esta_soleado and esta_caluroso
print("¿Ir a la playa?", ir_a_la_playa)  # False
````



#### 4.3.2. Operador O:


  > [!NOTE]
  > Combina dos condiciones (x) `or` (y) para verificar si al menos una de ellas es cierta. Si una de las condiciones es cierta, el resultado de la expresión completa será `True`.


````Python
tiene_suficiente_dinero = False
tiene_tarjeta_credito = True
puede_pagar = tiene_suficiente_dinero or tiene_tarjeta_credito
print("¿Puede pagar?", puede_pagar)  # True
````



#### 4.3.3. Operador NO:


  > [!NOTE]
  > Si la condición original es `True`, el resultado de la expresión con `not` será `False`.
  > 
  > Si la condición original es `False`, el resultado de la expresión con `not` será `True`.


````Python
es_de_noche = True
es_de_dia = not es_de_noche
print("¿Es de día?", es_de_dia)  # False
````



### 4.4. Operadores de pertenencia:


  > [!NOTE]
  > Comprueba si un elemento está dentro `in` o no `not in` de una secuencia (lista, cadena de texto, etc.).


````Python
estudiantes = ["Ana", "Juan", "Pedro", "María"]
nombre_buscar = "Carlos"
esta_en_la_lista = nombre_buscar in estudiantes
no_esta_en_la_lista = "Carmen" not in estudiantes
print(nombre_buscar, "está en la lista de estudiantes:", esta_en_la_lista)  # False
print("Carmen", "no está en la lista de estudiantes:", no_esta_en_la_lista)  # True
````




## 5. Entrada y salida:


  > [!NOTE]
  > La función `input()` permite obtener información del usuario, como su nombre o la opción que desea seleccionar. La información se captura como una cadena de texto.


````Python
nombre_usuario = input("¿Cómo te llamas? ")
print("¡Hola,", nombre_usuario, "!")
````


  > [!NOTE]
  > La función `print()` permite mostrar resultados o mensajes en la pantalla.


````Python
resultado = 10 + 5
print("El resultado de la suma es = ", resultado)
````




## 6. Sentencias condicionales:


  > Permiten que el programa ejecute diferentes bloques de código dependiendo de si se cumple o no una condición específica.



### 6.1. Sentencia if:


  > [!NOTE]
  > `if` se utiliza para evaluar una condición y ejecutar un bloque de código si esta es verdadera.


````Python
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
# Se verifica si la variable edad es mayor o igual a 18. Si lo es, se imprime el mensaje "Eres mayor de edad".
````



### 6.2. Sentencia elif:


  > [!NOTE]
  > `elif` se utiliza para agregar más condiciones a una sentencia `if`. Permite evaluar varias condiciones de forma consecutiva.


<details>
  <summary>La sintaxis es la siguiente:</summary>


  ````Python
if condición1:
    código_a_ejecutar_si_se_cumple_la_condición1
elif condición2:
    código_a_ejecutar_si_se_cumple_la_condición2
elif condición3:
    código_a_ejecutar_si_se_cumple_la_condición3
else:
    código_a_ejecutar_si_ninguna_condición_se_cumple
````
</details>


````Python
calificacion = 85
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Sobresaliente")
elif calificacion >= 70:
    print("Notable")
elif calificacion >= 50:
    print("Aprobado")
else:
    print("Suspendido")
# Se evalúa la variable calificacion para determinar la calificación final de un estudiante.
````



### 6.3. Sentencia else:


  > [!NOTE]
  > `else` se utiliza para ejecutar un bloque de código si ninguna de las condiciones en las sentencias `if` o `elif` se cumple.


````Python
dia = "Lunes"
if dia == "Sabado":
    print("Fin de semana")
elif dia == "Domingo":
    print("Fin de semana")
else:
    print("Día de la semana")
# Se verifica el valor de la variable dia para determinar si es fin de semana.
````




## 7. Bucles:


  > Permiten ejecutar un bloque de código de forma repetitiva hasta que se cumpla una condición específica.



### 7.1. Bucle while:


  > [!NOTE]
  > `while` se utiliza para ejecutar un bloque de código mientras una condición específica sea verdadera.


````Python
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
# El bucle se ejecuta mientras la variable contador sea menor o igual a 10.
# Se imprime el valor de contador y luego se incrementa en 1.
````



## 7.2. Bucle for:


  > [!NOTE]
  > `for` se utiliza para iterar sobre una secuencia de elementos, como una lista o un rango de números.


````Python
nombres = ["Juan", "María", "Pedro"]
for nombre in nombres:
    print(f"Hola {nombre}")
# El bucle itera sobre la lista nombres y asigna cada elemento a la variable nombre.
# Se imprime un mensaje de saludo personalizado para cada nombre.
````


<details>
  <summary>Diferencias entre `while` y `for`:</summary>
  
  > 1. Uso: `while` se usa para ejecutar código mientras se cumpla una condición, mientras que `for` se usa para iterar sobre una secuencia.
  > 
  > 2. Condición: `while` requiere una condición explícita que se evalúa antes de cada iteración, mientras que `for` utiliza la posición actual en la secuencia como condición implícita.
  >   
  > 3. Modificación de la secuencia: `while` permite modificar la secuencia iterada dentro del bucle, mientras que `for` no lo permite directamente.
</details>


  > [!TIP]
> <details>
  > <summary>Elección del bucle adecuado:</summary>
  >
  > Si necesitas ejecutar un bloque de código mientras se cumpla una condición que puede cambiar con el tiempo, utiliza `while`.
  > 
  > Si necesitas iterar sobre una secuencia de elementos de forma ordenada, utiliza `for`.
</details>



### 7.3. Sentencias y bloques en bucles:


  > Además de las estructuras básicas de bucles, hay sentencias adicionales para controlar el flujo de ejecución dentro de ellos.



#### 7.3.1. Sentencia continue:


  > [!NOTE]
  > `continue` se utiliza dentro de un bucle para omitir la iteración actual y saltar directamente a la siguiente. Descarta el resto del código dentro del bucle para la iteración actual y comienza la siguiente.


````Python
for numero in range(10):
  if numero % 2 == 0:  # Omitir números pares
    continue
  print(numero)
# El bucle itera del 0 al 9. La condición if verifica si el número es par.
# Si lo es, se ejecuta la sentencia continue, omitiendo el print y pasando a la siguiente iteración.
# De esta forma, solo se imprimen los números impares.
````



#### 7.3.2. Sentencia break:


  > [!NOTE]
  > `break` se utiliza dentro de un bucle para detener la ejecución del bucle por completo. Una vez que se ejecuta, el control del programa salta fuera del bucle y continúa con la siguiente línea de código después del bucle.


````Python
for letra in "Hola mundo":
  if letra == " ":
    break  # Detener al encontrar un espacio
  print(letra)
# El bucle itera sobre cada letra de la cadena "Hola mundo".
# Cuando se encuentra un espacio, se ejecuta break, deteniendo el bucle y evitando imprimir los caracteres posteriores.
````



#### 7.3.3. Sentencia pass:

  > [!NOTE]
  > `pass` es una instrucción vacía. Se utiliza como marcador de posición para indicar un bloque de código vacío. Su principal función es mantener la sintaxis correcta del programa cuando se necesita un bloque de código pero no hay nada específico que ejecutar en ese momento.


````Python
# Ejemplo 1: Bucle vacío con pass
for i in range(3):
  pass  # Bloque vacío, solo itera 3 veces
# El bucle for itera 3 veces, pero el bloque con pass está vacío, por lo que no se ejecuta ninguna acción dentro del bucle.
````



#### 7.3.4. Bloque else en bucles:


  > [!NOTE]
  > Los bucles pueden tener un bloque `else` opcional. Este bloque se ejecuta solo una vez después de que finaliza el bucle completo. Es útil para realizar acciones que deban ocurrir después de que todas las iteraciones del bucle hayan terminado.


````Python
 for letra in "Hola":
  print(letra)
 else:
  print("Fin del bucle")
````




## 8. Iteradores:


  > [!NOTE]
  > Un iterador es un objeto que implementa el protocolo de iteración. Este protocolo define un método especial llamado `__next__` que devuelve el siguiente elemento de la secuencia en cada llamada.


  > Los iteradores permiten recorrer una secuencia sin necesidad de almacenar toda la secuencia en memoria a la vez, lo que resulta muy útil para trabajar con grandes conjuntos de datos.


````Python
def generador_numeros():
  for i in range(10):
    yield i  # Utiliza la palabra clave "yield" para generar valores.
iterador_generador = generador_numeros()  # Crea un iterador a partir de la función generadora.
for numero in iterador_generador:  # Recorre el iterador de la función generadora
  print(numero)
````



### 8.1. Iterabilidad en una clase:


  > [!NOTE]
  > 
  > `__iter__()`: Este método debe devolver un objeto iterador que representa la clase. El objeto iterador es el que permite recorrer los elementos de la clase.
  > 
  > `__next__()`: Este método debe implementarse en el objeto iterador y es el que devuelve el siguiente elemento de la secuencia cada vez que se llama.


````Python
class MiClaseIterable:

    def __init__(self, datos):
        self.datos = datos
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.datos):
            elemento = self.datos[self.indice]
            self.indice += 1
            return elemento
        else:
            raise StopIteration()

# Ejemplo de uso
clase_iterable = MiClaseIterable([1, 2, 3, 4, 5])

for elemento in clase_iterable:
    print(elemento)
````


  > [!TIP]
  >
  > La clase `MiClaseIterable` implementa los métodos `__iter__()` y `__next__()`, lo que la hace iterable.
  > 
  > El método `__iter__()` devuelve la instancia de la clase en sí misma como objeto iterador.
  > 
  > El método `__next__()` recorre la lista datos y devuelve cada elemento uno a la vez.




## 9. Funciones:


  > [!NOTE]
  > Son bloques de código reutilizables que permiten organizar y ejecutar tareas específicas dentro de un programa. Son herramientas esenciales para modularizar el código, hacerlo más legible y evitar la repetición innecesaria.


````Python
def nombre_funcion(parámetros):
    """
    Documentación de la función (opcional)
    """
    # Bloque de código que se ejecuta cuando se llama a la función
    código_a_ejecutar
    return valor_de_retorno  # Opcional, devuelve un valor
````


````Python
def saludar(nombre):    # Saluda a la persona indicada por nombre.
  print(f"¡Hola {nombre}!")
saludar("Juan")  # Imprime "¡Hola Juan!"  # Llamada a la función con un argumento.
````




## 10. Módulos:


  > [!NOTE]
  > Un módulo se crea simplemente creando un archivo de texto con la extensión `.py` y escribiendo el código Python que deseas agrupar. Por ejemplo, un módulo llamado `mis_funciones.py` podría contener:


````Python
def saludar(nombre):
  print(f"¡Hola {nombre}!")
def sumar(a, b):
  return a + b
````


> Para utilizar el código de un módulo en otro programa, se debe importar utilizando la instrucción `import`.


Importación completa:


````Python
import mis_funciones  # Importa todas las funciones y variables del módulo
mis_funciones.saludar("Pedro")  # Llama a la función saludar del módulo
resultado = mis_funciones.sumar(10, 5)  # Llama a la función sumar y almacena el resultado
````


Importación específica:


````Python
from mis_funciones import saludar, sumar  # Importa solo las funciones/variables especificadas
saludar("Ana")
total = sumar(7, 3)
````




## 11. Excepciones:


  > Son mecanismos para manejar errores que ocurren durante la ejecución de un programa. Permiten controlar el flujo del programa cuando se encuentra con un problema inesperado, evitando que se bloquee o se comporte de forma impredecible.


  > [!NOTE]
  > El manejo de excepciones en Python se basa en dos bloques de código:
  >
  > Bloque `try`: Contiene el código que se intenta ejecutar. Si se produce una excepción durante la ejecución de este bloque, se pasa al bloque `except`.
  > 
  > Bloque `except`: Se utiliza para capturar y manejar la excepción. Se puede especificar uno o más bloques `except` para diferentes tipos de excepciones.


````Python
try:
  # Código que se intenta ejecutar

except Exception as e:  # Excepción genérica
  # Código para manejar la excepción general

except TypeError as e:  # Excepción específica de tipo
  # Código para manejar la excepción de tipo

except ZeroDivisionError as e:  # Excepción específica
  # Código para manejar la excepción de división por cero

finally:
  # Código que se ejecuta siempre, independientemente de si hay o no una excepción
````



### 11.1. Elementos clave:


  > [!NOTE]
  > `try`: Inicia el bloque donde se intenta ejecutar el código.
  > 
  > `except`: Inicia el bloque para manejar excepciones.
  > 
  > `Exception`: Captura cualquier tipo de excepción.
  > 
  > `TypeError`: Captura excepciones relacionadas con tipos de datos inválidos.
  > 
  > `ZeroDivisionError`: Captura la excepción específica de división por cero.
  > 
  > `as e`: Asigna la excepción a una variable e para acceder a su información.
  > 
  > `finally`: Contiene código que se ejecuta siempre, incluso si hay una excepción o no.


````Python
def dividir(numerador, denominador):
  try:
    resultado = numerador / denominador
  except ZeroDivisionError as e:
    print("¡Error! No se puede dividir por cero.")
  except TypeError as e:
    print(f"Error de tipo: {e}")
  else:
    print(f"El resultado de la división es: {resultado}")
  finally:
    print("Finalizando la función dividir.")

dividir(10, 2)  # Imprime: El resultado de la división es: 5.0
dividir(10, 0)  # Imprime: ¡Error! No se puede dividir por cero. Finalizando la función dividir.
dividir("Hola", 2)  # Imprime: Error de tipo: 'str' no se puede dividir por 'int'. Finalizando la función dividir.
````


> [!TIP]
> <details>
  > <summary>Beneficios del manejo de excepciones:</summary>
  >
  > Robustez: Permite que el programa continúe funcionando incluso si hay errores, evitando que se bloquee.
  >
  > Legibilidad: Mejora la legibilidad del código al separar la lógica normal del manejo de errores.
  >
  > Mantenimiento: Facilita la identificación y corrección de errores, ya que proporciona información sobre la causa del problema.
  >
  > Buenas prácticas: Es considerado una buena práctica de programación para escribir código resiliente y confiable.
</details>



### 11.2. raise y assert:


  > Tanto `raise` como `assert` son mecanismos para controlar el flujo del programa, pero con propósitos y funcionalidades diferentes:


  > [!NOTE]
  > `raise`
  > 
  > Se utiliza para lanzar o generar una excepción de forma explícita en el código.
  > 
  > Permite crear excepciones personalizadas o propagar excepciones existentes.
  > 
  > Se suele usar dentro de funciones o bloques `try-except` para indicar un error específico.


````Python
def validar_edad(edad):
  if edad < 0:
    raise ValueError("La edad no puede ser negativa")
  else:
    print(f"La edad ingresada es: {edad}")

try:
  validar_edad(-5)  # Genera una excepción ValueError
except ValueError as e:
  print(f"Error: {e}")
````


  > [!NOTE]
  > `assert`
  >
  > Se utiliza para verificar una condición durante la ejecución del programa.
  > 
  > Si la condición no se cumple, se genera una excepción `AssertionError`.
  > 
  > Se suele usar para comprobaciones internas del código y depuración.


````Python
numero = 10
assert numero > 0, "El número debe ser positivo"  # No se genera error
numero = -5
assert numero > 0, "El número debe ser positivo"  # Genera una AssertionError
````

