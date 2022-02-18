    """
        Seguindo as entradas dadas no enunciado, foram obtidas as saídas devidas
        mas não foi tratado o caso de haverem mais de um par das mesmas letras.

    """

entrada=input('Digite a palavra de entrada: ')

matriz=[]
for i in entrada:
    if entrada.count(i)==2 and [i,i] not in matriz:
        inicio = entrada.find(i)
        fim = entrada.rfind(i)
        elemento = [entrada[inicio:fim],entrada[inicio+1:fim+1]]
        if len(elemento[0])>1:         
            matriz.append([i,i])
            matriz.append(elemento)
        else:
            matriz.append([i,i])
    
print(len(matriz))
