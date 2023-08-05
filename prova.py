'''Você foi contratado para desenvolver um programa que calcule a média de notas dos alunos de uma turma. Para isso, 
você deverá criar uma lista com as notas de cada aluno e, em seguida, implementar uma função que calcule a média aritmética das notas. 
Além disso, você deverá utilizar um loop while para pedir ao usuário que insira as notas dos alunos até que ele decida parar. 
Por fim, você deverá utilizar um loop for para imprimir a média de cada aluno.



a) Escreva o código para a função que calcule a média aritmética das notas.

b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.

c) Escreva o código para o loop for que imprime a média de cada aluno.
'''

def calculo_nota (nota:float, quantidade:int):
    media = nota  / quantidade
    return media

list_alunos = []
soma_notas = 0
sair = 1
quantidade_de_notas = 0
while sair == 1:
    quantidade_de_notas = int(input('Digite a quantidade de notas: '))
    for i in range(0,quantidade_de_notas):
        nota = float(input('Digite sua nota:'))
        soma_notas += nota
    
    resultado_media = calculo_nota(soma_notas, quantidade_de_notas)
    print(f'O resultado da media é {resultado_media}')
    list_alunos.append(resultado_media)
    

    sair = int(input('Deseja continuar digite 1, se desejar sair digite 2:'))
    
print(list_alunos)


        
        
    








    
    
    