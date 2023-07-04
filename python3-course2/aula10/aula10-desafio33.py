# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input("Digite 1 numero: "))
b = int(input("Digite 2 numero: "))
c = int(input("Digite 3 numero: "))
#Verificando quem é o menor numero
menor = a
  if b<a and b<c:
  menor = b
  if c<a and c<b:
  menor = c
#Verificando quem é o maior numero
maior = a
  if b>a and b>c:
   maior = b
  if c>a and c>b:
   maior = c

print("O menor digitado foi o {}".format(menor))
print("O maior digitado foi o {}".format(maior))