import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.digits +"!@#?" * 2
    senha = ''.join (random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha =  int(input('Digite a quantidade de caracteres que deseja:'))
senha_gerada = gerar_senha(tamanho_senha)
print ('a senha gerada é:', senha_gerada)

while True:
    opcao = input('Deseja refazer a senha? (S/N):')
    if opcao.lower() == 's':
        tamanho_senha = int(input('digite a quantidade de caracterer que deseja:'))
        senha_gerada= gerar_senha(tamanho_senha)
        print('A senha gerada é:', senha_gerada)
    elif opcao.lower() == 'n':
        break

