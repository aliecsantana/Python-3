# Operadores aritméticos em Python:
# Soma: +
# Subtração: -
# Multiplicação: *
# Divisão: /
# Potência: **
# Divisão inteira: //
# Resto da divisão: %

# Ordem de precedência dos operadores:
# 1º: ()
# 2º: **
# 3º: * / // %
# 4º: + -

# Solicita dois números inteiros ao usuário
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

# Realiza as operações matemáticas básicas
soma = n1 + n2               # Soma
subtracao = n1 - n2          # Subtração
multiplicacao = n1 * n2      # Multiplicação
divisao = n1 / n2            # Divisão (resultado com ponto flutuante)
divisao_inteira = n1 // n2   # Divisão inteira (resultado sem casas decimais)
resto_divisao = n1 % n2      # Resto da divisão
potencia = n1 ** n2          # Potência

# Exibe os resultados formatados em uma única linha, com quebras e espaçamento
print(
    'Os resultados das operações são:\n'
    'soma: {}, subtração: {}, multiplicação: {},\n'
    'divisão: {:.3f}, divisão inteira: {}, resto da divisão: {},\n'
    'e potência: {}.'.format(soma, subtracao, multiplicacao, divisao, divisao_inteira, resto_divisao, potencia), 
    end=' '
)
