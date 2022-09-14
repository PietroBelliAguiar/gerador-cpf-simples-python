# Gerador de CPF #
from ntpath import join
from random import randint
import calcularDigitosVerificadores as calc

digitos = []
cpf = ''


for i in range(9, 0, -1):
    digitos.append(randint(0, 9))
 
digitos.append(calc.calcularDigito(digitos))
digitos.append(calc.calcularDigito(digitos))
digitos.insert(3, '.')
digitos.insert(7, '.')
digitos.insert(11, '-')

for i in digitos:
    cpf += str(i)


print(f'CPF Gerado: {cpf}')