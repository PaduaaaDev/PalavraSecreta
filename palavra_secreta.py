palavra_secreta = 'batata'
palavras_acertadas = ''
quantidade_tentativas = 0

while True:
    letra = input('Digite UMA letra: ').lower()
    quantidade_tentativas += 1

    if len(letra) != 1:
        print("Por favor, digite APENAS UMA LETRA")
        continue
    
    if letra in palavra_secreta:
        palavras_acertadas += letra
   
    palavra_correta = ''
    for i in palavra_secreta:
        if i in palavras_acertadas:
            palavra_correta += i
        else:
            palavra_correta += '*'
    print('-------------------------------')
    print('Palavra Secreta:', palavra_correta)
    print('-------------------------------')
    print('Tentativa número: ', quantidade_tentativas)
    print('-------------------------------')

    if palavra_correta == palavra_secreta:
        print('Você GANHOU, PARABENS!!!!')
        print('Palavra secreta era:', palavra_secreta)
        print('Quantidade de tentativas:', quantidade_tentativas)
        break

