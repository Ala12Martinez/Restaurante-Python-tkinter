def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero"

def calculadora():
    while True:  # Loop para permitir múltiples operaciones
        print("\nSelecciona una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        operacion = input("Ingresa el número de la operación (1/2/3/4/5): ")

        if operacion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Debes ingresar un número válido.")
                continue  # Vuelve al inicio del bucle si hay un error

            if operacion == '1':
                print(f"{num1} + {num2} = {suma(num1, num2)}")
            elif operacion == '2':
                print(f"{num1} - {num2} = {resta(num1, num2)}")
            elif operacion == '3':
                print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
            elif operacion == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
        elif operacion == '5':
            print("Saliendo del programa.")
            break  # Sale del bucle y cierra el programa
        else:
            print("Operación no válida.")

if __name__ == "__main__":
    calculadora()
