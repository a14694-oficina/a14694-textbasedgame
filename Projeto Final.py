#Projeto Final  

introducao = "Bem vindo á floresta encantada"
print(introducao)
nome = input(f"Qual é o teu nome?: ")
print(nome)
sorte = "Desejo-te boa sorte!"
print(sorte)
escolha = input(f"Queres ir para o caminho da direita ou da esquerda?: ")
print(escolha)
if escolha == "direita":
  print(f"Como escolheste o caminho da direita vais encontrar monstros")
else:
  print(f"Se escolheste o caminho da esquerda tás safo!")
caminhos = input(f"Depois de escolheres o caminho da esquerda, vais ter mais 2 caminhos e se fores para a esquerda morres, se fores para a direita vais continuar o teu caminho tranquilo")
if caminhos == "caminhos":
  print(f"")
