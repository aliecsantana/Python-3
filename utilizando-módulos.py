# Importando a função sqrt (raiz quadrada) do módulo math
from math import sqrt

# Solicita ao usuário que insira um número inteiro
num = int(input('Digite um número inteiro: '))

# Calcula a raiz quadrada do número
raiz = sqrt(num)

# Exibe o resultado formatado usando f-strings
print(f'A raiz quadrada de {num} é aproximadamente {raiz:.2f}.')