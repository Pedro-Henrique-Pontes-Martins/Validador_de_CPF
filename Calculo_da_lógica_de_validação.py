multiplicadores = [10, 9, 8, 7, 6, 5, 4, 3, 2]
númerosDeUmCPF = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def verificador(cpf):
    cpfFiltrado = []
    for i in cpf:
        if(i in númerosDeUmCPF):
            cpfFiltrado.append(int(i))
    cpfComparação = cpfFiltrado
    cpfComparação.pop()
    cpfComparação.pop()

    somaDosNúmeros = cpfComparação
    contador = 0
    for i in somaDosNúmeros:
        i *= multiplicadores[contador]
        somaDosNúmeros.append(i)
        contador += 1

    somaDosNúmeros = sum(somaDosNúmeros)
    resto = somaDosNúmeros % 11 
    if resto < 2:
        cpfComparação.append(0)
    if resto >= 2:
        cpfComparação.append(11 - resto)