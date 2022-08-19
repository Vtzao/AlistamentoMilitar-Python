#########################
#  ALISTAMENTO MILITAR  #
#########################
from re import M

##Identificação se o usuário é Homem ou Mulher#
sex = input('Qual é o seu gênero? (H/M) ')
while True:
    if sex == M:
    print('O alimento militar é somente para Homens, não será possível continuar.')
    break
    
    else sex == H:
    continue
### Se o usuário for homem, o programa continua...

#Infos YD
from datetime import date
atual = date.today().year
nasc = int(input('Qual é o seu ano de nascimento? '))
idade = atual - nasc
#Question
print('Quem nasceu em {} tem {} anos em {}. '.format(nasc,idade,atual))


if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE! Procure já um justa militar mais próxima.')
elif idade < 18:
    saldo = 18 - idade
    print('Você não tem 18 anos, ainda falntam {} para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
else
