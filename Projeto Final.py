#Projeto Final 

#Introdução 
introducao = "Bem vindo á floresta encantada"
print(introducao)
#Perguntar o nome e deseja-lhe boa sorte
nome = input("Qual é o teu nome?: ")
sorte = "Desejo-te boa sorte!"
print(sorte)
#Perguntar qual o caminho que quer seguir 
escolha = input("Queres ir para o caminho da direita ou da esquerda?: ")
if escolha == "direita":
  print("Os monstros vão te atacar!")
  escolha = input("Queres fugir ou atacar?: ")
  if escolha == "fugir":
    print("Se fugires tás safo!")
    if escolha == "atacar":
      print("Se atacares vais morrer. GAME OVER!")

if escolha == "esquerda": 
  escolha = input("Vais ter mais 2 caminhos, qual vais escolher?: ")
  if escolha == "esquerda": 
    print("Escolheste o caminho errado. GAME OVER!")
    if escolha == "direita":
      print("Podes continuar o teu caminho sem preocupação!")
#Fim de jogo 
print(f"Fim de jogo {nome}!") 
