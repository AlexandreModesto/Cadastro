cadastro = {'nome':[],'sexo':[], 'ano':[]}
totalCadastrados = 0
while True:
    sair = input('Deseja mais um cadastro?')
    if sair.lower() in 'nao':
        break
    if sair.lower() not in 'sim':
        print('digite sim ou nao')
    nome = input('Digite o nome:')
    sexo = input('Digite o sexo(M/F):')
    ano = int(input('Digite o nascimento:'))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo)
    cadastro['ano'].append(ano)
    totalCadastrados += 1
    idade = 2021 - ano
    media = idade / totalCadastrados

    mulheresComMenosDe30 = []
    homensComIdadeAcimaDaMedia = []
    if sexo == 'f' and ano > 1991:
        mulheresComMenosDe30.append(nome)
    if sexo == 'm' and idade > media:
        homensComIdadeAcimaDaMedia.append(nome)


print('mulheres com menos de 30:{}'.format(mulheresComMenosDe30))
print('homens com idade acima da media:{}'.format(homensComIdadeAcimaDaMedia))
print(cadastro)
