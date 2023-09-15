from random import randint

num_g = tuple(randint(0,100) for i in (range(5)))
#num_g = (int(randint(1,100)), int(randint(1,100)), int(randint(1,100)), int(randint(1,100)), int(randint(1,100)))
print(f'Os valores soteados foram: {num_g}')
print(f'O maior valor sorteado foi: {max(num_g)}')
print(f'O menor valor sorteado foi {min(num_g)}')
