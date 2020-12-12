# REPOSITÓRIO DIRECIONADO A INICIANTES EM PROGRAMAÇÃO.
# exemplificarei usando o cálculo da média de um estudante
# dividirei em três diferentes funções as etapas do cálculo para melhor entendimento da lógica

# começe definindo uma função e os comandos que ela irá executar

def media(): # definindo a função
    #comandos de exemplos
    nota1 = float(input("minha primeira nota : ")) # adicionando valores a variavel
    nota2 = float(input("minha segunda nota : "))
    return calcular_media(nota1,nota2) # retornando o valor da função

def calcular_media(nota1,nota2): # pegando os valores por parâmetros
    media = (nota1 + nota2) / 2 # cálculo da média do aluno
    return media # retornando uma função por inteiro

# função de saida
def calculando_aprovacao(media): # chamando uma função inteira por parâmetro
    if(media >= 5):# condicional
        print("ALUNO APROVADO.")
    else:
        print("ALUNO REPROVADO.")

calculando_aprovacao(media()) # chamando a função.

<<<<<<< HEAD
# Outra forma de calcular a média de um aluno

def main():
    primeira_avaliacao = float(input('Qual é a nota da primeira avaliação: ')) # incerssão dos dados
    segunda_avaliacao = float(input('Qual é a nota da segunda avaliação: '))
    media_aluno = (primeira_avaliacao + segunda_avaliacao) / 2 # cálculo da média
    
    if media_aluno >= 7.5: # condicional
        print('você foi aprovado,parabéns sua média foi ',media_aluno)
    else:
        print('você foi reprovado,sua média foi ',media_aluno)

main() # chamando a função
=======
# EXERCICO DE ADVINHAÇÃO DE NUMERO
# (NÃO HAVERÁ ESTRUTURAS COMPLEMENTARES NESSE REPOSITORIO)

def tilt(): # definindo a função
    numero_certo = 98764 # adicionado valor a variavel
    numero_do_chute = float(input("Tente acerta o número certo : ")) # valor inserido pelo usuario

    if numero_do_chute > numero_certo: # condicionais
        print("Diminua o valor do chute")
    elif numero_do_chute < numero_certo:
        print("Aumente o valor do chute")
    else:
        print("Você acertou o valor do chute Parabens!")

tilt()
>>>>>>> 75bcd87101368f19b9cee7d5bb6a1a6c551df1b1
