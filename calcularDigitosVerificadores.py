def calcularDigito(lista):
    valorOperacao = len(lista)+1
    digito = 0
    
    for item in range(len(lista)):
        elemento = lista[item]
        digito += elemento * valorOperacao
        valorOperacao = valorOperacao - 1
    
    if digito%10 < 2:
        digito = 0
    else:
        digito = 11-(digito%11)
    
    # print(digito)
    return digito