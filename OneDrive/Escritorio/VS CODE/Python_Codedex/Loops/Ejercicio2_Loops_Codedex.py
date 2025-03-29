#Adivina el númerc

guess  = 0
tries = 0
while guess != 6 and tries < 5:
  guess = int(input("Gues the number: "))
  tries =  tries +1

if guess != 6:
  gues = int(input("Gues the number: "))
else:
  print("You got it!")