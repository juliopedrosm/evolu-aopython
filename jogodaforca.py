palavra_secreta = 'hipopotamo'


digitadas = []
erros = 3
usuário = input('Qual o seu nome? ')

print('-' * 40)
print(f' Fala {usuário},\n '
      'bem-vindo ao jogo da palavra secreta!')
print('-' * 40)
print(f'* Dica: sua palavra tem {len(palavra_secreta)} letras\n'
      f'e tem apenas letras minúsculas! *')
print('-' * 40)

while True:
    if erros <= 0:
        print('\nZerou filhão, perdeu feio, tenta de novo!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('\nIiih, meteu essa? Digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in palavra_secreta:
        print('-' * 40)
        print(f'Foi dentro, a letra "{letra}" existe na palavra secreta.')
    else:
        print('-' * 40)
        print(f'Errou mané, a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''

    for letra_digitada in palavra_secreta:
        if letra_digitada in digitadas:
            secreto_temporario += letra_digitada
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavra_secreta:
        print('-' * 40)
        print(f'Acertou mané, se você não for o mais'
                      f' brabo eu sou um poste!!! A palavra era {palavra_secreta}.')
        print('-' * 40)
        break
    else:
        print(f'\nA palavra secreta está assim: {secreto_temporario}')
        print('-' * 40)

    if letra not in palavra_secreta:
        erros -= 1
    print(f'\nVocê ainda tem {erros} possíveis erros.')
    print()