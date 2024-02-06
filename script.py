total = 0;
price1000 = 0;
cont = 0;
smaller = 0;
smaller_name = '';

print('-' *13, end='');
print('KABUM', end='');
print('-' *13);

while True:
  name = input('Nome do produto: ');
  value = float(input('Valor do produto: '));
  print('-' *30);

  cont += 1;
  total += value;
  
  if value >= 1000:
    price1000 += 1;

  if cont == 1:
    smaller = value;
  else:
    if value < smaller:
      smaller = value;
      smaller_name = name;

  proceed = ' ';
  
  while proceed not in 'SN':
    proceed = input('Deseja continuar? [S/N]').upper().strip()[0];
  print('-' *5, end='');

  if proceed == 'N':
    break;


print('FINALIZANDO A COMPRA', end='');
print('-' *5);
print(f'O total gasto na compra foi de R$ {total:.2f}.');
print(f'Na lista contem {price1000} produtos que custam mais de R$ 1000.00.');
print(f'O produto mais barato da lista é o {smaller_name.upper()} que custa R$ {smaller:.2f}.');
print('-=' *15);
