def menu():
  print("MENU")
  print("1. factorial")
  print("2.suma de primeros numeros naturales")
  print("3.fibonacci")
  print("4.cuantas letras en una palabra")
  print("5.Invertir texto")
  print("6.calcular potencia")
  print("7.Salir")
opcion = int(input("Ingresa una opcion: "))
if opcion == 1:
    def factorial(n):
        if n == 0:
            return 1
        else :
            return n * factorial(n-1)
    n = int(input("Ingresa un numero: "))
    factorial(n)
    print(f"el factorial de {n} es {factorial(n)}")

menu()