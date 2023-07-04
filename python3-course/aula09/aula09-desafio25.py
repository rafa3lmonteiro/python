# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo aqui: ')).strip()

print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
