##from PIL import Image 

##image = Image.open('C:/Users/HP/Pictures/Saved Pictures/libro.jpg')
##image.show()

def mostrar_menu():
    print("1. Ejercicios del hito 2")
    print("2. Ejercicios del hito 3")
    print("3. Ejercicios del hito 4")
    print("4. Salir")

def opcion_1():
    print("Seleccionaste ejercicios del hito 2")
    opcion_1_submenu()

def opcion_1_submenu():
    print("Submenú de Ejercicios de lógica proposicional:")
    print("a. Tabla de Verdad")
    print("b. Identificador de Concetores Logicos")
    sub_opcion = input("Elige una opción de lógica proposicional: ")
    if sub_opcion == "a":
        opcion_1_tabla_de_verdad()
    elif sub_opcion == "b":
        opcion_1_identificador_de_conectores_logicos()
    else:
        print("Opción no válida del submenú.")

def opcion_1_tabla_de_verdad():
    print("Realizando tabla de verdad")
    import itertools

    def reemplazar_operadores(expr):
        expr = expr.replace('¬', ' not ')
        expr = expr.replace('∧', ' and ')
        expr = expr.replace('∨', ' or ')
        expr = expr.replace('→', ' <= ')
        expr = expr.replace('↔', ' == ')
        return expr

    def evaluar_expresion(expr, valores):
        for variable, valor in valores.items():
            expr = expr.replace(variable, str(valor))
        
        expr = reemplazar_operadores(expr)
        
        try:
            return eval(expr)
        except Exception as e:
            print(f"Error en la evaluación de la expresión: {e}")
            return None

    def tabla_de_verdad(expr):
        variables = sorted(set(filter(str.isalpha, expr)))
        combinaciones = list(itertools.product([False, True], repeat=len(variables)))
        
        # Imprimir encabezados
        encabezado = ' | '.join(variables) + ' | ' + expr
        print(encabezado)
        print('-' * len(encabezado))
        
        for combinacion in combinaciones:
            valores = dict(zip(variables, combinacion))
            resultado = evaluar_expresion(expr, valores)
            if resultado is None:
                continue
            valores_str = ' | '.join(['V' if val else 'F' for val in combinacion])  # Convertir True/False a V/F
            print(f"{valores_str} | {'V' if resultado else 'F'}")

    expr = input("Ingrese una expresión lógica: ")
    expr = expr.replace('v', '∨').replace('^', '∧').replace('~', '¬')
    tabla_de_verdad(expr)

def opcion_1_identificador_de_conectores_logicos():
    print("Identificar los Lonectores Logicos")
    
    def mostrar_menu():
        print("\nMenú Principal:")
        print("1. Ingresar oración lógica")
        print("2. Salir")

    def convertir_a_logica(oracion):
        oracion = oracion.lower()
        oracion = oracion.replace(' no ', ' ¬')
        oracion = oracion.replace(' y ', ' ∧ ')
        oracion = oracion.replace(' o ', ' ∨ ')
        oracion = oracion.replace(' si ', '')
        oracion = oracion.replace(' entonces ', ' → ')
        oracion = oracion.replace(' si y solo si ', ' ↔ ')
        return oracion

    while True:
       mostrar_menu()
       opcion = input("Elige una opción: ")

       if opcion == "1":
           oracion = input("Ingrese una oración lógica: ")
           expr = convertir_a_logica(oracion)
           print(f"Expresión lógica: {expr}")
       elif opcion == "2":
           print("Saliendo del programa...")
           break
       else:
           print("Opción no válida. Por favor, elige una opción del menú.")


def opcion_2():
    print("Seleccionaste ejercicios del hito 3")
    opcion_2_numeros_complejos_submenu() 
      
def opcion_2_numeros_complejos_submenu():
    print("\nSubmenú de Ejercicios del hito 3:")
    print("a. Suma y Resta de Números Complejos")
    print("b. Multiplicación y División de Números Complejos")
    sub_opcion = input("Elige una opción de los ejercicios del hito 3: ")
    if sub_opcion == "a":
        submenu_suma_resta_de_numeros_complejos()
    elif sub_opcion == "b":
        submenu_multiplicacion_division_de_numeros_complejos()
    else:
        print("Opción no válida del submenú.")
        
def submenu_suma_resta_de_numeros_complejos():
    while True:
        print("\nSubmenú de Suma y Resta de Números Complejos")
        print("1. Suma de Numeros Complejos")
        print("2. Resta de NUmeros Complejos")
        print("3. Volver al Menú Principal")
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == '1':
            suma_de_numeros_complejos()
        elif opcion == '2':
            resta_de_numeros_complejos()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

def suma_de_numeros_complejos():
    def ingresar_numero_complejo():
        while True:
            try:
                entrada = input("Ingresa un número complejo (ej. 3+5j): ").replace(" ", "").replace("(", "").replace(")", "")
                if '+' in entrada:
                    partes = entrada.split('+')
                    real = float(partes[0])
                    imaginaria = float(partes[1].replace('j', ''))
                elif '-' in entrada:
                    partes = entrada.split('-')
                    if partes[0] == '':
                        real = -float(partes[1])
                        imaginaria = -float(partes[2].replace('j', '')) if len(partes) > 2 else 0
                    else:
                        real = float(partes[0])
                        imaginaria = -float(partes[1].replace('j', ''))
                else:
                    raise ValueError
                return complex(real, imaginaria)
            except (ValueError, IndexError):
                print("Entrada no válida. Por favor, sigue el formato correcto (ej. 3+5j).")

    z1 = ingresar_numero_complejo()
    z2 = ingresar_numero_complejo()
    resultado = z1 + z2
    print(f"\nResultado de la suma: {resultado.real} + {resultado.imag}j")

def resta_de_numeros_complejos():
    def ingresar_numero_complejo():
        while True:
            try:
                entrada = input("Ingresa un número complejo (ej. 3+5j): ").replace(" ", "").replace("(", "").replace(")", "")
                if '+' in entrada:
                    partes = entrada.split('+')
                    real = float(partes[0])
                    imaginaria = float(partes[1].replace('j', ''))
                elif '-' in entrada:
                    partes = entrada.split('-')
                    if partes[0] == '':
                        real = -float(partes[1])
                        imaginaria = -float(partes[2].replace('j', '')) if len(partes) > 2 else 0
                    else:
                        real = float(partes[0])
                        imaginaria = -float(partes[1].replace('j', ''))
                else:
                    raise ValueError
                return complex(real, imaginaria)
            except (ValueError, IndexError):
                print("Entrada no válida. Por favor, sigue el formato correcto (ej. 3+5j).")

    z1 = ingresar_numero_complejo()
    z2 = ingresar_numero_complejo()
    resultado = z1 - z2
    print(f"\nResultado de la resta: {resultado.real} + {resultado.imag}j")

def submenu_multiplicacion_division_de_numeros_complejos():
    while True:
        print("\nSubmenú de Multiplicación y División de Números Complejos")
        print("1. Multiplicación")
        print("2. División")
        print("3. Volver al Menú Principal")
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == '1':
            multiplicacion_de_numeros_complejos()
        elif opcion == '2':
            division_de_numeros_complejos()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

def multiplicacion_de_numeros_complejos():
    def ingresar_numero_complejo():
        while True:
            try:
                entrada = input("Ingresa un número complejo (ej. 3+5j): ").replace(" ", "").replace("(", "").replace(")", "")
                if '+' in entrada:
                    partes = entrada.split('+')
                    real = float(partes[0])
                    imaginaria = float(partes[1].replace('j', ''))
                elif '-' in entrada:
                    partes = entrada.split('-')
                    if partes[0] == '':
                        real = -float(partes[1])
                        imaginaria = -float(partes[2].replace('j', '')) if len(partes) > 2 else 0
                    else:
                        real = float(partes[0])
                        imaginaria = -float(partes[1].replace('j', ''))
                else:
                    raise ValueError
                return complex(real, imaginaria)
            except (ValueError, IndexError):
                print("Entrada no válida. Por favor, sigue el formato correcto (ej. 3+5j).")

    z1 = ingresar_numero_complejo()
    z2 = ingresar_numero_complejo()
    resultado = z1 * z2
    print(f"\nResultado de la multiplicación: {resultado.real} + {resultado.imag}j")

def division_de_numeros_complejos():
    def ingresar_numero_complejo():
        while True:
            try:
                entrada = input("Ingresa un número complejo (ej. 3+5j): ").replace(" ", "").replace("(", "").replace(")", "")
                if '+' in entrada:
                    partes = entrada.split('+')
                    real = float(partes[0])
                    imaginaria = float(partes[1].replace('j', ''))
                elif '-' in entrada:
                    partes = entrada.split('-')
                    if partes[0] == '':
                        real = -float(partes[1])
                        imaginaria = -float(partes[2].replace('j', '')) if len(partes) > 2 else 0
                    else:
                        real = float(partes[0])
                        imaginaria = -float(partes[1].replace('j', ''))
                else:
                    raise ValueError
                return complex(real, imaginaria)
            except (ValueError, IndexError):
                print("Entrada no válida. Por favor, sigue el formato correcto (ej. 3+5j).")

    z1 = ingresar_numero_complejo()
    z2 = ingresar_numero_complejo()
    try:
        resultado = z1 / z2
        print(f"\nResultado de la división: {resultado.real} + {resultado.imag}j")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")


def opcion_3():
    print("Seleccionaste ejercicios del hito 4")
    opcion_3_operaciones_matrices_submenu()

def opcion_3_operaciones_matrices_submenu():
    print("Submenú de Ejercicios del hito 4:")
    print("a. Operaciones de matrices")
    print("b. Transpuesta de una matriz")
    sub_opcion = input("Elige una opción de los ejercicios del hito 4: ")
    if sub_opcion == "a":
        opcion_3_operaciones_matrices()
    elif sub_opcion == "b":
        opcion_3_transpuesta_de_una_matriz()
    else:
        print("Opción no válida del submenú.")

def opcion_3_operaciones_matrices():
    print("Realizando Operaciones con Matrices")
    while True:
        print("Submenú de Operaciones de matrices:")
        print("1. Sumar matrices")
        print("2. Restar matrices")
        print("3. Multiplicar matrices")
        print("4. Volver al menú anterior")
        
        sub_opcion = input("Elige una opción: ")
        if sub_opcion == "1":
            suma_matrices()
        elif sub_opcion == "2":
            resta_matrices()
        elif sub_opcion == "3":
            multiplicacion_matrices()
        elif sub_opcion == "4":
            break
        else:
            print("Opción no válida del submenú.")

def suma_matrices():
    matriz_a = crear_matriz("A")
    matriz_b = crear_matriz("B")
    if matriz_a and matriz_b:
        resultado = sumar_matrices(matriz_a, matriz_b)
        if resultado:
            print("\nMatriz A:")
            mostrar_matriz(matriz_a)
            print("\nMatriz B:")
            mostrar_matriz(matriz_b)
            print("\nProcedimiento para sumar matrices:")
            print("1. Sumar elemento por elemento de las matrices A y B.")
            print("2. Colocar el resultado en la matriz de resultado.")
            print("\nResultado de la suma:")
            mostrar_matriz(resultado)

def resta_matrices():
    matriz_a = crear_matriz("A")
    matriz_b = crear_matriz("B")
    if matriz_a and matriz_b:
        resultado = restar_matrices(matriz_a, matriz_b)
        if resultado:
            print("\nMatriz A:")
            mostrar_matriz(matriz_a)
            print("\nMatriz B:")
            mostrar_matriz(matriz_b)
            print("\nProcedimiento para restar matrices:")
            print("1. Restar elemento por elemento de las matrices A y B.")
            print("2. Colocar el resultado en la matriz de resultado.")
            print("\nResultado de la resta:")
            mostrar_matriz(resultado)

def multiplicacion_matrices():
    matriz_a = crear_matriz("A")
    matriz_b = crear_matriz("B")
    if matriz_a and matriz_b:
        resultado = multiplicar_matrices(matriz_a, matriz_b)
        if resultado:
            print("\nMatriz A:")
            mostrar_matriz(matriz_a)
            print("\nMatriz B:")
            mostrar_matriz(matriz_b)
            print("\nProcedimiento para multiplicar matrices:")
            print("1. Multiplicar filas de la matriz A con columnas de la matriz B.")
            print("2. Sumar los productos de los elementos correspondientes.")
            print("3. Colocar el resultado en la matriz de resultado.")
            print("\nResultado de la multiplicación:")
            mostrar_matriz(resultado)

def crear_matriz(nombre):
    try:
        filas = int(input(f"Ingrese el número de filas de la matriz {nombre}: "))
        columnas = int(input(f"Ingrese el número de columnas de la matriz {nombre}: "))
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}) de la matriz {nombre}: "))
                fila.append(valor)
            matriz.append(fila)
        return matriz
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        return None

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def sumar_matrices(matriz_a, matriz_b):
    try:
        if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones para poder sumarse.")
        filas = len(matriz_a)
        columnas = len(matriz_a[0])
        resultado = [[0 for _ in range(columnas)] for _ in range(filas)]
        for i in range(filas):
            for j in range(columnas):
                resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]
        return resultado
    except ValueError as e:
        print(f"Error: {e}")
        return None

def restar_matrices(matriz_a, matriz_b):
    try:
        if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones para poder restarse.")
        filas = len(matriz_a)
        columnas = len(matriz_a[0])
        resultado = [[0 for _ in range(columnas)] for _ in range(filas)]
        for i in range(filas):
            for j in range(columnas):
                resultado[i][j] = matriz_a[i][j] - matriz_b[i][j]
        return resultado
    except ValueError as e:
        print(f"Error: {e}")
        return None

def multiplicar_matrices(matriz_a, matriz_b):
    try:
        if len(matriz_a[0]) != len(matriz_b):
            raise ValueError("El número de columnas de la matriz A debe ser igual al número de filas de la matriz B para poder multiplicarse.")
        filas_a = len(matriz_a)
        columnas_a = len(matriz_a[0])
        columnas_b = len(matriz_b[0])
        resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]
        for i in range(filas_a):
            for j in range(columnas_b):
                for k in range(columnas_a):
                    resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
        return resultado
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
def opcion_3_transpuesta_de_una_matriz():
    print("Realizando la transpuest de una matriz")
    def transponer_matriz(matriz):
        # Obtener las dimensiones de la matriz original
        filas = len(matriz)
        columnas = len(matriz[0])  
        # Crear una matriz transpuesta inicialmente llena de ceros
        transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
        
        for i in range(filas):
            for j in range(columnas):
                transpuesta[j][i] = matriz[i][j]
        
        return transpuesta
    
    def crear_matriz(filas, columnas):
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
                fila.append(valor)
            matriz.append(fila)
        return matriz

    # Pedir al usuario las dimensiones de la matriz
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matriz = crear_matriz(filas, columnas)

    resultado = transponer_matriz(matriz)

    print("\nProcedimiento para calcular la transpuesta de una matriz:")
    print("1. La matriz original es:")
    for fila in matriz:
        print(fila)

    print("\n2. Para calcular la transpuesta:")
    print("- Intercambiar las filas por columnas.")
    print("- Colocar los elementos de cada fila de la matriz original en columnas correspondientes en la transpuesta.")
    print("- Esto da como resultado la siguiente matriz transpuesta:")

    # Mostrar la matriz original y su transpuesta
    print("\nMatriz original:")
    for fila in matriz:
        print(fila)

    print("\nMatriz transpuesta:")
    for fila in resultado:
        print(fila)

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    elif opcion == "3":
        opcion_3()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")