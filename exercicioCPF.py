cpf = '74682489070'




def definir_cpf(cpf):
    soma = 0
    indices = 0
    
    
    lista_inteiros= []
    for i in range(9):
        
        lista_inteiros.append(cpf[i])
    for i in range(9):
        lista_inteiros[i] = int(lista_inteiros[i])
    
    for numeros in range(10,1,-1):
        soma += numeros * lista_inteiros[indices]
        indices += 1

    soma *= 10
    soma = soma % 11
    if soma > 9:
        soma = 0

    lista_inteiros.append(soma)
    indices = 0
    soma = 0
    for numeros in range(11,1,-1):
        soma += numeros * lista_inteiros[indices]
        indices += 1

    soma *= 10
    soma = soma % 11
    if soma > 9:
        soma = 0  
    lista_inteiros.append(soma)
    return lista_inteiros  

print(definir_cpf(cpf))