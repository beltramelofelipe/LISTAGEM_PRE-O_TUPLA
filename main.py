lista_compras = ('Borracha', 0.30, 
 'Lapis', 1.00,
 'caderno', 5.00)
print('-' * 30)
print(f'{"LISTA DE COMPRAS":^30}')
print('-' * 30)
for n in range(0, len(lista_compras)):
  if n % 2 == 0:
    print(f'{lista_compras[n]:.<30}', end='')
  else:
    print(f'R$ {lista_compras[n]:.2f}')