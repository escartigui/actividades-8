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
        if n <= 0:
            return 1
        else :
            return n * factorial(n-1)
    n = int(input("Ingresa un numero: "))
    factorial(n)
    print(f"el factorial de {n} es {factorial(n)}")
  if opcion == 2:
      def numerosnaturales(n):
        if n <= 0:
          return 0
        else :
            return n + numerosnaturales(n-1)
      n = int(input("Ingresa un numero natural: "))
      numerosnaturales(n)
      print(f"El numero natural de {n} es {numerosnaturales(n)}")
  if opcion == 3:
      print("No se que es el fibonacci")
  if opcion == 4:
      print("cuantas veces aparece una letra en una palabra")
  if opcion == 5:
      print("invertir texto")
  if opcion == 6:
      def poten(base,expo):
          if expo == 0:
              return 1
          else:
              return base * poten(base,expo-1)
      base = int(input("Ingresa un numero base: "))
      expo = int(input("Ingresa un numero exponente: "))
      print(f"el potencia de {base} es {poten(base,expo)}")
menu()