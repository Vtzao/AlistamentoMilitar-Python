#########################
#  ALISTAMENTO MILITAR  #
#########################
from datetime import date

print('ALISTAMENTO MILITAR')
sexo = str(input('Qual é o seu gênero? '))
if sexo in 'Feminino feminino Mulher mulher':
    print('Você não é obrigada a se alistar no exécito.')
    deseja = str(input('Mesmo assim você deseja se alistar? '))
    if deseja in 'Sim sim':
        print('Ok, então continue preenchendo o formuláriio')
    if deseja in 'Não não':
        print('Mesmo assim continue preenchendo o formulário para caso mude de ideia')

if sexo in 'Masculino masculino Homem homem':
    print('O seu alistamento é obrigatório\nContinue preenchendo o formulário')

else:
    print('Gênero inválido. Tente novamente')
    exit()

#Infos YD
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
else:
  print('Operação Inválida.')
