# Loop Aninhados
# Pais + Estação
paises = ['brasil', 'india', 'estados unidos']
estacao_do_ano = ['primavera', 'verão', 'outono', 'inverno']
for pais in paises:
    for estacao in estacao_do_ano:
        print(f'{pais} {estacao}')


for x in range(1, 11):
    for y in range(1, 6):
        print(f'Valor externo {x} e interno de {y}')



#Desafio
##imprima na tela a marca + celular de todos celulares, usando as informaçoes abaixo

celulares = ['Asus', 'Sansung', 'Sony', 'Iphone']
versoe = ['Plus', 'Premium', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for modelo in versoe:
        print(f'{celular} {modelo}')
