    # Ejercicio 1 Loops

pin = int(input("Enter your pin: "))

while pin != 1234:
  pin = int(input("Incorrect PIN. Enter your PIN again: "))
if pin == 1234:
  print("PIN accepted") 