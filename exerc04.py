def verifica_senha (senha):
    conta_caract = len(senha)
    conta_letras= 0
    conta_num = 0
    conta_pontuacoes = 0
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    pontuacoes = [',','.','!',';','?',':']
    
    for caract in senha:
        if caract in numeros:
            conta_num += 1
        if caract.isalpha(): #isalpha verifica se tem so letra retornando true ou false.
            conta_letras += 1
        if caract in pontuacoes:
            conta_pontuacoes += 1

    if conta_caract <= 5:
        return 'Senha Fraca'
    elif conta_letras > 0  and conta_num > 0 and conta_pontuacoes == 0:
        return 'Senha Forte'
    elif conta_letras > 0 and conta_num > 0 and conta_pontuacoes > 0:
        return 'Senha Muito Forte'
   # return conta_caract, conta_num, conta_letras, conta_pontuacoes



resultado = verifica_senha('tes,te:123')

print(resultado)