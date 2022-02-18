senha = input('Digite a senha: ')

def validaSenha(senha):
    '''
    Fora do escopo de saída, essa função testa todos os
    critérios descritos na questão , se a senha:
    Possui no mínimo 6 caracteres. (length_ok)
    Contém no mínimo 1 digito. (numeric_ok)
    Contém no mínimo 1 letra em maiúsculo. (lower_ok)
    Contém no mínimo 1 letra em minúsculo. (upper_ok)
    Contém no mínimo 1 caractere especial. Os caracteres especiais são: not @#$%^&*()-+ (symbol_ok)
    '''
    length_ok=False
    numeric_ok=False
    lower_ok=False
    upper_ok=False
    symbol_ok=False

    if len(senha)>=6:
        length_ok=True
    for i in senha:
        if i.isnumeric():
            numeric_ok=True
        elif not i.isnumeric() and i.isupper():
            upper_ok=True
        elif not i.isnumeric() and not i.isupper():
            lower_ok=True
        elif i in '!@#$%^&*()-+':
            symbol_ok=True
            
    if not length_ok:
        print(f'Sua senha é muito curta, faltam {6-len(senha)} caracteres para uma senha forte')
    if not numeric_ok:
        print('Sua senha precisa de um caractere numérico')
    if not lower_ok:
        print('Sua senha precisa de pelo menos  um caractere minúsculo')
        
    if not upper_ok:
        print('Sua senha precisa de pelo menos  um caractere maiúsculo')
    
    if not symbol_ok:
        print('Sua senha precisa de pelo menos um caractere especial: (!@#$%^&*()-+)')




#------------------------
### A PARTIR DAQUI A SAIDA ESPERADA PELO ENUNCIADO:

if len(senha)<6:
    print(6-len(senha))