multiplicadores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2,]
númerosDeUmCPF = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def verificador(cpf):
    validade = False
    cpfFiltrado = []
    cpfComparação = []
    for i in cpf:
        if(i in númerosDeUmCPF):
            cpfFiltrado.append(int(i))
            cpfComparação.append(int(i))
    if len(cpfFiltrado) == 11:
        cpfComparação.pop()
        cpfComparação.pop()
        
        somaDosNúmeros = []
        contador = 1
        for i in cpfComparação:
            i *= multiplicadores[contador]
            somaDosNúmeros.append(i)
            contador += 1

        somaDosNúmeros = sum(somaDosNúmeros)
        resto = somaDosNúmeros % 11 
        if resto < 2:
            cpfComparação.append(0)
        if resto >= 2:
            cpfComparação.append(11 - resto)

        if cpfComparação[len(cpfComparação) -1] == cpfFiltrado[len(cpfFiltrado) - 2]:
            somaDosNúmeros = []
            contador = 0
            for i in cpfComparação:
                i *= multiplicadores[contador]
                somaDosNúmeros.append(i)
                contador += 1

            somaDosNúmeros = sum(somaDosNúmeros)
            resto = somaDosNúmeros % 11 
            if resto < 2:
                cpfComparação.append(0)
            if resto >= 2:
                cpfComparação.append(11 - resto)
            
            if cpfFiltrado == cpfComparação:
                validade = True
        
        return validade
    else:
        return 7

válido = False
while válido == False:
    print('Digite um CPF:')
    CPF = input()
    if verificador(CPF) == True:
        print('Este CPF é verdadeiro.')
        válido = True
    elif verificador(CPF) == False:
        print('Este CPF é falso.')
        válido = True
    else:
        print('O CPF digitado é inválido')