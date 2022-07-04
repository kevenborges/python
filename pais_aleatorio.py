import random
lista = ["alemanha", "arábia saudita", "argentina", "austrália", "bélgica", "brasil", "camarões", "canadá", "catar", "coreia do sul", "costa rica", "croácia", "dinamarca", "equador", "espanha", "estados unidos", "frança", "gana", "holanda", "inglaterra", "irã", "japão", "marrocos", "méxico", "país de gales", "polônia", "portugal", "senegal", "sérvia", "suíça", "tunísia", "uruguai"]
pais = random.choice(lista)
tentativas = 4
resposta = str(input("Descubra o nome de um país da Copa do Mundo de 2022 (digite com letras minúsculas e ponha acento se tiver): "))
while (resposta != pais and tentativas > 0):
    print("Você errou!") 
    print( )
    print("Você ainda tem ", tentativas, "tentativas.")
    if tentativas == 1:
        print("Dica: A primeira letra do país é", pais[0])
    tentativas = (tentativas - 1)
    resposta = str(input("Digite novamente o nome de um país (em letras minúsculas): "))
if resposta == pais:
        print("Você acertou!!!")
else:
        print( )
        print("Você errou todas as tentativas, o país era:", pais)

        # code by Keven Borges Barros, discente em Bacharelado em Sistemas de Informação - FURG
